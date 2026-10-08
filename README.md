# SIP-AI-RAG

Capa de inteligencia documental sobre fuentes oficiales de salud del Perú (MINSA, INS, CDC-MINSA). Recupera evidencia con RAG antes de generar respuestas y entrega citas con trazabilidad (norma, resolución, página, sección y URL oficial) usando **NVIDIA NIM** como proveedor de modelos.

## Estado actual

- Backend seguro en **FastAPI** con endpoint `/api/chat` y `/health`.
- Pipeline RAG completo: ingesta documental, chunking, embeddings, recuperación y citas.
- Conector **NVIDIA NIM** para chat (`nvidia/nemotron-3.5-lightning-30b-a3b`) y embeddings (`nvidia/nemotron-3-embed-1b`).
- Corpus documental: Normas Técnicas de Salud, manuales HIS, guías INS y compendios SERUMS (PDF + Markdown + metadatos normalizados).
- Frontend móvil responsive con panel de fuentes, selector de proveedor y visualización de la arquitectura RAG.
- Respuesta `EVIDENCIA_INSUFICIENTE` cuando la recuperación no sustenta una respuesta (anti-alucinación).

## Arquitectura

```text
Frontend (index.html + js/)
  ↓
API FastAPI (backend/api)
  ↓
RAG (rag/)
  ├─ ingestion   — carga de PDF/MD/JSON con sidecars de metadata
  ├─ chunking    — segmentación por página con solape
  ├─ embeddings  — NVIDIA NIM (modos query/passage)
  ├─ retrieval   — índice vectorial en memoria (similitud coseno)
  ├─ reranking   — etapa opcional (reranker desacoplado)
  └─ citations   — citas con norma, resolución, página y URL oficial
  ↓
LLM Provider (backend/providers) — NVIDIA NIM, extensible a Groq/Cerebras
```

## Estructura

```text
SIP-AI-RAG/
├─ index.html          # Frontend móvil
├─ css/                # Estilos
├─ js/                 # Cliente API y lógica de UI
├─ backend/
│  ├─ api/main.py      # FastAPI: /api/chat, /health
│  ├─ config/          # Configuración por variables de entorno
│  └─ providers/       # Adaptadores LLM (NVIDIA NIM)
├─ rag/
│  ├─ ingestion/       # Carga de documentos y sincronización (El Peruano, SERUMS)
│  ├─ chunking/        # Chunking con trazabilidad de página
│  ├─ embeddings/      # Proveedor de embeddings NVIDIA
│  ├─ retrieval/       # Índice vectorial en memoria
│  ├─ reranking/       # Interfaz de reranker
│  └─ citations/       # Construcción de citas y contexto
├─ knowledge/          # Documentos fuente (PDF/MD)
├─ data/metadata/      # Metadatos normalizados por documento
├─ docs/               # Arquitectura y reglas de fuentes
└─ tests/              # Validaciones automatizadas
```

## Configuración

Las API keys se gestionan **solo en backend** mediante variables de entorno (nunca en `index.html` ni en JavaScript público). Ver `.env.example`.

| Variable | Descripción | Default |
| --- | --- | --- |
| `NVIDIA_API_KEY` | API key de NVIDIA NIM (requerida) | — |
| `NVIDIA_BASE_URL` | URL del endpoint de chat | `https://integrate.api.nvidia.com/v1` |
| `NVIDIA_MODEL` | Modelo de chat | `nvidia/nemotron-3.5-lightning-30b-a3b` |
| `NVIDIA_EMBEDDING_MODEL` | Modelo de embeddings | `nvidia/nemotron-3-embed-1b` |
| `REQUEST_TIMEOUT_SECONDS` | Timeout de peticiones | `60` |

## Ejecución

```bash
pip install -r backend/requirements.txt
export NVIDIA_API_KEY=...
uvicorn backend.api.main:app --reload
```

Al arrancar, la API ingiere `knowledge/` y `data/metadata/` en segundo plano; `/health` reporta el estado de la ingesta y los chunks indexados.

## Fuentes

MINSA, INS, OMS/OPS, Normas Técnicas de Salud, guías, manuales HIS y compendios SERUMS. Reglas detalladas en `docs/RAG-SOURCES.md`.

## Próximos pasos

- Persistencia del índice vectorial (hoy se re-ingiere en memoria en cada arranque).
- Reranker real en la etapa de reranking.
- Chunking semántico por secciones de norma.
- Set de evaluación de calidad de recuperación.

© 2026 SIP
