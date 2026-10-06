from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from backend.config.settings import settings

def get_nvidia_embeddings():
    """
    Inicializa y retorna el modelo de embeddings de NVIDIA.
    Usa nemotron-3-embed-1b con el parámetro obligatorio input_type.
    """
    return NVIDIAEmbeddings(
        model="nvidia/nemotron-3-embed-1b",
        base_url=settings.nvidia_embedding_base_url,
        api_key=settings.nvidia_api_key,
        model_type="query"  # OBLIGATORIO para este modelo
    )

def get_nvidia_embeddings_passage():
    """
    Versión para indexar documentos (passage).
    """
    return NVIDIAEmbeddings(
        model="nvidia/nemotron-3-embed-1b",
        base_url=settings.nvidia_embedding_base_url,
        api_key=settings.nvidia_api_key,
        model_type="passage"  # OBLIGATORIO para indexar documentos
    )
