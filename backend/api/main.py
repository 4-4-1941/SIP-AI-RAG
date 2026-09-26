from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from backend.config.settings import settings
from backend.providers.nvidia.provider import NvidiaNIMProvider
from rag.embeddings.nvidia import NvidiaEmbeddingProvider
from rag.pipeline import RAGPipeline

ROOT_DIR = Path(__file__).resolve().parents[2]
KNOWLEDGE_DIR = ROOT_DIR / "knowledge"
METADATA_DIR = ROOT_DIR / "data" / "metadata"
RAG_DIRECTORIES = (KNOWLEDGE_DIR, METADATA_DIR)

_rag: RAGPipeline | None = None
_rag_ingested = False
_rag_ingestion_stats: list[dict] = []
_rag_ingestion_error: str | None = None


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)


async def get_rag() -> RAGPipeline:
    global _rag, _rag_ingested, _rag_ingestion_stats, _rag_ingestion_error

    if _rag is None:
        _rag = RAGPipeline(NvidiaEmbeddingProvider())

    if not _rag_ingested:
        stats: list[dict] = []
        try:
            for directory in RAG_DIRECTORIES:
                if not directory.exists():
                    stats.append({
                        "directory": str(directory),
                        "exists": False,
                        "documents": 0,
                        "chunks": 0,
                        "indexed": _rag.index.size,
                    })
                    continue

                result = await _rag.ingest_directory(directory)
                stats.append({
                    "directory": str(directory),
                    "exists": True,
                    **result,
                })

            _rag_ingestion_stats = stats
            _rag_ingested = True
            _rag_ingestion_error = None
        except Exception as exc:
            _rag_ingestion_stats = stats
            _rag_ingestion_error = f"{type(exc).__name__}: {exc}"
            raise

    return _rag


@asynccontextmanager
async def lifespan(app: FastAPI):
    global _rag_ingestion_error
    try:
        await get_rag()
    except Exception as exc:
        _rag_ingestion_error = f"{type(exc).__name__}: {exc}"
    yield


app = FastAPI(title=settings.app_name, version="0.4.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"service": settings.app_name, "status": "ok", "health": "/health"}


@app.get("/health")
async def health():
    return {
        "status": "ok" if _rag_ingestion_error is None else "degraded",
        "service": settings.app_name,
        "nvidia_configured": bool(settings.nvidia_api_key),
        "rag_active": bool(_rag and _rag.index.size),
        "rag_documents_directories": [str(path) for path in RAG_DIRECTORIES],
        "rag_ingested": _rag_ingested,
        "rag_ingestion_stats": _rag_ingestion_stats,
        "rag_ingestion_error": _rag_ingestion_error,
        "rag_indexed_chunks": _rag.index.size if _rag else 0,
    }


@app.post("/api/chat")
async def chat(payload: ChatRequest):
    if not settings.nvidia_api_key:
        raise HTTPException(status_code=503, detail="NVIDIA_API_KEY no está configurada.")

    try:
        rag = await get_rag()
        evidence = await rag.retrieve(payload.message, top_k=5) if rag.index.size else {
            "context": "",
            "citations": [],
            "matches": [],
        }

        if not evidence["matches"]:
            return {
                "answer": "EVIDENCIA_INSUFICIENTE",
                "provider": None,
                "model": None,
                "rag_active": False,
                "citations": [],
            }

        prompt = (
            "Responde exclusivamente con la evidencia recuperada. "
            "No inventes normas, páginas, puntajes, criterios ni referencias. "
            "Si la evidencia no basta, responde EVIDENCIA_INSUFICIENTE.\n\n"
            f"CONSULTA:\n{payload.message}\n\n"
            f"EVIDENCIA:\n{evidence['context']}"
        )
        result = await NvidiaNIMProvider().chat(prompt)
        return {
            "answer": result.text,
            "provider": result.provider,
            "model": result.model,
            "rag_active": True,
            "citations": evidence["citations"],
        }
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
        
