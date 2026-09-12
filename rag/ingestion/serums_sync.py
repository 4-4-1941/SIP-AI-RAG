from __future__ import annotations
import argparse, hashlib, json, re, tempfile, time
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urljoin, urlparse, urlunparse
import httpx
from pypdf import PdfReader

MASTER_COLLECTION="https://www.gob.pe/institucion/minsa/colecciones/61810"
COMPENDIA_METADATA=Path("data/metadata/serums/serums-2026-ii-compendios.json")
DEFAULT_OUTPUT=Path("knowledge/minsa/serums-2026-ii")
USER_AGENT="SIP-AI-RAG/1.1 (+biblioteca SERUMS; fuente oficial gob.pe)"
NORM_RE=re.compile(r"/institucion/minsa/normas-legales/\d+")
COLLECTION_RE=re.compile(r"/institucion/minsa/colecciones/\d+")
EXPECTED_COMPENDIA=17

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.link_details=[]; self._href=""; self._text=[]; self._attrs={}
    def handle_starttag(self,tag,attrs):
        if tag.lower()=="a":
            self._attrs=dict(attrs); self._href=self._attrs.get("href") or ""; self._text=[]
    def handle_data(self,data):
        if self._href:self._text.append(data)
    def handle_endtag(self,tag):
        if tag.lower()=="a" and self._href:
            text=" ".join("".join(self._text).split())
            self.links.append((self._href,text)); self.link_details.append((self._href,text,self._attrs))
            self._href=""; self._text=[]; self._attrs={}

@dataclass
class OfficialDocument:
    norm_url:str
    title:str=""
    pdf_url:str=""
    compendia:set[str]=field(default_factory=set)
    compendia_urls:set[str]=field(default_factory=set)
    index_labels:set[str]=field(default_factory=set)

def links(html,base):
    p=LinkParser(); p.feed(html)
    return [(urljoin(base,h),t) for h,t in p.links if h]
def detailed_links(html,base):
    p=LinkParser(); p.feed(html)
    return [(urljoin(base,h),t,a) for h,t,a in p.link_details if h]
def canonical(url):
    p=urlparse(url); return urlunparse((p.scheme or "https",p.netloc,p.path.rstrip("/"),"","",""))
def with_sheet(url,sheet):
    p=urlparse(url); q=parse_qs(p.query); q["sheet"]=[str(sheet)]
    return urlunparse((p.scheme,p.netloc,p.path,p.params,urlencode(q,doseq=True),""))
def safe_slug(v,fallback):
    v=re.sub(r"[^a-z0-9]+","-",v.lower()); return (v.strip("-")[:100] or fallback).strip("-")
def gob_id(url):
    p=[x for x in urlparse(url).path.split("/") if x]
    return p[-1].split("-",1)[0] if p else hashlib.sha1(url.encode()).hexdigest()[:12]
def fetch(client,url,attempts=3):
    last=None
    for i in range(attempts):
        try:
            r=client.get(url); r.raise_for_status(); return r
        except (httpx.HTTPError,httpx.TimeoutException) as e:
            last=e
            if i+1<attempts: time.sleep(1.2*(i+1))
    raise RuntimeError(f"No se pudo recuperar fuente oficial: {url}") from last

def page_heading(html):
    m=re.search(r"<h1[^>]*>(.*?)</h1>",html,re.I|re.S)
    if not m: return ""
    return " ".join(re.sub(r"<[^>]+>"," ",m.group(1)).split())

def clean_compendium_name(title):
    title=re.sub(r"^Evaluaci[oó]n para el Serums:\s*","",title,flags=re.I)
    title=re.sub(r"^bibliograf[ií]a relacionada a los contenidos (?:de|del|de la)\s*","",title,flags=re.I)
    return title.strip(" .:-") or "Compendio SERUMS"

def discover_compendia(client):
    data=json.loads(COMPENDIA_METADATA.read_text(encoding="utf-8"))
    items=data.get("compendios",[])
    if len(items)!=EXPECTED_COMPENDIA:
        raise RuntimeError(f"Se esperaban {EXPECTED_COMPENDIA} compendios en metadata y hay {len(items)}.")
    resolved=[]; seen=set()
    for item in items:
        name=str(item.get("nombre") or "").strip()
        url=canonical(str(item.get("url_oficial") or "").strip())
        expected=int(item.get("cantidad_normas") or 0)
        if not name or not url or url in seen:
            raise RuntimeError("Metadata de compendios incompleta o duplicada.")
        seen.add(url)
        resolved.append((url,name,expected))
    return resolved

def discover_norms(client,collection_url,expected,max_sheets=40):
    found={}; occurrences={}; empty=0
    for sheet in range(1,max_sheets+1):
        r=fetch(client,collection_url if sheet==1 else with_sheet(collection_url,sheet)); n=0
        page_seen=set()
        for url,text,attrs in detailed_links(r.text,str(r.url)):
            c=canonical(url)
            if not NORM_RE.search(c):
                continue
            # Las colecciones incluyen en todas sus hojas la norma de creación
            # institucional dentro de los menús web y móvil. No es un elemento
            # del compendio y debe excluirse por su contexto de navegación, no
            # por una URL o por una posición de página inferida.
            section=(attrs.get("data-ga-title-section") or "").strip().lower()
            origin=(attrs.get("data-origin") or "").strip().lower()
            if section=="menu" or "menu-minsa-norma-de-creacion" in origin:
                continue
            label=text.strip()
            occurrences.setdefault(c,[]).append({"sheet":sheet,"texto":label})
            if c not in page_seen and c not in found:
                n+=1
            page_seen.add(c)
            found[c]=label or found.get(c,"")
        empty=empty+1 if n==0 else 0
        if empty>=2:break

    return found,[]

def discover_pdf(client,norm_url):
    r=fetch(client,norm_url); title=page_heading(r.text)
    candidates=[]
    for url,_ in links(r.text,str(r.url)):
        if ".pdf" in url.lower() and ("gob.pe" in url): candidates.append(url)
    for raw in re.findall(r'https?://[^"\'<>\s]+',r.text):
        raw=raw.replace("\\u0026","&").replace("\\/","/")
        if "gob.pe" in raw and ".pdf" in raw.lower():candidates.append(raw)
    unique=list(dict.fromkeys(candidates))
    return title, unique[0] if unique else ""

def pdf_to_markdown(data,title,source,pdf):
    with tempfile.NamedTemporaryFile(suffix=".pdf") as tmp:
        tmp.write(data); tmp.flush(); reader=PdfReader(tmp.name)
        parts=[f"# {title}","",f"Fuente oficial: {source}",f"PDF oficial: {pdf}",""]; n=0
        for i,page in enumerate(reader.pages,1):
            text=(page.extract_text() or "").strip()
            if text:n+=1; parts += [f"[[PAGINA {i}]]",text,""]
        if not n: raise RuntimeError("PDF sin texto extraíble; requiere revisión manual/OCR.")
        return "\n".join(parts).strip()+"\n"

def sidecar(path,doc):
    p=path.with_suffix(".metadata.json")
    payload={"id":f"MINSA-SERUMS-2026-II-{gob_id(doc.norm_url)}","titulo":doc.title or path.stem,
      "institucion":"Ministerio de Salud del Perú","bibliografia":"SERUMS 2026-II",
      "compendios_origen":sorted(doc.compendia),"compendios_urls":sorted(doc.compendia_urls),
      "texto_indice":" | ".join(sorted(doc.index_labels)),
      "url_oficial":doc.norm_url,"pdf_oficial":doc.pdf_url,"estado_validacion":"VALIDADO_OFICIAL",
      "tipo_fuente":"texto_extraido_pdf_oficial","regla_evidencia":"Conservar página exacta del PDF para afirmaciones documentales."}
    p.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); return p

def materialize(client,doc,out):
    r=fetch(client,doc.pdf_url)
    if "pdf" not in r.headers.get("content-type","").lower() and not r.content.startswith(b"%PDF"):
        raise RuntimeError("El recurso no parece PDF")
    ident=gob_id(doc.norm_url); path=out/f"{ident}-{safe_slug(doc.title,f'documento-{ident}')}.md"
    path.write_text(pdf_to_markdown(r.content,doc.title or path.stem,doc.norm_url,doc.pdf_url),encoding="utf-8")
    return path,sidecar(path,doc)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    ap.add_argument("--materialize",action="store_true"); ap.add_argument("--limit",type=int,default=0)
    ap.add_argument("--timeout",type=float,default=30.0); a=ap.parse_args(); a.output.mkdir(parents=True,exist_ok=True)
    docs={}
    with httpx.Client(timeout=a.timeout,follow_redirects=True,headers={"User-Agent":USER_AGENT,"Accept-Language":"es-PE,es;q=0.9"}) as client:
        comps=discover_compendia(client); comp_stats=[]
        for cu,cn,expected in comps:
            norms,discarded=discover_norms(client,cu,expected)
            comp_stats.append({"url":cu,"nombre":cn,"esperadas":expected,"descubiertas":len(norms),
              "coincide":len(norms)==expected,"descartados":discarded})
            for x in discarded:
                print(f'DESCARTADO | {cn} | {x["url"]} | {x["texto"]} | {x["motivo"]}')
            for nu,label in norms.items():
                d=docs.setdefault(nu,OfficialDocument(nu)); d.compendia.add(cn); d.compendia_urls.add(cu)
                if label:
                    d.index_labels.add(label)
                    if not d.title:d.title=label
        mismatches=[x for x in comp_stats if not x["coincide"]]
        if mismatches:
            raise RuntimeError("Conteo oficial inconsistente: "+json.dumps(mismatches,ensure_ascii=False))
        ordered=sorted(docs.values(),key=lambda d:d.norm_url)
        if a.limit>0:ordered=ordered[:a.limit]
        items=[]; materialized=failures=0
        for d in ordered:
            try:
                t,p=discover_pdf(client,d.norm_url); d.title=t or d.title; d.pdf_url=p
                state="VALIDADO_OFICIAL" if p else "CORROBORADO_PENDIENTE_PDF_OFICIAL"
                item={"id":f"MINSA-SERUMS-2026-II-{gob_id(d.norm_url)}","titulo":d.title,"url_oficial":d.norm_url,
                  "pdf_oficial":p or None,"compendios_origen":sorted(d.compendia),"compendios_urls":sorted(d.compendia_urls),
                  "texto_indice":" | ".join(sorted(d.index_labels)),"estado_validacion":state}
                if a.materialize and p:
                    cp,mp=materialize(client,d,a.output); item["archivo_rag"]=cp.name; item["metadata_rag"]=mp.name; materialized+=1
                items.append(item)
            except Exception as e:
                failures+=1; items.append({"id":f"MINSA-SERUMS-2026-II-{gob_id(d.norm_url)}","titulo":d.title,
                 "url_oficial":d.norm_url,"pdf_oficial":d.pdf_url or None,"compendios_origen":sorted(d.compendia),
                 "compendios_urls":sorted(d.compendia_urls),"texto_indice":" | ".join(sorted(d.index_labels)),"estado_validacion":"CORROBORADO_PENDIENTE_PDF_OFICIAL",
                 "error_sincronizacion":str(e)})
    manifest={"id":"SERUMS-2026-II-CORPUS","fuente_maestra":MASTER_COLLECTION,"institucion":"Ministerio de Salud del Perú",
      "compendios_descubiertos":len(comps),"compendios":comp_stats,
      "documentos_unicos":len(docs),"documentos_procesados":len(items),"documentos_materializados_rag":materialized,
      "fallos":failures,"deduplicacion":"url_oficial","documentos":items}

    manifest_path=a.output/"manifest.json"; tmp_path=a.output/"manifest.tmp.json"
    previous=manifest_path.read_bytes() if manifest_path.exists() else None
    tmp_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    try:
        candidate=json.loads(tmp_path.read_text(encoding="utf-8"))
        candidate_docs=candidate.get("documentos",[])
        if candidate.get("compendios_descubiertos")!=EXPECTED_COMPENDIA:
            raise RuntimeError("Manifest temporal inválido: compendios_descubiertos != 17")
        if len(candidate.get("compendios",[]))!=EXPECTED_COMPENDIA:
            raise RuntimeError("Manifest temporal inválido: no contiene 17 compendios")
        if any(not x.get("coincide") for x in candidate["compendios"]):
            raise RuntimeError("Manifest temporal inválido: conteo de compendios inconsistente")
        if not candidate_docs:
            raise RuntimeError("Manifest temporal inválido: documentos vacío")
        if candidate.get("documentos_unicos",0)<=0 or candidate.get("documentos_procesados")!=len(candidate_docs):
            raise RuntimeError("Manifest temporal inválido: totales de documentos")
        ids=[x.get("id") for x in candidate_docs]; urls=[x.get("url_oficial") for x in candidate_docs]
        if not all(ids) or len(ids)!=len(set(ids)):
            raise RuntimeError("Manifest temporal inválido: IDs vacíos o duplicados")
        if not all(urls) or len(urls)!=len(set(urls)):
            raise RuntimeError("Manifest temporal inválido: URLs vacías o duplicadas")
        if any(not x.get("compendios_origen") or not x.get("compendios_urls") for x in candidate_docs):
            raise RuntimeError("Manifest temporal inválido: documento sin compendio real de origen")
        if any(re.search(r"^Ver las \\d+ normas$",str(v),re.I)
               for x in candidate_docs for v in x.get("compendios_origen",[])):
            raise RuntimeError("Manifest temporal inválido: etiqueta 'Ver las X normas'")
        pending=sum(1 for x in candidate_docs if not x.get("archivo_rag"))
        if candidate.get("documentos_materializados_rag",0)+pending!=len(candidate_docs):
            raise RuntimeError("Manifest temporal inválido: materializados + pendientes != total")
        tmp_path.replace(manifest_path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        if previous is not None and not manifest_path.exists():
            manifest_path.write_bytes(previous)
        raise

    if len(comps)!=EXPECTED_COMPENDIA:return 2
    if not docs:return 3
    if a.materialize and materialized==0:return 4
    return 0
if __name__=="__main__": raise SystemExit(main())
