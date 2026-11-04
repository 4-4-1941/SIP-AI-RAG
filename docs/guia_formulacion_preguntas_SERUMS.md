# Guía de formulación de preguntas tipo examen SERUMS

Fuente de los números: 3538 preguntas oficiales MINSA (`knowledge/serums/banco_preguntas/banco_oficial_minsa_parte1-4`) y `blueprints_por_carrera.json` (bloque "reciente", suma de carreras). El banco generado por IA se comparó contra esos mismos datos.

## 1. Estructura (lo que hace el examen real)
| Elemento | Examen oficial | Banco IA actual | Regla |
|---|---|---|---|
| Alternativas | siempre 4 (A-D), 1 correcta | 4 | 4, una sola correcta |
| Largo del enunciado | mediana 37 palabras (p10 21, p90 57) | mediana ~84 caracteres | 25 a 55 palabras; casi siempre con contexto |
| Largo de cada alternativa | mediana 2 palabras (p90 7) | mediana 4 (p90 13) | 1 a 7 palabras |
| Clave en la alternativa más larga | 37 % | 83 % | no más del 30 %; igualar longitudes |
| Posición de la clave | A 24, B 25, C 25, D 26 % | 24-26 % | repartir al azar |
| Enunciados con "NO/excepto" | 0 % | — | no usar |
| "Todas/ninguna de las anteriores" | 0 % | — | no usar |

## 2. Tipo y eje (blueprint reciente, suma de carreras)
- **Tipo:** 55 % caso aplicado · 45 % definición conceptual.
- **Eje:** Salud pública 31 % · Cuidado integral 24 % · Gestión 21 % · Ética e interculturalidad 12 % · Investigación 11 %.
- El banco IA tiene ~86 % en "Cuidado integral": está desbalanceado frente a esto. Para una carrera concreta usar su propio blueprint.

## 3. Redacción
1. **Un solo concepto por pregunta.** Se pregunta una decisión, clasificación o identificación, no un dato suelto.
2. **Caso aplicado:** 1 a 3 oraciones de contexto (lugar, edad o servicio, dato clave) + pregunta final clara (`¿Cuál es…?`, `¿A qué…?`, `¿Qué tipo…?`, `¿Cómo se…?`). Ejemplo oficial: brote de malaria con 2 fallecidos entre 50 casos → ¿qué medida epidemiológica? (clave: tasa de letalidad).
3. **Definición conceptual:** enunciado completo sin pistas en la forma; no repetir en el enunciado palabras que solo aparecen en la clave.
4. **Nivel: competencia, no memoria.** El examen mide si el profesional sabe actuar: aplicar, clasificar, decidir o priorizar ante una situación. Evitar "recordar el número, año o artículo de la norma" y definiciones literales del tipo "Según la Ley X, la telesalud es:".
5. **Adaptación a las normas:** el contenido de la norma va en la **clave y el contexto**, sin citarla (no escribir "según la RM N.° …"). La cita oficial y la página van en los datos de la pregunta (`fuente`, `pagina`, `cita_textual`), no en el enunciado.

## 4. Distractores
- Misma categoría que la clave (ejemplo oficial: tasa de ataque / letalidad / incidencia acumulada / mortalidad general).
- Plausibles: errores reales de aplicación, no absurdos.
- Largo y forma parecidos a la clave (misma estructura gramatical).
- Sin pistas: sin "siempre", "nunca", "solo"; sin repetir texto del enunciado solo en la clave.
- Independientes entre sí (que dos opciones no impliquen una a la otra).

## 5. Parafraseo de una pregunta oficial
Se conserva: concepto evaluado, nivel, eje y clave. Se cambia: contexto (edad, lugar, servicio), redacción, orden de las alternativas y distractores equivalentes. Prohibido cambiar el contenido clínico o normativo de la clave. La parafraseada lleva `parafraseada_de: Qxxxx` y se marca para revisión por muestreo, no una por una.

## 6. Control de calidad automático (antes de revisión humana)
- 4 alternativas distintas; la clave existe y es una sola.
- Clave no es la más larga (si lo es, reescribir).
- Enunciado entre 25 y 55 palabras en casos; sin "NO/excepto".
- Eje y tipo dentro del blueprint; cita textual presente en el documento fuente.

## 7. Fijas (preguntas que se repiten entre exámenes)
- El banco oficial reúne 4 exámenes: 2025-I (510), 2025-II (1352), 2026-I (814) y 2026-II (863). Repetidas **exactas**: casi ninguna (1 de 3538).
- Repetidas **adaptadas** (mismo concepto, otras palabras): al menos **91 preguntas en 37 familias** (32 familias en 2 exámenes y 5 en 3). Es un mínimo, medido por similitud de palabras. Ejemplo: temperatura de almacenamiento de productos refrigerados (2 a 8 °C), en 2025-I y 2026-II con distinta redacción. Detalle en `fijas_familias.json`.
- **Premisa al parafrasear:** una fija es un concepto que el examen vuelve a preguntar. Por eso: (1) las 37 familias se parafrasean primero; (2) por familia se generan hasta 3 variantes de redacción manteniendo concepto y clave; (3) las demás oficiales se parafrasean después, sin perder su concepto.
- Se asume que el equipo de diseño de ítems adapta preguntas anteriores y no renueva todo el banco cada año. Eso es una hipótesis razonable, respaldada por estos datos, pero no la confirma el MINSA.
