from __future__ import annotations

import asyncio

import requests

from backend.config.settings import settings
from rag.embeddings.provider import EmbeddingProvider


def _embeddings_url() -> str:
    base_url = settings.nvidia_embedding_base_url.rstrip("/")
    if base_url.endswith("/embeddings"):
        return base_url
    return f"{base_url}/embeddings"


NVIDIA_EMBEDDINGS_URL = _embeddings_url()
NVIDIA_EMBEDDING_MODEL = settings.nvidia_embedding_model


def _call_nvidia_embeddings(texts: list[str], input_type: str) -> list[list[float]]:
    if not texts:
        return []
    if not settings.nvidia_api_key:
        raise RuntimeError("NVIDIA_API_KEY no está configurada.")

    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "input": texts,
        "model": settings.nvidia_embedding_model,
        "input_type": input_type,
        "encoding_format": "float",
        "truncate": "NONE",
    }
    response = requests.post(
        _embeddings_url(),
        json=payload,
        headers=headers,
        timeout=settings.timeout_seconds,
    )
    if response.status_code >= 400:
        detail = response.text.strip()
        if len(detail) > 1200:
            detail = detail[:1200] + "…"
        raise RuntimeError(
            f"NVIDIA embeddings error {response.status_code}: {detail or 'empty response'}"
        )

    try:
        data = response.json()
        rows = data["data"]
        embeddings = [
            item["embedding"]
            for item in sorted(rows, key=lambda item: item["index"])
        ]
    except (ValueError, KeyError, TypeError) as exc:
        raise RuntimeError("NVIDIA devolvió una respuesta de embeddings inválida.") from exc

    if len(embeddings) != len(texts):
        raise RuntimeError(
            f"NVIDIA devolvió {len(embeddings)} embeddings para {len(texts)} textos."
        )
    return embeddings


def get_nvidia_embeddings(texts: list[str]) -> list[list[float]]:
    return _call_nvidia_embeddings(texts, input_type="query")


def get_nvidia_embeddings_passage(texts: list[str]) -> list[list[float]]:
    return _call_nvidia_embeddings(texts, input_type="passage")


class NvidiaEmbeddingProvider(EmbeddingProvider):
    async def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return await asyncio.to_thread(get_nvidia_embeddings_passage, texts)

    async def embed_query(self, text: str) -> list[float]:
        embeddings = await asyncio.to_thread(get_nvidia_embeddings, [text])
        if not embeddings:
            raise RuntimeError("NVIDIA no devolvió el embedding de la consulta.")
        return embeddings[0]
