from __future__ import annotations
import argparse, hashlib, json, re, tempfile, time
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urljoin, urlparse, urlunparse
import httpx
from pypdf import PdfReader

MASTER_COLLECTION="https://www.gob.pe/institucion/minsa/colecciones/61810"
DEFAULT_OUTPUT=Path("knowledge/minsa/serums-2026-ii")
USER_AGENT="SIP-AI-RAG/1.1 (+biblioteca SERUMS; fuente oficial gob.pe)"
NORM_RE=re.compile(r"/institucion/minsa/normas-legales/\d+")
COLLECTION_RE=re.compile(r"/institucion/minsa/colecciones/\d+")
EXPECTED_COMPENDIA=17

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self._href=""; self._text=[]
    def handle_starttag(self,tag,attrs):
        if tag.lower()=="a":
            self._href=dict(attrs).get("href") or ""; self._text=[]
    def handle_data(self,data):
        if self._href:self._text.append(data)
    def handle_endtag(self,tag):
        if tag.lower()=="a" and self._href:
            self.links.append((self._href," ".join("".join(self._text).split())))
            self._href=""; self._text=[]

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
    r=fetch(client,MASTER_COLLECTION); urls=[]
    for url,_ in links(r.text,str(r.url)):
        c=canonical(url)
        if COLLECTION_RE.search(c) and c!=canonical(MASTER_COLLECTION) and c not in urls:
            urls.append(c)
    resolved=[]
    for c in urls:
        cr=fetch(client,c); h=page_heading(cr.text)
        if "serums" in h.lower():
            resolved.append((c,clean_compendium_name(h)))
    if len(resolved)!=EXPECTED_COMPENDIA:
        raise RuntimeError(f"Se esperaban {EXPECTED_COMPENDIA} compendios oficiales y se detectaron {len(resolved)}.")
    return sorted(resolved,key=lambda x:x[1].lower())

def discover_norms(client,collection_url,max_sheets=30):
    found={}; empty=0
    for sheet in range(1,max_sheets+1):
        r=fetch(client,collection_url if sheet==1 else with_sheet(collection_url,sheet)); n=0
        for url,text in links(r.text,str(r.url)):
            c=canonical(url)
            if NORM_RE.search(c):
                if c not in found:n+=1
                found[c]=text.strip() or found.get(c,"")
        empty=empty+1 if n==0 else 0
        if empty>=2:break
    return found

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
        comps=discover_compendia(client)
        for cu,cn in comps:
            for nu,label in discover_norms(client,cu).items():
                d=docs.setdefault(nu,OfficialDocument(nu)); d.compendia.add(cn); d.compendia_urls.add(cu)
                if label:
                    d.index_labels.add(label)
                    if not d.title:d.title=label
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
      "compendios_descubiertos":len(comps),"compendios":[{"url":u,"nombre":n} for u,n in comps],
      "documentos_unicos":len(docs),"documentos_procesados":len(items),"documentos_materializados_rag":materialized,
      "fallos":failures,"deduplicacion":"url_oficial","documentos":items}
    (a.output/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    if len(comps)!=EXPECTED_COMPENDIA:return 2
    if not docs:return 3
    if a.materialize and materialized==0:return 4
    return 0
if __name__=="__main__": raise SystemExit(main())
