from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

SUPPORTED_EXTENSIONS = {".txt", ".md"}


@dataclass(frozen=True)
class Document:
    document_id: str
    source_path: str
    title: str
    text: str


def load_document(path: str | Path) -> Document:
    file_path = Path(path)
    if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Formato no soportado todavía: {file_path.suffix}. "
            "Use .txt o .md hasta integrar PDF."
        )

    text = file_path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("El documento está vacío.")

    return Document(
        document_id=file_path.stem,
        source_path=str(file_path),
        title=file_path.stem.replace("-", " ").replace("_", " ").strip(),
        text=text,
    )


def load_directory(path: str | Path) -> list[Document]:
    directory = Path(path)
    documents: list[Document] = []
    for file_path in sorted(directory.rglob("*")):
        if file_path.is_file() and file_path.suffix.lower() in SUPPORTED_EXTENSIONS:
            documents.append(load_document(file_path))
    return documents
  
