from rag.chunking.chunker import chunk_document
from rag.ingestion.loader import Document
from rag.retrieval.memory_index import MemoryVectorIndex


def test_chunking_creates_multiple_chunks():
    doc = Document(
        document_id="d1",
        source_path="d1.txt",
        title="Documento 1",
        text="a " * 1000,
    )
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
