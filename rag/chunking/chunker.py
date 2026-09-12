from __future__ import annotations

import re
from dataclasses import dataclass

from rag.ingestion.loader import Document


PAGE_MARKER = re.compile(r"\[\[PAGINA\s+(\d+)\]\]", re.IGNORECASE)


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    document_id: str
    source_path: str
    title: str
    chunk_index: int
    text: str
    metadata: dict | None = None


def _segments(document: Document) -> list[tuple[str, dict | None]]:
    """Divide PDF/texto marcado por página sin perder trazabilidad."""
    matches = list(PAGE_MARKER.finditer(document.text))
    if not matches:
        return [(document.text, document.metadata)]

    segments: list[tuple[str, dict | None]] = []
    for pos, match in enumerate(matches):
        start = match.end()
        end = matches[pos + 1].start() if pos + 1 < len(matches) else len(document.text)
        text = document.text[start:end].strip()
        if not text:
            continue
        metadata = dict(document.metadata or {})
        metadata["pagina"] = int(match.group(1))
        segments.append((text, metadata))
    return segments


def chunk_document(document: Document, chunk_size: int = 900, overlap: int = 150) -> list[Chunk]:
    if chunk_size <= 0:
        raise ValueError("chunk_size debe ser mayor que 0.")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap debe ser >= 0 y menor que chunk_size.")

    chunks: list[Chunk] = []
    index = 0

    for source_text, metadata in _segments(document):
        text = " ".join(source_text.split())
        start = 0

        while start < len(text):
            end = min(start + chunk_size, len(text))
            segment = text[start:end].strip()
            if segment:
                page = (metadata or {}).get("pagina")
                suffix = f":p{page}" if page is not None else ""
                chunks.append(
                    Chunk(
                        chunk_id=f"{document.document_id}{suffix}:{index}",
                        document_id=document.document_id,
                        source_path=document.source_path,
                        title=document.title,
                        chunk_index=index,
                        text=segment,
                        metadata=metadata,
                    )
                )
                index += 1
            if end == len(text):
                break
            start = end - overlap

    return chunks
