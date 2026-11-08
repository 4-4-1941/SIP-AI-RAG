#!/usr/bin/env python3
"""Justificador normativo: busca en las normas y guías (knowledge/**/*.md y *.json con texto extraído) el respaldo
de la clave de cada pregunta parafraseada y la audita con la IA.
Veredictos: RESPALDADA / PARCIAL / SIN_RESPALDO / CONTRADICE.
La cita textual se verifica por código: si no existe literal en la norma,
el veredicto baja a SIN_RESPALDO.
NO modifica parafraseadas.json ni toca Supabase.
Uso (desde ~/SIP-AI-RAG):
  python3 rag/justificador_normativo.py            -> prueba con 100 preguntas
  python3 rag/justificador_normativo.py --todo     -> todas
  python3 rag/justificador_normativo.py --todo --reevaluar -> repite las SIN_RESPALDO con las guías y normas JSON
Opciones: --n 100  --rpm 30  --reintentar (repite las que fallaron)"""
import argparse, json, math, os, random, re, sys, time, unicodedata, urllib.error, urllib.request
from collections import Counter, defaultdict

RAIZ = os.getcwd()
PARAF = os.path.join(RAIZ, "data", "preguntas", "parafraseadas.json")
SALIDA = os.path.join(RAIZ, "data", "preguntas", "justificacion_normativa.json")
PROMPT = os.path.join(RAIZ, "data", "flashcards", "config", "prompt_justificacion_normativa.txt")
URL = "https://integrate.api.nvidia.com/v1/chat/completions"
MODELO = "nvidia/nemotron-3.5-lightning-30b-a3b"
VEREDICTOS = ("RESPALDADA", "PARCIAL", "SIN_RESPALDO", "CONTRADICE")
STOP = set("de la el los las del y o en a al un una por para con que se su sus es lo como e u "
           "son ser debe deben cual cuales segun entre sobre".split())
INSTRUCCION = (
    "\n\nResponde SOLO un JSON con estas claves: veredicto (RESPALDADA, PARCIAL, SIN_RESPALDO o "
    "CONTRADICE), norma (nombre del documento o vacio), cita_textual (copia EXACTA de un "
    "fragmento dado, maximo 40 palabras, o vacio), explicacion (maximo 25 palabras). "
    "Si ningun fragmento respalda la respuesta, usa SIN_RESPALDO. No inventes citas.")
PROMPT_BASE = ("Eres auditor normativo de preguntas del examen SERUMS (Peru). Te doy una pregunta, "
               "su respuesta marcada como correcta y fragmentos de normas oficiales. Decide si los "
               "fragmentos respaldan, respaldan en parte, no respaldan o contradicen esa respuesta.")


def norm(t):
    t = unicodedata.normalize("NFD", str(t).lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]+", " ", t)


def toks(t):
    return [w for w in norm(t).split() if w not in STOP and len(w) > 1]


# ---------- índice BM25 ----------
def trocear(texto, palabras=120, paso=90):
    w = texto.split()
    for i in range(0, max(len(w), 1), paso):
        trozo = " ".join(w[i:i + palabras])
        if len(trozo.split()) >= 25:
            yield trozo


def textos_json(obj, minimo=150):
    """Devuelve todos los textos largos de un JSON (páginas, contenido documental, etc.)."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k.startswith(("huella", "url", "pdf_", "archivo")):
                continue
            yield from textos_json(v, minimo)
    elif isinstance(obj, list):
        for v in obj:
            yield from textos_json(v, minimo)
    elif isinstance(obj, str) and len(obj) >= minimo:
        yield obj


def construir_indice():
    chunks, origen = [], []
    for base, dirs, files in os.walk(os.path.join(RAIZ, "knowledge")):
        dirs[:] = [d for d in dirs if d not in (".git", "archive", "banco_preguntas")]
        for f in files:
            if re.search(r"\(\d+\)|_\d\.json$", f) or f.endswith(("metadata.json", "manifest.json")):
                continue
            ruta = os.path.join(base, f)
            try:
                if f.endswith(".md"):
                    txt, nombre = open(ruta, encoding="utf-8", errors="ignore").read(), f[:-3]
                elif f.endswith(".json"):
                    d = json.load(open(ruta, encoding="utf-8"))
                    txt = "\n".join(textos_json(d))
                    nombre = (d.get("titulo") or d.get("title") or f[:-5]) if isinstance(d, dict) else f[:-5]
                    nombre = str(nombre)[:110]
                else:
                    continue
            except Exception:
                continue
            for c in trocear(txt):
                chunks.append(c)
                origen.append(nombre)
    inv, largos = defaultdict(list), []
    for i, c in enumerate(chunks):
        t = toks(c)
        largos.append(len(t))
        for w, n in Counter(t).items():
            inv[w].append((i, n))
    prom = (sum(largos) / len(largos)) if largos else 1
    return {"chunks": chunks, "origen": origen, "inv": inv, "largos": largos, "prom": prom}


def buscar(ix, consulta, k=5):
    N = len(ix["chunks"])
    puntaje = defaultdict(float)
    for w in set(toks(consulta)):
        lista = ix["inv"].get(w)
        if not lista:
            continue
        idf = math.log(1 + (N - len(lista) + 0.5) / (len(lista) + 0.5))
        for i, n in lista:
            d = 1.5 * (1 - 0.75 + 0.75 * ix["largos"][i] / ix["prom"])
            puntaje[i] += idf * n * 2.5 / (n + d)
    return sorted(puntaje, key=puntaje.get, reverse=True)[:k]


# ---------- IA ----------
def leer_clave():
    for k, v in os.environ.items():
        if k.startswith("NVIDIA") and "KEY" in k and v:
            return v
    ruta = os.path.join(RAIZ, ".env")
    if os.path.exists(ruta):
        for linea in open(ruta, encoding="utf-8"):
            m = re.match(r"\s*(NVIDIA\w*KEY\w*)\s*=\s*(.+)", linea)
            if m:
                return m.group(2).strip().strip("'\"")
    sys.exit("No encontré la clave NVIDIA en .env (variable que empiece con NVIDIA y tenga KEY).")


def llamar_ia(clave, sistema, usuario):
    cuerpo = {"model": MODELO, "temperature": 0, "max_tokens": 500,
              "messages": [{"role": "system", "content": sistema},
                           {"role": "user", "content": usuario}],
              "chat_template_kwargs": {"enable_thinking": False}}
    for intento in range(4):
        req = urllib.request.Request(URL, json.dumps(cuerpo).encode(), {
            "Authorization": "Bearer " + clave, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(15 * (intento + 1))
                continue
            raise
    raise RuntimeError("429 repetido")


def extraer_json(txt):
    m = re.search(r"\{.*\}", txt, re.S)
    return json.loads(m.group(0)) if m else None


def auditar(clave, sistema, p, ix):
    consulta = f"{p['enunciado']} {p['clave_texto']} {p.get('justificacion', '')}"
    idx = buscar(ix, consulta)
    frags = [(ix["origen"][i], ix["chunks"][i]) for i in idx]
    if not frags:
        return {"veredicto": "SIN_RESPALDO", "motivo": "sin_fragmentos"}
    bloque = "\n\n".join(f"[{n}] ({o}) {c}" for n, (o, c) in enumerate(frags, 1))
    usuario = (f"PREGUNTA: {p['enunciado']}\nOPCIONES: {json.dumps(p['opciones'], ensure_ascii=False)}\n"
               f"RESPUESTA CORRECTA: {p['clave']}) {p['clave_texto']}\n\nFRAGMENTOS:\n{bloque}")
    r = extraer_json(llamar_ia(clave, sistema, usuario))
    if not r or r.get("veredicto") not in VEREDICTOS:
        raise ValueError("respuesta de IA sin formato")
    cita = str(r.get("cita_textual") or "").strip()
    todo = norm(" ".join(c for _, c in frags))
    if r["veredicto"] != "SIN_RESPALDO":
        if not cita or norm(cita).strip() not in todo:
            r["motivo"] = "cita_no_literal_o_vacia"
            r["veredicto"] = "SIN_RESPALDO"
            cita = ""
    return {"veredicto": r["veredicto"], "norma": r.get("norma", ""), "cita_textual": cita,
            "explicacion": r.get("explicacion", ""), "motivo": r.get("motivo", ""),
            "fuentes": sorted({o for o, _ in frags})}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--todo", action="store_true")
    ap.add_argument("--n", type=int, default=100)
    ap.add_argument("--rpm", type=int, default=30)
    ap.add_argument("--reintentar", action="store_true")
    ap.add_argument("--reevaluar", action="store_true", help="repite las SIN_RESPALDO y con error usando el índice ampliado")
    a = ap.parse_args()
    if not os.path.exists(PARAF):
        sys.exit("No existe data/preguntas/parafraseadas.json. ¿Estás en ~/SIP-AI-RAG?")
    L = json.load(open(PARAF, encoding="utf-8"))
    L = L if isinstance(L, list) else next(v for v in L.values() if isinstance(v, list))
    if not a.todo:
        L = random.Random(7).sample(L, min(a.n, len(L)))
    res = json.load(open(SALIDA, encoding="utf-8")) if os.path.exists(SALIDA) else {}
    def repetir(r):
        return "error" in r or r.get("veredicto") == "SIN_RESPALDO"
    pend = [p for p in L if p["id"] not in res or ((a.reintentar or a.reevaluar) and "error" in res[p["id"]])
            or (a.reevaluar and repetir(res[p["id"]]))]
    print(f"Preguntas: {len(L)} | pendientes: {len(pend)}")
    if not pend:
        resumen(L, res)
        return
    sistema = (open(PROMPT, encoding="utf-8").read() if os.path.exists(PROMPT) else PROMPT_BASE) + INSTRUCCION
    ix = construir_indice()
    print(f"Índice: {len(ix['chunks'])} fragmentos de normas")
    if not ix["chunks"]:
        sys.exit("No encontré .md en knowledge/. ¿Estás en ~/SIP-AI-RAG?")
    clave, espera = leer_clave(), 60.0 / a.rpm
    for n, p in enumerate(pend, 1):
        t0 = time.time()
        try:
            antes = res.get(p["id"], {}).get("veredicto")
            res[p["id"]] = auditar(clave, sistema, p, ix)
            if antes:
                res[p["id"]]["antes"] = antes
        except Exception as e:
            res[p["id"]] = {"error": str(e)[:150]}
        if n % 10 == 0 or n == len(pend):
            json.dump(res, open(SALIDA, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print(f"[avance] {n}/{len(pend)}")
        time.sleep(max(0, espera - (time.time() - t0)))
    resumen(L, res)


def resumen(L, res):
    c = Counter(res[p["id"]].get("veredicto", "ERROR") for p in L if p["id"] in res)
    n = sum(c.values()) or 1
    print("\nRESULTADO:")
    for k, v in c.most_common():
        print(f"  {k}: {v} ({100 * v / n:.0f}%)")
    print("\nDetalle: data/preguntas/justificacion_normativa.json")


if __name__ == "__main__":
    main()
      
