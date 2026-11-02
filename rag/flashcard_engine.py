#!/usr/bin/env python3
"""Motor incremental de flashcards para SIP AI RAG.

No modifica el pipeline RAG. Reutiliza rag.ingestion.loader y
rag.chunking.chunker; mantiene candidatos separados del estado incremental.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = ROOT / "knowledge"
STATE_PATH = ROOT / "data/metadata/flashcard_engine_state.json"
CANDIDATES_PATH = ROOT / "data/metadata/flashcard_candidates.json"
EXPORT_PATH = ROOT / "data/metadata/flashcards_approved.json"

AXES = (
    "Cuidado Integral de Salud",
    "Salud Pública",
    "Ética e Interculturalidad",
    "Gestión de Servicios de Salud",
    "Investigación",
)
CARD_TYPES = (
    "conceptual", "comparativa", "procedimental",
    "secuencial", "aplicada", "evaluacion",
)

try:
    from rag.ingestion.loader import load_document, SUPPORTED_EXTENSIONS
    from rag.chunking.chunker import chunk_document
except ImportError:  # permite ejecutar `python rag/flashcard_engine.py` desde raíz
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from rag.ingestion.loader import load_document, SUPPORTED_EXTENSIONS
    from rag.chunking.chunker import chunk_document


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"No se pudo leer JSON válido en {path}: {exc}") from exc


def atomic_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value.casefold())
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def fingerprint(card: dict[str, Any]) -> str:
    basis = normalize(str(card.get("question", ""))) + "|" + normalize(str(card.get("answer", "")))
    return hashlib.sha256(basis.encode("utf-8")).hexdigest()


def token_similarity(left: str, right: str) -> float:
    a, b = set(normalize(left).split()), set(normalize(right).split())
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def find_duplicate(card: dict[str, Any], existing: Iterable[dict[str, Any]], threshold: float = 0.90) -> dict[str, Any] | None:
    fp = fingerprint(card)
    for other in existing:
        if other.get("fingerprint") == fp:
            return {"card_id": other.get("card_id"), "method": "sha256_exact"}
        score = token_similarity(str(card.get("question", "")), str(other.get("question", "")))
        if score >= threshold:
            return {"card_id": other.get("card_id"), "method": "question_jaccard", "similarity": round(score, 4)}
    return None


def extract_location(text: str, metadata: dict[str, Any] | None) -> tuple[int | None, str | None]:
    metadata = metadata or {}
    page = metadata.get("pagina") or metadata.get("page")
    section = metadata.get("apartado") or metadata.get("seccion") or metadata.get("section")
    if page is None:
        match = re.search(r"\[\[PAGINA\s+(\d+)\]\]", text, re.IGNORECASE)
        if match:
            page = int(match.group(1))
    if not section:
        for line in text.splitlines():
            candidate = line.strip().strip("# ")
            if candidate.startswith("[[PAGINA"):
                continue
            if candidate.startswith("#") or re.match(r"^(?:\d+(?:\.\d+)*\s+)[A-ZÁÉÍÓÚÑ]", candidate):
                section = candidate[:240]
                break
    try:
        page = int(page) if page is not None else None
    except (TypeError, ValueError):
        page = None
    return page, str(section) if section else None


def provider_config() -> dict[str, str]:
    provider = os.getenv("FLASHCARD_PROVIDER", "openai").strip().lower()
    if provider in {"nvidia", "nvidia-nim"}:
        return {
            "provider": "nvidia-nim",
            "api_key": os.getenv("NVIDIA_API_KEY", ""),
            "base_url": os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1"),
            "model": os.getenv("NVIDIA_MODEL", "nvidia/nemotron-3.5-lightning-30b-a3b"),
        }
    return {
        "provider": "openai-compatible",
        "api_key": os.getenv("OPENAI_API_KEY", ""),
        "base_url": os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
        "model": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    }


def call_chat(messages: list[dict[str, str]], temperature: float = 0.15, max_tokens: int = 1800) -> tuple[str, str, str]:
    cfg = provider_config()
    if not cfg["api_key"]:
        key_name = "NVIDIA_API_KEY" if cfg["provider"] == "nvidia-nim" else "OPENAI_API_KEY"
        raise RuntimeError(f"Falta {key_name}. Configure proveedor y credenciales antes de procesar.")
    payload = json.dumps({"model": cfg["model"], "messages": messages, "temperature": temperature,
                          "max_tokens": max_tokens, "stream": False}, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        cfg["base_url"].rstrip("/") + "/chat/completions", data=payload,
        headers={"Authorization": f"Bearer {cfg['api_key']}", "Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    timeout = float(os.getenv("FLASHCARD_TIMEOUT_SECONDS", "90"))
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Fallo del proveedor {cfg['provider']}: {exc}") from exc
    try:
        content = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Respuesta Chat Completions no reconocida: {str(data)[:500]}") from exc
    if isinstance(content, list):
        content = "".join(part.get("text", "") for part in content if isinstance(part, dict))
    return str(content), cfg["provider"], cfg["model"]


def parse_json_response(content: str) -> dict[str, Any]:
    text = content.strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.IGNORECASE)
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start < 0 or end <= start:
            raise ValueError("El proveedor no devolvió un objeto JSON.")
        parsed = json.loads(text[start:end + 1])
    if not isinstance(parsed, dict) or not isinstance(parsed.get("cards"), list):
        raise ValueError("La respuesta debe contener un array 'cards'.")
    return parsed


def generation_prompt(chunk: Any, document: Any, limit: int) -> list[dict[str, str]]:
    metadata = document.metadata or {}
    context = {
        "document_id": document.document_id, "title": document.title,
        "source_path": document.source_path, "metadata": metadata,
        "chunk_index": chunk.chunk_index, "chunk_id": chunk.chunk_id,
        "text": chunk.text,
    }
    system = (
        "Eres un diseñador de flashcards clínicas y académicas para la preparación SERUMS Perú. "
        "Usa exclusivamente la evidencia del fragmento; no completes vacíos con conocimiento externo. "
        "No inventes cifras, puntos de corte, recomendaciones, dosis ni normas. Si la evidencia no permite "
        "una tarjeta sólida, devuelve menos tarjetas o ninguna. Responde SOLO JSON válido. "
        "Cada tarjeta: question, answer, explanation, type, axis, subaxis, evidence_quote, confidence. "
        "type debe ser uno de: conceptual, comparativa, procedimental, secuencial, aplicada, evaluacion. "
        "axis debe ser exactamente uno de: Cuidado Integral de Salud; Salud Pública; Ética e Interculturalidad; "
        "Gestión de Servicios de Salud; Investigación. Si no puede determinarse con evidencia, usa null. "
        "La cita evidence_quote debe ser una cita literal y continua del texto proporcionado. "
        "No conviertas preguntas de un banco ni respuestas existentes en tarjetas que revelen respuestas sin contexto. "
        "Incluye distractores solo si están en la fuente. confidence: alta, media o baja."
    )
    user = "Genera como máximo " + str(limit) + " tarjetas útiles, variadas y no redundantes. Formato: {\"cards\":[...]}.\n" + json.dumps(context, ensure_ascii=False)
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def validate_card(raw: dict[str, Any], document: Any, chunk: Any, provider: str, model: str) -> dict[str, Any] | None:
    question = str(raw.get("question", "")).strip()
    answer = str(raw.get("answer", "")).strip()
    evidence = str(raw.get("evidence_quote", "")).strip()
    kind = str(raw.get("type", "")).strip().lower()
    axis = raw.get("axis")
    if not question or not answer or len(question) < 12 or len(answer) < 4:
        return None
    if kind not in CARD_TYPES or axis not in AXES:
        return None
    # La evidencia debe aparecer literalmente en el chunk, normalizando solo espacios.
    source_compact = " ".join(chunk.text.split())
    quote_compact = " ".join(evidence.split())
    if not quote_compact or quote_compact not in source_compact:
        return None
    page, section = extract_location(chunk.text, chunk.metadata or document.metadata)
    provenance = {
        "document_id": document.document_id,
        "document_title": document.title,
        "source_path": str(document.source_path),
        "page": page,
        "section": section,
        "chunk_id": chunk.chunk_id,
        "chunk_index": chunk.chunk_index,
    }
    card = {
        "card_id": "fc_" + hashlib.sha256((document.document_id + chunk.chunk_id + question).encode("utf-8")).hexdigest()[:16],
        "question": question, "answer": answer,
        "explanation": str(raw.get("explanation", "")).strip(),
        "type": kind, "axis": axis,
        "subaxis": str(raw.get("subaxis", "")).strip() or None,
        "confidence": str(raw.get("confidence", "media")).lower(),
        "evidence": {"quote": evidence, "provenance": provenance},
        "source_sha256": None,
        "provider": provider, "model": model,
        "status": "pending_review", "review": None,
        "created_at": utc_now(),
    }
    card["fingerprint"] = fingerprint(card)
    return card


def discover_documents(corpus: Path) -> list[Path]:
    ignored = {".git", ".venv", "venv", "__pycache__", "node_modules"}
    files = []
    for path in corpus.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
        if any(part in ignored for part in path.parts) or path.name.endswith(".metadata.json") or path.name == "manifest.json":
            continue
        files.append(path)
    return sorted(files)


def process_corpus(corpus: Path = DEFAULT_CORPUS, force: bool = False, limit_per_chunk: int = 6,
                   state_path: Path = STATE_PATH, candidates_path: Path = CANDIDATES_PATH) -> dict[str, Any]:
    corpus = corpus.resolve()
    state = read_json(state_path, {"version": 1, "documents": {}, "updated_at": None})
    candidates_data = read_json(candidates_path, {"version": 1, "cards": []})
    cards: list[dict[str, Any]] = candidates_data.get("cards", [])
    if not isinstance(cards, list):
        raise RuntimeError("flashcard_candidates.json debe contener 'cards' como array.")
    by_source: dict[str, list[dict[str, Any]]] = {}
    for card in cards:
        source = (card.get("evidence") or {}).get("provenance", {}).get("source_path")
        if source:
            by_source.setdefault(str(source), []).append(card)
    processed = skipped = generated = duplicates = failed = 0
    document_state = state.setdefault("documents", {})

    for path in discover_documents(corpus):
        rel = path.relative_to(corpus).as_posix()
        digest = sha256_file(path)
        previous = document_state.get(rel, {})
        if not force and previous.get("sha256") == digest:
            skipped += 1
            continue
        try:
            document = load_document(path)
            chunks = chunk_document(document)
            new_cards: list[dict[str, Any]] = []
            for chunk in chunks:
                content, provider, model = call_chat(generation_prompt(chunk, document, limit_per_chunk))
                parsed = parse_json_response(content)
                for raw in parsed["cards"]:
                    if not isinstance(raw, dict):
                        continue
                    card = validate_card(raw, document, chunk, provider, model)
                    if not card:
                        continue
                    card["source_sha256"] = digest
                    duplicate = find_duplicate(card, cards + new_cards)
                    if duplicate:
                        card["duplicate_of"] = duplicate
                        card["status"] = "duplicate_review"
                        duplicates += 1
                    new_cards.append(card)
            # Mantener decisiones humanas previas como historial, marcando versión obsoleta.
            for old in by_source.get(str(path), []):
                if old.get("status") in {"approved", "rejected"}:
                    old["status_before_superseded"] = old["status"]
                old["status"] = "superseded"
                old["superseded_at"] = utc_now()
            cards.extend(new_cards)
            generated += len(new_cards)
            processed += 1
            document_state[rel] = {"sha256": digest, "document_id": document.document_id,
                                   "source_path": str(path), "chunks": len(chunks),
                                   "cards_generated": len(new_cards), "processed_at": utc_now()}
        except Exception as exc:  # no marcar hash exitoso cuando hubo fallo
            failed += 1
            print(f"ERROR {rel}: {exc}", file=sys.stderr)

    state["updated_at"] = utc_now()
    state["corpus_root"] = str(corpus)
    atomic_json(state_path, state)
    candidates_data["updated_at"] = utc_now()
    candidates_data["cards"] = cards
    atomic_json(candidates_path, candidates_data)
    return {"processed": processed, "skipped_unchanged": skipped, "generated": generated,
            "duplicates": duplicates, "failed": failed, "total_candidates": len(cards)}


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
                candidates_path: Path = CANDIDATES_PATH) -> dict[str, Any]:
    if decision not in {"approve", "reject"}:
        raise ValueError("La decisión debe ser approve o reject.")
    if not reviewer.strip():
        raise ValueError("Debe identificarse el revisor humano.")
    data = read_json(candidates_path, {"version": 1, "cards": []})
    found = None
    for card in data.get("cards", []):
        if card.get("card_id") == card_id:
            found = card
            break
    if found is None:
        raise KeyError(f"No existe tarjeta: {card_id}")
    if found.get("status") == "superseded":
        raise ValueError("No se puede revisar una tarjeta supersedida por una versión documental posterior.")
    found["status"] = "approved" if decision == "approve" else "rejected"
    found["review"] = {"decision": decision, "reviewer": reviewer.strip(), "note": note.strip(), "reviewed_at": utc_now()}
    atomic_json(candidates_path, data)
    return found


def export_approved(output: Path = EXPORT_PATH, candidates_path: Path = CANDIDATES_PATH) -> int:
    data = read_json(candidates_path, {"cards": []})
    approved = [card for card in data.get("cards", []) if card.get("status") == "approved"]
    atomic_json(output, {"schema_version": 1, "generated_at": utc_now(), "count": len(approved), "cards": approved})
    return len(approved)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Motor incremental de flashcards SIP AI RAG")
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS, help="Directorio raíz del corpus (default: knowledge/)")
    parser.add_argument("--state", type=Path, default=STATE_PATH)
    parser.add_argument("--candidates", type=Path, default=CANDIDATES_PATH)
    sub = parser.add_subparsers(dest="command", required=True)
    process = sub.add_parser("process", help="Procesa documentos nuevos o modificados")
    process.add_argument("--force", action="store_true", help="Reprocesa todos los documentos")
    process.add_argument("--limit-per-chunk", type=int, default=6)
    sub.add_parser("stats", help="Estadísticas de candidatos")
    review = sub.add_parser("review", help="Registrar decisión humana")
    review.add_argument("card_id")
    review.add_argument("decision", choices=["approve", "reject"])
    review.add_argument("--reviewer", required=True)
    review.add_argument("--note", default="")
    export = sub.add_parser("export", help="Exporta tarjetas aprobadas")
    export.add_argument("--output", type=Path, default=EXPORT_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "process":
            if args.limit_per_chunk < 1:
                raise ValueError("--limit-per-chunk debe ser mayor que cero.")
            result = process_corpus(args.corpus, args.force, args.limit_per_chunk, args.state, args.candidates)
        elif args.command == "stats":
            result = stats(args.candidates, args.state)
        elif args.command == "review":
            card = review_card(args.card_id, args.decision, args.reviewer, args.note, args.candidates)
            result = {"card_id": card["card_id"], "status": card["status"]}
        else:
            count = export_approved(args.output, args.candidates)
            result = {"exported": count, "output": str(args.output)}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
