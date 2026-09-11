from __future__ import annotations
import httpx
from backend.config.settings import settings
from backend.providers.base import LLMProvider, ProviderResponse

class NvidiaNIMProvider(LLMProvider):
    async def chat(self, message: str) -> ProviderResponse:
        if not settings.nvidia_api_key:
            raise RuntimeError("NVIDIA_API_KEY no está configurada.")

        endpoint = f"{settings.nvidia_base_url.rstrip('/')}/chat/completions"
        payload = {
            "model": settings.nvidia_model,
            "messages": [{"role": "user", "content": message}],
            "temperature": 0.2,
            "max_tokens": 1024,
            "stream": False,
        }
        headers = {
            "Authorization": f"Bearer {settings.nvidia_api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        async with httpx.AsyncClient(timeout=settings.timeout_seconds) as client:
            response = await client.post(endpoint, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()

        try:
            text = data["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError("Respuesta inesperada de NVIDIA NIM.") from exc

        return ProviderResponse(text=text, provider="nvidia-nim", model=settings.nvidia_model)
