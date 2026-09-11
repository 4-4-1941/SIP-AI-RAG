import asyncio
import json
from pathlib import Path

from rag.chunking.chunker import chunk_document
from rag.citations.formatter import build_citations
from rag.embeddings.provider import EmbeddingProvider
from rag.ingestion.loader import Document, load_document
from rag.pipeline import RAGPipeline
from rag.retrieval.memory_index import MemoryVectorIndex


class FakeEmbeddingProvider(EmbeddingProvider):
    async def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return [[1.0, 0.0] for _ in texts]

    async def embed_query(self, text: str) -> list[float]:
        return [1.0, 0.0]


def test_chunking_creates_multiple_chunks():
    doc = Document("d1", "d1.txt", "Documento 1", "a " * 1000)
    chunks = chunk_document(doc, chunk_size=100, overlap=10)
    assert len(chunks) > 1


def test_memory_index_returns_best_match():
    doc = Document("d1", "d1.txt", "Documento 1", "texto")
    chunks = chunk_document(doc, chunk_size=100, overlap=10)
    index = MemoryVectorIndex()
    index.add(chunks, [[1.0, 0.0]])
    result = index.search([1.0, 0.0], top_k=1)
    assert len(result) == 1
    assert result[0].score == 1.0


def test_json_metadata_is_loaded_and_cited(tmp_path: Path):
    payload = {
        "id": "norma-1",
        "titulo": "Norma de prueba",
        "numero_norma": "NTS 1",
        "resolucion_aprobatoria": "RM 1",
        "fuentes_oficiales": [{"url": "https://www.gob.pe/prueba"}],
    }
    path = tmp_path / "norma.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    doc = load_document(path)
    chunk = chunk_document(doc)[0]
    index = MemoryVectorIndex()
    index.add([chunk], [[1.0, 0.0]])
    result = index.search([1.0, 0.0], top_k=1)
    citation = build_citations(result)[0]
    assert citation.numero_norma == "NTS 1"
    assert citation.resolucion == "RM 1"
    assert citation.url_oficial == "https://www.gob.pe/prueba"


def test_pipeline_returns_empty_evidence_without_ingestion():
    pipeline = RAGPipeline(FakeEmbeddingProvider())
    result = asyncio.run(pipeline.retrieve("consulta"))
    assert result == {"context": "", "citations": [], "matches": []}
