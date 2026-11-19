# Motor de códigos HIS — SERUM-APP

**Documento de traspaso** · 18-nov-2026
Para retomar el trabajo en una conversación nueva sin volver a empezar.

**Convención:** [V] = verificado en el código o en el PDF. [P] = pendiente, no comprobado.

---

## 1. Fuentes de códigos (cuatro piezas distintas)

| Archivo / página | Qué contiene | Dónde se ve |
|---|---|---|
| `core/view-assistant.js` | 29 constantes `HIS_*` con los códigos por grupo, `HIS_GROUPS`, `HIS_MANUALES` (PDF por manual) y funciones de interfaz (`renderHisCodesChild`, `hisOpenPdf`, `hisManual`) | Pestaña **Códigos HIS** del Asistente (buscador) |
| `core/sip-data-assistant.js` | `data.hisCodigosNino` (grupo Niño) | Entra en la misma lista como grupo "Niño" |
| `capacitacion/recursos/formatos/his-paquetes.html` | Página **Hoja HIS por paquetes**: busca en Supabase en las tablas `cie10` (solo `activo=true`) y `cpms`, y arma la hoja de registro | Botón "Abrir Hoja HIS por paquetes" en el Asistente |
| `core/sip-data-fichas.js` | `window.SERUMS_DATA` (fichas) | Cargado por `core/view-reference.js` |

**[V]** Los códigos de grupos (Materno, Emergencias, Zoonosis, DNT, Vacunas, Promoción, Transversal, etc.) **no están en `sip-data-assistant.js`**. Están en `view-assistant.js`. Por eso el archivo de la vista pesa unos 1,3 MB: el 99 % son datos.

## 2. Cómo se arma la lista "Códigos HIS" [V]

`renderHisCodesChild` concatena:
`data.hisCodigosNino` + `HIS_EXTRA`, `HIS_BUCAL`, `HIS_ADULTO_MAYOR`, `HIS_ADULTO`, `HIS_SALUD_MENTAL`, `HIS_PUEBLOS`, `HIS_PLANIFICACION`, `HIS_OCULAR`, `HIS_ITS`, `HIS_TBC`, `HIS_CANCER`, `HIS_DISCAPACIDAD`, `HIS_ADOLESCENTE`, `HIS_METAXENICAS`, `HIS_ANEMIA`, `HIS_MATERNO`, `HIS_EMERGENCIAS`, `HIS_ZOONOSIS`, `HIS_DNT`, `HIS_VACUNAS`, `HIS_PROMOCION`, `HIS_TRANSVERSAL`.

Comprobado en la copia de trabajo y en el repo: no hay constantes usadas sin declarar. Las constantes declaradas que **no** son códigos (y por eso no aparecen en la lista) son: `HIS_GROUPS`, `HIS_GUIAS`, `HIS_MANUALES`, `HIS_PDF_BUCKET`, `HIS_PDF_RESPALDO_REPO`, `HIS_PDF_SUPABASE`, `HIS_REPO_PDF`.

## 3. Por qué puede verse solo Niño [P]

El código sí incluye todos los grupos. **No he reproducido el síntoma en el navegador.** Causas a comprobar:
- **Caché:** `core/sip-router.js` carga cada vista con `?v=20261113-fichas`. Si el navegador o el service worker conserva la versión anterior, no verás los cambios. Hay que cambiar ese `v=` (requiere OK).
- **Carga incompleta:** si el archivo de 1,3 MB no termina de cargar, solo queda `data.hisCodigosNino`.
- **Filtro:** revisar que el chip seleccionado sea "Todos".

## 4. Qué es un "paquete" (definición de Richard)

Cada **cruce de códigos** de una tabla de manual es un paquete. Un paquete combina diagnóstico, procedimiento y consejería, con sintaxis de registro (tipo de diagnóstico P/D/R, LAB) y se enruta a la ficha HIS.

**Ejemplo: retinopatía de la prematuridad** (Manual de Salud Ocular, págs. 12–13 del material de la imagen):
- Fila 1, diagnóstico **H351** (retinopatía de la prematuridad), marcada **R** (repetitivo).
- Fila 2, procedimiento, marcada **D**:
  - Láser: **67229** (destrucción de retinopatía extensa).
  - Antiangiogénico: **67028** (inyección intravítrea).
  - Láser + antiangiogénico: 67229 + 67028.
  - Vitrectomía posterior + endofotocoagulación: **67043**.
- Teleinterconsulta asíncrona: **99499.12**. Oftalmoscopia indirecta: **92226**.

**[V]** Todos estos códigos existen en `view-assistant.js` (grupo Salud ocular, o sus equivalentes).

**[P]** No he encontrado en `his-paquetes.html` la lógica que convierta un paquete en una ficha HIS. Sí existen la búsqueda y la hoja de registro. Hay que definir y verificar ese enrutamiento.

## 5. Supabase

- Proyecto **SERUMS Intelligence Platform** (`xcfdhwqjudzngvlssyeg`).
- `his-paquetes.html` consulta las tablas `cie10` y `cpms`.
- **[P]** No he verificado si existe una tabla de paquetes. No tocar Supabase sin pedido explícito.
- Bucket `manuales-his`: los PDF de los manuales. Los nombres reales están en la sección 7.

## 6. Estado de los cambios en SERUM-APP

| Qué | Dónde | Estado |
|---|---|---|
| Repo GitHub local | `core/view-assistant.js` | **Sin cambios** |
| Copia con U069 quitado, A925, A9501, A9502, Y4184, Y4185 y grupo Transversal (298) | `/mnt/user-data/outputs/view-assistant.js` | Lista, **sin subir** (espera aprobación) |

Pendientes:
- **A970 duplicado:** aparece en Metaxénicas y en Pueblos indígenas (categoría "Enfermedades metaxénicas"). Sin decidir.
- **Sin botón PDF:** las filas de la RM 447-2024 (Metaxénicas nuevas y Transversal) no abren ningún manual, porque la RM 447 no está en el bucket `manuales-his`.
- **Separación del archivo:** propuesta, no ejecutada. Mover los datos a `core/his-codigos.js` y dejar en `view-assistant.js` solo la interfaz. Requiere aprobación.

## 7. Nombres reales en el bucket `manuales-his` [V]

- `Manual-atencion-materna-2023-2da-edicion.pdf`
- `Manual-emergencias-urgencias-primer-nivel-atencion-2022.pdf`
- `Manual-zoonosis-rabia-2022.pdf`
- `danos_no_transmisibles-2025.pdf`
- `Metaxenicas.pdf`
- `Manual His de Anemia por deficiencia 2024.pdf`
- `salud-ocular-2025.pdf`, `salud-bucal-2025.pdf`, `adulto-2025.pdf`, `adulto-mayor-2025.pdf`, `nino-2021.pdf`, `inmunizaciones-2019.pdf`, `promocion-salud-2024.pdf`, y otros (ver `HIS_MANUALES`).

## 8. Reglas de trabajo (pedidas por Richard)

1. **Explicar antes de ejecutar.** Un paso a la vez.
2. **No crear carpetas ni archivos sin OK**, y mostrar la ruta exacta.
3. **Entregar el archivo completo**, listo para copiar.
4. **La fuente es solo el documento** (manual, NTS, RM o anexo, y página). No escribir notas de vigencia ni "por confirmar" en el archivo.
5. **Verificar en el PDF**, no en el `.md` derivado. Los `.md` del Anexo I de la RM 447 tienen el encabezado de A925 mal ubicado.
6. **No dilatar.** Si algo falta, decirlo en una línea y pedir solo el dato indispensable.

## 9. Próximo paso

Con tu OK:
1. Separar los datos HIS en `core/his-codigos.js` (archivo nuevo, dentro de `core/`).
2. Dejar en `core/view-assistant.js` solo la interfaz, y que cargue los datos antes de dibujar.
3. Verificar que la lista muestra todos los grupos.
