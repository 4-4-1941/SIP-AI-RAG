# Guías de práctica clínica para RAG

Este directorio contiene guías clínicas en formato PDF, datos JSON asociados y versiones textuales Markdown para el pipeline RAG de SIP-AI-RAG.

- **Markdown (`.md`):** texto por página delimitado con `[[PAGINA N]]`, conservando la referencia de página para el chunker.
- **JSON (`.json`):** metadatos y texto extraído previamente, cuando está disponible.
- **`manifest.json`:** inventario que relaciona cada PDF con su JSON y Markdown.

Los documentos escaneados se procesaron con OCR en español cuando el texto del PDF no era extraíble. La precisión del OCR puede variar; se recomienda revisar páginas con tablas, diagramas o texto de baja calidad.
