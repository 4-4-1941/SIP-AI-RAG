# HIS-FICHAS-MOTOR.md — Reglas de registro HIS por actividad (v0.6)

> Uso: **pedagógico** (simulador HIS SERUMS). El HIS real se entrega por escrito con lapicero azul.
> Compilado: 12 oct 2026 (v0.6: NTS 246-2026 parte 1 leída por OCR en lo de registro y códigos; D-13, D-14 y D-15 resueltas; códigos CPMS de hexavalente y VRS confirmados; inventario de los 9 manuales nuevos del repo (M27 a M35); simulador v0.2; D-19 y D-20; pendiente G-16). Antes, 12 oct 2026 (v0.5: M24 leído hasta la p.102 y tablas LAB ilegibles verificadas sobre la imagen del PDF: alta de continuidad, causalidad de farmacovigilancia, fases y profesional en situación de calle, y las de hogares protegidos y penales; discrepancia D-18; pendiente G-15). Antes, 11 oct 2026 (v0.4: se añade M26 Pueblos Indígenas u Originarios 2022, leído completo (22 págs.); sección B recibe la regla de hoja individual por turno y de no mezclar meses y las reglas de M26; M01 pasa a LEÍDA según los fragmentos enviados por el usuario; se borró `registro-diario-his.html` del repo; discrepancias D-16 y D-17; pendientes G-13 y G-14). Antes, 7 oct 2026 (v0.3: M24 leído en el PDF del repo hasta p.74 + listado de diagnósticos; se añaden M25 NTS 246-2026 y R.M. 561-2026; RM 447-2024 verificada; fichas F-011 a F-018; discrepancias D-13 a D-15). v0.2 (6 oct): se añadió Salud Mental 2025, M24. · Fuentes: 26 archivos PDF (23 documentos distintos) + guía general leída en línea + búsquedas en El Peruano/gob.pe + tabla de manuales de GERESA Arequipa (15-04-2026) + PDFs del repo SIP-AI-RAG (`knowledge/minsa/manuales-his/`).
> Principio: **una ficha por actividad**; cada ficha cita **todos** los manuales que la cubren y marca cuál manda.

---

## 0. REGLAS DE ESTRUCTURA (no romper)

1. Las secciones **A–H** y sus letras son fijas. No renumerar ni reordenar.
2. **Agregar un manual nuevo** = copiar la plantilla **H.1** al final de la sección A con el siguiente ID libre (`M24`, `M25`…). No tocar los demás bloques.
3. **Agregar una actividad nueva** = copiar la plantilla **H.2** al final de la sección E con el siguiente ID libre (`F-009`, `F-010`…).
4. **Agregar una discrepancia** = copiar la plantilla **H.3** al final de la sección F (`D-11`, `D-12`…).
5. Los IDs (`M##`, `F-###`, `D-##`) **nunca se reutilizan ni se borran**; una edición vieja se marca `SUPERADA`, no se elimina.
6. Cita siempre así: `[M05 p.38]` = manual + **página impresa**. En M05 la página impresa = página del PDF + 1. En los demás, salvo aviso, se cita la página del PDF.
7. Estados de vigencia permitidos (vocabulario fijo):
   - `ULTIMA_EDICION_LOCALIZADA` — es la edición más nueva que encontré (no equivale a confirmada por MINSA).
   - `SUPERADA` — existe una edición más nueva localizada.
   - `BASE_NORMATIVA_REEMPLAZADA` — la norma que cita el manual fue reemplazada.
   - `HISTORICA` — se conserva solo para comparar.
   - `VIGENCIA_NO_DETERMINADA` — no pude determinarla.
   - `ILEGIBLE_REQUIERE_OCR` — el texto del PDF no se puede leer bien.

---

## A. INVENTARIO DE MANUALES

Columna "Última en GERESA" = lo que lista la tabla pública de manuales de GERESA Arequipa (15-04-2026), copia regional: **confirmar en MINSA**.

| ID | Manual | Edición (portada/créditos) | Págs. | Normas que cita el propio manual | Última en GERESA (2026-04) | Estado |
|---|---|---|---|---|---|---|
| M01 | Guía de uso y registro de la hoja HIS (general) | 2017 (copia DIRESA Tumbes, leída en línea; **no subida**) | — | — | **2020** (© MINSA, enero 2020; copia DIRESA Junín) | VIGENCIA_NO_DETERMINADA + **LEÍDA** (11 oct, por instrucción del usuario: leída a partir de los fragmentos de la Guía 2020 que él envió; no tengo el PDF completo, por eso no cito páginas de la 2020) |
| M02 | Promoción de la Salud (DPROM) | **2.ª ed., mayo 2024** | 166 | R.M. 958-2012/MINSA (sesiones demostrativas) | 2024 | ULTIMA_EDICION_LOCALIZADA |
| M03 | Promoción de la Salud | 1.ª ed., abril 2022 | 156 | RM 834-2019 | — | SUPERADA por M02 (misma obra) |
| M04 | Salud Familiar (ESN) | 2014 | 11 | no visible | ≤2019 (sigue siendo el único independiente) | HISTORICA — su contenido pasó a M02 págs. 164-165 y M03 pág. 153 |
| M05 | Adulto Mayor (Curso de vida) | **2.ª ed., marzo 2025** (1.ª feb 2020) | 50 | NTS 196-2022 (R.M. 884-2022); NTS 207-2023 (R.M. 789-2023) | 2025 | ULTIMA_EDICION_LOCALIZADA |
| M06 | Adulto Mayor (Etapa de vida) | portada 2020, edición 2019 | 26 | no visible | — | SUPERADA por M05 |
| M07 | Inmunizaciones | 2019 | 26 | NTS 141-2018 (R.M. 719-2018) | 2019 (sintaxis ESNI 2023 act. 10-10-2025) | ULTIMA_EDICION_LOCALIZADA + BASE_NORMATIVA_REEMPLAZADA (NTS 141 → NTS 196 → NTS 246-2026). Según el usuario (7 oct): se sigue usando en la práctica, se le agregan códigos de otros documentos y no hay manual HIS nuevo |
| M08 | Atención Materno Perinatal | **2.ª ed., marzo 2023** | 56 | RM 069-2016/MINSA | 2023 | ULTIMA_EDICION_LOCALIZADA |
| M09 | Atención Materno Perinatal | 1.ª ed., enero 2023 | 47 | RM 069-2016/MINSA | — | SUPERADA por M08 |
| M10 | Salud Mental | 1.ª ed., feb 2021 | 120 | RM 701-2018/MINSA | **2025** | SUPERADA por M24 |
| M11 | Etapa de vida Niño | 1.ª ed., feb 2021 | 68 | NTS 154-2019; RM 250-2017, 537-2017, 975-2017 | 2021 (sintaxis versión 27-08-2025) | ULTIMA_EDICION_LOCALIZADA |
| M12 | Etapa de vida Adolescente | 1.ª ed., nov 2020 | 42 | NTS 157-2019 | **2026** | SUPERADA por M28 (la 2026 ya está subida, 12 oct) |
| M13 | Planificación Familiar | 2.ª ed., nov 2023 | 66 | RM 975-2017/MINSA | 2024 | VIGENCIA_NO_DETERMINADA (puede haber edición 2024). Subida al repo como `Manual-planificacion_familiar-2024.pdf`: es esta misma 2.ª ed. de noviembre 2023 (66 págs.; Depósito Legal 2023-05635), no una edición 2024 |
| M14 | Salud Bucal | 3.ª ed., marzo 2022 | 57 | RM 860-2021/MINSA | **2025 (4.ª ed., dic 2025)** | SUPERADA |
| M15 | Tuberculosis | 1.ª ed., junio 2024 | 50 | RM 1001-2017, 117-2020, 146-2020, 550-2023, 780-2015, 895-2018 | 2025 | VIGENCIA_NO_DETERMINADA (puede haber edición 2025) |
| M16 | VIH (DPVIH) | 1.ª ed., agosto 2022 | 82 | NTS 126-2016, 129-2016, 145-2018, 159-2019, 167-2020, 169-2020; RM 975-2017, 715-2017, 099-2014, 1001-2017, 1012-2016, 1044-2020 | 2023 (ITS-VIH-Hepatitis) | SUPERADA (probable; la 2023 no está subida) |
| M17 | Discapacidad | 1.ª ed., enero 2023 | 106 | RM 478-2006, 653-2020 | **2025** | SUPERADA |
| M18 | Salud Ocular | sin edición visible (la presentación M19 es de 2020) | 40 | RM 537-2009, 539-2006 | **2025** | SUPERADA |
| M19 | Capacitación HIS Salud Ocular (presentación) | 2020 | 59 | — | — | HISTORICA (no es manual; 2 archivos idénticos) |
| M20 | Cáncer | 1.ª ed., mayo 2022 | 40 | — | **2025** | SUPERADA + ILEGIBLE_REQUIERE_OCR |
| M21 | Viruela del mono | 1.ª ed., julio 2022 | 12 | RM 780-2015 | no listada | VIGENCIA_NO_DETERMINADA + ILEGIBLE_REQUIERE_OCR (parcial) |
| M22 | Alimentación y Nutrición Saludable | 2013-2015 (año por confirmar) | 33 | RM 1041-2006 | ≤2019 (archivo 2015) | ULTIMA_EDICION_LOCALIZADA |
| M23 | Actividades de Promoción — Articulado Nutricional | 2018 (sin edición visible) | 25 | no visible | — | VIGENCIA_NO_DETERMINADA (probablemente absorbida por M02/M03; por confirmar) |
| M24 | Salud Mental | **2.ª ed., febrero 2025** (1.ª feb 2021); Depósito Legal 2025-01619; © MINSA | 117 impresas (119 pág. PDF; **pág. impresa = pág. PDF − 1**) | normas base no revisadas | 2025 | ULTIMA_EDICION_LOCALIZADA — leída ahora en el PDF del repo SIP-AI-RAG (`Manual-salud_mental-2025.pdf`): págs. 1-74 y listado de diagnósticos (p.103 en adelante, cruzado por código). **No leídas:** pp.75-102 (hogares protegidos, penales, glosario). Versión digital MINSA: https://bvs.minsa.gob.pe/local/MINSA/7615.pdf |
| M25 | Esquema Nacional de Inmunizaciones, **NTS N.° 246-MINSA/DGIESP-2026** — solo **parte 2** (Anexos 8 a 21 y bibliografía) | R.M. 561-2026/MINSA, Lima 12-jun-2026 (md del repo indica 13-jun-2026) | págs. impresas 98-140 | Art. 2 de la R.M. deja sin efecto las R.M. 884-2022, 099-2023, 218-2024, 474-2025, 709-2025 y 403-2026 | no aplica | ULTIMA_EDICION_LOCALIZADA (norma, **no** es manual HIS; parte 1 no disponible, G-10). Contiene el Registro Diario de Vacunación Unificado (Anexo 10) y códigos CPT en el Anexo 20 |
| M26 | Manual de Registro y Codificación de las Actividades de Dirección de Pueblos Indígenas u Originarios (consulta externa por pueblos indígenas u originarios) — MINSA, Oficina General de Tecnología de la Información / Dirección de Pueblos Indígenas u Originarios | Portada y créditos: **2022** (la catalogación de la p.2 dice «Lima: Ministerio de Salud; 2021»); archivo del usuario fechado 14-01-22 | 22 (impresa = PDF; la p.22 es contraportada) | Directiva Administrativa N.° 240-MINSA/2017/INS (R.M. 975-2017/MINSA) [p.9]; R.M. 1120-2017/MINSA, GT factores de riesgo cardiovascular y diabetes [p.15] | 2022 (la tabla de GERESA lista «Pueblos indígenas u originarios 2022») | ULTIMA_EDICION_LOCALIZADA + **LEÍDO COMPLETO** (11 oct, pp.1-22). Subido por el usuario como manual para poblaciones originarias; **pendiente subirlo al RAG** (G-14). La numeración de secciones del propio manual es inconsistente: ver D-17 |
| M27 | Adulto (Curso de vida) — consulta externa, MINSA OGTI | 2.ª ed., marzo 2025 (1.ª feb 2019); Depósito Legal 2025-02693 | 52 (PDF) | no leída | 2025 | ULTIMA_EDICION_LOCALIZADA + INVENTARIADO (portada y créditos leídos el 12 oct; contenido sin leer, G-16). Reemplaza a M35 |
| M28 | Etapa de vida Adolescente — consulta externa | 2.ª ed., junio 2026 (1.ª nov 2020); Depósito Legal 2026-06454 | 44 (PDF) | no leída | 2026 | ULTIMA_EDICION_LOCALIZADA + INVENTARIADO (contenido sin leer, G-16). Reemplaza a M12 |
| M29 | Salud Bucal | 4.ª ed., diciembre 2025 (3.ª mar 2022); Depósito Legal 2025-15497 | 59 (PDF) | no leída | 2025 | ULTIMA_EDICION_LOCALIZADA + INVENTARIADO (contenido sin leer, G-16). Reemplaza a M14 |
| M30 | Tuberculosis | 2.ª ed., diciembre 2025 (1.ª jun 2024); Depósito Legal 2025-15585 | 50 (PDF) | D.S. 008-2017-SA (ROF) citado en la introducción | 2025 | ULTIMA_EDICION_LOCALIZADA + INVENTARIADO (contenido sin leer, G-16). Reemplaza a M15 |
| M31 | Prevención y Control del Cáncer | 2.ª ed., diciembre 2025 (1.ª may 2022); Depósito Legal 2025-15372 | 71 (PDF) | D.S. 008-2017-SA (ROF) citado en la introducción | 2025 | ULTIMA_EDICION_LOCALIZADA + INVENTARIADO (contenido sin leer, G-16). Reemplaza a M20 |
| M32 | Persona con Discapacidad | 3.ª ed., diciembre 2025 (2.ª dic 2023); Depósito Legal 2025-15358 | 87 (PDF) | no leída | 2025 | ULTIMA_EDICION_LOCALIZADA + INVENTARIADO (contenido sin leer, G-16). Reemplaza a M17; ver D-20 |
| M33 | Salud Ocular y Prevención de la Ceguera | 1.ª ed., enero 2025; Depósito Legal 2025-00020 | 53 (PDF) | no leída | 2025 | ULTIMA_EDICION_LOCALIZADA + INVENTARIADO (contenido sin leer, G-16). Reemplaza a M18 |
| M34 | VIH-SIDA, Infecciones de Transmisión Sexual y Hepatitis (DPVIH) | 1.ª ed., enero 2023 (© MINSA, enero 2023) | 82 (PDF) | D.S. 008-2017-SA (ROF) citado en la introducción | 2023 | VIGENCIA_NO_DETERMINADA + INVENTARIADO (contenido sin leer, G-16). Su relación con M16 está por confirmar: ver D-20 |
| M35 | Adulto mujer y varón (etapa de vida) | edición 2018 | 29 (PDF) | no leída | — | HISTORICA, SUPERADA por M27 (inventariada, sin leer) |

### A.1 Manuales que aparecen en GERESA y **no están subidos**
Guía general 2020 (M01) · Adulto (2025) · Prevención y control de daños no transmisibles (2025) · Salud Mental 2025 (ya leída en línea como M24; falta el PDF oficial) · Adolescente 2026 · Salud Bucal 4.ª ed. 2025 · Cáncer 2025 · TBC 2025 · Discapacidad 2025 · ITS-VIH-Hepatitis 2023 · Salud Ocular 2025 · Planificación Familiar 2024 · Anemia 2024 · Telemedicina 2021 · Emergencias y Urgencias 2022 · ~~Pueblos indígenas u originarios 2022~~ (subido el 11 oct → **M26**) · Zoonosis-rabia 2022 · Metales pesados 2022 · Vigilancia epidemiológica 2024.

**Actualización 7 oct:** el repo SIP-AI-RAG (`knowledge/minsa/manuales-his/`) ya contiene los PDF de: Adulto Mayor 2025, Curso de vida adulto 2025, ITS y hepatitis 2023, Planificación Familiar 2024, Promoción 2024, Salud Mental 2025, Salud Ocular 2025, Cáncer 2025, Discapacidad 2025, TBC, Salud Bucal 2025 y Adolescente 2026. Están localizados pero **aún no leídos ni inventariados** como M## (G-07).

### A.2 Norma transversal sobre códigos
**R.M. 447-2024/MINSA — VERIFICADA (7 oct 2026)** en el texto del PDF (copia de lpderecho.pe, sin numeración impresa legible y sin fecha de firma visible; la nota de LP es del 25-jun-2024; no se abrió El Peruano directo). Art. 1: se usan los códigos del Anexo 1 **en adición** al CIE-10 de la R.M. 553-2002-SA/DM. Art. 2: **cesa** el uso de los códigos del Anexo 2.
- **Cesan (Anexo 2):** A90X dengue, A91X dengue hemorrágico, U069 Zika no especificada, I840-I849 hemorroides, F640, F641, F642, F648, F649, F651, F661.
- **Se agregan (Anexo 1), entre otros:** A970-A972 dengue, A925 Zika, K640-K649 hemorroides, E41X0-E41X3 y E45X0-E45X2 desnutrición, **F1011** alto riesgo por consumo excesivo de alcohol, F9121 y F9122 (pandilla / grupos organizados), T7411, T7412 y T7480, Z0011-Z0018, **Z3181 y Z3182** (psicoprofilaxis general/específica), Z6361-Z6363 (adulto mayor independiente/dependiente), **Z770-Z773** (discordancia de género / asesoramiento sexual).
- **Cruce con M24:** el listado de diagnósticos de Salud Mental 2025 (p.103 en adelante) **contiene** F1011, F9121 y F9122 y **no contiene** F640-F649, F651 ni F661. Está alineado con la R.M. 447-2024.
- **Cruce con fichas:** ningún código de F-006 a F-018 aparece en los Anexos 1 y 2 (lectura sobre texto OCR con ruido).
- **Cruce con M26:** el ejemplo de dengue usa **A970** [M26 p.18], que está entre los códigos que agrega la R.M. 447-2024; no usa A90X.

**R.M. 561-2026/MINSA (12-jun-2026, firmada por el Ministro de Salud):** Art. 1 aprueba la NTS 246-MINSA/DGIESP-2026; Art. 2 deja sin efecto las R.M. 884-2022 (NTS 196), 099-2023, 218-2024, 474-2025, 709-2025 y 403-2026; Art. 3 ordena publicarla en El Peruano y en gob.pe/minsa. Archivo subido: `8265031-resolucion-ministerial-n-561-2026-minsa.pdf` (3 págs.).

---

## B. REGLAS GENERALES DE LA HOJA HIS

Fuente base: M01 (versión 2017, leída en línea; M01 pasó a LEÍDA el 11 oct con los fragmentos de la Guía 2020 enviados por el usuario) + coincidencias en M04, M06, M07 y M26. **Revisar contra M01-2020** (D-10).

| Regla | Detalle | Fuente |
|---|---|---|
| Hoja | Una hoja por turno. La **hoja doble cara es de uso individual por turno**: no la comparten dos profesionales. **No se mezclan atenciones de meses distintos en la misma hoja.** Hoja doble cara = 22 registros (aclaración del usuario). | Guía HIS 2020 (M01), fragmentos enviados por el usuario; **página por confirmar**. M26 p.21 muestra el Anexo 1 con casilla de turno M/T/N y 12 filas por cara |
| Responsable y momento del registro | Lo registra el personal que atiende o realiza la actividad, **en el momento** en que ocurre. Los formularios se acopian y se digitan **diariamente**. | M26 p.6 |
| Pertenencia étnica (ítem 9, ETNIA) | Se registra a **todas las edades**, urbano y rural, por **autoidentificación**. Se pregunta: «Por sus costumbres y por sus antepasados, ¿usted se siente o se considera…?». No suponer ni inducir la respuesta, no deducirla por apariencia, ropa o idioma; en menores o con impedimentos se anota el dato del responsable; se puede preguntar en lengua materna. Se anota el **código numérico** de la tabla de pertinencia étnica. | M26 pp.8-11 (tabla con fuente R.M. 975-2017/MINSA) |
| Más de 3 actividades (confirmación) | Mismo procedimiento que M06/M07/M04: se pasa al siguiente registro con línea oblicua entre Día y Servicio y se usan los 3 renglones de diagnósticos. | M26 p.10 |
| Atención de salud | Se registran: día, HC, DNI, financiador, etnia, distrito, edad, sexo, establecimiento, servicio. | M06 p.11; M07 p.6; M04 p.4 |
| Actividad APP / AAA | En la columna HC/DNI va el código `APP###` (o `AAA###` en animales). Edad, sexo, condición de establecimiento y servicio no se registran: **línea oblicua**. | M01 pp.8, 10-14; M04 p.9; M07 p.24 |
| Tipo de diagnóstico | **P** presuntivo (sin certeza o a la espera de laboratorio). **D** definitivo (una sola vez por episodio en agudos; una sola vez en crónicos). **R** repetido (seguimiento posterior). | M06 p.11; M04 p.4; M01 p.13 |
| Controles | Un diagnóstico preexistente o un control se registra con **R** para no duplicar casos. | M06 pp.14, 18 |
| Actividades | El tipo de diagnóstico de una **actividad** es siempre **D**. | M06 pp.12-24; M07 pp.6, 23-24 |
| Más de 3 diagnósticos | Se continúa en el siguiente registro con una línea oblicua desde Día hasta Servicio. | M06 p.11; M07 p.6; M04 p.4 |
| Máximo por registro | En Salud Mental 2025: hasta 20 actividades por atención, continuando en los siguientes registros. | M24 p.7 |
| Condición de la persona | En Salud Mental 2025, el LAB del diagnóstico definitivo lleva siglas: `TPE` trata de personas, `PTB` TB, `DIS` discapacidad, `JUD` judicializada, `IE` actividad en institución educativa. Gestante/puérpera: se escribe la palabra. | M24 p.7 |
| LAB | Su contenido **depende de la actividad y del manual**: dosis, número de control, número de sesión, participantes, siglas. | M01 pp.13-14 |

---

## C. SIGLAS DE LAB VERIFICADAS (por manual)

> Una misma sigla puede cambiar de sentido según actividad y casillero. El simulador debe buscar por **(actividad, manual)**, nunca por sigla sola.

| Manual | Siglas |
|---|---|
| M06 Adulto Mayor 2019 | VACAM: `AS` saludable, `E` enfermo, `AF` frágil, `GC` geriátrico complejo · plan: `TA` ejecutado · nutrición: `IMC`, `RSM`/`RSA`/`RMA` (riesgo), `MVN` (mini valoración), `PR` (recuperado) · tamizaje: `EP` psicosis, `AD` alcohol y drogas, `VIF` violencia intrafamiliar, `TD` trastorno depresivo [pp.12-21] |
| M07 Inmunizaciones 2019 | Dosis `1`,`2`,`3` · `DA` refuerzo · `BU` bloqueo/dosis única · `ST` personal de salud · `CE` contacto de TB · `G` gestante · `P` puérpera · extramural `DU`,`D1`,`D2`,`D3`,`DDA` · barridos `BU`,`B1`,`B2`,`B3`,`BDA` · grupos de riesgo `TS`,`HSH`,`TRA`,`HTS`,`TTS`,`PNP`,`M`,`BOM`,`DCI`,`EST`,`PPL` [pp.6-21] |
| M04 Salud Familiar 2014 | `TA` plan culminado · sesión educativa: `AD`, `VIF`, `TD` [pp.7, 9] |
| M24 Salud Mental 2025 | `TPE`,`PTB`,`DIS`,`JUD`,`IE` (condición) · `ACP` (acompañamiento clínico psicosocial) · `COO` (coordinación) · `DVC` (referido, 1.er nivel/IE) · `DVR` (derivado, continuidad de cuidados) · `IA` (ingreso, continuidad de cuidados) · `TA` (alta de continuidad de cuidados) · `VIF` (taller a personal de salud sobre violencia) · `ST` (personal de salud en primeros auxilios psicológicos) · valores numéricos según actividad: tipo de opioide 1-3, tipo de alta 1-5, tipo de crisis humanitaria 1-11, profesional 1-6, edad del hijo 1-2, resultado de tamizaje 1-3 [pp.7-69] |
| M24 Salud Mental 2025 — tablas de valores LAB verificadas con imagen (12 oct) | Alta de continuidad de cuidados (LAB 2.º de la 2.ª actividad): `1` recuperación, `2` voluntaria [p.41], `3` abandono, `4` traslado [p.42] · Manejo del alta (99217), LAB 1.º de la 2.ª: `1` recuperación, `2` voluntaria, `3` abandono, `4` referencia/contrarreferencia, `5` defunción [p.75] · Hogar protegido: ingreso `IA` [p.75]; egreso LAB 1.º `TA` y LAB 2.º `1` reintegro familiar, `2` reinserción laboral, `3` voluntario, `4` otros motivos [p.79]; tabla de la p.78 (redes de apoyo del HP): `1` establecimiento de salud, `2` instituciones educativas, `3` instituciones laborales, `4` organizaciones de inclusión social, `5` otros; logro en actividades de la vida diaria: `1` básicas, `2` instrumentales, `3` avanzadas [p.79]; evaluación de la comisión de derivación: LAB 1.º n.º de evaluación, 2.º tipo (`1` ingreso, `2` monitoreo), 3.º `1` coordinadora del HP o `2` otro profesional de la comisión [p.80] · Tamizaje de drogas múltiples: LAB 1.º resultado (`1` negativo, `2` positivo, `3` inválido), LAB 2.º n.º de tamizaje [p.83] · Causalidad de farmacovigilancia: `1` definida, `2` probable, `3` posible, `4` improbable, `5` condicional [p.57], `6` no evaluable [p.58] · Plan participativo de salud mental: `COO` coordinación, `FO` organización, `FSE` sensibilización, `PP` diagnóstico y planificación participativa, `FE` ejecución, `FEV` evaluación [pp.58-59] · Situación de calle: fases `FO`, `PP`, `FE`, `FEV` [p.59]; profesional 1 a 4 (psiquiatra, psicólogo, enfermero, trabajador social) [p.60] o 1 a 3 (psicólogo, enfermero, trabajador social) [p.61]; ver D-18 |
| M25 NTS 246-2026, Anexo 20 | `Lab (3)` = 3.ª dosis (pentavalente; "niño protegido" con 3 dosis), `Lab (1)` = 1.ª dosis (SPR1), `Lab (DA)` = refuerzo (DPT 4 años). Coincide con el uso de M07 [pp.134-136] |
| M26 Pueblos Indígenas 2022 | Población indígena en **contacto inicial**: LAB `1` en el 1.er casillero (CI); en **contacto reciente**: LAB `2` (CR) [p.13] · plan integral: `1` elaboración, `TA` ejecución [pp.12-13] · valoración clínica de factores de riesgo: `DNT` (daños no transmisibles) [p.16] · sesión demostrativa: `LME` (lactancia materna exclusiva o prolongada), `ALI` (preparación de alimentos) [p.19] · dengue, 3.er renglón (administración de tratamiento): `1` inicio, `TA` fin [p.18] · tamizaje de violencia en gestante: `G` en el 1.er LAB de la primera actividad [p.14] |
| M02 Promoción 2024 (solo tabla PPoR 1001, p.16) | `LME`, `ALI`, `FCO`, `DXA`, `SBS`, `AA`, `COO`, `FSE`, `FO`, `PP`, `FEV`, `VCO`, `AE`, `GL`, `PNO`, `ENM`, `FIS`, `TA`. Otros programas presupuestales pueden añadir más (pendiente G-01). |

### C.1 Códigos APP verificados
| Código | Significado | Fuente |
|---|---|---|
| APP93 | Actividad con Instituciones educativas | M02 p.16 |
| APP96 | Actividad con Comité Multisectorial | M02 p.16 |
| APP166 | Actividades con líderes escolares | M24 p.5 |
| APP100 | Establecimiento / Personal de salud | M07 p.24; M24 pp.30, 54, 69 |
| APP101 | Otras organizaciones no mencionadas | M24 pp.50-53, 59-60 |
| APP104 | Actividad con Municipios | M02 p.16 |
| APP108 | Actividades con la Comunidad | M02 p.16; M04 p.8 |
| APP136 | Familia | M04 p.8 |
| APP138 | Agentes Comunitarios de Salud | M02 p.16; M07 p.24 |
| APP140 / 141 / 142 / 143 | Niños / adolescentes / adultos / adulto mayor | M04 p.8 |
| APP144 | Docentes (M02: "Docentes Ciclo I") | M02 p.16; M07 p.24 |
| APP145 / 146 / 157 | Alumnos / Padres / Trabajadores en general | M07 p.24 |
| APP150 | Autoridades y líderes comunales | M02 p.16 |
| APP151 | Mujeres (M02: "Mujeres (madres de grupos de apoyo)") | M02 p.16; M04 p.8 |
| APP152 / 153 | Gestantes / Puérperas | M04 p.8 |
| APP165 | Centro de Promoción y Vigilancia Comunal | M02 p.16 |

---

## D. ÍNDICE DE ACTIVIDADES (cruce entre manuales)

| Actividad | Código(s) | Manuales que la cubren | Ficha |
|---|---|---|---|
| Sesión educativa | C0009 | M02, M03, M04, M05, M06, M07 | F-001 |
| Sesión demostrativa | C0010 | M02, M03, M05, M06, M07 | F-002 |
| Visita familiar / domiciliaria | C0011, C0011.01, 99344, 99509 | M02, M03, M04, M05, M06, M07 | F-003 |
| Valoración clínica del adulto mayor (VACAM) | 99387 (2019) / 99215.03 (2025) | M05, M06 | F-004 |
| Plan de atención integral | C8002 (2019) / 99801 (2025) | M05, M06 | F-005 |
| Tamizaje de salud mental | 96150.01 a 96150.08, 80104, 99402.09, Z133, R456, Z720-Z722, Z654, Z655 (2025); U140 y 99404 (2019) | M24 (manda), M06, M10 | F-006 |
| Salud mental: atención individual, grupal y alta | 99207.01, 99207.02, 99217, 99366, 99205 | M24 | F-008 |
| Salud mental en instituciones educativas (psicología) | APP93/144/145/146, C0005, C0003, 99402.14, 96100.02, 99207.08 | M24 | F-009 |
| Familias Fuertes y habilidades sociales | C2111.02, 96150.05, 99401.15, 90872, Z734 | M24 | F-010 |
| Vacunación | 9xxxx, Z28x, U0009 | M07 (norma base reemplazada), M25 (códigos CPT, Anexo 20) | F-007 |
| Continuidad de cuidados (CSMC) | 99207.09, C8002 | M24 | F-011 |
| Rehabilitación psicosocial y laboral (CSMC) | 99207, 90872, 97537.01 | M24 | F-012 |
| Salud mental en crisis humanitarias | 99207.08, Z655, 99402.09, C2111.01, 99207.02 | M24 | F-013 |
| Comunidades víctimas de violencia política | C0071, 99207.07, C0006, Z654 | M24 | F-014 |
| Personas en situación de calle o población distante (ficha parcial) | Z590, C0003 | M24 | F-015 |
| Capacitación a cuidadores de niños con trastornos del desarrollo (CST) | 96154, C2111.01 | M24 | F-016 |
| Participación social y comunitaria; acompañamiento clínico psicosocial | C3001, C3051, C3141, C1001, C7004, C7002 | M24 | F-017 |
| Atención farmacéutica | 99605, 99606, C0061.02 | M24 | F-018 |
| Pertenencia étnica (código 1 a 60, autoidentificación) | tabla de la p.8-9 | M26 | pendiente (G-13) |
| Atención a población indígena de contacto inicial / reciente | LAB `1` / `2` | M26 | pendiente (G-13) |
| Tamizaje de violencia (negativo / positivo) | 96150.01, 99402.09, R456 (ejemplos) | M26, M24 | pendiente (G-13) |
| Valoración clínica de factores de riesgo (daños no transmisibles) | 99401.13, E6690 (ejemplos; otros dos códigos con lectura dudosa) | M26 | pendiente (G-13) |
| Caso probable de dengue | A970, U2142, U310 (ejemplo) | M26 | pendiente (G-13) |
| Salud mental: intervención en crisis, intervención grupal e individual, movilización de redes, psicoeducación individual y a la familia | 99285.01, 99207.02, 99207.01, C1043, 99207.04, C2111.01 (códigos de las filas de ejemplo) | M24 pp.94-96 | pendiente (G-15) |
| Psicoterapia individual y grupal; rehabilitación cognitiva; activación física | 90834 (o 90806, 90860), 90857, 96100.05, 99402.17 | M24 pp.96-98 | pendiente (G-15) |
| Telesalud: telecapacitación, teleconsulta, teleIEC, teleinterconsulta, teleorientación, telemonitoreo | 99499.13, 99499.01, 99499.14, 99499.11, 99499.08, 99499.10 (códigos de las filas de ejemplo) | M24 pp.98-101 | pendiente (G-15) |
| Terapia de lenguaje, terapia ocupacional grupal, visita domiciliaria | 97009, 97535.01 (el código de la visita no se leyó) | M24 pp.101-102 | pendiente (G-15) |
| Hogares protegidos (ingreso, redes, PIC, AVD, egreso, seguimiento, comisión de derivación) y penales (tamizaje de drogas, evaluación) | 99217, 99366, 99324, 80104 (ejemplos) | M24 pp.75-83 | pendiente (G-15) |
| Tabla de vacunas con código CPMS | 90585 BCG, 90744 HVB pediátrico, 90746 HVB adulto, 90713 IPV, 90712 APO, 90722 DPT-HVB-HIB, 90702 dT pediátrico, 90714 dT adulto, 90648 HiB, 90681 rotavirus, 90670 neumo 13V, 90657/90658 influenza pediátrica/adulto trivalente, 90687/90688 cuadrivalente, 90707 SPR, 90708 SR, 90716 varicela, 90717 AMA, 90633.01 HAV, 90701 DPT, 90649 VPH-4V, 90715 TdaP, 90749.01 a 90749.05 COVID/viruela del mono/dengue, **90749.06 hexavalente**, 90651 VPH-9V (2 o 3 dosis), 90651.01 VPH-9V (1 dosis), 90677 neumo 20V, **90678 VRS** | NTS 246-2026 parte 1, pp.70-71 (verificada con imagen) | F-007 (actualizar) |
| Reglas generales de la hoja | — | M01, M04, M06, M07, M26 | Sección B |
| Reuniones y talleres comunitarios | C0001, C0002, C0003, C1041, C3011, C3131, C6114, 90872 | M02, M04, M06 | pendiente (G-02) |
| Consejería | 99401, 99403, 99403.01, 99404 | M02, M05, M06 | pendiente (G-02) |

---

## E. FICHAS POR ACTIVIDAD

### F-001 · Sesión educativa (C0009)
```
id: F-001
codigo: C0009
modalidad: grupal
hc_dni: codigo APP del grupo [M04 p.9; M06 pp.23-24; M07 p.24]
se_tachan: DNI, financiador, etnia, edad, sexo, establecimiento, servicio (linea oblicua) [M04 p.9; M06 p.23; M07 p.24]
tipo_dx: D en todos los casilleros
casillero_1: Sesion Educativa (C0009)
casillero_2: depende de la estrategia (ver variantes)
lab_1: numero de participantes
duracion_tipica: 15 a 30 participantes, 1 a 2 horas [M04 p.9; M06 p.23; M07 p.24]
estado: VIGENCIA_NO_DETERMINADA (regla de M02 por subproducto pendiente de extraer, G-01)
```
**Variantes por manual**
| Manual | 2.º casillero | LAB 2 | Ejemplo | Fuente |
|---|---|---|---|---|
| M04 Salud Familiar 2014 | Actividades de la ESN Salud Familiar (U0020) | `AD`, `VIF` o `TD` | APP151 · 12 · C0009 · VIF · U0020 | pp.9-10 |
| M07 Inmunizaciones 2019 | Actividades de Inmunizaciones (U0009) | en blanco | APP142 · 18 · C0009 · U0009 | p.24 |
| M06 Adulto Mayor 2019 | no indica | no indica | APP143 · 15 · C0009 | pp.23-24 |
| M06 Círculo/club del adulto mayor | C3131 (3.er casillero) | LAB 1 = `1`; LAB 2 = participantes | APP100 · 1 · 20 · C0009 · C3131 | p.25 |
| M24 Salud Mental 2025 (instituciones educativas) | no usa C0009: usa **C0005 + 99402.14** (F-009) | LAB 1.º = n.º de sesión; LAB 2.º = participantes | APP144/145/146 | pp.28-30 |
| M05 Adulto Mayor 2025 (círculo) | — | LAB 1 participantes; LAB 2 = `1` si es en círculo | ver D-04 | sec. 11.3, p.38 |

### F-002 · Sesión demostrativa (C0010) — **dos modalidades**
```
id: F-002
codigo: C0010
modalidades: grupal general | individual PPoR (Promocion 2024)
tipo_dx: D
estado: VIGENCIA_NO_DETERMINADA (M02 es la edicion mas nueva localizada)
```
**A) Grupal general** [M06 p.23; M07 p.23]
- HC/DNI: código APP del grupo (ej. APP141, APP143). Se tachan DNI, financiador, etnia, edad, sexo, establecimiento y servicio.
- 1.º casillero: Sesión demostrativa. En Inmunizaciones, 2.º casillero: Estrategia Sanitaria Nacional de Inmunizaciones (U0009), LAB 2 en blanco.
- LAB 1: número de personas que participan.
- Ejemplos: `APP143 · 15 · C0010` [M06 p.23]; `APP141 · 12 · C0010 · U0009` [M07 p.23].

**B) Individual, familias con niños de 6-11 meses y gestantes (PPoR 1001)** [M02 pp.17-18]
- HC/DNI: **DNI del niño(a) o de la gestante** (no se usa línea oblicua).
- Gestante: en la columna Gestante/Puérpera se anota "Gestante" + fecha de última regla.
- 1.º casillero: Sesión demostrativa · código `C0010` · tipo `D`.
- **LAB 1 = `ALI`** (preparación de alimentos).
- Si se hace en Centros de Promoción y Vigilancia Comunal: **LAB 2 = `AE`** [M02 p.18].
- Condiciones: 6 a 15 participantes, unas 2 horas; metodología según R.M. 958-2012/MINSA [M02 p.17].

### F-003 · Visita familiar / domiciliaria — **el código depende de la edición**
```
id: F-003
codigos: 99344 | C0011 | C0011.01 | 99509
tipo_dx: D en la visita; R en el diagnostico preexistente
estado: VIGENCIA_NO_DETERMINADA (ver D-01)
```
| Manual | Qué es | Código | LAB | Fuente |
|---|---|---|---|---|
| M04 Salud Familiar 2014 | Visita de Salud Familiar (servicio 302101); HC = n.º de ficha familiar; DNI del miembro | **99344** | LAB 1.º = n.º de visita; al culminar el plan `TA` (el texto dice 2.º casillero; el ejemplo lo muestra en la primera fila: D-03) | pp.4-7 |
| M02 Promoción 2024 | Visita familiar del PPoR / Salud Familiar | **C0011.01** (primera) y **C0011** (al finalizar) | LAB 1 = `FAM`; al finalizar LAB 2 = `TA` | pp.164-165 |
| M06 Adulto Mayor 2019 | Visita familiar integral (APP) | **C0011** + plan familiar `U721`/`U722`/`U723` | LAB 2.º = n.º de visita (desde 2 si la 1.ª elaboró el plan); LAB 3.º = `1` al elaborar el plan; `TA` al terminar | p.22-23 |
| M06 Adulto Mayor 2019 | Atención del adulto mayor en domicilio | **99344** | LAB 2.º = n.º de visita; diagnóstico del motivo = `R`, visita = `D` | p.16 |
| M07 Inmunizaciones 2019 | Visita domiciliaria de seguimiento | **99344** | LAB 2.º = n.º de visita; no vacunación efectiva: Z280-Z289 | p.22 |
| M24 Salud Mental 2025 | Visita domiciliaria (acompañamiento a NNA en orfandad) y "Visita familiar integral/visita domiciliaria" | **C0011** (4.º casillero en el ejemplo) | LAB = n.º de sesión (1 a 12) | pp.6, 19 |
| M05 Adulto Mayor 2025 | Visita domiciliaria de ayuda en actividades de vida diaria | **99509**; visita familiar C0011; **99344 = consulta a domicilio de paciente nuevo, elevada severidad** | ver M05 sec. X y XI | Anexo 3, p.45 |

### F-004 · Valoración clínica del adulto mayor (VACAM)
```
id: F-004
codigo: 99387 (M06, 2019) | 99215.03 (M05, 2025)
tipo_dx: D en ambos (VACAM y consejeria)
lab_1: AS | E | AF | GC (categoria funcional)
consejeria: 99401; LAB = numero de consejeria
categoria_dx: Z6361 independiente | Z6362 dependiente parcial | Z6363 dependiente total
estado: M05 = ULTIMA_EDICION_LOCALIZADA
```
Registro 2019: saludable → 1.º VACAM, 2.º consejería integral, LAB 1.º `AS`, LAB 2.º n.º de consejería [M06 pp.11-12]. Enfermo: 1.º VACAM, 2.º diagnóstico, 3.º consejería; LAB 1.º `E`, LAB 3.º n.º de consejería [M06 p.12]. Frágil: `AF` [M06 p.13]. Geriátrico complejo: `GC`, consejería en el 4.º casillero [M06 p.13].
**Para el simulador, usar M05** (código 99215.03) y conservar M06 como histórica. Revisar M05 sec. II antes de programar.

### F-005 · Plan de atención integral
```
id: F-005
codigo: C8002 (M06, 2019) | 99801 Plan de Cuidado Integral de Salud (M05, 2025)
tipo_dx: D en ambos casilleros (VACAM + plan)
lab: 1 al elaborar el plan; TA al terminar todas las actividades del plan
estado: M05 = ULTIMA_EDICION_LOCALIZADA
```
Fuente M06: pp.14-15. Se registra solo al elaborar y al finalizar la ejecución.

### F-006 · Tamizaje de salud mental
```
id: F-006
hc_dni: DNI de la persona
tipo_dx: D en todas las actividades
consejeria: 99402.09 (Consejeria de prevencion de riesgos en salud mental)
negativo: 1.o tamizaje; 2.o consejeria 99402.09
positivo: 1.o tamizaje; 2.o codigo de positividad; 3.o consejeria 99402.09
estado: M24 (2025) = ULTIMA_EDICION_LOCALIZADA; M06 (2019) = SUPERADA
```
**Códigos del tamizaje (2025)** [M24 pp.6, 10]
| Tamizaje | Código | Positividad (2.º casillero si es positivo) |
|---|---|---|
| Violencia | 96150.01 | R456 Problemas relacionados con violencia |
| Alcohol y drogas | 96150.02 | Z720 tabaco · Z721 alcohol · Z722 drogas |
| Trastornos depresivos | 96150.03 | Z133 Pesquisa de problemas relacionados a la salud mental |
| Psicosis | 96150.04 | **Z133** (celda combinada de la tabla, vista en la imagen de p.11) |
| M-CHAT (niños de 2 años) | 96150.06 | **Z133** (celda combinada; p.70 lo muestra expresamente) |
| Deterioro cognitivo (60 años y más) | 96150.07 | **Z133** (celda combinada, p.11) |
| Trastornos mentales y del comportamiento, 6-17 años (PSC) | 96150.08 | Z133 (ejemplo 3, p.11) |
| Drogas múltiples (método no cromatográfico) | 80104 | — |

**LAB** [M24 pp.9-12]
- Madres de niños menores de 5 años (depresión, violencia, alcohol): LAB 1.º de la 1.ª actividad = `1` (hijo menor de 1 año) o `2` (de 1 a 5 años) [p.9].
- NNA con tamizaje positivo: LAB 1.º de la 1.ª actividad = `1` problemas emocionales, `2` de atención, `3` de conducta [pp.11-12].
- Drogas múltiples (80104): LAB 1.º = `1` negativo, `2` positivo, `3` inválido; LAB 2.º = n.º de vez que se aplica [p.12].
- Condiciones `TPE`, `PTB`, `DIS`, `JUD`: en el 1.er LAB de la primera actividad, o se agrega Z654 o Z65.3 (en drogas múltiples, en el 3.er LAB) [p.12].
- Víctima de violencia política (registro único de víctimas): se agrega **Z654**; víctima de desastre: **Z655** [M24 p.8; M06 p.16].
- Telemedicina: se agrega 99499.08 teleorientación (tamizaje) [M24 p.8].
- Hospitales y niveles II-III (consulta externa): misma regla de tamizaje [M24 pp.69-72].

**Versión histórica 2019 (M06 pp.15-16):** tamizaje **U140** con LAB `EP` psicosis, `AD` alcohol y drogas, `VIF` violencia intrafamiliar o `TD` trastorno depresivo; consejería 99404. Ya no manda (D-11).

### F-007 · Vacunación (consulta externa de inmunizaciones)
```
id: F-007
tipo_dx: D en todas las dosis [M07 p.6]
lab_intramural: n.º de dosis (1,2,3); dosis unica en blanco; refuerzo DA
lab_extramural: DU, D1, D2, D3, DDA; grupo de riesgo en el LAB contiguo
extramural: servicio y establecimiento = "C" para no generar atendidos [M07 pp.19-20]
estado: ULTIMA_EDICION_LOCALIZADA + BASE_NORMATIVA_REEMPLAZADA
```
- La NTS 141-2018 (R.M. 719-2018) que cita M07 fue **dejada sin efecto** por la R.M. 884-2022/MINSA (NTS 196-2022).
- **NUEVO (7 oct):** la **R.M. 561-2026/MINSA (12-jun-2026)** aprueba la **NTS 246-MINSA/DGIESP-2026** y **deja sin efecto** la R.M. 884-2022 y sus modificatorias (099-2023, 218-2024, 474-2025, 709-2025, 403-2026) [R.M. 561 arts. 1-2]. La base normativa vigente de vacunación es ahora la NTS 246; **la NTS 196 ya no rige**.
- M07 (2019) sigue siendo el único manual HIS de Inmunizaciones localizado. Según el usuario, se sigue usando en la práctica y se le agregan códigos tomados de otros documentos; no hay manual HIS nuevo. GERESA lo lista con sintaxis actualizada el 10-10-2025.
- **Usar M07 como guía de forma de registro; la NTS 246 como esquema vigente.** Cualquier código nuevo debe tener cita de página (regla de G-11).

**Códigos CPT/CIE que sí aparecen en la NTS 246, Anexo 20 [M25 pp.134-136]** (criterios de medición del programa presupuestal 1001 y PP 0002; no es un manual de registro):
| Vacuna | Código | LAB indicado | Pág. |
|---|---|---|---|
| BCG, recién nacido | 90585 | `(1)` | 136 |
| Hepatitis B (HvB), recién nacido | 90744 | — | 136 |
| Pentavalente (DPT-HvB-HiB), "niño protegido" con 3 dosis | 90723 | `Lab (3)` | 134 |
| SPR, 1 año | 90707 | `Lab (1)` | 134 |
| DPT, 4 años (2.º refuerzo) | 90701 | `Lab (DA)` | 134 |
| Influenza, 2 y 3 años | 90657 | — | 135 |
| Neumococo, menor de 1 año hijo de madre con VIH | 90670 | `Lab (3)` | 136 |
| Tdap, gestante | 90715 | — | 136 |

- **No aparecen** en las págs. 98-140 los códigos HIS de hexavalente, vacuna VRS, nirsevimab ni meningococo. No se inventan (G-11).
- El Anexo 10 es un **Registro Diario de Vacunación Unificado** con columnas Vacuna (código CPMS), Lote, Dosis, Grupo de riesgo, Comorbilidad y Contacto TBP [M25 p.101]. Su relación con la hoja HIS está abierta (D-13).

**Biológicos que el simulador puede ver en el esquema 2026** (solo para reconocerlos; **no es guía clínica**) [M25 Anexo 17]: anticuerpo monoclonal nirsevimab en el recién nacido (p.121); hexavalente celular "supeditada al agotamiento de stocks de pentavalente e IPV" (pp.122-123); vacuna VRS en gestantes de 32 a 36 semanas (p.126); Tdap en gestantes de 20 a 36 semanas (p.126); VPH dosis única de 9 a 18 años (p.125); meningococo y hexavalente acelular o DPT-IPV en niños con VIH (p.129).

### F-008 · Salud mental: atención individual, grupal y alta (M24)
```
id: F-008
hc_dni: DNI de la persona usuaria
orden: primero el diagnostico clinico (CIE-10), luego la actividad o procedimiento [M24 p.13]
individual: 1.o diagnostico (P, D o R); 2.o intervencion, por ejemplo 99207.01 (D); LAB 1.o de la 2.a actividad = n.o de sesion [p.13]
grupal con personas usuarias: 1.o diagnostico, SIEMPRE R y el mismo de la evaluacion inicial; 2.o intervencion grupal 99207.02 (D); LAB 1.o de la 2.a actividad = n.o de sesion [p.13]
alta: 1.o diagnostico (R); 2.o Manejo del alta 99217 (D); LAB 1.o de la 2.a actividad = tipo de alta [pp.14, 37]
tipo_alta: 1 recuperacion | 2 voluntaria | 3 abandono | 4 referencia (en CSMC: referencia/contrarreferencia) | 5 defuncion
opioides F11.0-F11.9: 1.o dx (D); 2.o intervencion; LAB 1.o de la 1.a actividad = 1 fentanilo | 2 tramadol | 3 otro opioide [p.9]
primer_episodio_psicotico: LAB 1.o del diagnostico = 1 durante todo el tratamiento [p.36]
estado: ULTIMA_EDICION_LOCALIZADA
```
**Centro de salud mental comunitaria (CSMC)** [M24 pp.34-37]
- Acogida (enfermería): 1.º Atención de enfermería en I nivel (99205), D.
- Evaluación integral interdisciplinaria: 1.º diagnóstico (el médico marca D y el resto del equipo R); 2.º Reunión del equipo de salud mental (99366), todos D. LAB 1.º de la 2.ª actividad = `1`; LAB 2.º = profesional que participa: 1 psiquiatra, 2 psicólogo(a), 3 enfermero(a), 4 trabajador(a) social, 5 médico de familia, 6 otros. Cada profesional registra su participación.
- Evaluación del PAI: diagnóstico siempre R; reunión del equipo D; LAB 1.º de la 2.ª actividad = n.º de evaluación desde el 2.
- Continuidad de cuidados: ver F-011; rehabilitación: F-012. Consulta externa de 2.º y 3.er nivel [M24 pp.69-74]: mismas reglas de tamizaje (F-006); en individual y grupal ver D-15.

### F-009 · Salud mental en instituciones educativas, por psicología (M24 pp.23-30)
```
id: F-009
codigo_modular: se registra el codigo modular de la IE [pp.23-24]
dx_permitidos: Tabla N.o 01 (Z61.x, Z62.x, Z63.x) [p.23]
tipo_dx_regla: D en la primera atencion y R desde la segunda [pp.25-27]
lab_IE: el valor `IE` diferencia el trabajo en IE [p.24]; ver D-12
estado: ULTIMA_EDICION_LOCALIZADA
```
| Actividad | HC/DNI | Casilleros | LAB | Pág. |
|---|---|---|---|---|
| Formación de redes de apoyo | **APP93** | 1.º Reunión en comunidad (C0003), D | LAB 1.º = n.º de reunión; LAB 2.º = `IE` | 24 |
| Tamizaje PSC negativo (96150.08) | DNI del NNA | 1.º tamizaje; 2.º consejería 99402.09; D | LAB 1.º = `IE` | 24 |
| Tamizaje PSC positivo | DNI del NNA | 1.º tamizaje; 2.º pesquisa (Z133); 3.º consejería; D | LAB 1.º = 1/2/3 (emocionales/atención/conducta); LAB 2.º = `IE`; LAB 3.º = `DVC` (referido) | 25 |
| Consejería y orientación psicológica (96100.02) | DNI del NNA | 1.º dx Tabla 01; 2.º consejería y orientación psicológica (D) | LAB 1.º 1.ª = `IE`; LAB 1.º 2.ª = n.º de sesión; si se refiere, `DVC` en el 2.º LAB de la 2.ª | 25-26 |
| Primeros auxilios psicológicos (99207.08) | DNI del NNA | 1.º PAP; 2.º dx Tabla 01; D | LAB 1.º = `IE` | 26 |
| Cuestionario de parentalidad | DNI del NNA | 1.º dx Tabla 01 (R); 2.º cuestionario (D) | LAB 1.º 1.ª = `IE`; LAB 1.º 2.ª = 1 deficiente / 2 regular / 3 adecuada | 27 |
| Orientación familiar | DNI del NNA | 1.º dx Tabla 01 (D la primera vez, luego R); 2.º Orientación familiar (D) | LAB 1.º 1.ª = `IE`; LAB 1.º 2.ª = n.º de sesión | 27-28 |
| Talleres con docentes / estudiantes / padres | **APP144 / APP145 / APP146** | 1.º Taller para instituciones educativas (C0005); 2.º Promoción del buen trato y salud mental (99402.14); D | LAB 1.º 1.ª = n.º de sesión (docentes y estudiantes 1-4; padres 1-11); LAB 2.º 1.ª = n.º de participantes; LAB 1.º 2.ª = tema (tabla de cada grupo); LAB 2.º 2.ª = `IE` | 28-30 |

Aquí la sesión grupal con APP **no usa C0009** sino **C0005 + 99402.14** (ver F-001).

### F-010 · Prevención en salud mental: Familias Fuertes y habilidades sociales (M24 pp.14-19)
```
id: F-010
familias_fuertes: C2111.02; 7 sesiones; grupo maximo 15; cumplida con la 7.a sesion [p.15]
habilidades_sociales: cuestionario 96150.05 + consejeria 99401.15; taller 90872; Z734 Habilidades sociales inadecuadas [pp.16-17]
estado: ULTIMA_EDICION_LOCALIZADA
```
- **Familias Fuertes, niños y adolescentes:** registro **individual** por sesión; DNI del NNA; 1.º taller C2111.02, D; LAB 1.º = n.º de sesión (1 a 7). **Padres:** registro **grupal**, HC/DNI = APP146; LAB 1.º = n.º de sesión, LAB 2.º = total de participantes [p.15].
- **Habilidades sociales, niños de 8 a 11 años:** (1) cuestionario: DNI, 1.º Aplicación del cuestionario (96150.05), 2.º Consejería en habilidades sociales (99401.15), D; si hay déficit se agrega Z734 (D). (2) Sesiones: 1.º Z734 (R), 2.º Taller de habilidades sociales (90872, D); LAB 1.º de la 2.ª actividad = n.º de sesión (1 a 10) [p.16].
- **Habilidades sociales, adolescentes de 12 a 17 años:** igual; Z734 se marca R desde la primera sesión; registro individual; cumplida con la 10.ª sesión [pp.17-18].
- **Acompañamiento psicosocial a NNA en orfandad:** 1.º Z634 (D la primera vez, luego R); 2.º intervención grupal 99207.02 (D); LAB 1.º de la 2.ª = n.º de sesión (1 a 8); cuidadores con APP146 y LAB 2.º = participantes. Visita domiciliaria: 2.º intervención individual, 3.º psicoeducación a la familia (C2111.01), 4.º visita domiciliaria (C0011); LAB = sesión (1 a 12) [pp.18-19].

### F-011 · Continuidad de cuidados (CSMC) (99207.09) [M24 pp.38-42]
```
id: F-011
codigo: 99207.09 Continuidad de cuidados a personas con trastorno mental grave y/o problemas psicosociales de riesgo
hc_dni: DNI de la persona usuaria
regla: el codigo 99207.09 acompana a las actividades del flujo de continuidad de cuidados [p.38, linea parcial]
tipo_dx: D cuando se define el diagnostico (derivacion, ingreso); R en las etapas siguientes
estado: ULTIMA_EDICION_LOCALIZADA
```
| Etapa | Casilleros | LAB | Pág. |
|---|---|---|---|
| A. Derivación | 1.º dx CIE-10; 2.º intervención (p. ej. consulta de salud mental 99207); 3.º 99207.09 | 2.ª act.: n.º de sesión; 3.ª act.: **`DVR`** | 38-39 |
| B. Evaluación para el ingreso | 1.º dx; 2.º Intervención individual 99207.01; 3.º 99207.09 | 2.ª: n.º de sesión; 3.ª: `1` | 39 |
| C. Ingreso | 1.º dx; 2.º 99207.09 | 2.ª: **`IA`** | 39-40 |
| D. Evaluación del proceso de recuperación y calidad de vida | 1.º dx (R); 2.º 99207.01; 3.º 99207.09 | 2.ª: n.º de sesión | 40 |
| E. Discusión del caso y formulación del PCCI | 1.º dx (R); 2.º presentación del caso; 3.º **Plan de continuidad de cuidados individualizado (C8002)**; 4.º 99207.09 | 2.ª y 3.ª: n.º de reunión | 40-41 |
| F. Reevaluación del grado de afectación | 1.º dx; 2.º 99207.01; 3.º 99207.09 | 2.ª: n.º de sesión; 3.ª: n.º de sesión desde 2 | 41 |
| G. Alta de continuidad de cuidados | 1.º dx; 2.º 99207.09; D | 2.ª: LAB 1.º **`TA`**; LAB 2.º = tipo de alta: `1` alta por recuperación, `2` alta voluntaria [p.41], `3` alta por abandono, `4` alta por traslado [p.42]; el ejemplo de la p.42 muestra `TA` y `1` | 41-42 |

### F-012 · Rehabilitación psicosocial y laboral (CSMC) [M24 pp.42-43]
```
id: F-012
psicosocial: 1.o dx CIE-10 (R), por ejemplo F201 esquizofrenia hebefrenica; 2.o Consulta de salud mental 99207 (D); 3.o intervencion de rehabilitacion, por ejemplo Taller de habilidades sociales 90872 (D); LAB 1.o de la 2.a y de la 3.a = n.o de sesion; minimo 10 sesiones [pp.42-43]
laboral: 1.o dx (R); 2.o Entrenamiento para la insercion laboral 97537.01 (D); LAB 1.o de la 2.a = n.o de sesion; minimo 10 sesiones [p.43]
estado: ULTIMA_EDICION_LOCALIZADA
```
Nota: en la lista de actividades frecuentes [M24 p.6] 97537.01 se llama "Rehabilitación profesional: entrenamiento para la inserción laboral"; 97537.02 es "Entrenamiento para la inserción/reinserción social".

### F-013 · Salud mental en contextos de crisis humanitarias [M24 pp.31-33 y 46-48]
```
id: F-013
tipo_dx: D en todas las actividades
dx_motivo: Z655 exposicion a desastre, guerra u otras hostilidades; alternativas Z654, Z658, Z588, Z603 [p.31, tabla]
tipo_crisis_LAB: 1 deslizamientos o huaycos | 2 heladas y friajes | 3 incendios | 4 lluvias e inundaciones | 5 sequias | 6 sismos o tsunamis | 7 volcanes | 8 olas de calor | 9 emergencias sanitarias | 10 conflictos armados o desplazamientos | 11 accidentes de transito
estado: ULTIMA_EDICION_LOCALIZADA
```
| Actividad | HC/DNI | Casilleros | LAB | Pág. |
|---|---|---|---|---|
| Primeros auxilios psicológicos (sesión única, primeras 72 h) | DNI e HC | 1.º PAP 99207.08 (solo una vez); 2.º Z655 u otro | LAB 1.º de la 2.ª = tipo de crisis; si el atendido es personal de salud: `ST` en LAB 1.º de la 1.ª | 31-32, 46-47 |
| Consejería de prevención de riesgos (99402.09) o psicoeducación a la familia (C2111.01) | DNI e HC | 1.º 99402.09 o C2111.01; 2.º Z655 u otro | LAB 1.º de la 1.ª = n.º de sesión (1 o 2); LAB 1.º de la 2.ª = tipo de crisis | 32-33, 47-48 |
| Intervención grupal comunitaria (99207.02) | **APP108** | 1.º 99207.02; 2.º Z655 u otro | LAB 1.º de la 1.ª = tipo de crisis; LAB 2.º = n.º de participantes | 33, 48-49 |

### F-014 · Comunidades víctimas de violencia política [M24 pp.20-23 y 43-46]
```
id: F-014
hc_dni: APP108 (Actividades con la comunidad)
tipo_dx: D siempre
casillero_2: Z654 Victima de crimen o terrorismo, incluyendo tortura
lab: LAB 1.o de la 1.a = n.o de reunion o sesion (1 a 6); LAB 2.o = n.o de participantes
regla: minimo 6 reuniones de 4 a 5 horas, cada 15 dias (3 meses); comunidades inscritas en el RUV, en el registro de desplazados del MIMP o en el de familiares de desaparecidos de la Defensoria
estado: ULTIMA_EDICION_LOCALIZADA
```
| Actividad | 1.º casillero | Pág. |
|---|---|---|
| Fortalecimiento de redes de apoyo psicosocial | C0071 Análisis de la situación de salud | 20-21, 44 |
| Acompañamiento psicosocial a comunidades | 99207.07 | 21-22, 45 |
| Reconstrucción de la identidad colectiva | C0006 Taller comunitario | 22-23, 45-46 |

### F-015 · Personas en situación de calle o población distante y dispersa (FICHA PARCIAL) [M24 pp.59-64]
```
id: F-015
estado: PARCIAL. Tablas LAB de las pp.59-61 verificadas sobre la imagen del PDF el 12 oct (ver abajo). Faltan por revisar con imagen las pp.62-64.
```
- Diagnóstico situacional y formación de redes: HC/DNI = **APP101**; 1.º Reunión en comunidad; D; LAB con siglas de fase, n.º de profesional y n.º de sesión o reunión [pp.59-60].
  - **Fases (LAB 1.º de la 1.ª actividad):** `FO` organización, `PP` diagnóstico y planificación, `FE` ejecución, `FEV` evaluación [p.59]. El ejemplo de la p.60 muestra `FO`, `2`, `2`.
  - **Diagnóstico situacional:** LAB 2.º = profesional (`1` médico psiquiatra, `2` psicólogo(a), `3` enfermero(a), `4` trabajador(a) social); LAB 3.º = n.º de sesión de la fase [p.60].
  - **Formación de redes de apoyo:** LAB 1.º = profesional (mismos valores 1 a 4); LAB 2.º = n.º de reunión [p.60].
  - **Identificación y vinculación (solo personas en situación de calle):** LAB 1.º = profesional con **otra tabla**: `1` psicólogo(a), `2` enfermero(a), `3` trabajador(a) social; LAB 2.º = n.º de sesión [p.61]. Ver D-18.
  - A las prestaciones se agrega **Z590** (falta de vivienda, personas en situación de calle) o **Z753** (atención de salud no disponible o inaccesible, población distante y dispersa) [p.61].
- Atención: DNI de la persona o un código; se agrega **Z590** (falta de vivienda); 1.º "Observación por sospecha de trastorno mental y del comportamiento" (D) [p.61]. Sin atención disponible: 1.º "Atención de salud no disponible o inaccesible" (P) + 2.º atención de enfermería 99205 (D) [p.61].
- Seguimiento del PAI: dx de calle y dx CIE-10 en R; 3.º actividad del PAI o reunión de monitoreo; LAB 1.º de la 3.ª = n.º de evaluación desde 2 [pp.62-63]. Derivación: 3.º derivación/referencia (D) [p.64].

### F-016 · Capacitación a cuidadores de niños con trastornos del desarrollo (CST) [M24 pp.64-66]
```
id: F-016
programa: 9 sesiones grupales de 90 min + 3 visitas familiares; dos facilitadores
sesion: DNI del NNA; 1.o dx del neurodesarrollo CIE-10 (R), por ejemplo autismo en la infancia; 2.o Intervencion en salud y comportamiento 96154 (D); LAB 1.o de la 2.a = n.o de sesion (1 a 9); el co-responsable registra C2111.01 en lugar de 96154
visita: 1.o dx (R); 2.o Visita familiar integral (D); 3.o 96154 (D); LAB 1.o de la 2.a = n.o de visita (1 a 3)
seguimiento_telefonico: 2.o intervencion de telesalud (por ejemplo telemonitoreo) (D); 3.o 96154; LAB 1.o de la 2.a = n.o de intervencion
estado: ULTIMA_EDICION_LOCALIZADA
```

### F-017 · Participación social y comunitaria; acompañamiento clínico psicosocial (CSMC) [M24 pp.49-55]
```
id: F-017
tipo_dx: D siempre
nota: los codigos se leyeron de los ejemplos; ver D-14 para C7002 / C7002.01
estado: ULTIMA_EDICION_LOCALIZADA
```
| Actividad | HC/DNI | Casilleros (códigos de los ejemplos) | LAB | Pág. |
|---|---|---|---|---|
| Reuniones de trabajo comunitario | APP108 | 1.º coordinaciones con actores (C1043) | LAB 1.º = n.º de reunión | 49 |
| Sesiones educativas a organizaciones de usuarios y familiares | **APP101** | 1.º C3141 | LAB 1.º = n.º del tema; LAB 2.º = participantes | 49-50 |
| Conformación de asociación de usuarios y familiares | APP101 | 1.º C3001 (reunión de participación comunitaria y empoderamiento social); 2.º C3051 | LAB 1.º de la 2.ª = tipo de organización (1 o 2); se registra una sola vez | 50-51 |
| Asistencia técnica a la organización | APP101 | 1.º C3001; 2.º C7004 | LAB 1.º de la 1.ª = n.º de sesión; LAB 2.º = según actividad; al lograr el registro: LAB 1.º de la 2.ª = entidad de registro | 51-52 |
| Abogacía y políticas públicas | APP101 | 1.º C1001 | LAB 1.º = entidad con la que participó | 53 |
| Vigilancia y acompañamiento comunitario (agentes comunitarios) | **APP138** | 1.º C3001; 2.º Sesión educativa C0009 | LAB 1.º de la 2.ª = n.º del tema; LAB 2.º = participantes | 53-54 |
| Acompañamiento clínico psicosocial (ACP) a un establecimiento | **APP100** | 1.º Asistencia técnica C7004; 2.º Supervisión C7002 | 1.ª: LAB `ACP`, n.º de sesión (1 a 10), n.º de personal que recibió ACP; 2.ª: n.º del profesional coordinador y n.º del establecimiento | 54-55 |

### F-018 · Atención farmacéutica a personas con problemas de salud mental (CSMC) [M24 pp.55-57]
```
id: F-018
dispensacion_y_consejeria: DNI; 1.o dx (R); 2.o Dispensacion de medicamentos y dispositivos medicos (D); 3.o Consejeria en uso racional de medicamentos (D); LAB 1.o de la 2.a = n.o de entrega; LAB 1.o de la 3.a = n.o de consejeria
consejeria_grupal: APP108; 1.o Consejeria en uso racional de medicamentos (D); LAB 1.o = n.o de veces; LAB 2.o = participantes
seguimiento_farmacoterapeutico: inicial 99605; de continuidad 99606; 1.o dx (R); 2.o seguimiento (D); LAB 1.o de la 2.a = n.o de seguimiento
farmacovigilancia: C0061.02; 1.o dx (R); 2.o Farmacovigilancia (D); LAB 1.o de la 2.a = n.o de farmacovigilancia; LAB 2.o = causalidad: `1` Definida, `2` Probable, `3` Posible, `4` Improbable, `5` Condicional [p.57], `6` No evaluable [p.58]; el ejemplo de la p.58 muestra LAB `2` y `2`
estado: ULTIMA_EDICION_LOCALIZADA
```

---

## F. REGISTRO DE DISCREPANCIAS

| ID | Qué | Detalle | Estado |
|---|---|---|---|
| D-01 | Significado de 99344 | M04, M06 y M07 lo usan para visita familiar/domiciliaria; M05 (2025) lo define como consulta a domicilio de paciente nuevo; M02 (2024) y M24 (2025, págs. leídas 1-38) usan C0011 y no mencionan 99344 como visita. | Abierta: confirmar con catálogo CPMS vigente |
| D-02 | Sesión demostrativa | Grupal con APP y participantes (M06, M07) frente a individual con DNI y LAB `ALI` (M02 pp.17-18). | Resuelta como dos modalidades (F-002) |
| D-03 | Posición de `TA` en Salud Familiar 2014 | El texto dice 2.º casillero de LAB; el ejemplo lo muestra en la primera fila [M04 p.7]. | Abierta |
| D-04 | Sesión educativa en círculo, M05 | El texto pone LAB 2 = `1`; una nota pone LAB 2 = `2` [M05 p.38]. | Abierta |
| D-05 | Plan y VACAM | M06: 99387 / C8002. M05: 99215.03 / 99801. | Resuelta: manda M05 |
| D-06 | Inmunizaciones | Norma base reemplazada dos veces (NTS 141 → NTS 196 → **NTS 246-2026**, R.M. 561-2026, que deja sin efecto la 196 y todas sus modificatorias). M07 sigue como único manual HIS. | Parcial: lo normativo está resuelto; los códigos HIS nuevos siguen abiertos (G-11) |
| D-07 | Rotulado de APP | APP151 y APP144 se nombran distinto en M02 y M04/M07. | Menor |
| D-08 | "22 registros" frente a 12 filas del anexo | La hoja es doble cara. | Resuelta por el usuario |
| D-09 | Número de la NTS en nota al pie de M05 | Sale impreso "20^"; se confirmó como **NTS 207-MINSA/DGIESP-2023, R.M. 789-2023/MINSA** (modificada solo en el 5.1 por R.M. 948-2023). | Resuelta |
| D-10 | Guía general | Se leyó la versión 2017; GERESA lista una versión 2020. | Parcial (11 oct): M01 pasa a LEÍDA con fragmentos de la 2020 enviados por el usuario; ya se incorporó la regla de hoja individual por turno y de no mezclar meses (sección B). Falta el PDF completo para citar páginas |
| D-11 | Tamizaje de salud mental | M06 (2019) usa U140 + siglas EP/AD/VIF/TD y consejería 99404; M24 (2025) usa 96150.01-.08 y consejería 99402.09. | Resuelta: manda M24 |
| D-12 | Valor `IE` en M24 | La p.30 dice que los psicólogos asignados a establecimientos de salud que hacen actividades en IE **no** registran `IE`, pero el resto de la sección 2.1.5 lo exige. | Abierta |
| D-13 | Anexo 10 de la NTS 246 (Registro Diario de Vacunación Unificado) frente a la hoja HIS | El Anexo 10 pide Vacuna (código CPMS), Lote, Dosis, Grupo de riesgo, Comorbilidad y Contacto TBP [M25 p.101]; M07 describe el registro de vacunas en la hoja HIS. No sé si el Anexo 10 la reemplaza o es complementario. Sin el cuerpo de la norma (parte 1) no se puede decidir. **Cierre 12 oct:** La NTS ordena registrar la vacuna «inmediatamente en el carné, en el registro diario unificado de vacunados», y además garantizar el ingreso en el HIS MINSA o en el componente de inmunizaciones del SIHCE [NTS 246 parte 1, p.55]. El personal que vacuna debe registrar y codificar las dosis todos los días según el Manual de Registro Diario de Atención y Otras Actividades de Salud HIS/MINSA [pp.66 y 70]. | **Resuelta (12 oct):** son complementarios; el Anexo 10 no reemplaza la hoja HIS |
| D-14 | Códigos de plan y de supervisión en M24 | El Plan de continuidad de cuidados individualizado se registra con **C8002** [M24 p.41], el mismo código que M06 (2019) usa para "plan de atención integral" del adulto mayor, que M05 (2025) cambió a 99801. En ACP, un ejemplo usa **C7002.01** (recepción, p.31) y otro **C7002** "Supervisión" (p.54). **Cierre 12 oct:** C8002 es «Plan de atención integral» en M26 (2022, pp.12-13) y en M06 (2019), pero «Plan de continuidad de cuidados individualizado» en M24 (2025, p.41); M05 (2025) usa 99801 para el plan del adulto mayor. C7002 es «Supervisión» [M24 pp.54-55] y C7002.01 es «Acompañamiento profesional de intervención realizada por experto» [M24 p.31]: son actividades distintas. | **Resuelta con reserva (12 oct):** no hay contradicción dentro de un mismo manual; cada código vale para la actividad que ese manual describe. Falta confirmar en el catálogo CPMS (no está en el repo) |
| D-15 | Tipo de diagnóstico en consulta externa de 2.º y 3.er nivel | En 1.er nivel, individual: diagnóstico P/D/R e intervención **D** [M24 p.13]. En 2.º y 3.er nivel, individual, el texto dice "marque **R**" [M24 p.73]; en grupal también R. No queda claro si R aplica al diagnóstico o a la intervención. **Cierre 12 oct:** En 2.º y 3.er nivel: el diagnóstico clínico del 1.er casillero se marca P, D o R, y la intervención individual del 2.º casillero se marca **R** [M24 p.73]; en la actividad grupal el diagnóstico va siempre R y la intervención también R [M24 p.73]. En 1.er nivel la intervención va D [M24 p.13]. | **Resuelta (12 oct)** con texto e imagen de la p.73 |
| D-16 | Código del plan de atención integral | M26 (2022) lo registra con **C8002** [pp.12-13], igual que M06 (2019); M05 (2025) usa 99801. | Resuelta: manda M05 (es la edición más nueva); coincide con D-05 |
| D-17 | Numeración y códigos de M26 | (a) El índice de la p.4 numera 5.1 a 5.7, pero en las páginas la numeración difiere (5.3 aparece dos veces: tamizaje en violencia, p.14, y valoración clínica de factores de riesgo, p.15) y las inmunizaciones aparecen como 5.4 (p.17) frente al 5.5 del índice. **Se cita siempre por página impresa.** (b) La tabla de códigos de pertinencia étnica de la p.9 pasa del 40 (Quechuas) al 42 (Resigaro): **no aparece el 41**. (c) En el ejemplo de la p.16 los códigos de «valoración clínica» y «examen de laboratorio» se leen como `2019` y `2017` (lectura dudosa; parecen truncados). | Abierta: confirmar (b) con la Directiva Administrativa 240-2017/MINSA/INS; (c) con el catálogo CPMS |
| D-19 | Código de la pentavalente | La tabla de códigos CPMS de la NTS 246 da **90722** (vacuna DPT-HVB-HIB) [p.70, verificada con imagen]; el Anexo 20 de la misma NTS escribe **90723** en el indicador de cobertura [parte 2, p.134, lectura por OCR]. | Abierta: confirmar con el equipo de inmunizaciones; el simulador v0.2 reconoce ambos y avisa |
| D-20 | Ediciones de M32 y M34 | M32 (Discapacidad) se declara 3.ª ed. dic 2025 con 2.ª ed. dic 2023, mientras M17 figura como 1.ª ed. enero 2023 (106 págs.). M34 (ITS y hepatitis, 1.ª ed. enero 2023, 82 págs.) tiene las mismas 82 págs. que M16 (VIH, 1.ª ed. agosto 2022). | Abierta: leer los créditos de M16/M17 y confirmar si son la misma obra (G-16) |
| D-18 | Tabla de profesional (LAB) en «situación de calle» | En el diagnóstico situacional y en la formación de redes la tabla es `1` médico psiquiatra, `2` psicólogo(a), `3` enfermero(a), `4` trabajador(a) social [p.60]; en identificación y vinculación es `1` psicólogo(a), `2` enfermero(a), `3` trabajador(a) social [p.61]. El mismo número significa otra persona según la actividad. | Abierta: el simulador debe usar una tabla distinta por actividad; confirmar con el equipo de salud mental del MINSA si es intencional |

---

## G. PENDIENTES (por prioridad)

- **G-01** Extraer de M02 la regla de cada subproducto (C0009, C0011, 99401…) y la tabla completa de siglas LAB.
- **G-02** Completar fichas de reuniones, talleres y consejerías.
- **G-03** Salud Mental 2025 (M24): **leída hasta la p.102** (12 oct; texto y, para las tablas LAB, imagen del PDF) y cruzado el listado de diagnósticos (p.103+) contra la R.M. 447-2024. Las tablas LAB ilegibles (alta de continuidad, fases de situación de calle, causalidad de farmacovigilancia) ya están verificadas: ver sección C. Queda comparar con M10 y revisar con imagen las pp.62-64 (F-015).
- **G-04** ~~Verificar si las R.M. 099-2023… 403-2026 cambian el registro HIS~~ **CERRADA por cambio de norma (7 oct):** la R.M. 561-2026 las deja sin efecto junto con la R.M. 884-2022. Sigue abierto qué cambia en el registro HIS: ver G-10 y G-11.
- **G-05** **CERRADA (7 oct):** R.M. 447-2024 verificada; resumen y cruce en A.2. Queda opcional abrir El Peruano para fecha y página oficial.
- **G-06** ~~Obtener y leer la Guía general 2020 (M01)~~ **CERRADA por instrucción del usuario (11 oct):** M01 pasa a LEÍDA con los fragmentos que él envió (© MINSA, enero 2020). La copia de DIRESA Junín no se pudo abrir desde aquí (error 401); sin el PDF completo no hay páginas citables de la 2020.
- **G-07** ~~Leer e inventariar los manuales nuevos~~ **INVENTARIADOS (12 oct):** M27 a M35 (portada, edición, Depósito Legal, páginas). El contenido de esos manuales **no se leyó**: ver G-16.
- **G-08** OCR de M20 (Cáncer) y M21 (Viruela del mono).
- **G-09** Buscar en El Peruano la R.M. de aprobación de cada manual (no apareció una R.M. propia en M05).
- **G-10** ~~Conseguir la parte 1 de la NTS 246-2026~~ **PARCIAL (12 oct):** el PDF de 97 págs. ya está en el repo (escaneado). Se leyó por OCR solo en lo de registro, códigos y anexo 10 (pp.54-55, 66 y 70-71). El resto del cuerpo (esquema por edad, dosis, intervalos) **no se leyó**.
- **G-11** Códigos HIS de las vacunas nuevas: **hexavalente = 90749.06** y **VRS = 90678** [NTS 246 parte 1, p.71, confirmado con imagen]. **Nirsevimab** y **meningococo** no figuran en la tabla de códigos CPMS (pp.70-71) y el cuerpo no da código; siguen abiertos.
- **G-12** ~~Probar en el celular el simulador y subir v0.1~~ **CERRADA (8-11 oct):** `simulador-his-integral-v0.1.html` abre y funciona en el celular del usuario; `registro-diario-his.html` y `simulador-his-integral-v0.html` ya no están en el repo SERUM-APP (verificado el 11 oct); el botón del Asistente Profesional abre el v0.1. Sigue pendiente decidir el destino de `simulador-his-serums.html`, que no está en ese repo. **Actualización 12 oct:** el simulador pasó a **v0.2** (`simulador-his-integral-v0.2.html`, con listas desplegables y bloqueos por edad o sexo con cita).
- **G-13** Crear fichas de M26 (una por actividad, con página impresa): pertenencia étnica; atención a población en contacto inicial/reciente; tamizaje de violencia; valoración clínica de factores de riesgo (DNT); caso probable de dengue. Verificar antes los códigos dudosos de D-17(c), y la sección 6 (códigos COVID-19, p.20), de la que no se comprobó la vigencia.
- **G-15** Crear las fichas de M24 pp.75-102 (hogares protegidos, penales y actividades 6.8 a 6.26) con página impresa; verificar con imagen los códigos de las filas de ejemplo (varios salen del texto de la imagen) y el código de la visita domiciliaria (p.102, cortado en el texto).
- **G-16** Leer M27 a M34 en orden de uso para SERUMS (Adolescente 2026, Adulto 2025, Salud Bucal 2025, Cáncer 2025, TBC 2025, Discapacidad 2025, Salud Ocular 2025, ITS y hepatitis 2023) y comparar con sus ediciones anteriores; resolver D-20.
- **G-14** (a pedido del usuario, «más adelante») Agregar el PDF de M26 al RAG: `SIP-AI-RAG/knowledge/minsa/manuales-his/` y luego a `data/metadata/` cuando se retome el RAG (hoy pausado). Nombre del archivo subido: `Actividades_de_Registro_y__codificacion_de_Pueblos_Indigenas__Etnias_14_01_22__1_.pdf`.

---

## H. PLANTILLAS (copiar y completar)

### H.1 Manual
```
| M## | Nombre | Edicion | Pags. | Normas que cita | Ultima en GERESA | Estado |
```

### H.2 Ficha
```
### F-### · Nombre (codigo)
id: F-###
codigo:
modalidad:
hc_dni:
se_tachan:
tipo_dx:
casillero_1:
casillero_2:
lab_1:
lab_2:
ejemplo:
fuentes: [M## p.##]
estado:
```

### H.3 Discrepancia
```
| D-## | Que | Detalle con citas | Estado |
```

---

## I. FUENTES WEB CONSULTADAS (6 oct 2026)

- El Peruano — R.M. 474-2025/MINSA (modifica NTS 196): https://busquedas.elperuano.pe/dispositivo/NL/2420436-1
- El Peruano — R.M. 403-2026/MINSA (modifica NTS 196; incorpora VRS): https://busquedas.elperuano.pe/dispositivo/NL/2508383-1
- R.M. 709-2025/MINSA (modifica NTS 196): https://iuslatin.pe/modifican-la-norma-tecnica-de-salud-que-establece-el-esquema-nacional-de-vacunacion-resolucion-ministerial-no-709-2025-minsa/
- GERESA Arequipa — Manuales HIS y sintaxis (act. 15-04-2026): https://saludarequipa.gob.pe/manuales-his/
- Promoción 2024 (copia gob.pe): https://cdn.www.gob.pe/uploads/document/file/7668680/6496924-his-dprom-2021-2024promsa.pdf
- Salud Mental 2.ª ed. 2025 — versión digital MINSA (no se pudo abrir desde aquí): https://bvs.minsa.gob.pe/local/MINSA/7615.pdf · copia leída (no oficial): https://crimsejus.wordpress.com/wp-content/uploads/2025/03/manual-his-de-salud-mental-2025.pdf
- Adulto Mayor 2.ª ed. 2025 — versión digital MINSA: https://bvs.minsa.gob.pe/local/MINSA/7631.pdf · Promoción 2.ª ed. 2024: https://bvs.minsa.gob.pe/local/MINSA/7318.pdf
- Salud Bucal 4.ª ed. 2025 (copia regional): https://www.saludarequipa.gob.pe/redislay/manuales_HIS/SALUD_BUCAL_2025.pdf
- R.M. 447-2024/MINSA, PDF del texto (copia de lpderecho.pe): https://img.lpderecho.pe/wp-content/uploads/2024/06/RM-447-2024-Minsa-LPDerecho.pdf
- R.M. 561-2026/MINSA y NTS 246-MINSA/DGIESP-2026: archivos subidos por el usuario (`8265031-resolucion-ministerial-n-561-2026-minsa.pdf`, `8265031-nts-n-246-minsa-digiesp-2026-parte-2.pdf`); enlace oficial citado en el repo: https://www.gob.pe/institucion/minsa/normas-legales/8265031-561-2026-minsa
- Salud Mental 2025 en el repo: `SIP-AI-RAG/knowledge/minsa/manuales-his/Manual-salud_mental-2025.pdf`
- M26 Pueblos Indígenas u Originarios 2022: archivo subido por el usuario el 11 oct (`Actividades_de_Registro_y__codificacion_de_Pueblos_Indigenas__Etnias_14_01_22__1_.pdf`, 22 págs.); sin enlace oficial verificado.
- El Peruano, nota del 10-jul-2026 (esquema pasa de 18 a 23 vacunas): https://elperuano.pe/noticia/298110-minsa-refuerza-esquema-de-vacunacion-para-gestantes-y-recien-nacidos-conoce-las-nuevas-dosis
- R.M. 884-2022/MINSA (NTS 196), R.M. 789-2023/MINSA y R.M. 948-2023/MINSA (NTS 207): verificadas en búsquedas en El Peruano/gob.pe; guardar el enlace oficial al citarlas.
