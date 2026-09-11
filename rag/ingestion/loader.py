from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

SUPPORTED_EXTENSIONS = {".txt", ".md", ".json"}


@dataclass(frozen=True)
class Document:
    document_id: str
    source_path: str
    title: str
    text: str
    metadata: dict | None = None


def _json_to_text(data: object) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def load_document(path: str | Path) -> Document:
    file_path = Path(path)
    suffix = file_path.suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Formato no soportado: {suffix}. Use .txt, .md o .json.")

    metadata = None
    if suffix == ".json":
        data = json.loads(file_path.read_text(encoding="utf-8"))
        text = _json_to_text(data).strip()
        metadata = data if isinstance(data, dict) else None
        document_id = str((metadata or {}).get("id") or file_path.stem)
        title = str((metadata or {}).get("titulo") or file_path.stem)
    else:
        text = file_path.read_text(encoding="utf-8").strip()
        document_id = file_path.stem
        title = file_path.stem.replace("-", " ").replace("_", " ").strip()

    if not text:
        raise ValueError("El documento está vacío.")

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
    return [
        load_document(file_path)
        for file_path in sorted(directory.rglob("*"))
        if file_path.is_file() and file_path.suffix.lower() in SUPPORTED_EXTENSIONS
    ]
