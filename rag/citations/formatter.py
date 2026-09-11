from __future__ import annotations

from dataclasses import dataclass
from rag.retrieval.memory_index import RetrievedChunk


@dataclass(frozen=True)
class Citation:
    number: int
    document_id: str
    title: str
    source_path: str
    chunk_id: str


def build_citations(items: list[RetrievedChunk]) -> list[Citation]:
    citations: list[Citation] = []
    seen: set[str] = set()

    for item in items:
        chunk = item.chunk
        if chunk.chunk_id in seen:
            continue
        seen.add(chunk.chunk_id)
        citations.append(
            Citation(
                number=len(citations) + 1,
                document_id=chunk.document_id,
                title=chunk.title,
                source_path=chunk.source_path,
                chunk_id=chunk.chunk_id,
            )
        )
    return citations


def format_context(items: list[RetrievedChunk]) -> str:
    blocks: list[str] = []
    for index, item in enumerate(items, start=1):
        blocks.append(
            f"[Fuente {index}] {item.chunk.title}\n"
            f"{item.chunk.text}"
        )
    return "\n\n".join(blocks)
  
