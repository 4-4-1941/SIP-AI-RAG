from __future__ import annotations
import httpx
from backend.config.settings import settings

class NvidiaEmbeddingProvider:
    async def embed(self, text: str) -> list[float]:
        if not settings.nvidia_api_key:
            raise RuntimeError("NVIDIA_API_KEY no está configurada para embeddings.")
        
        endpoint = f"{settings.nvidia_embedding_base_url.rstrip('/')}/embeddings"
        payload = {
            "model": settings.nvidia_embedding_model,
            "input": text,
        }
        headers = {
            "Authorization": f"Bearer {settings.nvidia_api_key}",
            "Content-Type": "application/json",
        }
        async with httpx.AsyncClient(timeout=settings.timeout_seconds) as client:
            response = await client.post(endpoint, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            return data["data"][0]["embedding"]
