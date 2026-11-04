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
VISOR_PATH = ROOT / "data/metadata/flashcards_visor.json"
PROMPTS_PATH = ROOT / "data/metadata/flashcards_prompts_escena.json"
CATALOG_PATH = ROOT / "data/metadata/catalog.json"
FUENTES_PATH = ROOT / "data/metadata/flashcards_fuentes.json"  # {"incluir": ["normas/serums/*.json", ...]} (rutas relativas a knowledge/)
MAX_CARDS_PER_DOC = int(os.getenv("FLASHCARD_MAX_PER_DOC", "10"))  # tope de fichas candidatas por norma/documento
OTROS = "Otros"  # fichas válidas que no encajan en los 5 ejes
CITAS_PATH = ROOT / "data/metadata/citas_oficiales.json"  # opcional: {"<document_id o id_fuente_oficial>": "Cita oficial"}
SCENES_DIR = ROOT / "data/flashcards/escenas"
RENDER_DIR = ROOT / "data/flashcards/render"
LOGO_PATH = Path(os.getenv("FLASHCARD_LOGO", str(ROOT / "data/flashcards/logo.png")))
# Numeración secuencial: la primera ficha aprobada recibe este número (las fichas 01-76 ya existen en el visor).
START_NUMBER = int(os.getenv("FLASHCARD_START_NUMBER", "77"))

def _load_env_file() -> None:
    """Carga .env de la raíz del proyecto si existe, sin dependencias externas.

    No sobrescribe variables ya exportadas en el entorno.
    """
    env_file = ROOT / ".env"
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


_load_env_file()

AXES = (  # mismos nombres que el visor de SERUM-APP
    "Cuidado integral de salud",
    "Salud pública",
    "Ética e interculturalidad",
    "Gestión de servicios de salud",
    "Investigación",
)
AXIS_COLORS = {
    "Salud pública": (47, 143, 114),
    "Cuidado integral de salud": (23, 107, 135),
    "Ética e interculturalidad": (123, 79, 163),
    "Gestión de servicios de salud": (184, 101, 26),
    "Investigación": (192, 57, 43),
    OTROS: (95, 99, 104),
}
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


def canon_axis(value: Any) -> str | None:
    """Devuelve el nombre oficial del eje (acepta mayúsculas/tildes distintas) o None si no existe."""
    if value is None:
        return None
    key = normalize(str(value))
    for axis in AXES:
        if normalize(axis) == key:
            return axis
    return None


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
    provider = os.getenv("FLASHCARD_PROVIDER", "").strip().lower()
    if not provider:  # auto-detección: NVIDIA primero (stack del proyecto), luego OpenAI
        provider = "nvidia" if os.getenv("NVIDIA_API_KEY") else "openai"
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
        raise RuntimeError(
            f"Falta {key_name}. Configure NVIDIA_API_KEY u OPENAI_API_KEY antes de procesar."
        )
    body: dict[str, Any] = {"model": cfg["model"], "messages": messages, "temperature": temperature,
                            "max_tokens": max_tokens, "stream": False}
    if cfg["provider"] == "nvidia-nim" and os.getenv("FLASHCARD_THINKING", "0") != "1":
        # Nemotron 3.5 razona por defecto y puede gastar todos los tokens sin escribir la respuesta.
        body["chat_template_kwargs"] = {"enable_thinking": False}
    payload = json.dumps(body, ensure_ascii=False).encode("utf-8")
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
        finish = data["choices"][0].get("finish_reason")
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Respuesta Chat Completions no reconocida: {str(data)[:500]}") from exc
    if content is None or (isinstance(content, str) and not content.strip()):
        raise RuntimeError(f"La IA devolvió una respuesta vacía (finish_reason={finish}).")
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
        "Cada tarjeta: title, topic, question, answer, dato_clave, error_frecuente, aplicacion_serums, "
        "explanation, type, axis, subaxis, evidence_quote, confidence. "
        "Longitudes máximas (la ficha es una imagen y el texto debe caber): title 6 palabras; topic 8 palabras; "
        "question 140 caracteres; answer 200; dato_clave 150; error_frecuente 150; aplicacion_serums 160. "
        "dato_clave, error_frecuente y aplicacion_serums deben deducirse directamente del fragmento; "
        "si el fragmento no los respalda, usa null (nunca los inventes). "
        "type debe ser uno de: conceptual, comparativa, procedimental, secuencial, aplicada, evaluacion. "
        "axis debe ser exactamente uno de: Cuidado integral de salud; Salud pública; Ética e interculturalidad; "
        "Gestión de servicios de salud; Investigación. Si el tema es válido pero no encaja en ninguno, usa \"Otros\". "
        "La cita evidence_quote debe ser una cita literal y continua del texto proporcionado. "
        "No cites nombres ni números de archivo como fuente; la cita oficial de la norma la asigna el motor. "
        "No conviertas preguntas de un banco ni respuestas existentes en tarjetas que revelen respuestas sin contexto. "
        "Incluye distractores solo si están en la fuente. confidence: alta, media o baja."
    )
    user = "Genera como máximo " + str(limit) + " tarjetas útiles, variadas y no redundantes. Formato: {\"cards\":[...]}.\n" + json.dumps(context, ensure_ascii=False)
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def _opt_text(raw: dict[str, Any], key: str) -> str | None:
    value = raw.get(key)
    if value is None:
        return None
    text = " ".join(str(value).split())
    return text if text and text.lower() != "null" else None


_TITULOS_GENERICOS = {"ministerio de salud", "congreso de la república", "presidencia del consejo de ministros", ""}
_RUIDO_TITULO = re.compile(r"\s*[-–]\s*Normas y documentos legales.*$|\s+Dirigid[oa]s?\b.*$|\s+Archivo\s*\d+.*$", re.IGNORECASE)
_TIPO_NORMA = (r"RESOLUCI[ÓO]N MINISTERIAL|RESOLUCI[ÓO]N VICEMINISTERIAL|DECRETO SUPREMO|DECRETO LEGISLATIVO|"
               r"DIRECTIVA ADMINISTRATIVA|NORMA T[ÉE]CNICA DE SALUD|NTS|LEY|R\.?M\.?|D\.?S\.?")
_NUM_NORMA = re.compile(r"\b(" + _TIPO_NORMA + r")\s*(?:N[°ºo.]{0,2}\s*)?(\d{1,5}(?:[-/]\d{2,4})?(?:[-/][A-ZÑ0-9]{2,12}){0,3})", re.IGNORECASE)
_NOMBRES = {"resolución ministerial": "Resolución Ministerial", "resolucion ministerial": "Resolución Ministerial",
            "resolución viceministerial": "Resolución Viceministerial", "resolucion viceministerial": "Resolución Viceministerial",
            "decreto supremo": "Decreto Supremo", "decreto legislativo": "Decreto Legislativo", "ley": "Ley",
            "directiva administrativa": "Directiva Administrativa", "norma técnica de salud": "NTS",
            "norma tecnica de salud": "NTS", "nts": "NTS", "rm": "Resolución Ministerial", "r.m.": "Resolución Ministerial",
            "ds": "Decreto Supremo", "d.s.": "Decreto Supremo"}


def limpiar_titulo(title: str) -> str:
    """Quita ruido de portal/archivo; nunca devuelve nombres de archivo ni números de repositorio."""
    t = _RUIDO_TITULO.sub("", " ".join(str(title or "").split())).strip(" .-–")
    return "" if t.lower() in _TITULOS_GENERICOS or re.fullmatch(r"[\d\-_. ]+", t) else t


def _cita_override(document: Any, meta: dict[str, Any]) -> str | None:
    data = read_json(CITAS_PATH, {})
    for key in (document.document_id, str(meta.get("id_fuente_oficial") or ""), str(meta.get("id") or "")):
        if key and str(data.get(key) or "").strip():
            return str(data[key]).strip()
    return None


def official_citation(document: Any) -> tuple[str, str, bool]:
    """(texto, método, oficial). Cita con el nombre oficial de la norma/documento, nunca el nombre del archivo."""
    meta = document.metadata or {}
    manual = _cita_override(document, meta)
    if manual:
        return manual, "manual", True
    nums = []
    for key in ("resolucion_aprobatoria", "numero_norma"):
        v = str(meta.get(key) or "").strip()
        if v and v.lower() != "none" and v not in nums:
            nums.append(v)
    if nums:
        return " — ".join(nums), "metadata", True
    titulo = limpiar_titulo(document.title) or limpiar_titulo(meta.get("titulo"))
    mt = _NUM_NORMA.match(titulo) if titulo else None
    if mt:  # el título oficial ya es la norma: "Resolución Ministerial N.° 534-2025-MINSA ..."
        return f"{_NOMBRES.get(mt.group(1).lower(), mt.group(1).title())} N.° {mt.group(2).upper()}", "titulo_norma", True
    head = " ".join(str(document.text or "")[:1800].split())
    mx = _NUM_NORMA.search(head[:300])
    if mx:  # derivado del encabezado del texto: requiere revisión humana
        return f"{_NOMBRES.get(mx.group(1).lower(), mx.group(1).title())} N.° {mx.group(2).upper()}", "texto_inicial", False
    anio = re.search(r"\b(19[89]\d|20[0-3]\d)\b", head)
    if titulo:
        return f"MINSA. {titulo.capitalize() if titulo.isupper() else titulo}" + (f" ({anio.group(1)})" if anio else ""), "titulo", False
    return "Documento oficial MINSA", "sin_dato", False


def build_normative_source(document: Any, page: int | None) -> dict[str, Any]:
    """Cita normativa oficial para la ficha (nunca el nombre del archivo ni su número de repositorio)."""
    meta = document.metadata or {}
    texto, metodo, oficial = official_citation(document)
    vigencia = str(meta.get("vigencia") or "VIGENCIA_NO_DETERMINADA").strip()
    partial = str(meta.get("verificacion_modificatorias") or "").strip().lower().startswith("parcial")
    return {
        "texto": texto,
        "documento": limpiar_titulo(document.title) or str(document.title).strip(),
        "pagina": page,
        "cita_metodo": metodo,
        "cita_oficial": oficial,
        "vigencia": vigencia,
        "por_confirmar": (not vigencia.upper().startswith("VIGENTE")) or partial,
    }


def validate_card(raw: dict[str, Any], document: Any, chunk: Any, provider: str, model: str) -> dict[str, Any] | None:
    question = str(raw.get("question", "")).strip()
    answer = str(raw.get("answer", "")).strip()
    evidence = str(raw.get("evidence_quote", "")).strip()
    kind = str(raw.get("type", "")).strip().lower()
    axis = canon_axis(raw.get("axis")) or OTROS
    axis_propuesto = None if canon_axis(raw.get("axis")) else (str(raw.get("axis")).strip()[:80] if raw.get("axis") else None)
    if not question or not answer or len(question) < 12 or len(answer) < 4:
        return None
    if kind not in CARD_TYPES:
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
    topic = _opt_text(raw, "topic")
    subaxis = str(raw.get("subaxis", "")).strip() or None
    dato_clave = _opt_text(raw, "dato_clave")
    error_frecuente = _opt_text(raw, "error_frecuente")
    aplicacion = _opt_text(raw, "aplicacion_serums")
    card = {
        "card_id": "fc_" + hashlib.sha256((document.document_id + chunk.chunk_id + question).encode("utf-8")).hexdigest()[:16],
        "numero": None,  # se asigna al aprobar (secuencial)
        "title": (_opt_text(raw, "title") or topic or subaxis or "Ficha SIP")[:80],
        "topic": topic or subaxis,
        "question": question, "answer": answer,
        "dato_clave": dato_clave,
        "error_frecuente": error_frecuente,
        "aplicacion_serums": aplicacion,
        "ficha_completa": bool(dato_clave and error_frecuente and aplicacion),
        "fuente_normativa": build_normative_source(document, page),
        "explanation": str(raw.get("explanation", "")).strip(),
        "type": kind, "axis": axis, "axis_propuesto_modelo": axis_propuesto,
        "subaxis": subaxis,
        "confidence": str(raw.get("confidence", "media")).lower(),
        "evidence": {"quote": evidence, "provenance": provenance},
        "source_sha256": None,
        "provider": provider, "model": model,
        "nota_revision": "Campos dato_clave, error_frecuente y aplicacion_serums: análisis propio, clasificación por IA pendiente de revisión humana.",
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


def allowed_documents(corpus: Path) -> set[Path]:
    """Solo se generan fichas desde documentos del catálogo (normas validadas) o de flashcards_fuentes.json."""
    allowed: set[Path] = set()
    for entry in read_json(CATALOG_PATH, {}).get("documentos", []):
        ruta = str(entry.get("ruta") or "")
        if ruta.startswith("knowledge/") and ruta.endswith(".metadata.json"):
            base = ROOT / ruta[: -len(".metadata.json")]
            for ext in SUPPORTED_EXTENSIONS:
                if base.with_suffix(ext).is_file():
                    allowed.add(base.with_suffix(ext).resolve())
                    break
    for pattern in read_json(FUENTES_PATH, {}).get("incluir", []):
        for found in corpus.glob(str(pattern)):
            if found.is_file() and found.suffix.lower() in SUPPORTED_EXTENSIONS and not found.name.endswith(".metadata.json"):
                allowed.add(found.resolve())
    return allowed


def process_corpus(corpus: Path = DEFAULT_CORPUS, force: bool = False, limit_per_chunk: int = 6, max_per_doc: int = MAX_CARDS_PER_DOC,
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

    allowed = allowed_documents(corpus)
    if not allowed:
        raise RuntimeError("No hay documentos permitidos: revise data/metadata/catalog.json y data/metadata/flashcards_fuentes.json.")
    for path in discover_documents(corpus):
        if path.resolve() not in allowed:
            continue
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
            # Muestreo repartido por todo el documento (orden determinista) y tope de fichas por norma.
            for chunk in sorted(chunks, key=lambda c: hashlib.sha256(c.chunk_id.encode("utf-8")).hexdigest()):
                remaining = max_per_doc - len(new_cards)
                if remaining <= 0:
                    break
                content, provider, model = call_chat(generation_prompt(chunk, document, min(limit_per_chunk, remaining)))
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
                    if len(new_cards) < max_per_doc:
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
        "by_axis": dict(Counter(c.get("axis") or "unclassified" for c in cards)),
        "by_type": dict(Counter(c.get("type", "unknown") for c in cards)),
        "documents_in_state": len(read_json(state_path, {"documents": {}}).get("documents", {})),
    }


def next_number(cards: Iterable[dict[str, Any]]) -> int:
    """Siguiente número secuencial de ficha (nunca reutiliza números ya asignados)."""
    used = [int(c["numero"]) for c in cards if str(c.get("numero") or "").isdigit()]
    return max(used + [START_NUMBER - 1]) + 1


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
    if decision == "approve" and not found.get("numero"):
        found["numero"] = next_number(data.get("cards", []))
    found["review"] = {"decision": decision, "reviewer": reviewer.strip(), "note": note.strip(), "reviewed_at": utc_now()}
    atomic_json(candidates_path, data)
    return found


def export_approved(output: Path = EXPORT_PATH, candidates_path: Path = CANDIDATES_PATH) -> int:
    data = read_json(candidates_path, {"cards": []})
    approved = [card for card in data.get("cards", []) if card.get("status") == "approved"]
    atomic_json(output, {"schema_version": 1, "generated_at": utc_now(), "count": len(approved), "cards": approved})
    return len(approved)


# ---------------------------------------------------------------------------
# Ficha visual: la IA de imágenes (DALL·E 3) dibuja SOLO la escena; todo el texto
# se escribe con código desde el JSON aprobado, para que nunca salga con errores.
# ---------------------------------------------------------------------------
REGIONES = (
    {"region": "costa",
     "rasgos": ("de tez trigueña", "de ascendencia afroperuana"),
     "detalle": "uniforme clínico turquesa con bata blanca y un detalle costeño discreto (pañuelo de colores o pequeño collar de conchitas)",
     "lugar": "un establecimiento de salud en la costa peruana, con palmeras, cielo azul brillante, malecón y mar al fondo, paredes de colores"},
    {"region": "sierra",
     "rasgos": ("de origen andino quechua", "de origen andino aymara"),
     "detalle": "uniforme clínico con una lliclla (manta andina tejida en rojo, magenta y turquesa) sobre los hombros",
     "lugar": "un puesto de salud de adobe y techo de teja entre cerros andinos, con andenes verdes, cielo azul intenso y llamas a lo lejos"},
    {"region": "selva",
     "rasgos": ("de un pueblo originario amazónico", "de origen mestizo ribereño amazónico"),
     "detalle": "uniforme clínico con un collar de semillas y bordados geométricos de patrón amazónico, sin tocados de plumas",
     "lugar": "un puesto de salud amazónico de madera sobre pilotes junto a un río, con vegetación tropical exuberante, una canoa y cielo luminoso"},
)
PERFILES = (
    ("médica", "mujer"), ("enfermero", "hombre"), ("obstetra", "mujer"),
    ("nutricionista", "hombre"), ("odontóloga", "mujer"), ("tecnólogo médico", "hombre"),
)


def scene_prompt(card: dict[str, Any]) -> dict[str, str]:
    """Texto base para DALL·E 3: solo escena y personaje, sin ningún texto en la imagen."""
    n = int(card["numero"])
    zona = REGIONES[n % 3]
    profesion, genero = PERFILES[(n // 3) % 6]
    rasgos = zona["rasgos"][(n // 6) % 2]
    contexto = str(card.get("topic") or card.get("title") or "atención en salud")
    prompt = (
        "Ilustración 3D estilo película de animación (personaje 3D de formas redondeadas y texturas suaves), "
        "colores vivos y saturados, iluminación cálida y luminosa. Formato horizontal 16:9 (1792x1024). "
        f"Personaje: {profesion} ({genero}) de la {zona['region']} del Perú, {rasgos}, profesional de la salud con "
        f"{zona['detalle']}; sonriente, con gesto didáctico; representación respetuosa y digna, sin caricatura ni estereotipos. "
        f"Escenario: {zona['lugar']}. "
        f"Contexto visual de la ficha (solo ambientación): {contexto}. "
        "Composición: personaje de medio cuerpo en el tercio izquierdo y en la mitad superior de la imagen; fondo detallado detrás; "
        "el resto de la imagen con elementos sencillos y de poco contraste, porque se cubrirá con paneles de texto. "
        "REGLAS ESTRICTAS: NO incluir texto, letras, números, palabras, carteles legibles, logotipos ni marcas de agua en ninguna parte; "
        "los rótulos, pizarras y señales deben quedar en blanco; sin marcos ni paneles ni cuadros de información."
    )
    return {"region": zona["region"], "perfil": f"{profesion} ({genero}), {rasgos}", "prompt": prompt}


def approved_numbered(candidates_path: Path = CANDIDATES_PATH) -> list[dict[str, Any]]:
    cards = read_json(candidates_path, {"cards": []}).get("cards", [])
    found = [c for c in cards if c.get("status") == "approved" and c.get("numero")]
    return sorted(found, key=lambda c: int(c["numero"]))


def card_number(card: dict[str, Any]) -> str:
    return f"{int(card['numero']):02d}"


def export_visor(output: Path = VISOR_PATH, candidates_path: Path = CANDIDATES_PATH) -> int:
    """Entradas listas para pegar en el arreglo `flashcards` del visor de SERUM-APP."""
    entries = []
    for card in approved_numbered(candidates_path):
        ready = bool(card.get("axis"))
        entry = {
            "archivo": f"sip-serums-ficha-{card_number(card)}.png",
            "codigo": card_number(card),
            "titulo": card.get("title") or "Ficha SIP",
            "tema": card.get("topic") or card.get("subaxis") or "",
            "eje": card.get("axis"),
            "estado": "CONFIRMADO" if ready else "REVISAR",
        }
        if not ready:
            entry["nota"] = "La ficha no tiene eje determinado; requiere revisión manual."
        entries.append(entry)
    atomic_json(output, {"schema_version": 1, "generated_at": utc_now(), "count": len(entries), "flashcards": entries})
    return len(entries)


def export_prompts(output: Path = PROMPTS_PATH, candidates_path: Path = CANDIDATES_PATH) -> int:
    items = []
    for card in approved_numbered(candidates_path):
        info = scene_prompt(card)
        items.append({"numero": card_number(card), "card_id": card["card_id"],
                      "archivo_escena": f"{card_number(card)}.png", **info})
    atomic_json(output, {"schema_version": 1, "generated_at": utc_now(), "count": len(items), "prompts": items})
    return len(items)


def _font_path(bold: bool) -> str:
    env = os.getenv("FLASHCARD_FONT_BOLD" if bold else "FLASHCARD_FONT_REGULAR", "").strip()
    if env and Path(env).is_file():
        return env
    names = (("DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf", "NotoSans-Bold.ttf", "arialbd.ttf") if bold
             else ("DejaVuSans.ttf", "LiberationSans-Regular.ttf", "NotoSans-Regular.ttf", "arial.ttf"))
    folders = ("/usr/share/fonts/truetype/dejavu", "/usr/share/fonts/truetype/liberation",
               "/usr/share/fonts/truetype/noto", "/usr/share/fonts/dejavu", "/Library/Fonts", "C:/Windows/Fonts")
    for folder in folders:
        for name in names:
            candidate = Path(folder) / name
            if candidate.is_file():
                return str(candidate)
    raise RuntimeError("No se encontró una fuente TrueType con tildes. Defina FLASHCARD_FONT_BOLD y FLASHCARD_FONT_REGULAR.")


def _wrap(draw: Any, text: str, font: Any, max_w: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def _fit(draw: Any, text: str, path: str, max_w: int, max_h: int, size: int, min_size: int) -> tuple[Any, list[str], bool]:
    """Ajusta el tamaño de letra para que el texto COMPLETO quepa; avisa si hubo que recortar."""
    from PIL import ImageFont
    current = size
    while current >= min_size:
        font = ImageFont.truetype(path, current)
        lines = _wrap(draw, text, font, max_w)
        if len(lines) * int(current * 1.2) <= max_h and all(draw.textlength(line, font=font) <= max_w for line in lines):
            return font, lines, False
        current -= 2
    font = ImageFont.truetype(path, min_size)
    lines = _wrap(draw, text, font, max_w)
    keep = max(1, max_h // int(min_size * 1.2))
    lines = lines[:keep]
    while lines and draw.textlength(lines[-1] + "…", font=font) > max_w:
        lines[-1] = lines[-1].rsplit(" ", 1)[0] if " " in lines[-1] else lines[-1][:-1]
    lines[-1] = lines[-1] + "…"
    return font, lines, True


def render_card(card: dict[str, Any], scene_path: Path, out_path: Path, logo_path: Path | None = None) -> list[str]:
    """Compone la ficha final: escena (imagen IA) + encabezado, paneles y textos escritos por código."""
    from PIL import Image, ImageDraw, ImageFont
    W, H = 1792, 1024
    regular, bold = _font_path(False), _font_path(True)
    scene = Image.open(scene_path).convert("RGB")
    k = max(W / scene.width, H / scene.height)
    scene = scene.resize((int(scene.width * k + 0.5), int(scene.height * k + 0.5)), Image.LANCZOS)
    left, top = (scene.width - W) // 2, (scene.height - H) // 2
    canvas = scene.crop((left, top, left + W, top + H)).convert("RGBA")

    navy, ink = (11, 47, 107), (21, 50, 74)
    axis = card.get("axis")
    axis_color = AXIS_COLORS.get(axis, (138, 153, 163))
    fuente = card.get("fuente_normativa") or {}
    extras = [(label, color, card.get(key)) for label, color, key in (
        ("DATO CLAVE", (230, 126, 34), "dato_clave"),
        ("ERROR FRECUENTE", (192, 57, 43), "error_frecuente"),
        ("APLICACIÓN SERUMS", (123, 79, 163), "aplicacion_serums")) if card.get(key)]

    x0, x1 = 760, W - 24
    panels: list[dict[str, Any]] = [
        {"box": (x0, 126, x1, 306), "label": "PREGUNTA", "color": (23, 107, 210), "text": card["question"], "size": 40, "min": 26},
        {"box": (x0, 364, x1, 588 if extras else 912), "label": "RESPUESTA", "color": (47, 143, 114), "text": card["answer"],
         "size": 40, "min": 26},
    ]
    if extras:
        gap = 16
        width = (W - 48 - gap * (len(extras) - 1)) // len(extras)
        for i, (label, color, text) in enumerate(extras):
            bx = 24 + i * (width + gap)
            panels.append({"box": (bx, 600, bx + width, 912), "label": label, "color": color, "text": text, "size": 36, "min": 24})

    # Pasada 1: formas translúcidas sobre la escena
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    d.rectangle((0, 0, W, 110), fill=navy + (246,))
    d.rounded_rectangle((20, 12, 330, 98), radius=16, fill=(255, 255, 255, 255))
    d.rounded_rectangle((350, 14, 470, 96), radius=14, fill=(255, 208, 0, 255))
    d.rounded_rectangle((x0, 314, x1, 356), radius=21, fill=axis_color + (255,))
    d.rectangle((0, 924, W, H), fill=navy + (246,))
    for panel in panels:
        bx0, by0, bx1, by1 = panel["box"]
        d.rounded_rectangle(panel["box"], radius=18, fill=(255, 255, 255, 240), outline=panel["color"] + (255,), width=4)
        d.rounded_rectangle((bx0, by0, bx1, by0 + 44), radius=18, fill=panel["color"] + (255,))
        d.rectangle((bx0, by0 + 26, bx1, by0 + 44), fill=panel["color"] + (255,))
    canvas = Image.alpha_composite(canvas, overlay).convert("RGB")

    # Pasada 2: todo el texto (nítido y exacto)
    t = ImageDraw.Draw(canvas)
    warnings: list[str] = []
    logo_file = logo_path if logo_path is not None else LOGO_PATH
    if logo_file and Path(logo_file).is_file():
        logo = Image.open(logo_file).convert("RGBA")
        logo.thumbnail((290, 70))
        canvas.paste(logo, (30 + (290 - logo.width) // 2, 55 - logo.height // 2), logo)
    else:
        t.text((30, 24), "SIP SERUMS PERÚ", font=ImageFont.truetype(bold, 26), fill=navy)
        t.text((30, 62), "Tu aliado en el SERUMS", font=ImageFont.truetype(regular, 22), fill=(60, 80, 100))
    number = card_number(card)
    nf = ImageFont.truetype(bold, 58)
    t.text((410 - t.textlength(number, font=nf) / 2, 55), number, font=nf, fill=navy, anchor="lm")
    font, lines, cut = _fit(t, str(card.get("title") or "Ficha SIP"), bold, W - 500 - 30, 92, 56, 32)
    if cut:
        warnings.append("title")
    ty = 55 - (len(lines) * int(font.size * 1.2)) // 2
    for line in lines:
        t.text((500, ty), line, font=font, fill=(255, 255, 255))
        ty += int(font.size * 1.2)
    ef = ImageFont.truetype(bold, 26)
    t.text((x0 + 18, 335), f"EJE TEMÁTICO · {axis or 'Eje por revisar'}", font=ef, fill=(255, 255, 255), anchor="lm")
    for panel in panels:
        bx0, by0, bx1, by1 = panel["box"]
        t.text((bx0 + 18, by0 + 22), panel["label"], font=ImageFont.truetype(bold, 26), fill=(255, 255, 255), anchor="lm")
        font, lines, cut = _fit(t, str(panel["text"]), regular, bx1 - bx0 - 36, by1 - by0 - 44 - 22, panel["size"], panel["min"])
        if cut:
            warnings.append(panel["label"].lower())
        ty = by0 + 44 + 12
        for line in lines:
            t.text((bx0 + 18, ty), line, font=font, fill=ink)
            ty += int(font.size * 1.2)
    source = "Fuente: " + str(fuente.get("texto") or "Documento oficial MINSA")
    if fuente.get("pagina"):
        source += f" (p. {fuente['pagina']})"
    if fuente.get("cita_oficial") is False:
        warnings.append("cita_no_oficial")
    font, lines, cut = _fit(t, source, bold, W - 48, 56, 28, 18)
    if cut:
        warnings.append("fuente")
    ty = 932
    for line in lines:
        t.text((24, ty), line, font=font, fill=(255, 255, 255))
        ty += int(font.size * 1.2)
    t.text((24, 990), "Material pedagógico. No sustituye la norma oficial vigente.   © SIP SERUMS PERÚ",
           font=ImageFont.truetype(regular, 22), fill=(255, 208, 0))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_path, "PNG", optimize=True)
    return warnings


def render_all(scenes: Path = SCENES_DIR, out_dir: Path = RENDER_DIR, candidates_path: Path = CANDIDATES_PATH) -> dict[str, Any]:
    rendered: list[str] = []
    missing: list[str] = []
    warnings: dict[str, list[str]] = {}
    for card in approved_numbered(candidates_path):
        number = card_number(card)
        scene = next((scenes / f"{number}{ext}" for ext in (".png", ".jpg", ".jpeg", ".webp") if (scenes / f"{number}{ext}").is_file()), None)
        if scene is None:
            missing.append(number)
            continue
        problems = render_card(card, scene, out_dir / f"sip-serums-ficha-{number}.png")
        if problems:
            warnings[number] = problems
        rendered.append(number)
    return {"rendered": rendered, "missing_scene": missing, "text_cut_warnings": warnings}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Motor incremental de flashcards SIP AI RAG")
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS, help="Directorio raíz del corpus (default: knowledge/)")
    parser.add_argument("--state", type=Path, default=STATE_PATH)
    parser.add_argument("--candidates", type=Path, default=CANDIDATES_PATH)
    sub = parser.add_subparsers(dest="command", required=True)
    process = sub.add_parser("process", help="Procesa documentos nuevos o modificados")
    process.add_argument("--force", action="store_true", help="Reprocesa todos los documentos")
    process.add_argument("--limit-per-chunk", type=int, default=6)
    process.add_argument("--max-per-doc", type=int, default=MAX_CARDS_PER_DOC, help="Tope de fichas por norma (default 10)")
    sub.add_parser("stats", help="Estadísticas de candidatos")
    review = sub.add_parser("review", help="Registrar decisión humana")
    review.add_argument("card_id")
    review.add_argument("decision", choices=["approve", "reject"])
    review.add_argument("--reviewer", required=True)
    review.add_argument("--note", default="")
    export = sub.add_parser("export", help="Exporta tarjetas aprobadas")
    export.add_argument("--output", type=Path, default=EXPORT_PATH)
    visor = sub.add_parser("export-visor", help="Entradas para el visor de SERUM-APP (fichas aprobadas y numeradas)")
    visor.add_argument("--output", type=Path, default=VISOR_PATH)
    prompts = sub.add_parser("prompts", help="Texto base para DALL·E 3 (solo escena, sin texto)")
    prompts.add_argument("--output", type=Path, default=PROMPTS_PATH)
    render = sub.add_parser("render", help="Compone la ficha final: escena + textos escritos por código")
    render.add_argument("--scenes", type=Path, default=SCENES_DIR, help="Carpeta con las escenas NN.png")
    render.add_argument("--out", type=Path, default=RENDER_DIR)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "process":
            if args.limit_per_chunk < 1:
                raise ValueError("--limit-per-chunk debe ser mayor que cero.")
            result = process_corpus(args.corpus, args.force, args.limit_per_chunk, args.max_per_doc, args.state, args.candidates)
        elif args.command == "stats":
            result = stats(args.candidates, args.state)
        elif args.command == "review":
            card = review_card(args.card_id, args.decision, args.reviewer, args.note, args.candidates)
            result = {"card_id": card["card_id"], "status": card["status"], "numero": card.get("numero")}
        elif args.command == "export-visor":
            result = {"exported": export_visor(args.output, args.candidates), "output": str(args.output)}
        elif args.command == "prompts":
            result = {"prompts": export_prompts(args.output, args.candidates), "output": str(args.output)}
        elif args.command == "render":
            result = render_all(args.scenes, args.out, args.candidates)
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
