# Pendientes para enriquecer SIP-AI-RAG

**Fecha:** 2026-10-18
**Estado:** recordatorio de trabajo, sin aprobar ni programar.
**Para qué sirve:** referencia de lo que falta en el RAG y de cómo usar sus fuentes. Aplica a la Ficha Familiar Digital, a SERUM-APP (capacitación y banco de preguntas) y a proyectos futuros, como los códigos rojo y azul.

---

## 1. Regla de prioridad de fuentes

Cuando dos fuentes difieren, manda la de mayor rango:

1. Norma técnica de salud vigente (NTS o RM).
2. Guía de práctica clínica vigente (INS-CETS u otras guías institucionales).
3. Manuales HIS (sirven para **registrar y codificar**, no para decidir la conducta clínica).
4. Guías de llenado o documentos regionales (por ejemplo, la guía de la ficha familiar de 2015).
5. Páginas web y prensa, solo para ubicar el documento oficial.

**Ejemplo real (2026-10-18):** el manual HIS de Cáncer 2025 daba el examen clínico de mama cada año y el tamizaje colorrectal de 50 a 70 años cada año. Las guías clínicas dicen examen clínico de mama **cada 2 años** (mujeres de 40 a 69 con bajo riesgo) y tamizaje colorrectal de **45 a 75 años** con evaluación de riesgo. Se corrigió la ficha. Antes de programar una regla, contrastarla con la guía.

Toda fuente debe llevar su **estado de vigencia** (vigente, derogada, reemplazada o por verificar).

---

## 2. Estado de `knowledge/guia-clinica/` (revisada el 2026-10-18)

- 34 documentos (PDF y JSON) más `manifest.json`, con 0 errores de extracción.
- **Con texto y listas para consulta:** las guías extensas (colorrectal, mama, dislipidemia, HTA 2026, ITU en embarazo, trastorno hipertensivo del embarazo, preeclampsia, sepsis neonatal, analgesia, leucemia, entre otras) y las guías cortas de 4 a 7 páginas (asfixia perinatal, membrana hialina, TB pediátrica, fibrosis quística, sepsis obstétrica).
- **Sin texto, necesitan OCR (4 archivos):**

| Archivo | Páginas |
|---|---|
| Guía de Depresión en adultos (HVLH) | 82 |
| Guía de Esquizofrenia (HVLH) | 92 |
| Guía de Ansiedad en pacientes adultos con cáncer | 78 |
| Fe de erratas 5707273 | 2 |

- **Nombres duplicados o raros para limpiar** (confirmar antes de borrar nada):
  - `analgesia_INMP.pdf.pdf.pdf` y su JSON `.pdf.pdf.json`.
  - Pares con `(2)` en el PDF y `_2` en el JSON: `gpc-n-01-2025` (estadiaje y versión resumida), `gpc-n-04-2025` versión resumida y la guía HTA 2026.
  - `guia-tecnica-n-005-inscets-2025-vs-01` y `...-vs-01-2`.
  - La versión resumida de HTA fue eliminada del repo (commit `e9c431e`): confirmar que fue intencional.

---

## 3. Qué fuentes alimentan hoy cada panel de la ficha

| Profesión | Atención | Fuente | Estado |
|---|---|---|---|
| Enfermería | Vacunas por dosis | NTS 246-2026 (numeral 6.2 y Anexos 1 y 2) | Leída en imágenes; el resto de la parte 1 sin leer |
| Enfermería | Controles CRED | NTS 238-2025 (numeral 6.4) | Leída; falta tamizaje del desarrollo y suplementación |
| Nutrición | Vaso de Leche | Ley 27470 | Verificada; la edad de "anciano" no está fijada |
| Psicología | Tamizaje de salud mental | Ficha Familiar oficial (guía 2015) | Instrumento y frecuencia sin definir |
| Psicología | Tamizaje de depresión (18 años o más) | RM 136-2023-MINSA | PDF oficial pendiente; la guía HVLH está escaneada |
| Medicina | Cáncer colorrectal | GPC INS-CETS de tamizaje colorrectal | Verificada |
| Medicina | Tamizaje lipídico | GPC INS-CETS de dislipidemia 2025 | Verificada |
| Medicina | Cáncer de piel | Manual HIS Cáncer 2025 | Sin guía clínica en la carpeta |
| Medicina y Obstetricia | Cáncer de mama | GPC INS-CETS de tamizaje de mama | Verificada |
| Odontología | Atención preventiva y citas en gestantes | Manual HIS Salud Bucal 2025 | Falta contrastar con una guía clínica |

---

## 4. Documentos que faltan o hay que completar

| Prioridad | Qué falta | Detalle |
|---|---|---|
| Alta | **Tamizaje de cáncer de cuello uterino** (Papanicolaou, IVAA, VPH) | No está en la carpeta. Las dos guías de cuello uterino son de estadiaje y tratamiento en estadios tempranos |
| Alta | OCR de la **guía de Depresión en adultos (HVLH)** y obtener el PDF oficial de la RM 136-2023 | Hoy el `.md` de la RM 136-2023 es solo una ficha |
| Alta | Extraer reglas de la **guía de HTA 2026** (tamizaje) | El texto está disponible |
| Media | Reglas de las guías de **embarazo**: ITU, trastorno hipertensivo y preeclampsia | Para Obstetricia y Medicina |
| Media | **NTS 246 parte 1** completa y **NTS 238** completa | Solo se leyeron partes; el resto está escaneado |
| Media | **Ficha Familiar:** RM 204-2015, guía de llenado, RM 030-2020, `MU_SALUD_FAMILIAR` (manual del SIHCE) y el Manual de Registro y Codificación en Salud Familiar 2014 | No estaban en SIP-AI-RAG al revisarlo el 2026-10-16 |
| Media | Tamizaje de **próstata** | Los manuales no fijan la edad |
| Baja | **Dengue:** NTS 230-2025, NTS 198-2023 y NTS 211-2024 | Verificar que estén los PDF. La vacuna solo aparece como campaña en el Anexo 20 de la NTS 246 |
| Baja | Criterio oficial de **agua segura** | No se encontró |
| A definir | **Códigos rojo y azul** | Definir qué guías necesita ese proyecto. Ya están preeclampsia y eclampsia, sepsis obstétrica, sepsis neonatal y asfixia perinatal |

---

## 5. Vigencia de normas que ya aparecieron (marcar en el RAG)

| Norma | Estado |
|---|---|
| RM 464-2011/MINSA (Modelo de Atención Integral basado en Familia y Comunidad) | **Derogada** por la RM 030-2020/MINSA |
| NTS 137-2017 (CRED) | Reemplazada por la NTS 238-MINSA/DGIESP-2025 (RM 682-2025) |
| NTS 196-2022 (esquema de vacunación) | Reemplazada por la NTS 246-MINSA/DGIESP-2026 (RM 561-2026) |
| RM 990-2010 (CRED, citada por la guía de 2015) | La vigente es la NTS 238-2025 |
| Guía de llenado de la Ficha Familiar (2015) | Base legal desactualizada |

---

## 6. Cómo incorporar cada documento

- **Metadatos mínimos** (ver `docs/RAG-SOURCES.md`): organismo emisor, título, fecha y versión, tipo, página o sección, procedencia, rol de evidencia y estado de vigencia.
- **Reglas del repo** (`AGENTS.md`): usar carpetas que ya existen, no crear carpetas ni archivos nuevos sin permiso y mostrar la ruta exacta antes.
- **OCR:** usar el idioma español, porque sin él se pierden tildes y aparecen errores. Las tablas conviene confirmarlas mirando la página como imagen.
- **Citar siempre** página o sección, y marcar como "por confirmar" lo que venga de OCR.

---

## 7. Orden sugerido

1. Subir o localizar la guía de **tamizaje de cuello uterino**.
2. OCR de la **guía de Depresión (HVLH)** y del PDF de la RM 136-2023.
3. Extraer reglas de **HTA 2026** y de las guías de **embarazo**.
4. Completar **NTS 246** y **NTS 238**.
5. Subir los documentos de la **Ficha Familiar** y marcar la vigencia (sección 5).
6. Limpiar los nombres duplicados de la carpeta `guia-clinica`.
