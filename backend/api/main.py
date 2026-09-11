from __future__ import annotations
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from backend.config.settings import settings
from backend.providers.nvidia.provider import NvidiaNIMProvider

app = FastAPI(title=settings.app_name, version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": settings.app_name,
        "nvidia_configured": bool(settings.nvidia_api_key),
        "rag_active": False,
    }

@app.post("/api/chat")
async def chat(payload: ChatRequest):
    if not settings.nvidia_api_key:
        raise HTTPException(status_code=503, detail="NVIDIA_API_KEY no está configurada.")
    try:
        result = await NvidiaNIMProvider().chat(payload.message)
        return {
            "answer": result.text,
            "provider": result.provider,
            "model": result.model,
            "rag_active": False,
        }
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
  
