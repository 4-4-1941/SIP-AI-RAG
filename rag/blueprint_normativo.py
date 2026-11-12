# Blueprint normativo SERUMS. Uso (desde la carpeta del repo): python rag/blueprint_normativo.py
import json, glob, os, re, collections, subprocess
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
SAL = R + 'data/metadata/serums/blueprint_normativo.json'
EX = ['2025-I', '2025-II', '2026-I', '2026-II']

def limpio(t):
    t = re.sub(r'\s*-\s*Normas y documentos legales.*$', '', t)
    return re.sub(r'\s+', ' ', t).strip(' #-')

meta, ruta = {}, {}
for f in glob.glob(R + 'knowledge/**/*.metadata.json', recursive=True):
    try: m = json.load(open(f, encoding='utf8'))
    except Exception: continue
    s = os.path.basename(f)[:-14]; meta[s] = m; ruta[s] = f[:-14] + '.md'

def texto(s, n=9000):
    p = ruta.get(s)
    if p and os.path.exists(p):
        t = open(p, encoding='utf8', errors='ignore').read(n)
    else:
        pdf = R + 'knowledge/normas/serums/' + s + '.pdf'
        if not os.path.exists(pdf): return ''
        try: t = subprocess.run(['pdftotext', '-l', '3', pdf, '-'], capture_output=True, text=True).stdout[:n]
        except Exception: return ''
    return re.sub(r'[ \t]+', ' ', re.sub(r'\[\[PAGINA \d+\]\]', '', t))

ALIAS = {'7665': ('NTS N° 213-MINSA/DGIESP-2024 (RM 251-2024/MINSA y RM 429-2024/MINSA)', 'Norma Técnica de Salud para la Prevención y Control de la Anemia por Deficiencia de Hierro en niños, adolescentes, mujeres en edad fértil, gestantes y puérperas'),
         'RM 175 2021 MINSA CDC': ('NTS N° 175-MINSA/2021/CDC', 'Norma Técnica de Salud para la Vigilancia Epidemiológica y Diagnóstico de Laboratorio del Síndrome de Guillain Barré en el Perú'),
         '7667': ('NTS N° 221-MINSA/DGIESP-2024 (RM 894-2024-MINSA)', 'Norma Técnica de Salud para la Prevención y Control de la Tuberculosis')}

def nombre(s):
    if s in ALIAS: return ALIAS[s][0]
    m = meta.get(s)
    if m:
        t = m.get('texto_indice') or ''
        if re.search(r'\d', t) and t != 'Ministerio de Salud': return limpio(t)
        for ln in texto(s, 600).splitlines():
            if ln.startswith('# ') and re.search(r'\d', ln): return limpio(ln[2:])
        return limpio(t or s)
    return limpio(s)[:110]

def sumilla(s):
    if s in ALIAS: return ALIAS[s][1]
    t = texto(s)
    if not t: return ''
    pats = [r'((?:LEY|DECRETO SUPREMO|DECRETO LEGISLATIVO) (?:QUE|GENERAL|DE|MARCO)\b[^\n]{0,200}(?:\n[A-ZÁÉÍÓÚÑ ,]{3,120}){0,2})',
            r'((?:Aprueban?|Aprobar|Apruébase|Aprueba)\b[^\n]{0,400}(?:\n[^\n]{0,300}){0,1})',
            r'(POL[ÍI]TICA NACIONAL[^\n]{0,200})',
            r'(NORMA T[ÉE]CNICA DE SALUD[^\n]{0,250})']
    for p in pats:
        m = re.search(p, t)
        if m: return re.sub(r'(?<=\d) (?=\d)', '', re.sub(r'\s+', ' ', m.group(1)).replace('N”','N°').replace('N*','N°')).strip()[:330]
    return ''

def dudoso(x):
    return (not x) or bool(re.search(r'\b\d \d \d\b|[|{}\\]|\w\s\.\s\w', x))

j = json.load(open(R + 'data/preguntas/justificacion_normativa.json', encoding='utf8'))
P = {x['id']: x for x in json.load(open(R + 'data/preguntas/parafraseadas.json', encoding='utf8'))['preguntas']}
N = collections.defaultdict(lambda: {'t': 0, 'ex': collections.Counter(), 'eje': collections.Counter(), 'tema': collections.Counter(), 's': None})
for k, x in j.items():
    if x.get('veredicto') != 'RESPALDADA' or not x.get('fuentes') or k not in P: continue
    s = x['fuentes'][0]; d = N[nombre(s)]
    d['s'] = d['s'] or s; d['t'] += 1
    for c in P[k]['convocatorias_origen']: d['ex'][c] += 1
    d['eje'][P[k]['eje']] += 1; d['tema'][P[k]['tema']] += 1
tot = sum(d['t'] for d in N.values())
ejes = collections.Counter(); porex = collections.Counter()
for d in N.values():
    ejes.update(d['eje']); porex.update(d['ex'])
out = []
for nom, d in sorted(N.items(), key=lambda a: -a[1]['t']):
    m = meta.get(d['s']) or {}; su = sumilla(d['s'])
    if not su and len(nom) > 25 and not re.match(r'^(Resolución|Decreto|Ley)', nom): su = re.sub(r'^1 ', '', nom)
    out.append({'norma': nom, 'sumilla': su, 'sumilla_por_verificar': dudoso(su),
      'eje': d['eje'].most_common(1)[0][0], 'preguntas': d['t'], 'porcentaje': round(100 * d['t'] / tot, 1),
      'por_examen': {e: d['ex'].get(e, 0) for e in EX}, 'temas': [t for t, _ in d['tema'].most_common(4)],
      'compendio': (m.get('compendios_origen') or [''])[0], 'url_oficial': m.get('url_oficial') or ''})
json.dump({'version': '2026-11-11', 'criterio': 'Preguntas RESPALDADAS con la norma como fuente principal; un examen se cuenta si la pregunta apareció en él. Es orientativo.',
  'total_preguntas': tot, 'peso_por_eje': {e: round(100 * n / tot, 1) for e, n in ejes.most_common()},
  'preguntas_por_examen': {e: porex.get(e, 0) for e in EX}, 'normas': out}, open(SAL, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('normas', len(out), 'preguntas', tot, '->', SAL)
