from __future__ import annotations
import argparse, hashlib, json, re
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse
import httpx

LISTING="https://www.gob.pe/institucion/minsa/normas-legales"
REGISTRY=Path("data/metadata/serums/serums-normas.json")
OUTPUT=Path("knowledge/normas/serums")
OFFICIAL={"gob.pe","www.gob.pe","busquedas.elperuano.pe","elperuano.pe","www.elperuano.pe"}
DETAIL_RX=re.compile(r"/institucion/minsa/normas-legales/\d+")
DIRECT=("serums","servicio rural y urbano marginal de salud","ley 23330","ley n° 23330","ley nº 23330",
        "005-97-sa","evaluación para el serums","evaluacion para el serums")
INDIRECT=("plazas remuneradas","plazas equivalentes","adjudicación de plazas","adjudicacion de plazas",
          "profesionales de la salud","dirección general de personal de la salud","digep")
NUMBER=re.compile(r"\b(\d{1,5}-\d{4}(?:/MINSA|-MINSA|-SA|/SA|-[A-Z]+-MINSA)?)\b",re.I)

class LinkParser(HTMLParser):
    def __init__(self): super().__init__(); self.items=[]; self.href=""; self.buf=[]
    def handle_starttag(self,tag,attrs):
        if tag.lower()=="a": self.href=dict(attrs).get("href") or ""; self.buf=[]
    def handle_data(self,data):
        if self.href:self.buf.append(data)
    def handle_endtag(self,tag):
        if tag.lower()=="a" and self.href:
            self.items.append((self.href," ".join("".join(self.buf).split()))); self.href=""; self.buf=[]

def canonical(url):
    p=urlparse(url); return urlunparse((p.scheme or "https",p.netloc.lower(),p.path.rstrip("/"),"","",""))
def official(url): return urlparse(url).netloc.lower() in OFFICIAL
def classify(text):
    low=text.lower()
    if any(x in low for x in DIRECT): return "confirmada"
    if any(x in low for x in INDIRECT): return "pendiente"
    return "descartada"
def norm_number(text):
    m=NUMBER.search(text); return m.group(1).upper() if m else ""
def norm_type(text):
    low=text.lower()
    for key,name in [("resolución ministerial","Resolución Ministerial"),("resolucion ministerial","Resolución Ministerial"),
      ("resolución directoral","Resolución Directoral"),("resolucion directoral","Resolución Directoral"),
      ("decreto supremo","Decreto Supremo"),("decreto legislativo","Decreto Legislativo"),
      ("decreto de urgencia","Decreto de Urgencia"),("norma técnica","Norma Técnica de Salud"),
      ("directiva","Directiva"),("lineamiento","Lineamiento"),("ley","Ley")]:
        if key in low:return name
    return "Otra disposición"
def page_title(html):
    m=re.search(r"<h1[^>]*>(.*?)</h1>",html,re.I|re.S) or re.search(r"<title[^>]*>(.*?)</title>",html,re.I|re.S)
    return " ".join(re.sub(r"<[^>]+>"," ",m.group(1)).split()) if m else ""
def plain(html): return " ".join(re.sub(r"<[^>]+>"," ",html).split())
def pubdate(text):
    m=re.search(r"(?:Fecha de publicaci[oó]n[:\s]*)?(\d{1,2})\s+de\s+([a-záéíóú]+)\s+de\s+(\d{4})",text,re.I)
    months={"enero":1,"febrero":2,"marzo":3,"abril":4,"mayo":5,"junio":6,"julio":7,"agosto":8,"septiembre":9,"setiembre":9,"octubre":10,"noviembre":11,"diciembre":12}
    if m and m.group(2).lower() in months:return f"{m.group(3)}-{months[m.group(2).lower()]:02d}-{int(m.group(1)):02d}"
    return ""
def discover_from_listing(html,base=LISTING):
    p=LinkParser(); p.feed(html); out=[]
    for href,label in p.items:
        u=canonical(urljoin(base,href))
        if official(u) and DETAIL_RX.search(urlparse(u).path): out.append((u,label))
    return list(dict.fromkeys(out))
def load(path=REGISTRY):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"schema_version":1,"baseline_creado":None,"normas":[]}
def duplicate(item,reg):
    u,n,h=canonical(item.get("url_oficial","")),item.get("numero_norma","").upper(),item.get("hash_documento","")
    for old in reg.get("normas",[]):
        if u and u==canonical(old.get("url_oficial","")):return True
        if n and n==old.get("numero_norma","").upper():return True
        if h and h==old.get("hash_documento",""):return True
    return False

@dataclass
class Norm:
    id:str; organismo_emisor:str; tipo_documental:str; numero_norma:str; titulo:str
    fecha_publicacion:str; fecha_version:str; estado_vigencia:str; estado_validacion:str
    relacion_serums:str; resumen:str; impacto_serums:str; url_oficial:str; pdf_oficial:str
    compendios_origen:list; archivo_rag:str; pagina_seccion:str; texto_indice:str
    fecha_deteccion:str; fecha_incorporacion:str; visible_hasta:str; hash_documento:str
    tipo_novedad:str="NUEVA"

def build(url,html,now):
    txt=plain(html); ttl=page_title(html); rel=classify(ttl+" "+txt); num=norm_number(ttl+" "+txt)
    ident=hashlib.sha1((num or canonical(url)).encode()).hexdigest()[:16]; iso=now.isoformat(); date=pubdate(txt)
    return Norm(f"SERUMS-NORMA-{ident}","Ministerio de Salud del Perú",norm_type(ttl+" "+txt),num,ttl,date,date,
      "NO_DETERMINADO","VALIDADO_OFICIAL" if rel=="confirmada" else "PENDIENTE_REVISION",rel,"",
      "Requiere lectura de la publicación oficial para determinar el impacto concreto.",canonical(url),"",[],"",
      "publicación oficial",(ttl+" "+num+" SERUMS").strip(),iso,iso,(now+timedelta(hours=72)).isoformat(),
      hashlib.sha256(html.encode()).hexdigest())

def materialize(n,html,out=OUTPUT):
    out.mkdir(parents=True,exist_ok=True); slug=re.sub(r"[^a-z0-9]+","-", (n.numero_norma or n.id).lower()).strip("-")
    md=out/f"{slug}.md"; meta=out/f"{slug}.metadata.json"
    md.write_text(f"# {n.tipo_documental} {n.numero_norma}\n\n{n.titulo}\n\nFuente oficial: {n.url_oficial}\n\n[[SECCION PUBLICACION OFICIAL]]\n{plain(html)}\n",encoding="utf-8")
    n.archivo_rag=str(md)
    meta.write_text(json.dumps({"id":n.id,"titulo":n.titulo,"numero_norma":n.numero_norma,"url_oficial":n.url_oficial,
      "seccion":"publicación oficial","estado_validacion":n.estado_validacion,"relacion_serums":n.relacion_serums},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

def candidates(client,sheets):
    seen={}
    for sheet in range(1,sheets+1):
        url=LISTING if sheet==1 else f"{LISTING}?sheet={sheet}"
        r=client.get(url); r.raise_for_status()
        for u,label in discover_from_listing(r.text,str(r.url)):seen[u]=label
    return list(seen)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--candidate",action="append",default=[]); ap.add_argument("--sheets",type=int,default=3); ap.add_argument("--baseline",action="store_true")
    a=ap.parse_args(); reg=load(); now=datetime.now(timezone.utc); report={"incorporadas":[],"pendientes":[],"duplicadas":[],"descartadas":[]}
    with httpx.Client(timeout=30,follow_redirects=True,headers={"User-Agent":"SIP-AI-RAG vigilancia SERUMS"}) as c:
        urls=a.candidate or candidates(c,a.sheets)
        for url in urls:
            if not official(url):report["descartadas"].append({"url":url,"motivo":"fuente_no_oficial"});continue
            try:
                r=c.get(url);r.raise_for_status();n=build(str(r.url),r.text,now);item=asdict(n)
                if n.relacion_serums=="descartada":continue
                if duplicate(item,reg):report["duplicadas"].append(item);continue
                if n.relacion_serums=="pendiente":report["pendientes"].append(item);continue
                if a.baseline:n.tipo_novedad="HISTORICA";n.visible_hasta=n.fecha_incorporacion
                materialize(n,r.text);reg["normas"].append(asdict(n));report["incorporadas"].append(asdict(n))
            except Exception as e:report["descartadas"].append({"url":url,"motivo":f"{type(e).__name__}: {e}"})
    if a.baseline and not reg.get("baseline_creado"):reg["baseline_creado"]=now.isoformat()
    REGISTRY.parent.mkdir(parents=True,exist_ok=True);REGISTRY.write_text(json.dumps(reg,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:len(v) for k,v in report.items()},ensure_ascii=False))
if __name__=="__main__":main()
