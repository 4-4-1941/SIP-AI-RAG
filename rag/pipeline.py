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
            embeddings = await self.embedding_provider.embed_documents([chunk.text for chunk in chunks])
            self.index.add(chunks, embeddings)

        return {"documents": len(documents), "chunks": len(chunks)}

    async def retrieve(self, query: str, top_k: int = 5) -> dict:
        if not self.index.size:
            return {"context": "", "citations": [], "matches": []}

        query_embedding = await self.embedding_provider.embed_query(query)
        initial = self.index.search(query_embedding, top_k=max(top_k * 2, top_k))
        ranked = await self.reranker.rerank(query, initial, top_k=top_k)

        return {
            "context": format_context(ranked),
            "citations": [citation.__dict__ for citation in build_citations(ranked)],
            "matches": [
                {
                    "chunk_id": item.chunk.chunk_id,
                    "score": item.score,
                    "title": item.chunk.title,
                    "text": item.chunk.text,
                }
                for item in ranked
            ],
        }
