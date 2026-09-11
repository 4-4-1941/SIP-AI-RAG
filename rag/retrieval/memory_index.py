from __future__ import annotations
from dataclasses import dataclass
from math import sqrt
from rag.chunking.chunker import Chunk

@dataclass(frozen=True)
class RetrievedChunk:
    chunk: Chunk
    score: float

def cosine_similarity(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        raise ValueError("Los vectores deben tener la misma dimensión.")
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = sqrt(sum(x * x for x in a))
    norm_b = sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

class MemoryVectorIndex:
    def __init__(self) -> None:
        self._rows: list[tuple[Chunk, list[float]]] = []

    @property
    def size(self) -> int:
        return len(self._rows)

    def add(self, chunks: list[Chunk], embeddings: list[list[float]]) -> None:
        if len(chunks) != len(embeddings):
            raise ValueError("chunks y embeddings deben tener la misma longitud.")
        self._rows.extend(zip(chunks, embeddings))

    def search(self, query_embedding: list[float], top_k: int = 5) -> list[RetrievedChunk]:
        if top_k <= 0:
            return []
        scored = [
            RetrievedChunk(chunk=chunk, score=cosine_similarity(query_embedding, vector))
            for chunk, vector in self._rows
        ]
        scored.sort(key=lambda item: item.score, reverse=True)
        return scored[:top_k]
