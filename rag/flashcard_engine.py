```python
def provider_config() -> dict[str, str]:
    provider = os.getenv("FLASHCARD_PROVIDER", "openai").strip().lower()
    if provider in {"nvidia", "nvidia-nim"}:
        return {
            "provider": "nvidia-nim",
            "api_key": os.getenv("NVIDIA_API_KEY", ""),
            "base_url": os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1"),
            "model": os.getenv("NVIDIA_MODEL", ""),
        }
    return {
        "provider": "openai-compatible",
        "api_key": os.getenv("OPENAI_API_KEY", ""),
        "base_url": os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
        "model": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    }


def call_chat(messages: list[dict[str, str]], temperature: float = 0.15, max_tokens: int = 1800) -> tuple[str, str, str]:
    cfg = provider_config()
    key_name = "NVIDIA_API_KEY" if cfg["provider"] == "nvidia-nim" else "OPENAI_API_KEY"
    if not cfg["api_key"]:
        raise RuntimeError(f"Falta {key_name}.")
    if not cfg["model"]:
        raise RuntimeError("Falta NVIDIA_MODEL; configure un identificador de modelo vigente.")
    try:
        timeout = max(1.0, float(os.getenv("FLASHCARD_TIMEOUT_SECONDS", "90")))
    except (TypeError, ValueError):
        timeout = 90.0
    try:
        retries = max(0, min(6, int(os.getenv("FLASHCARD_RETRIES", "4"))))
    except ValueError:
        retries = 4
    payload = json.dumps({"model": cfg["model"], "messages": messages, "temperature": temperature,
                          "max_tokens": max_tokens, "stream": False}, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(cfg["base_url"].rstrip("/") + "/chat/completions", data=payload,
        headers={"Authorization": f"Bearer {cfg['api_key']}", "Content-Type": "application/json",
                 "Accept": "application/json"}, method="POST")
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                data = json.loads(response.read().decode("utf-8"))
            content = data["choices"][0]["message"]["content"]
            if isinstance(content, list):
                content = "".join(part.get("text", "") for part in content if isinstance(part, dict))
            return str(content), cfg["provider"], cfg["model"]
        except urllib.error.HTTPError as exc:
            if exc.code != 429 and not 500 <= exc.code <= 599 or attempt >= retries:
                detail = exc.read().decode("utf-8", errors="replace")[:1000]
                raise RuntimeError(f"Error API {exc.code}: {detail}") from exc
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, KeyError, IndexError) as exc:
            if attempt >= retries:
                raise RuntimeError(f"Fallo de comunicación o respuesta del proveedor: {exc}") from exc
        time.sleep(min(2 ** attempt, 20))
    raise RuntimeError("No se pudo completar la solicitud al proveedor.")


def generation_prompt(chunk: Any, document: Any, limit: int, source_path: str) -> list[dict[str, str]]:
    content = getattr(chunk, "text", None) or str(chunk)
    metadata = getattr(chunk, "metadata", {}) or {}
    page, section = extract_location(content, metadata)
    context = {
        "document_id": getattr(document, "document_id", None),
        "document_title": getattr(document, "title", None) or getattr(document, "filename", None),
        "source_path": source_path,
        "page": page,
        "section": section,
    }
    system = f"""Eres un especialista en diseño instruccional para profesionales de salud del Perú.
Genera hasta {limit} flashcards de alto valor formativo exclusivamente con información explícita
del fragmento documental. No inventes normas, cifras, criterios, dosis, plazos ni procedimientos.
No uses conocimiento externo para completar vacíos. Si el fragmento no permite una tarjeta fiable,
devuelve una lista vacía.

Devuelve SOLO JSON válido con esta estructura:
{{"cards":[{{"question":"...","answer":"...","axis":"... o null","subaxis":"... o null",
"type":"conceptual|comparativa|procedimental|secuencial|aplicada|evaluacion",
"difficulty":"basica|intermedia|avanzada","confidence":0.0,"evidence":"cita textual breve del fragmento"}}]}}

Ejes permitidos: {", ".join(AXES)}.
Una pregunta concreta por tarjeta; respuesta precisa, autosuficiente y verificable.
La evidencia debe ser una cita textual del fragmento, no una paráfrasis.
No repitas tarjetas ni generes preguntas triviales."""
    user = "METADATOS:\n" + json.dumps(context, ensure_ascii=False) + "\n\nFRAGMENTO:\n" + content
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def parse_json_response(content: str) -> dict[str, Any]:
    text = content.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s*```$", "", text)
    decoder = json.JSONDecoder()
    for index, char in enumerate(text):
        if char != "{":
            continue
        try:
            value, _ = decoder.raw_decode(text[index:])
            if isinstance(value, dict) and isinstance(value.get("cards"), list):
                return value
        except json.JSONDecodeError:
            continue
    raise ValueError("La respuesta del modelo no contiene un objeto JSON válido con 'cards'.")


def canonical_axis(value: Any) -> str:
    if value is None or not str(value).strip():
        return "unclassified"
    normalized = normalize(str(value))
    for axis in AXES:
        if normalize(axis) == normalized:
            return axis
    return "unclassified"


def validate_card(raw: dict[str, Any], document: Any, chunk: Any,
                  provider: str, model: str, source_path: str) -> dict[str, Any] | None:
    question = raw.get("question")
    answer = raw.get("answer")
    evidence = raw.get("evidence")
    if not all(isinstance(v, str) and v.strip() for v in (question, answer, evidence)):
        return None
    question, answer, evidence = question.strip(), answer.strip(), evidence.strip()
    if len(question) < 12 or len(answer) < 12 or len(evidence.split()) < 6:
        return None
    axis = canonical_axis(raw.get("axis"))
    card_type = str(raw.get("type") or "conceptual").strip().lower()
    if card_type not in CARD_TYPES:
        card_type = "conceptual"
    difficulty = str(raw.get("difficulty") or "intermedia").strip().lower()
    if difficulty not in {"basica", "intermedia", "avanzada"}:
        difficulty = "intermedia"
    try:
        confidence = float(raw.get("confidence") if raw.get("confidence") is not None else 0.5)
    except (TypeError, ValueError):
        confidence = 0.5
    confidence = min(1.0, max(0.0, confidence))
    content = getattr(chunk, "text", None) or str(chunk)
    if normalize(evidence) not in normalize(content):
        return None
    metadata = getattr(chunk, "metadata", {}) or {}
    page, section = extract_location(content, metadata)
    now = utc_now()
    document_id = getattr(document, "document_id", None)
    title = getattr(document, "title", None) or getattr(document, "filename", None)
    card = {
        "card_id": hashlib.sha256(
            f"{source_path}|{fingerprint({'question': question, 'answer': answer})}".encode("utf-8")
        ).hexdigest()[:20],
        "question": question,
        "answer": answer,
        "axis": axis,
        "subaxis": str(raw["subaxis"]).strip() if raw.get("subaxis") is not None else None,
        "type": card_type,
        "difficulty": difficulty,
        "confidence": confidence,
        "evidence": {
            "quote": evidence,
            "page": page,
            "section": section,
            "provenance": {
                "document_id": document_id,
                "document_title": title,
                "source_path": source_path,
                "provider": provider,
                "model": model,
            },
        },
        "status": "pending_review",
        "created_at": now,
    }
    card["fingerprint"] = fingerprint(card)
    return card


def canonical_source_path(value: Any, corpus: Path) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    candidate = Path(value)
    if candidate.is_absolute():
        try:
            return candidate.resolve().relative_to(corpus.resolve()).as_posix()
        except ValueError:
            return candidate.name
    return candidate.as_posix().lstrip("./")


def discover_documents(corpus: Path) -> list[Path]:
    corpus = corpus.resolve()
    if not corpus.is_dir():
        raise NotADirectoryError(f"No existe la raíz documental: {corpus}")
    supported = {str(ext).lower() if str(ext).startswith(".") else "." + str(ext).lower()
                 for ext in SUPPORTED_EXTENSIONS}
    ignored_dirs = {
        ".git", ".github", ".venv", "venv", "node_modules", "__pycache__",
        ".pytest_cache", ".mypy_cache", ".ruff_cache", ".next", "dist", "build",
        "coverage", "site-packages", "vendor", "target", ".idea", ".vscode",
        "cache", "caches", "tmp", "temp",
    }
    ignored_names = {
        "package-lock.json", "pnpm-lock.yaml", "yarn.lock", "poetry.lock",
        "requirements.txt", "pipfile.lock",
    }
    found: list[Path] = []
    for current, dirs, files in os.walk(corpus):
        dirs[:] = sorted(d for d in dirs if d not in ignored_dirs and not d.startswith("."))
        for name in sorted(files):
            path = Path(current) / name
            if name.lower() in ignored_names or path.suffix.lower() not in supported:
                continue
            if path.name.lower().endswith(".metadata.json"):
                continue
            found.append(path)
    return sorted(found, key=lambda p: p.relative_to(corpus).as_posix().casefold())
    def process_corpus(corpus: Path = DEFAULT_CORPUS, force: bool = False,
                   limit_per_chunk: int = 6, state_path: Path = STATE_PATH,
                   candidates_path: Path = CANDIDATES_PATH, dry_run: bool = False,
                   limit_documents: int | None = None) -> dict[str, Any]:
    corpus = Path(corpus).resolve()
    paths = discover_documents(corpus)
    if limit_documents is not None:
        if limit_documents < 1:
            raise ValueError("--limit-documents debe ser mayor que cero.")
        paths = paths[:limit_documents]

    with file_lock(candidates_path):
        state = read_json(state_path, {"version": 1, "documents": {}})
        docs_state = state.setdefault("documents", {})
        candidate_data = read_json(candidates_path, {"version": 1, "cards": []})
        cards = candidate_data.setdefault("cards", [])
        processed = skipped = generated = duplicates = failed = invalid_dropped = 0

        for path in paths:
            rel = path.relative_to(corpus).as_posix()
            digest = sha256_file(path)
            if not force and docs_state.get(rel, {}).get("sha256") == digest:
                skipped += 1
                continue
            try:
                document = load_document(path)
                chunks = chunk_document(document)
                # Primero se genera en memoria. Si falla el proveedor, la versión anterior
                # permanece intacta y el SHA no se marca como procesado.
                staged: list[dict[str, Any]] = []
                staged_invalid = 0
                for chunk in chunks:
                    content, provider, model = call_chat(
                        generation_prompt(chunk, document, limit_per_chunk, rel))
                    for raw in parse_json_response(content)["cards"]:
                        if not isinstance(raw, dict):
                            staged_invalid += 1
                            continue
                        card = validate_card(raw, document, chunk, provider, model, rel)
                        if card is None:
                            staged_invalid += 1
                            continue
                        card["source_sha256"] = digest
                        staged.append(card)

                # C1: marcar obsoletas antes de crear el índice; no compiten con su reemplazo.
                old_cards = [c for c in cards if
                    canonical_source_path((c.get("evidence") or {}).get("provenance", {}).get("source_path"), corpus) == rel
                    and c.get("status") != "superseded"]
                for old in old_cards:
                    old["status_before_superseded"] = old.get("status")
                    old["status"] = "superseded"
                    old["superseded_at"] = utc_now()

                duplicate_index = DuplicateIndex(cards)
                for card in staged:
                    duplicate = duplicate_index.find(card)
                    if duplicate:
                        card["duplicate_of"] = duplicate
                        card["status"] = "duplicate_review"
                        duplicates += 1
                    cards.append(card)
                    duplicate_index.add(card)
                generated += len(staged)
                invalid_dropped += staged_invalid
                docs_state[rel] = {"sha256": digest, "document_id": document.document_id,
                    "source_path": rel, "chunks": len(chunks), "cards_generated": len(staged),
                    "processed_at": utc_now()}
                processed += 1
                # Persistir al cerrar cada documento: conserva progreso previo sin estados a medias.
                if not dry_run:
                    atomic_json(candidates_path, {"version": 1, "updated_at": utc_now(), "cards": cards})
                    atomic_json(state_path, state)
            except Exception as exc:
                failed += 1
                print(f"ERROR {rel}: {exc}", file=sys.stderr)

        if not dry_run:
            state["updated_at"] = utc_now()
            state["corpus_root"] = str(corpus)
            atomic_json(state_path, state)
            atomic_json(candidates_path, {"version": 1, "updated_at": utc_now(), "cards": cards})
        return {"corpus_root": str(corpus), "documents_discovered": len(paths), "processed": processed,
            "skipped_unchanged": skipped, "generated": generated, "duplicates": duplicates,
            "invalid_dropped": invalid_dropped, "failed": failed, "total_candidates": len(cards),
            "dry_run": dry_run}


def stats(candidates_path: Path = CANDIDATES_PATH, state_path: Path = STATE_PATH) -> dict[str, Any]:
    data = read_json(candidates_path, {"cards": []})
    cards = data.get("cards", [])
    return {
        "total_cards": len(cards),
        "by_status": dict(Counter(c.get("status", "unknown") for c in cards)),
        "by_axis": dict(Counter(c.get("axis", "unclassified") for c in cards)),
        "by_type": dict(Counter(c.get("type", "unknown") for c in cards)),
        "documents_in_state": len(read_json(state_path, {"documents": {}}).get("documents", {})),
    }


def review_card(card_id: str, decision: str, reviewer: str, note: str = "",
                candidates_path: Path = CANDIDATES_PATH, force: bool = False) -> dict[str, Any]:
    if decision not in {"approve", "reject"}:
        raise ValueError("La decisión debe ser approve o reject.")
    if not isinstance(reviewer, str) or not reviewer.strip():
        raise ValueError("Debe identificarse el revisor humano.")
    with file_lock(candidates_path):
        data = read_json(candidates_path, {"version": 1, "cards": []})
        found = next((c for c in data.get("cards", []) if c.get("card_id") == card_id), None)
        if found is None:
            raise KeyError(f"No existe tarjeta: {card_id}")
        if found.get("status") == "superseded":
            raise ValueError("No se puede revisar una tarjeta supersedida.")
        was_duplicate = found.get("status") == "duplicate_review"
        if was_duplicate and decision == "approve" and not force:
            raise ValueError("Es duplicado potencial; use --force solo tras revisión explícita.")
        found["status"] = "approved" if decision == "approve" else "rejected"
        found["review"] = {"decision": decision, "reviewer": reviewer.strip(), "note": note.strip(),
            "reviewed_at": utc_now(), "was_duplicate": was_duplicate,
            "duplicate_override": bool(was_duplicate and decision == "approve" and force)}
        atomic_json(candidates_path, data)
        return found


def export_approved(output: Path = EXPORT_PATH, candidates_path: Path = CANDIDATES_PATH) -> int:
    data = read_json(candidates_path, {"cards": []})
    approved = [card for card in data.get("cards", []) if card.get("status") == "approved"]
    atomic_json(output, {"schema_version": 1, "generated_at": utc_now(), "count": len(approved), "cards": approved})
    return len(approved)


def prune_candidates(candidates_path: Path = CANDIDATES_PATH, keep_days: int = 90) -> int:
    from datetime import timedelta
    cutoff = datetime.now(timezone.utc).timestamp() - max(0, keep_days) * 86400
    with file_lock(candidates_path):
        data = read_json(candidates_path, {"version": 1, "cards": []})
        original = data.get("cards", [])
        kept = []
        for card in original:
            if card.get("status") not in {"superseded", "rejected"}:
                kept.append(card)
                continue
            stamp = card.get("superseded_at") or (card.get("review") or {}).get("reviewed_at") or card.get("created_at")
            try:
                age = datetime.fromisoformat(stamp.replace("Z", "+00:00")).timestamp()
            except (AttributeError, ValueError):
                age = 0
            if age >= cutoff:
                kept.append(card)
        data["cards"] = kept
        atomic_json(candidates_path, data)
        return len(original) - len(kept)
        def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Motor incremental de flashcards SIP AI RAG")
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS, help="Raíz documental a recorrer (por defecto, raíz del repositorio)")
    parser.add_argument("--state", type=Path, default=STATE_PATH)
    parser.add_argument("--candidates", type=Path, default=CANDIDATES_PATH)
    sub = parser.add_subparsers(dest="command", required=True)

    process = sub.add_parser("process", help="Procesa documentos nuevos o modificados")
    process.add_argument("--force", action="store_true", help="Reprocesa todos los documentos")
    process.add_argument("--limit-per-chunk", type=int, default=6)
    process.add_argument("--dry-run", action="store_true")
    process.add_argument("--limit-documents", type=int)

    sub.add_parser("stats", help="Estadísticas de candidatos")

    review = sub.add_parser("review", help="Registrar decisión humana")
    review.add_argument("card_id")
    review.add_argument("decision", choices=["approve", "reject"])
    review.add_argument("--reviewer", required=True)
    review.add_argument("--note", default="")
    review.add_argument("--force", action="store_true", help="Aprueba duplicado potencial tras revisión explícita")

    export = sub.add_parser("export", help="Exporta tarjetas aprobadas")
    export.add_argument("--output", type=Path, default=EXPORT_PATH)

    prune = sub.add_parser("prune", help="Elimina historial supersedido/rechazado antiguo")
    prune.add_argument("--keep-days", type=int, default=90)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "process":
            if args.limit_per_chunk < 1:
                raise ValueError("--limit-per-chunk debe ser mayor que cero.")
            result = process_corpus(
                args.corpus,
                args.force,
                args.limit_per_chunk,
                args.state,
                args.candidates,
                args.dry_run,
                args.limit_documents,
            )
        elif args.command == "stats":
            result = stats(args.candidates, args.state)
        elif args.command == "review":
            card = review_card(
                args.card_id,
                args.decision,
                args.reviewer,
                args.note,
                args.candidates,
                args.force,
            )
            result = {"card_id": card["card_id"], "status": card["status"]}
        elif args.command == "export":
            count = export_approved(args.output, args.candidates)
            result = {"exported": count, "output": str(args.output)}
        else:
            result = {"pruned": prune_candidates(args.candidates, args.keep_days)}

        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
