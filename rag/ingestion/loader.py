from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

SUPPORTED_EXTENSIONS = {".txt", ".md", ".json", ".pdf"}


@dataclass(frozen=True)
class Document:
    document_id: str
    source_path: str
    title: str
    text: str
    metadata: dict | None = None


def _sidecar_metadata(path: Path) -> dict:
    """Carga metadata documental opcional junto al archivo de conocimiento."""
    candidates = [
        path.with_suffix(".metadata.json"),
        path.with_name(f"{path.stem}.json"),
    ]
    for candidate in candidates:
        if candidate.exists() and candidate != path:
            try:
                data = json.loads(candidate.read_text(encoding="utf-8"))
                if isinstance(data, dict):
                    return data
            except (OSError, json.JSONDecodeError):
                pass
    return {}


def _pdf_text(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RuntimeError("Instale pypdf para ingerir PDF.") from exc

    reader = PdfReader(str(path))
    pages: list[str] = []
    for number, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        if text:
            pages.append(f"[[PAGINA {number}]]\n{text}")
    return "\n\n".join(pages)


def load_document(path: str | Path) -> Document:
    file_path = Path(path)
    suffix = file_path.suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Formato no soportado: {suffix}")

    metadata: dict | None = None

    if suffix == ".json":
        data = json.loads(file_path.read_text(encoding="utf-8"))
        metadata = data if isinstance(data, dict) else None
        text = json.dumps(data, ensure_ascii=False, indent=2)
        document_id = str((metadata or {}).get("id") or file_path.stem)
        title = str((metadata or {}).get("titulo") or file_path.stem)

    elif suffix == ".pdf":
        text = _pdf_text(file_path)
        metadata = _sidecar_metadata(file_path)
        metadata = {
            **metadata,
            "tipo_fuente": "pdf",
            "archivo": file_path.name,
        }
        document_id = str(metadata.get("id") or file_path.stem)
        title = str(metadata.get("titulo") or file_path.stem.replace("-", " "))

    else:
        text = file_path.read_text(encoding="utf-8")
        metadata = _sidecar_metadata(file_path) or None
        document_id = str((metadata or {}).get("id") or file_path.stem)
        title = str(
            (metadata or {}).get("titulo")
            or file_path.stem.replace("-", " ").replace("_", " ")
        )

    text = text.strip()
    if not text:
        raise ValueError(f"Documento vacío o sin texto extraíble: {file_path}")

    return Document(
        document_id=document_id,
        source_path=str(file_path),
        title=title,
        text=text,
        metadata=metadata,
    )


def load_directory(path: str | Path) -> list[Document]:
    directory = Path(path)
    if not directory.exists():
        return []

    documents: list[Document] = []
    for file_path in sorted(directory.rglob("*")):
        if not file_path.is_file() or file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
        # Un sidecar acompaña al documento; no debe indexarse como documento independiente.
        if file_path.name.endswith(".metadata.json"):
            continue
        try:
            documents.append(load_document(file_path))
        except ValueError:
            continue
    return documents
