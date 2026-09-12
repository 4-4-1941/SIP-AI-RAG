from __future__ import annotations

from pathlib import Path

from rag.chunking.chunker import chunk_document
from rag.citations.formatter import build_citations, format_context
from rag.embeddings.provider import EmbeddingProvider
from rag.ingestion.loader import load_directory
from rag.retrieval.memory_index import MemoryVectorIndex
from rag.reranking.base import PassThroughReranker, Reranker


class RAGPipeline:
    def __init__(self, embedding_provider: EmbeddingProvider, reranker: Reranker | None = None) -> None:
        self.embedding_provider = embedding_provider
        self.reranker = reranker or PassThroughReranker()
        self.index = MemoryVectorIndex()

    async def ingest_directory(self, path: str | Path) -> dict:
        documents = load_directory(path)
        chunks = []
        for document in documents:
            chunks.extend(chunk_document(document))

        if chunks:
            embeddings = await self.embedding_provider.embed_documents(
                [chunk.text for chunk in chunks]
            )
            self.index.add(chunks, embeddings)

        return {
            "documents": len(documents),
            "chunks": len(chunks),
            "indexed": self.index.size,
        }

    async def retrieve(self, query: str, top_k: int = 5) -> dict:
        query = (query or "").strip()
        if not query or not self.index.size:
            return {"context": "", "citations": [], "matches": []}

        query_embedding = await self.embedding_provider.embed_query(query)
        initial = self.index.search(
            query_embedding,
            top_k=max(top_k * 2, top_k),
        )
        ranked = await self.reranker.rerank(query, initial, top_k=top_k)

        citations = build_citations(ranked)

        return {
            "context": format_context(ranked),
            "citations": [citation.__dict__ for citation in citations],
            "matches": [
                {
                    "chunk_id": item.chunk.chunk_id,
                    "document_id": item.chunk.document_id,
                    "score": item.score,
                    "title": item.chunk.title,
                    "text": item.chunk.text,
                    "source_path": item.chunk.source_path,
                    "pagina": (item.chunk.metadata or {}).get("pagina"),
                    "seccion": (item.chunk.metadata or {}).get("seccion"),
                    "anexo": (item.chunk.metadata or {}).get("anexo"),
                }
                for item in ranked
            ],
        }
