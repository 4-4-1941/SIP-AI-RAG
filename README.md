# SIP-AI-RAG

Base móvil inicial de **SIP-AI RAG**.

## Objetivo
Crear una capa de inteligencia documental que recupere evidencia desde fuentes oficiales, aplique RAG antes de generar respuestas y entregue citas y trazabilidad usando proveedores como **NVIDIA NIM / Llama**.

## Estructura inicial
```text
SIP-AI-RAG/
├─ index.html
├─ css/
│  └─ styles.css
└─ README.md
```

## Estado actual
Esta entrega implementa la base frontend móvil:
- interfaz responsive;
- panel de fuentes;
- selector de proveedor;
- chat local de demostración;
- validación de longitud;
- limpieza del historial local;
- visualización de la arquitectura RAG.

**Todavía no conecta NVIDIA NIM, un backend ni un vector store.**

## Arquitectura prevista
```text
Frontend
  ↓
API segura
  ↓
RAG / Retrieval
  ↓
Índice documental + embeddings
  ↓
Contexto recuperado
  ↓
LLM Provider
  ├─ NVIDIA NIM / Llama
  ├─ Groq
  ├─ Cerebras
  └─ RAG-only fallback
```

## Fuentes previstas
MINSA, INS, OMS/OPS, Normas Técnicas de Salud, guías, manuales y otras fuentes oficiales.

## Seguridad
Las API keys no deben estar en `index.html` ni en JavaScript público. Deben gestionarse en backend mediante variables de entorno.

## Próximo bloque técnico
Backend seguro, adaptador `LLMProvider`, conector NVIDIA NIM, ingesta documental, chunking, embeddings, recuperación con citas e integración del endpoint RAG.

© 2026 SIP
