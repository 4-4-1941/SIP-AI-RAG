from __future__ import annotations

import os
import httpx

from rag.embeddings.provider import EmbeddingProvider


class NvidiaEmbeddingProvider(EmbeddingProvider):
    def __init__(self) -> None:
        self.api_key = os.getenv("NVIDIA_API_KEY", "")
        self.base_url = os.getenv(
            "NVIDIA_EMBEDDING_BASE_URL",
            "https://integrate.api.nvidia.com/v1",
        ).rstrip("/")
        self.model = os.getenv(
            "NVIDIA_EMBEDDING_MODEL",
            "nvidia/llama-nemotron-embed-1b-v2",
        )
        self.timeout = float(os.getenv("REQUEST_TIMEOUT_SECONDS", "60"))

    async def _embed(self, texts: list[str], input_type: str) -> list[list[float]]:
        if not self.api_key:
            raise RuntimeError("NVIDIA_API_KEY no está configurada.")

        payload = {
            "input": texts,
            "model": self.model,
            "input_type": input_type,
            "encoding_format": "float",
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(
                f"{self.base_url}/embeddings",
                headers=headers,
                json=payload,
            )
            response.raise_for_status()
            data = response.json()

        rows = data.get("data", [])
        if len(rows) != len(texts):
            raise RuntimeError("Respuesta de embeddings incompleta o inesperada.")

        return [row["embedding"] for row in rows]

    async def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return await self._embed(texts, "passage")

    async def embed_query(self, text: str) -> list[float]:
        return (await self._embed([text], "query"))[0]
          
