from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
import time
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urljoin, urlparse, urlunparse

import httpx
from pypdf import PdfReader

MASTER_COLLECTION = "https://www.gob.pe/institucion/minsa/colecciones/61810"
DEFAULT_OUTPUT = Path("knowledge/minsa/serums-2026-ii")
USER_AGENT = "SIP-AI-RAG/1.0 (+biblioteca SERUMS; fuente oficial gob.pe)"
NORM_RE = re.compile(r"/institucion/minsa/normas-legales/\d+")
COLLECTION_RE = re.compile(r"/institucion/minsa/colecciones/\d+")
PDF_RE = re.compile(r"\.pdf(?:$|\?)", re.I)
EXPECTED_COMPENDIA = 17


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._href = ""
        self._text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        values = dict(attrs)
        self._href = values.get("href") or ""
        self._text = []

    def handle_data(self, data: str) -> None:
        if self._href:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self._href:
            self.links.append((self._href, " ".join("".join(self._text).split())))
            self._href = ""
            self._text = []


@dataclass
class OfficialDocument:
    norm_url: str
    title: str = ""
    pdf_url: str = ""
    compendia: set[str] = field(default_factory=set)


def links(html: str, base_url: str) -> list[tuple[str, str]]:
    parser = LinkParser()
    parser.feed(html)
    return [(urljoin(base_url, href), text) for href, text in parser.links if href]


def canonical(url: str) -> str:
    p = urlparse(url)
    return urlunparse((p.scheme or "https", p.netloc, p.path.rstrip("/"), "", "", ""))


def with_sheet(url: str, sheet: int) -> str:
    p = urlparse(url)
    query = parse_qs(p.query)
    query["sheet"] = [str(sheet)]
    return urlunparse((p.scheme, p.netloc, p.path, p.params, urlencode(query, doseq=True), ""))


def safe_slug(value: str, fallback: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return (value.strip("-")[:100] or fallback).strip("-")


def gob_id(url: str) -> str:
    parts = [p for p in urlparse(url).path.split("/") if p]
    return parts[-1].split("-", 1)[0] if parts else hashlib.sha1(url.encode()).hexdigest()[:12]


def fetch(client: httpx.Client, url: str, attempts: int = 3) -> httpx.Response:
    last: Exception | None = None
    for attempt in range(attempts):
        try:
            response = client.get(url)
            response.raise_for_status()
            return response
        except (httpx.HTTPError, httpx.TimeoutException) as exc:
            last = exc
            if attempt + 1 < attempts:
                time.sleep(1.2 * (attempt + 1))
    raise RuntimeError(f"No se pudo recuperar fuente oficial: {url}") from last


def discover_compendia(client: httpx.Client) -> list[tuple[str, str]]:
    response = fetch(client, MASTER_COLLECTION)
    found: dict[str, str] = {}
    for url, text in links(response.text, str(response.url)):
        c = canonical(url)
        if COLLECTION_RE.search(c) and c != canonical(MASTER_COLLECTION):
            label = text.strip()
            if "serums" in (label + " " + c).lower():
                found[c] = label or c.rsplit("/", 1)[-1]
    if len(found) != EXPECTED_COMPENDIA:
        raise RuntimeError(
            f"Se esperaban {EXPECTED_COMPENDIA} compendios oficiales y se detectaron {len(found)}. "
            "Se aborta para evitar un corpus incompleto."
        )
    return sorted(found.items(), key=lambda item: item[1].lower())


def discover_norms(client: httpx.Client, collection_url: str, max_sheets: int = 30) -> dict[str, str]:
    found: dict[str, str] = {}
    empty_streak = 0
    for sheet in range(1, max_sheets + 1):
        page_url = collection_url if sheet == 1 else with_sheet(collection_url, sheet)
        response = fetch(client, page_url)
        page_found = 0
        for url, text in links(response.text, str(response.url)):
            c = canonical(url)
            if NORM_RE.search(c):
                if c not in found:
                    page_found += 1
                found[c] = text.strip() or found.get(c, "")
        empty_streak = empty_streak + 1 if page_found == 0 else 0
        if empty_streak >= 2:
            break
    return found


def discover_pdf(client: httpx.Client, norm_url: str) -> tuple[str, str]:
    response = fetch(client, norm_url)
    title = ""
    title_match = re.search(r"<title[^>]*>(.*?)</title>", response.text, re.I | re.S)
    if title_match:
        title = re.sub(r"<[^>]+>", " ", title_match.group(1))
        title = " ".join(title.split())

    candidates: list[str] = []
    for url, _ in links(response.text, str(response.url)):
        if (PDF_RE.search(urlparse(url).path) or "cdn.www.gob.pe" in url) and ".pdf" in url.lower():
            candidates.append(url)

    for raw in re.findall(r'https?://[^"\'<>\s]+', response.text):
        raw = raw.replace("\\u0026", "&").replace("\\/", "/")
        if "gob.pe" in raw and ".pdf" in raw.lower():
            candidates.append(raw)

    seen: set[str] = set()
    unique = [u for u in candidates if not (u in seen or seen.add(u))]
    return title, unique[0] if unique else ""


def pdf_to_markdown(pdf_bytes: bytes, title: str, source_url: str, pdf_url: str) -> str:
    with tempfile.NamedTemporaryFile(suffix=".pdf") as tmp:
        tmp.write(pdf_bytes)
        tmp.flush()
        reader = PdfReader(tmp.name)
        parts = [
            f"# {title}",
            "",
            f"Fuente oficial: {source_url}",
            f"PDF oficial: {pdf_url}",
            "",
        ]
        extracted = 0
        for number, page in enumerate(reader.pages, start=1):
            text = (page.extract_text() or "").strip()
            if not text:
                continue
            extracted += 1
            parts.append(f"[[PAGINA {number}]]")
            parts.append(text)
            parts.append("")
        if extracted == 0:
            raise RuntimeError("PDF sin texto extraíble; requiere revisión manual/OCR.")
        return "\n".join(parts).strip() + "\n"


def write_sidecar(content_path: Path, doc: OfficialDocument) -> Path:
    metadata_path = content_path.with_suffix(".metadata.json")
    payload = {
        "id": f"MINSA-SERUMS-2026-II-{gob_id(doc.norm_url)}",
        "titulo": doc.title or content_path.stem,
        "institucion": "Ministerio de Salud del Perú",
        "bibliografia": "SERUMS 2026-II",
        "compendios_origen": sorted(doc.compendia),
        "url_oficial": doc.norm_url,
        "pdf_oficial": doc.pdf_url,
        "estado_validacion": "VALIDADO_OFICIAL",
        "tipo_fuente": "texto_extraido_pdf_oficial",
        "regla_evidencia": "Conservar página exacta del PDF para afirmaciones documentales."
    }
    metadata_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return metadata_path


def materialize_document(
    client: httpx.Client, doc: OfficialDocument, output: Path
) -> tuple[Path, Path]:
    response = fetch(client, doc.pdf_url)
    content_type = response.headers.get("content-type", "").lower()
    if "pdf" not in content_type and not response.content.startswith(b"%PDF"):
        raise RuntimeError(f"El recurso no parece PDF: {doc.pdf_url}")

    ident = gob_id(doc.norm_url)
    slug = safe_slug(doc.title, f"documento-{ident}")
    content_path = output / f"{ident}-{slug}.md"
    content_path.write_text(
        pdf_to_markdown(response.content, doc.title or content_path.stem, doc.norm_url, doc.pdf_url),
        encoding="utf-8",
    )
    return content_path, write_sidecar(content_path, doc)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sincroniza bibliografía oficial MINSA SERUMS 2026-II hacia knowledge/."
    )
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--materialize",
        action="store_true",
        help="Extrae texto paginado de los PDF oficiales a Markdown y crea sidecars.",
    )
    parser.add_argument("--limit", type=int, default=0, help="Limita documentos para prueba; 0 = todos.")
    parser.add_argument("--timeout", type=float, default=30.0)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    documents: dict[str, OfficialDocument] = {}

    with httpx.Client(
        timeout=args.timeout,
        follow_redirects=True,
        headers={"User-Agent": USER_AGENT, "Accept-Language": "es-PE,es;q=0.9"},
    ) as client:
        compendia = discover_compendia(client)
        print(f"Compendios oficiales descubiertos: {len(compendia)}")

        for collection_url, collection_name in compendia:
            norms = discover_norms(client, collection_url)
            print(f"- {collection_name}: {len(norms)} referencias")
            for norm_url, label in norms.items():
                doc = documents.setdefault(norm_url, OfficialDocument(norm_url=norm_url))
                doc.compendia.add(collection_name)
                if label and not doc.title:
                    doc.title = label

        ordered = sorted(documents.values(), key=lambda d: d.norm_url)
        if args.limit > 0:
            ordered = ordered[: args.limit]

        manifest_docs = []
        materialized = 0
        failures = 0

        for index, doc in enumerate(ordered, start=1):
            try:
                page_title, pdf_url = discover_pdf(client, doc.norm_url)
                if page_title:
                    doc.title = page_title
                doc.pdf_url = pdf_url

                status = "VALIDADO_OFICIAL" if doc.pdf_url else "CORROBORADO_PENDIENTE_PDF_OFICIAL"
                item = {
                    "id": f"MINSA-SERUMS-2026-II-{gob_id(doc.norm_url)}",
                    "titulo": doc.title,
                    "url_oficial": doc.norm_url,
                    "pdf_oficial": doc.pdf_url or None,
                    "compendios_origen": sorted(doc.compendia),
                    "estado_validacion": status,
                }

                if args.materialize and doc.pdf_url:
                    content_path, metadata_path = materialize_document(client, doc, args.output)
                    item["archivo_rag"] = content_path.name
                    item["metadata_rag"] = metadata_path.name
                    materialized += 1
                    print(f"[{index}/{len(ordered)}] RAG: {content_path.name}")
                else:
                    print(f"[{index}/{len(ordered)}] {status}: {doc.norm_url}")

                manifest_docs.append(item)
            except Exception as exc:
                failures += 1
                print(f"[{index}/{len(ordered)}] ERROR: {doc.norm_url}: {exc}")
                manifest_docs.append({
                    "id": f"MINSA-SERUMS-2026-II-{gob_id(doc.norm_url)}",
                    "titulo": doc.title,
                    "url_oficial": doc.norm_url,
                    "pdf_oficial": doc.pdf_url or None,
                    "compendios_origen": sorted(doc.compendia),
                    "estado_validacion": "CORROBORADO_PENDIENTE_PDF_OFICIAL",
                    "error_sincronizacion": str(exc),
                })

    manifest = {
        "id": "SERUMS-2026-II-CORPUS",
        "fuente_maestra": MASTER_COLLECTION,
        "institucion": "Ministerio de Salud del Perú",
        "compendios_descubiertos": len(compendia),
        "documentos_unicos": len(documents),
        "documentos_procesados": len(manifest_docs),
        "documentos_materializados_rag": materialized,
        "fallos": failures,
        "deduplicacion": "url_oficial",
        "documentos": manifest_docs,
    }
    manifest_path = args.output / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"\nManifest: {manifest_path}")
    print(f"Documentos únicos descubiertos: {len(documents)}")
    print(f"Materializados para RAG: {materialized}")
    print(f"Fallos: {failures}")

    if len(compendia) != EXPECTED_COMPENDIA:
        return 2
    if not documents:
        return 3
    if args.materialize and materialized == 0:
        return 4
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
