from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, parse_qs, urlencode, urlunparse

import httpx

MASTER_COLLECTION = "https://www.gob.pe/institucion/minsa/colecciones/61810"
DEFAULT_OUTPUT = Path("knowledge/minsa/serums-2026-ii")
USER_AGENT = "SIP-AI-RAG/1.0 (+biblioteca SERUMS; fuente oficial gob.pe)"
NORM_RE = re.compile(r"/institucion/minsa/normas-legales/\d+")
COLLECTION_RE = re.compile(r"/institucion/minsa/colecciones/\d+")
PDF_RE = re.compile(r"\.pdf(?:$|\?)", re.I)


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
    value = value.strip("-")
    return (value[:100] or fallback).strip("-")


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
    if not found:
        raise RuntimeError("No se localizaron los compendios en la colección maestra oficial.")
    return sorted(found.items(), key=lambda item: item[1].lower())


def discover_norms(client: httpx.Client, collection_url: str, max_sheets: int = 20) -> dict[str, str]:
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
        if page_found == 0:
            empty_streak += 1
        else:
            empty_streak = 0
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
        if PDF_RE.search(urlparse(url).path) or "cdn.www.gob.pe" in url:
            if ".pdf" in url.lower():
                candidates.append(url)

    # Algunos enlaces PDF oficiales aparecen en atributos/JSON embebido y no como <a>.
    for raw in re.findall(r'https?://[^"\'<>\s]+', response.text):
        raw = raw.replace("\\u0026", "&").replace("\\/", "/")
        if "gob.pe" in raw and ".pdf" in raw.lower():
            candidates.append(raw)

    unique = []
    seen = set()
    for url in candidates:
        if url not in seen:
            seen.add(url)
            unique.append(url)

    return title, unique[0] if unique else ""


def write_sidecar(pdf_path: Path, doc: OfficialDocument) -> Path:
    metadata_path = pdf_path.with_suffix(".metadata.json")
    payload = {
        "id": f"MINSA-SERUMS-2026-II-{gob_id(doc.norm_url)}",
        "titulo": doc.title or pdf_path.stem,
        "institucion": "Ministerio de Salud del Perú",
        "bibliografia": "SERUMS 2026-II",
        "compendios_origen": sorted(doc.compendia),
        "url_oficial": doc.norm_url,
        "pdf_oficial": doc.pdf_url,
        "estado_validacion": "VALIDADO_OFICIAL",
        "tipo_fuente": "pdf_oficial",
        "regla_evidencia": "Conservar página exacta del PDF para afirmaciones documentales."
    }
    metadata_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return metadata_path


def download_pdf(client: httpx.Client, doc: OfficialDocument, output: Path) -> tuple[Path, Path]:
    response = fetch(client, doc.pdf_url)
    content_type = response.headers.get("content-type", "").lower()
    if "pdf" not in content_type and not response.content.startswith(b"%PDF"):
        raise RuntimeError(f"El recurso no parece PDF: {doc.pdf_url}")

    ident = gob_id(doc.norm_url)
    slug = safe_slug(doc.title, f"documento-{ident}")
    pdf_path = output / f"{ident}-{slug}.pdf"
    pdf_path.write_bytes(response.content)
    return pdf_path, write_sidecar(pdf_path, doc)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sincroniza bibliografía oficial MINSA SERUMS 2026-II hacia knowledge/."
    )
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--download", action="store_true", help="Descarga PDF oficiales y crea sidecars.")
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
        downloaded = 0
        for index, doc in enumerate(ordered, start=1):
            try:
                page_title, pdf_url = discover_pdf(client, doc.norm_url)
                if page_title:
                    doc.title = page_title
                doc.pdf_url = pdf_url

                item = {
                    "id": f"MINSA-SERUMS-2026-II-{gob_id(doc.norm_url)}",
                    "titulo": doc.title,
                    "url_oficial": doc.norm_url,
                    "pdf_oficial": doc.pdf_url or None,
                    "compendios_origen": sorted(doc.compendia),
                    "estado_validacion": "VALIDADO_OFICIAL" if doc.pdf_url else "CORROBORADO_PENDIENTE_PDF_OFICIAL",
                }
                manifest_docs.append(item)

                if args.download and doc.pdf_url:
                    pdf_path, metadata_path = download_pdf(client, doc, args.output)
                    downloaded += 1
                    print(f"[{index}/{len(ordered)}] PDF: {pdf_path.name}")
                    print(f"  metadata: {metadata_path.name}")
                else:
                    print(f"[{index}/{len(ordered)}] {'PDF localizado' if doc.pdf_url else 'PDF pendiente'}: {doc.norm_url}")
            except Exception as exc:
                print(f"[{index}/{len(ordered)}] ERROR: {doc.norm_url}: {exc}")
                manifest_docs.append({
                    "id": f"MINSA-SERUMS-2026-II-{gob_id(doc.norm_url)}",
                    "titulo": doc.title,
                    "url_oficial": doc.norm_url,
                    "pdf_oficial": None,
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
        "pdf_descargados": downloaded,
        "deduplicacion": "url_oficial",
        "documentos": manifest_docs,
    }
    manifest_path = args.output / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"\nManifest: {manifest_path}")
    print(f"Documentos únicos descubiertos: {len(documents)}")
    if not args.download:
        print("Modo inventario. Use --download para incorporar los PDF oficiales al corpus local.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
