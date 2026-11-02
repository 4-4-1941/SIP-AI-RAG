from __future__ import annotations
import os
from dataclasses import dataclass
from pathlib import Path


def _load_env_file() -> None:
    """Carga variables de un archivo .env en la raíz del proyecto.

    Se ejecuta antes de leer las variables de configuración. No sobrescribe
    variables ya exportadas en el entorno. No requiere dependencias externas.
    """
    root = Path(__file__).resolve().parents[2]
    env_file = root / ".env"
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


_load_env_file()


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "SIP-AI RAG")
    app_env: str = os.getenv("APP_ENV", "development")

    nvidia_api_key: str = os.getenv("NVIDIA_API_KEY", "")
    nvidia_base_url: str = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
    nvidia_model: str = os.getenv("NVIDIA_MODEL", "nvidia/nemotron-3.5-lightning-30b-a3b")

    nvidia_embedding_base_url: str = os.getenv("NVIDIA_EMBEDDING_BASE_URL", "https://integrate.api.nvidia.com/v1")
    nvidia_embedding_model: str = os.getenv("NVIDIA_EMBEDDING_MODEL", "nvidia/nemotron-3-embed-1b")

    timeout_seconds: float = float(os.getenv("REQUEST_TIMEOUT_SECONDS", "60"))


settings = Settings()
