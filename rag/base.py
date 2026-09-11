from __future__ import annotations

from abc import ABC, abstractmethod
from rag.retrieval.memory_index import RetrievedChunk


class Reranker(ABC):
    @abstractmethod
    async def rerank(
        self,
        query: str,
        items: list[RetrievedChunk],
        top_k: int = 5,
    ) -> list[RetrievedChunk]:
        raise NotImplementedError


class PassThroughReranker(Reranker):
    async def rerank(
        self,
        query: str,
        items: list[RetrievedChunk],
        top_k: int = 5,
    ) -> list[RetrievedChunk]:
        return items[:top_k]
