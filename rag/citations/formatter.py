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
    url_oficial: str | None = None
    numero_norma: str | None = None
    resolucion: str | None = None


def _source_metadata(metadata: dict | None) -> tuple[str | None, str | None, str | None]:
    if not metadata:
        return None, None, None
    url = None
    sources = metadata.get("fuentes_oficiales")
    if isinstance(sources, list):
        for source in sources:
            if isinstance(source, dict) and source.get("url"):
                url = str(source["url"])
                break
    return (
        url,
        metadata.get("numero_norma"),
        metadata.get("resolucion_aprobatoria") or metadata.get("resolucion"),
    )


def build_citations(items: list[RetrievedChunk]) -> list[Citation]:
    citations: list[Citation] = []
    seen: set[str] = set()

    for item in items:
        chunk = item.chunk
        if chunk.chunk_id in seen:
            continue
        seen.add(chunk.chunk_id)
        url, norma, resolucion = _source_metadata(chunk.metadata)
        citations.append(
            Citation(
                number=len(citations) + 1,
                document_id=chunk.document_id,
                title=chunk.title,
                source_path=chunk.source_path,
                chunk_id=chunk.chunk_id,
                url_oficial=url,
                numero_norma=norma,
                resolucion=resolucion,
            )
        )
    return citations


def format_context(items: list[RetrievedChunk]) -> str:
    blocks: list[str] = []
    for index, item in enumerate(items, start=1):
        url, norma, resolucion = _source_metadata(item.chunk.metadata)
        header = [f"[Fuente {index}] {item.chunk.title}"]
        if norma:
            header.append(f"Norma: {norma}")
        if resolucion:
            header.append(f"Resolución: {resolucion}")
        if url:
            header.append(f"URL oficial: {url}")
        blocks.append("\n".join(header) + "\n" + item.chunk.text)
    return "\n\n".join(blocks)
