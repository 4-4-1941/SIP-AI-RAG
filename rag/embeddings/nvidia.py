from __future__ import annotations

import httpx

from backend.config.settings import settings
from rag.embeddings.provider import EmbeddingProvider


class NvidiaEmbeddingProvider(EmbeddingProvider):
    def __init__(self, batch_size: int = 16) -> None:
        self.api_key = settings.nvidia_api_key
        self.base_url = settings.nvidia_embedding_base_url.rstrip("/")
        self.model = settings.nvidia_embedding_model
        self.timeout = settings.timeout_seconds
        self.batch_size = max(1, batch_size)

    async def _embed_batch(
        self,
        client: httpx.AsyncClient,
        texts: list[str],
        input_type: str,
    ) -> list[list[float]]:
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

        response = await client.post(
            f"{self.base_url}/embeddings",
            headers=headers,
            json=payload,
        )
        response.raise_for_status()
        data = response.json()

        rows = sorted(data.get("data", []), key=lambda row: row.get("index", 0))
        if len(rows) != len(texts):
            raise RuntimeError(
                f"NVIDIA devolvió embeddings incompletos: "
                f"{len(rows)} de {len(texts)}."
            )

        embeddings: list[list[float]] = []
        for row in rows:
            embedding = row.get("embedding")
            if not isinstance(embedding, list) or not embedding:
                raise RuntimeError("NVIDIA devolvió un embedding vacío o inválido.")
            embeddings.append(embedding)

        return embeddings

    async def _embed(
        self,
        texts: list[str],
        input_type: str,
    ) -> list[list[float]]:
        if not self.api_key:
            raise RuntimeError("NVIDIA_API_KEY no está configurada.")

        clean_texts = [str(text).strip() for text in texts]
        if not clean_texts:
            return []
        if any(not text for text in clean_texts):
            raise ValueError("No se pueden generar embeddings de textos vacíos.")

        result: list[list[float]] = []

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            for start in range(0, len(clean_texts), self.batch_size):
                batch = clean_texts[start:start + self.batch_size]
                batch_embeddings = await self._embed_batch(
                    client,
                    batch,
                    input_type,
                )
                result.extend(batch_embeddings)

        if len(result) != len(clean_texts):
            raise RuntimeError(
                f"Cantidad final de embeddings inválida: "
                f"{len(result)} de {len(clean_texts)}."
            )

        return result

    async def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return await self._embed(texts, "passage")

    async def embed_query(self, text: str) -> list[float]:
        rows = await self._embed([text], "query")
        if not rows:
            raise RuntimeError("NVIDIA no devolvió embedding para la consulta.")
        return rows[0]
