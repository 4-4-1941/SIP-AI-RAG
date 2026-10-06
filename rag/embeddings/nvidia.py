import requests
from backend.config.settings import settings

NVIDIA_EMBEDDINGS_URL = "https://integrate.api.nvidia.com/v1/embeddings"
NVIDIA_EMBEDDING_MODEL = "nvidia/nemotron-3-embed-1b"


def _call_nvidia_embeddings(texts, input_type):
    headers = {
        "Authorization": f"Bearer {settings.nvidia_api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "input": texts,
        "model": NVIDIA_EMBEDDING_MODEL,
        "input_type": input_type,
        "encoding_format": "float",
        "truncate": "NONE",
    }
    response = requests.post(
        NVIDIA_EMBEDDINGS_URL, json=payload, headers=headers, timeout=60
    )
    if response.status_code != 200:
        raise RuntimeError(
            f"NVIDIA embeddings error {response.status_code}: {response.text}"
        )
    data = response.json()
    return [item["embedding"] for item in sorted(data["data"], key=lambda x: x["index"])]


def get_nvidia_embeddings(texts):
    return _call_nvidia_embeddings(texts, input_type="query")


def get_nvidia_embeddings_passage(texts):
    return _call_nvidia_embeddings(texts, input_type="passage")
