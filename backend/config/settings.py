from __future__ import annotations
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "SIP-AI RAG")
    app_env: str = os.getenv("APP_ENV", "development")
    
    # VALORES FORZADOS DIRECTAMENTE PARA QUE FUNCIONE YA
    nvidia_api_key: str = "nvapi-AQUI_PEGA_TU_CLAVE_REAL"
    nvidia_base_url: str = "https://integrate.api.nvidia.com/v1"
    nvidia_model: str = "meta/llama-3.1-70b-instruct"
    nvidia_embedding_base_url: str = "https://integrate.api.nvidia.com/v1"
    nvidia_embedding_model: str = "nvidia/nv-embed-v1"
    
    timeout_seconds: float = float(os.getenv("REQUEST_TIMEOUT_SECONDS", "60"))

settings = Settings()
