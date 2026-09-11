# SIP-AI RAG — Arquitectura

```text
Frontend
   ↓
SIP-AI API
   ↓
RAG
├─ ingestion
├─ chunking
├─ embeddings
├─ retrieval
├─ reranking
└─ citations
   ↓
knowledge + metadata + indexes
   ↓
LLM providers
```

## Directorios

- `js/`: interfaz y comunicación con API.
- `backend/`: API y proveedores de modelos.
- `rag/`: canal documental RAG.
- `knowledge/`: documentos fuente.
- `data/metadata/`: metadatos normalizados.
- `data/indexes/`: índices generados.
- `docs/`: arquitectura y reglas de fuentes.
- `tests/`: validaciones automatizadas.

NVIDIA NIM/Llama es un proveedor. El diseño mantiene desacoplado el RAG del
proveedor para permitir otros modelos sin reconstruir la biblioteca documental.
