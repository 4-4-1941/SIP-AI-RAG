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

def _pdf_text(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RuntimeError("Instale pypdf para ingerir PDF.") from exc
    reader = PdfReader(str(path))
    pages = []
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
    metadata = None
    if suffix == ".json":
        data = json.loads(file_path.read_text(encoding="utf-8"))
        metadata = data if isinstance(data, dict) else None
        text = json.dumps(data, ensure_ascii=False, indent=2)
        document_id = str((metadata or {}).get("id") or file_path.stem)
        title = str((metadata or {}).get("titulo") or file_path.stem)
    elif suffix == ".pdf":
        text = _pdf_text(file_path)
        document_id = file_path.stem
        title = file_path.stem.replace("-", " ")
        metadata = {"tipo_fuente": "pdf", "archivo": file_path.name}
    else:
        text = file_path.read_text(encoding="utf-8")
        document_id = file_path.stem
        title = file_path.stem.replace("-", " ").replace("_", " ")
    text = text.strip()
    if not text:
        raise ValueError(f"Documento vacío o sin texto extraíble: {file_path}")
    return Document(document_id, str(file_path), title, text, metadata)

def load_directory(path: str | Path) -> list[Document]:
    directory = Path(path)
    if not directory.exists(): return []
    documents = []
    for file_path in sorted(directory.rglob("*")):
        if file_path.is_file() and file_path.suffix.lower() in SUPPORTED_EXTENSIONS:
            try:
                documents.append(load_document(file_path))
            except ValueError:
                continue
    return documents
