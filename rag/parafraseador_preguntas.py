#!/usr/bin/env python3
"""Parafraseador de preguntas oficiales MINSA (SERUMS).

Orden: primero las "fijas" (familias de preguntas adaptadas entre exámenes, hasta 3 variantes) y luego el resto
(1 variante). Guarda el avance después de CADA pregunta, cuenta los rechazos con su motivo y se detiene si la IA
falla 3 veces seguidas. Reutiliza call_chat/read_json/atomic_json de flashcard_engine (misma clave de API).

Uso:
  python -m rag.parafraseador_preguntas --solo-fijas --limit 5
  python -m rag.parafraseador_preguntas --stats
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import random
import re
import sys
from pathlib import Path
from typing import Any

from rag import flashcard_engine as fe

ROOT = fe.ROOT
BANCO_GLOB = "knowledge/serums/banco_preguntas/banco_oficial_minsa_parte*.json"
CONFIG_DIR = ROOT / "data/flashcards/config"
FAMILIAS_PATH = CONFIG_DIR / "fijas_familias.json"
PROMPT_PATH = CONFIG_DIR / "prompt_preguntas_examen.txt"
OUT_PATH = ROOT / "data/preguntas/parafraseadas.json"
MAX_VARIANTES_FIJA = 3
MAX_FALLOS_SEGUIDOS = 3
EJES = ("Cuidado integral de salud", "Salud pública", "Ética e interculturalidad",
        "Gestión de servicios de salud", "Investigación", "Otros")
_PROHIBIDO_ENUNCIADO = re.compile(r"\bNO\b|\b[Ee]xcepto\b|\bincorrecta\b")
_PROHIBIDO_OPCION = re.compile(r"todas las anteriores|ninguna de las anteriores|\bsiempre\b|\bnunca\b|\bsolo\b", re.IGNORECASE)


def cargar_oficiales() -> list[dict[str, Any]]:
    preguntas: list[dict[str, Any]] = []
    for ruta in sorted(glob.glob(str(ROOT / BANCO_GLOB))):
        preguntas += fe.read_json(Path(ruta), [])
    return preguntas


def orden_de_trabajo(oficiales: list[dict[str, Any]], familias_path: Path, solo_fijas: bool) -> list[tuple[dict[str, Any], str | None]]:
    """[(pregunta_oficial, id_familia|None)]: fijas primero (por familia), luego el resto."""
    por_id = {q["id"]: q for q in oficiales}
    cola: list[tuple[dict[str, Any], str | None]] = []
    vistas: set[str] = set()
    for fam in fe.read_json(familias_path, {}).get("detalle", []):
        for p in fam.get("preguntas", []):
            q = por_id.get(p["id"])
            if q and q["id"] not in vistas:
                cola.append((q, fam["familia"]))
                vistas.add(q["id"])
    if not solo_fijas:
        cola += [(q, None) for q in oficiales if q["id"] not in vistas]
    return cola


def mensajes(q: dict[str, Any], familia: str | None, variantes: int, prompt: str) -> list[dict[str, str]]:
    entrada = {"id": q["id"], "carreras": q.get("carreras", []), "enunciado": q["enunciado"],
               "alternativas": q["opciones"], "clave": q["clave"], "clave_texto": q["clave_texto"],
               "familia": familia, "variantes_solicitadas": variantes}
    user = ("MODO 2 · PARAFRASEAR UNA PREGUNTA OFICIAL. En este modo cita_textual y pagina van en null y "
            "parafraseada_de es el id indicado. Devuelve exactamente la clave \"preguntas\".\n"
            + json.dumps(entrada, ensure_ascii=False))
    return [{"role": "system", "content": prompt}, {"role": "user", "content": user}]


def parsear(content: str) -> list[dict[str, Any]]:
    texto = re.sub(r"^```(?:json)?\s*|\s*```$", "", content.strip(), flags=re.IGNORECASE)
    try:
        data = json.loads(texto)
    except json.JSONDecodeError:
        ini, fin = texto.find("{"), texto.rfind("}")
        if ini < 0 or fin <= ini:
            raise ValueError("La respuesta no es JSON.")
        data = json.loads(texto[ini:fin + 1])
    lista = data.get("preguntas") if isinstance(data, dict) else None
    if not isinstance(lista, list):
        raise ValueError("Falta la lista 'preguntas'.")
    return lista


def validar(v: dict[str, Any], q: dict[str, Any]) -> str | None:
    """Devuelve el motivo de rechazo o None si cumple las reglas de la guía."""
    enun = str(v.get("enunciado") or "").strip()
    correcta = str(v.get("correcta") or "").strip()
    dist = [str(x).strip() for x in (v.get("distractores") or [])]
    if not enun or not correcta or len(dist) != 3:
        return "formato_incompleto"
    opciones = [correcta] + dist
    if len({fe.normalize(o) for o in opciones}) != 4 or any(not fe.normalize(o) for o in opciones):
        return "alternativas_repetidas"
    palabras = len(enun.split())
    if not 15 <= palabras <= 65:
        return "largo_enunciado"
    if any(not 1 <= len(o.split()) <= 10 for o in opciones):
        return "largo_alternativa"
    if _PROHIBIDO_ENUNCIADO.search(enun) or any(_PROHIBIDO_OPCION.search(o) for o in opciones):
        return "patron_prohibido"
    if len(correcta) > max(len(d) for d in dist):
        return "correcta_mas_larga"
    if v.get("eje") not in EJES:
        return "eje_invalido"
    original = fe.normalize(q["clave_texto"])
    nueva = fe.normalize(correcta)
    if not (original in nueva or nueva in original or fe.token_similarity(original, nueva) >= 0.5):
        return "clave_cambiada"
    if fe.token_similarity(enun, q["enunciado"]) >= 0.90:
        return "igual_al_original"
    return None


def armar(v: dict[str, Any], q: dict[str, Any], familia: str | None, n: int, provider: str, model: str) -> dict[str, Any]:
    opciones = [str(v["correcta"]).strip()] + [str(x).strip() for x in v["distractores"]]
    rng = random.Random(hashlib.sha256(f"{q['id']}-{n}".encode()).hexdigest())
    rng.shuffle(opciones)
    letras = dict(zip("ABCD", opciones))
    clave = next(k for k, t in letras.items() if t == str(v["correcta"]).strip())
    return {"id": f"P-{q['id']}-v{n}", "parafraseada_de": q["id"], "familia": familia, "fija": bool(familia),
            "carreras": q.get("carreras", []), "convocatorias_origen": q.get("convocatorias", []),
            "tipo": v.get("tipo"), "eje": v["eje"], "tema": v.get("tema"), "enunciado": str(v["enunciado"]).strip(),
            "opciones": letras, "clave": clave, "clave_texto": str(v["correcta"]).strip(),
            "justificacion": v.get("justificacion"), "estado": "PARAFRASEADA_REVISAR_MUESTREO",
            "proveedor": provider, "modelo": model, "generada": fe.utc_now()}


def procesar(familias_path: Path = FAMILIAS_PATH, prompt_path: Path = PROMPT_PATH, out_path: Path = OUT_PATH,
             solo_fijas: bool = False, limite: int | None = None) -> dict[str, Any]:
    if not prompt_path.exists():
        raise RuntimeError(f"Falta el prompt: {prompt_path}")
    prompt = prompt_path.read_text(encoding="utf-8")
    estado = fe.read_json(out_path, {"preguntas": [], "procesadas": {}, "rechazos": {}})
    hechas = estado["procesadas"]
    nuevas = fallos = 0
    for q, familia in orden_de_trabajo(cargar_oficiales(), familias_path, solo_fijas):
        if q["id"] in hechas:
            continue
        if limite is not None and nuevas >= limite:
            break
        variantes = MAX_VARIANTES_FIJA if familia else 1
        try:
            contenido, proveedor, modelo = fe.call_chat(mensajes(q, familia, variantes, prompt), temperature=0.4, max_tokens=1800)
            crudas = parsear(contenido)
            fallos = 0
        except (RuntimeError, ValueError, json.JSONDecodeError) as exc:
            fallos += 1
            print(f"[{q['id']}] fallo de IA: {exc}", file=sys.stderr)
            if fallos >= MAX_FALLOS_SEGUIDOS:
                print("Se detiene: 3 fallos seguidos. El avance quedó guardado.", file=sys.stderr)
                break
            continue
        aceptadas: list[dict[str, Any]] = []
        for v in crudas[:variantes]:
            motivo = validar(v, q) if isinstance(v, dict) else "formato_incompleto"
            if motivo is None and any(fe.token_similarity(v["enunciado"], a["enunciado"]) >= 0.85 for a in aceptadas):
                motivo = "variante_repetida"
            if motivo:
                estado["rechazos"][motivo] = estado["rechazos"].get(motivo, 0) + 1
                continue
            aceptadas.append(armar(v, q, familia, len(aceptadas) + 1, proveedor, modelo))
        estado["preguntas"] += aceptadas
        hechas[q["id"]] = {"familia": familia, "aceptadas": len(aceptadas)}
        fe.atomic_json(out_path, estado)  # avance guardado después de cada pregunta
        nuevas += 1
    return resumen(estado) | {"procesadas_ahora": nuevas}


def resumen(estado: dict[str, Any]) -> dict[str, Any]:
    return {"preguntas_generadas": len(estado["preguntas"]), "oficiales_procesadas": len(estado["procesadas"]),
            "rechazos_por_motivo": estado["rechazos"]}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--solo-fijas", action="store_true", help="Solo las familias de fijas")
    ap.add_argument("--limit", type=int, default=None, help="Máximo de preguntas oficiales a procesar en esta corrida")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--familias", type=Path, default=FAMILIAS_PATH)
    ap.add_argument("--prompt", type=Path, default=PROMPT_PATH)
    ap.add_argument("--out", type=Path, default=OUT_PATH)
    a = ap.parse_args(argv)
    if a.stats:
        print(json.dumps(resumen(fe.read_json(a.out, {"preguntas": [], "procesadas": {}, "rechazos": {}})), ensure_ascii=False, indent=2))
        return 0
    print(json.dumps(procesar(a.familias, a.prompt, a.out, a.solo_fijas, a.limit), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
