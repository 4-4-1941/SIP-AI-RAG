#!/usr/bin/env python3
"""Compara la clave de cada pregunta parafraseada con la del banco oficial.
Solo LEE archivos. No llama a la IA ni toca Supabase.
Uso (desde ~/SIP-AI-RAG):  python3 rag/comparar_claves.py
Salida: data/preguntas/revision_claves.csv + resumen en pantalla."""
import csv, json, os, re, sys, unicodedata
from collections import Counter

RAIZ = os.getcwd()
PARAF = os.path.join(RAIZ, "data", "preguntas", "parafraseadas.json")
SALIDA = os.path.join(RAIZ, "data", "preguntas", "revision_claves.csv")
STOP = {"de", "la", "el", "los", "las", "del", "y", "o", "en", "a", "al", "un", "una",
        "por", "para", "con", "que", "se", "su", "sus", "es", "lo", "como", "e", "u"}


def norm(t):
    t = unicodedata.normalize("NFD", str(t).lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]+", " ", t)


def tokens(t):
    return {w for w in norm(t).split() if w not in STOP}


def score(a, b):
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / min(len(ta), len(tb))


def nums(t):
    return set(re.findall(r"\d+", str(t)))


def opciones(rec):
    o = rec.get("opciones")
    if isinstance(o, dict) and o:
        return {str(k).strip().upper(): str(v) for k, v in o.items()}
    if isinstance(o, list) and o:
        out = {}
        for i, v in enumerate(o):
            txt = v.get("texto") or v.get("text") if isinstance(v, dict) else v
            out["ABCDEFGH"[i]] = str(txt)
        return out
    letras = {k: str(rec[k]) for k in "ABCD" if k in rec}
    return letras


def clave(rec):
    for k in ("clave", "respuesta", "correcta", "respuesta_correcta"):
        v = rec.get(k)
        if isinstance(v, str) and v.strip():
            return v.strip().upper()[:1]
        if isinstance(v, int) and 0 <= v < 8:
            return "ABCDEFGH"[v]
    return None


def recorrer(obj):
    if isinstance(obj, dict):
        if "id" in obj:
            yield obj
        for v in obj.values():
            if isinstance(v, (dict, list)):
                yield from recorrer(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from recorrer(v)


def cargar_originales(ids):
    """Busca en todos los .json del repo los registros cuyo id esté en ids."""
    hallados, archivos = {}, Counter()
    for base, dirs, files in os.walk(RAIZ):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "__pycache__")]
        for f in files:
            if not f.endswith(".json"):
                continue
            ruta = os.path.join(base, f)
            if os.path.abspath(ruta) == os.path.abspath(PARAF):
                continue
            try:
                with open(ruta, encoding="utf-8") as fh:
                    data = json.load(fh)
            except Exception:
                continue
            for rec in recorrer(data):
                rid = str(rec.get("id"))
                if rid in ids and rid not in hallados and opciones(rec) and clave(rec):
                    hallados[rid] = rec
                    archivos[os.path.relpath(ruta, RAIZ)] += 1
    return hallados, archivos


def main():
    if not os.path.exists(PARAF):
        sys.exit("No existe data/preguntas/parafraseadas.json. ¿Estás en ~/SIP-AI-RAG?")
    with open(PARAF, encoding="utf-8") as fh:
        pf = json.load(fh)
    if isinstance(pf, dict):
        pf = next((v for v in pf.values() if isinstance(v, list)), [])
    ids = {p["parafraseada_de"] for p in pf if p.get("parafraseada_de")}
    orig, archivos = cargar_originales(ids)
    print(f"Parafraseadas: {len(pf)} | originales encontrados: {len(orig)}")
    for a, n in archivos.items():
        print(f"  banco oficial en: {a} ({n} preguntas)")
    if not orig:
        sys.exit("No encontré el banco oficial. Pega aquí la salida de: "
                 "find . -name '*.json' -size +300k -not -path './.git/*'")

    filas, cuenta = [], Counter()
    for p in pf:
        o = orig.get(p.get("parafraseada_de"))
        if not o:
            est, sc, oc, ol = "SIN_ORIGINAL", "", "", ""
        else:
            ops, cl = opciones(o), clave(o)
            oc = ops.get(cl, "")
            ol = cl
            sc = round(score(p["clave_texto"], oc), 2)
            if sc >= 0.6:
                est = "OK"
            else:
                otras = {k: score(p["clave_texto"], v) for k, v in ops.items() if k != cl}
                mejor = max(otras, key=otras.get) if otras else None
                est = f"CLAVE_CAMBIADA_a_{mejor}" if mejor and otras[mejor] >= 0.6 else "DUDOSA"
        nj = nums(p.get("clave_texto", ""))
        jj = nums(p.get("justificacion", ""))
        flag_num = "SI" if nj and jj and not nj <= jj else ""
        cuenta[est if est.startswith("OK") or est in ("DUDOSA", "SIN_ORIGINAL") else "CLAVE_CAMBIADA"] += 1
        if flag_num:
            cuenta["NUM_NO_COINCIDE_JUSTIF"] += 1
        filas.append([p["id"], est, sc, ol, oc, p.get("clave"), p.get("clave_texto"), flag_num,
                      str(p.get("justificacion", ""))[:120]])

    with open(SALIDA, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "estado", "similitud", "letra_orig", "correcta_original",
                    "letra_nueva", "correcta_nueva", "num_vs_justif", "justificacion"])
        w.writerows(filas)
    n = len(pf)
    print(f"\nRESULTADO sobre {n} preguntas:")
    for k, v in cuenta.most_common():
        print(f"  {k}: {v} ({100*v/n:.1f}%)")
    print(f"\nDetalle: {os.path.relpath(SALIDA, RAIZ)}")


if __name__ == "__main__":
    main()
