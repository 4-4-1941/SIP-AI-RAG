from __future__ import annotations
import httpx
from backend.config.settings import settings
from rag.embeddings.provider import EmbeddingProvider

class NvidiaEmbeddingProvider(EmbeddingProvider):
    def __init__(self) -> None:
        self.api_key = settings.nvidia_api_key
        self.base_url = settings.nvidia_embedding_base_url.rstrip("/")
        self.model = settings.nvidia_embedding_model
        self.timeout = settings.timeout_seconds

    async def _embed(self, texts: list[str], input_type: str) -> list[list[float]]:
        if not self.api_key:
            raise RuntimeError("NVIDIA_API_KEY no está configurada.")
        if not texts:
            return []
        payload = {
            "input": texts,
            "model": self.model,
            "input_type": input_type,
            "encoding_format": "float",
        }
        headers = {"Authorization": f"Bearer {self.api_key}", "Accept": "application/json"}
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(f"{self.base_url}/embeddings", headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
        rows = sorted(data.get("data", []), key=lambda row: row.get("index", 0))
        if len(rows) != len(texts):
            raise RuntimeError("NVIDIA devolvió embeddings incompletos.")
        return [row["embedding"] for row in rows]

    async def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return await self._embed(texts, "passage")

    async def embed_query(self, text: str) -> list[float]:
        rows = await self._embed([text], "query")
        return rows[0]
