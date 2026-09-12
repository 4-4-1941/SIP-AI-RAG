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
    pagina: int | str | None = None
    seccion: str | None = None
    anexo: str | None = None


def _source_metadata(metadata: dict | None) -> dict:
    if not metadata:
        return {
            "url": None, "norma": None, "resolucion": None,
            "pagina": None, "seccion": None, "anexo": None,
        }

    url = metadata.get("url_oficial") or metadata.get("url")
    sources = metadata.get("fuentes_oficiales")
    if not url and isinstance(sources, list):
        for source in sources:
            if isinstance(source, dict) and source.get("url"):
                url = str(source["url"])
                break

    return {
        "url": str(url) if url else None,
        "norma": metadata.get("numero_norma"),
        "resolucion": metadata.get("resolucion_aprobatoria") or metadata.get("resolucion"),
        "pagina": metadata.get("pagina"),
        "seccion": metadata.get("seccion"),
        "anexo": metadata.get("anexo"),
    }


def build_citations(items: list[RetrievedChunk]) -> list[Citation]:
    citations: list[Citation] = []
    seen: set[str] = set()

    for item in items:
        chunk = item.chunk
        if chunk.chunk_id in seen:
            continue
        seen.add(chunk.chunk_id)
        meta = _source_metadata(chunk.metadata)
        citations.append(
            Citation(
                number=len(citations) + 1,
                document_id=chunk.document_id,
                title=chunk.title,
                source_path=chunk.source_path,
                chunk_id=chunk.chunk_id,
                url_oficial=meta["url"],
                numero_norma=meta["norma"],
                resolucion=meta["resolucion"],
                pagina=meta["pagina"],
                seccion=meta["seccion"],
                anexo=meta["anexo"],
            )
        )
    return citations


def format_context(items: list[RetrievedChunk]) -> str:
    blocks: list[str] = []
    for index, item in enumerate(items, start=1):
        meta = _source_metadata(item.chunk.metadata)
        header = [f"[Fuente {index}] {item.chunk.title}"]
        if meta["norma"]:
            header.append(f'Norma: {meta["norma"]}')
        if meta["resolucion"]:
            header.append(f'Resolución: {meta["resolucion"]}')
        if meta["pagina"] is not None:
            header.append(f'Página: {meta["pagina"]}')
        if meta["seccion"]:
            header.append(f'Sección: {meta["seccion"]}')
        if meta["anexo"]:
            header.append(f'Anexo: {meta["anexo"]}')
        if meta["url"]:
            header.append(f'URL oficial: {meta["url"]}')
        blocks.append("\n".join(header) + "\n" + item.chunk.text)
    return "\n\n".join(blocks)
