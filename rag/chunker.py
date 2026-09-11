from __future__ import annotations

from dataclasses import dataclass
from rag.ingestion.loader import Document


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    document_id: str
    source_path: str
    title: str
    chunk_index: int
    text: str


def chunk_document(
    document: Document,
    chunk_size: int = 900,
    overlap: int = 150,
) -> list[Chunk]:
    if chunk_size <= 0:
        raise ValueError("chunk_size debe ser mayor que 0.")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap debe ser >= 0 y menor que chunk_size.")

    text = " ".join(document.text.split())
    chunks: list[Chunk] = []
    start = 0
    index = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        segment = text[start:end].strip()
        if segment:
            chunks.append(
                Chunk(
                    chunk_id=f"{document.document_id}:{index}",
                    document_id=document.document_id,
                    source_path=document.source_path,
                    title=document.title,
                    chunk_index=index,
                    text=segment,
                )
            )
            index += 1

        if end == len(text):
            break
        start = end - overlap

    return chunks
