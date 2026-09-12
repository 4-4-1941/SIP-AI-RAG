from __future__ import annotations
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "SIP-AI RAG")
    app_env: str = os.getenv("APP_ENV", "development")
    nvidia_api_key: str = os.getenv("NVIDIA_API_KEY", "")
    nvidia_base_url: str = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
    nvidia_model: str = os.getenv("NVIDIA_MODEL", "meta/llama-3.1-70b-instruct")
    nvidia_embedding_base_url: str = os.getenv("NVIDIA_EMBEDDING_BASE_URL", "https://integrate.api.nvidia.com/v1")
    nvidia_embedding_model: str = os.getenv("NVIDIA_EMBEDDING_MODEL", "nvidia/llama-nemotron-embed-1b-v2")
    timeout_seconds: float = float(os.getenv("REQUEST_TIMEOUT_SECONDS", "60"))

settings = Settings()
