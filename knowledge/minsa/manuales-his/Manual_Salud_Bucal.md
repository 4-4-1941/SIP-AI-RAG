# MANUAL DE REGISTRO Y CODIFICACIÓN DE LA ATENCIÓN EN SALUD BUCAL
## SISTEMA DE INFORMACIÓN HIS - DIRECCIÓN DE SALUD BUCAL
### PROGRAMA PRESUPUESTAL 0018 / CONSULTA AMBULATORIA (2025)

> **Ministerio de Salud del Perú (MINSA)**  
> Dirección General de Intervenciones Estratégicas en Salud Pública (DGIESP)  
> Dirección de Salud Bucal (DSABU)  
> Dirección General de Tecnologías de la Información (OGTI) - Oficina de Gestión de la Información (OGEI)  

---

### Autoridades del Ministerio de Salud

- **Dr. Luis Napoleón Quiroz Avilés** — Ministro de Salud
- **Dr. Leonardo Ronyald Rojas Mezarina** — Viceministro de Salud Pública
- **Dra. Shirley Monzón Villegas** — Viceministra de Prestaciones y Aseguramiento en Salud
- **Dr. Carlos Bernardo Linares Arcela** — Secretario General
- **Dr. Marlon Tenorio Anicama** — Director Ejecutivo de la Dirección de Salud Bucal (DSABU)

### Ficha Catalográfica y Créditos de Elaboración

- **Catalogación:** Biblioteca Central del Ministerio de Salud del Perú.
- **Depósito Legal BNP:** N° 2025-15497.
- **Título Oficial:** *Manual de Registro y Codificación de la Atención en Salud Bucal 2025. Sistema de Información HIS MINSA.* (MINSA/DGIESP/DSABU - OGTI, Lima, 2025).
- **Responsable de Elaboración DGIESP / DSABU:**
  - C.D. Iris Antoanet Quevedo Casquero (Equipo Técnico)
- **Revisión y Validación DGIESP / DSABU:**
  - C.D. Marlon Tenorio Anicama (Director Ejecutivo)
  - C.D. Jéssica Benítez Barrionuevo (Equipo Técnico)
  - C.D. Carla Sanguineti Ramírez (Equipo Técnico)
  - C.D. Juan José Portocarrero Olano (Equipo Técnico)
  - C.D. Rocío del Pilar Cámac Arrieta (Equipo Técnico)
- **Equipo de Trabajo OGTI / OGEI:**
  - Lic. Luis Pedro Valeriano Arteaga (Jefe de Equipo)
  - Ing. Adhemir Reynel Bellido Delgado (Equipo Técnico)
  - Karlo Miranda Blas (Diseño)

---

## 1. PRESENTACIÓN Y ESTRUCTURA DEL MANUAL

El presente manual técnico contiene las directrices, definiciones operacionales y modelos estandarizados para el registro y codificación de las actividades y procedimientos en salud bucal dentro del Sistema de Información HIS a nivel de todas las IPRESS del país.

Tiene como objetivo garantizar la calidad, oportunidad y consistencia de los datos sanitarios generados en la atención estomatológica preventiva, recuperativa y especializada en el marco de las metas del Programa Presupuestal 0018.

### Índice General de Contenidos

| N° | Sección Temática | Página Ref. |
|:---:|:---|:---:|
| I | Instrucciones Generales para el Registro y Codificación de las Atenciones y Actividades en Salud Bucal | 06 |
| II | Instrucciones para el Registro de Diagnósticos y Procedimientos Asociados a la Atención Estomatológica (CIE-10 / CPMSS) | 06 |
| III | Instrucciones para el Registro y Codificación de la Evaluación Oral Completa y la Consulta Estomatológica | 15 |
| IV | Instrucciones para el Registro y Codificación de la Persona Sana para Salud Bucal y el Alta Básica Odontológica (ABO) | 16 |
| V | Procedimientos del Producto de Atención Estomatológica Preventiva (PP0018) | 22 |
| VI | Procedimientos del Producto de Atención Estomatológica Recuperativa (PP0018) | 27 |
| VII | Procedimientos del Producto de Atención Estomatológica Especializada en los Tres Niveles de Atención | 31 |
| VIII | Procedimientos Estomatológicos en la Atención Prenatal Reenfocada | 42 |
| IX | Actividades en Salud Bucal Realizadas a través de Telemedicina | 46 |
| X | Procedimiento de Interconsulta, Referencia y Contrarreferencia | 49 |
| XI | Actividades de Monitoreo, Supervisión y Asistencia Técnica | 53 |
| XII | Procedimientos Realizados en Oferta Móvil | 55 |
| XIII | Procedimientos Realizados en Centro Quirúrgico (Sala de Operaciones) | 56 |

---

## 2. INSTRUCCIONES GENERALES PARA EL REGISTRO Y CODIFICACIÓN EN EL HIS

### 2.1 Condición del Usuario en el Establecimiento y Servicio

1. **Al Establecimiento:**
   - `Nuevo (N)`: Persona que por primera vez en su vida acude a solicitar atención de salud en el establecimiento.
   - `Continuador (C)`: Persona que acude a atenderse en el establecimiento por segunda o más veces en el año en curso.
   - `Reingreso (R)`: Persona que acude por primera vez en el año al establecimiento, pero ya fue atendida en años anteriores.
2. **Al Servicio:**
   - `Nuevo (N)`: Persona que por primera vez en el año acude a la consulta estomatológica.
   - `Continuador (C)`: Persona que acude a citas subsiguientes de tratamiento en el servicio durante el año.

### 2.2 Tipo de Diagnóstico

- `Presuntivo (P)`: Diagnóstico probable que amerita pruebas diagnósticas (ej. radiografías, biopsias) para confirmación.
- `Definitivo (D)`: Diagnóstico confirmado clínicamente o procedimiento ejecutado. En odontología, **todos los procedimientos terminados se registran como definitivos (D)**.
- `Repetido (R)`: Se usa para el seguimiento de condiciones crónicas o diagnósticos ya registrados previamente en el año.

### 2.3 Uso del Campo LAB en Estomatología

- **Pieza Dental:** Para procedimientos que se realizan en un diente específico (ej. obturación, sellante, endodoncia, exodoncia), se anota el número de la pieza según la nomenclatura dental internacional FDI (dígito de 2 números: 11 a 48 para permanentes; 51 a 85 para primarios/deciduos).
- **Número de Sesión / Entrega:** Para procedimientos de frecuencia programada (ej. profilaxis, flúor, asesoría nutricional), se registra el número de entrega (`1`, `2`, `3`).
- **Superficie Dental:** En restauraciones complejas se puede especificar la superficie tratada (`O`, `M`, `D`, `V`, `P`, `L`).
- **Condición Especial:** Se usa `CM` para Comorbilidad y `DIS` para Discapacidad.

---

## 3. CATÁLOGO DE DIAGNÓSTICOS (CIE-10) Y PROCEDIMIENTOS (CPMSS) EN SALUD BUCAL

### 3.1 Códigos CIE-10: Patología Estomatológica Frecuente

| Código | Diagnóstico Estomatológico |
|:---|:---|
| `K000` | Anodoncia |
| `K001` | Dientes supernumerarios |
| `K002` | Anomalías del tamaño y de la forma del diente |
| `K006` | Alteraciones en la erupción dentaria |
| `K010` | Dientes incluidos |
| `K011` | Dientes impactados |
| `K020` | Caries limitada al esmalte (mancha blanca) |
| `K021` | Caries de la dentina |
| `K022` | Caries del cemento |
| `K023` | Caries dentaria detenida |
| `K028` | Otras caries dentales |
| `K029` | Caries dental, no especificada |
| `K030` | Atrición excesiva de los dientes |
| `K031` | Abrasión de los dientes |
| `K032` | Erosión de los dientes |
| `K033` | Reabsorción patológica de los dientes |
| `K036` | Depósitos [acreciones] en los dientes (placa blanda, sarro dental) |
| `K040` | Pulpitis reversible e irreversible |
| `K041` | Necrosis de la pulpa |
| `K042` | Degeneración de la pulpa |
| `K044` | Periodontitis apical aguda originada en la pulpa |
| `K045` | Periodontitis apical crónica |
| `K046` | Absceso periapical con fístula |
| `K047` | Absceso periapical sin fístula |
| `K050` | Gingivitis aguda |
| `K051` | Gingivitis crónica |
| `K052` | Periodontitis aguda |
| `K053` | Periodontitis crónica |
| `K054` | Periodontosis |
| `K060` | Retracción gingival |
| `K070` | Anomalías mayores del tamaño de la mandíbula o del maxilar |
| `K072` | Anomalías de la relación entre los arcos dentarios (Maloclusión Clase I, II, III) |
| `K073` | Anomalías de la posición del diente (apiñamiento, diastema) |
| `K081` | Pérdida de dientes debida a accidente, extracción o afección periodontal local |
| `K102` | Afecciones inflamatorias de los maxilares (Osteítis, osteomielitis) |
| `K120` | Estomatitis aftosa recurrente |
| `K121` | Otras formas de estomatitis |
| `K140` | Glositis |
| `K141` | Lengua geográfica |
| `S025` | Fractura de los dientes |

### 3.2 Códigos CPMSS: Procedimientos Dentales Frecuentes

| Código CPMSS | Procedimiento Estomatológico |
|:---|:---|
| `D0140` | Consulta estomatológica no especializada |
| `D0150` | Evaluación oral completa |
| `D0151` | Consulta estomatológica especializada |
| `D0220` | Radiografía periapical, primera película |
| `D0230` | Radiografía periapical, cada película adicional |
| `D0272` | Radiografías de aleta de mordida (dos películas) |
| `D0330` | Radiografía panorámica de maxilares |
| `D1110` | Profilaxis dental en adulto |
| `D1120` | Profilaxis dental en niño |
| `D1206` | Aplicación tópica de flúor barniz |
| `D1208` | Aplicación tópica de flúor gel |
| `D1310` | Asesoría nutricional para el control de enfermedades dentales |
| `D1330` | Instrucción de higiene oral |
| `D1351` | Aplicación de sellante en fosas y fisuras (por pieza) |
| `D1354` | Aplicación provisional de medicamento para frenar caries (cariostáticos) |
| `E2398` | Restauración autocurable con ionómero de vidrio en una superficie |
| `E2399` | Restauración autocurable con ionómero de vidrio en dos superficies |
| `E2400` | Restauración autocurable con ionómero de vidrio en tres o más superficies |
| `E2395` | Restauración fotocurable con ionómero de vidrio en una superficie |
| `E2396` | Restauración fotocurable con ionómero de vidrio en dos superficies |
| `E2397` | Restauración fotocurable con ionómero de vidrio en tres o más superficies |
| `D2330` | Restauración con resina compuesta en una superficie, pieza anterior |
| `D2331` | Restauración con resina compuesta en dos superficies, pieza anterior |
| `D2332` | Restauración con resina compuesta en tres superficies, pieza anterior |
| `D2391` | Restauración con resina compuesta en una superficie, pieza posterior |
| `D2392` | Restauración con resina compuesta en dos superficies, pieza posterior |
| `D2393` | Restauración con resina compuesta en tres superficies, pieza posterior |
| `D2394` | Restauración con resina compuesta en cuatro o más superficies, pieza posterior |
| `D3110` | Recubrimiento pulpar directo |
| `D3120` | Recubrimiento pulpar indirecto |
| `D3220` | Pulpotomía terapéutica (remoción de pulpa coronal) |
| `D3230` | Pulpectomía en pieza decidua anterior |
| `D3240` | Pulpectomía en pieza decidua posterior |
| `D3310` | Endodoncia en pieza anterior permanente (un conducto) |
| `D3320` | Endodoncia en pieza premolar permanente (dos conductos) |
| `D3330` | Endodoncia en pieza molar permanente (tres o más conductos) |
| `D4341` | Raspaje periodontal y alisado radicular, por cuadrante |
| `D4355` | Raspaje dental (destartraje supragingival completo) |
| `E4110` | Pulido dental post-raspaje |
| `D7140` | Exodoncia simple de diente erupcionado o raíz expuesta |
| `D7210` | Exodoncia quirúrgica de diente erupcionado |
| `D7220` | Exodoncia de diente impactado en tejido blando |
| `D7230` | Exodoncia de diente parcialmente impactado en hueso |
| `D7240` | Exodoncia de diente totalmente impactado en hueso (terceros molares) |

---

## 4. EVALUACIÓN ORAL COMPLETA, PERSONA SANA Y ALTA BÁSICA ODONTOLÓGICA (ABO)

### 4.1 Evaluación Oral Completa (D0150)

Se realiza en todo usuario nuevo o reingresante al servicio, o continuador que culmina su tratamiento o cambia a condición de gestante. Comprende el odontograma completo, índice de higiene oral simplificado (IHO-S) y examen de tejidos blandos.

#### Caso: Evaluación Oral Completa en Paciente con Comorbilidad (Hipertensión)
> **Paciente:** DNI: `61968843` | Financ.: `2 (SIS)` | Distrito: `La Victoria` | Edad: `45 Años` | Sexo: `F` | Condición: Estab. `C`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMSS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Evaluación oral completa | D | CM | | | `D0150` |
| 2 | Caries de la dentina | D | 46 | | | `K021` |
| 3 | Gingivitis crónica | D | | | | `K051` |

---

### 4.2 Persona Sana para Salud Bucal y Alta Básica Odontológica (ABO)

#### Definiciones:
- **Persona Sana para Salud Bucal:** Persona evaluada clínicamente que no presenta caries dental activa, enfermedad periodontal ni ninguna patología estomatológica.
- **Alta Básica Odontológica (ABO):** Condición alcanzada por el paciente que concluye el 100% de los procedimientos preventivos y recuperativos planificados (boca sana).

#### Caso 1: Persona Sana en Primera Evaluación
> **Paciente:** DNI: `74589632` | Financ.: `2 (SIS)` | Distrito: `El Pino` | Edad: `8 Años` | Sexo: `M` | Condición: Estab. `C`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMSS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Evaluación oral completa | D | | | | `D0150` |
| 2 | Persona sana para salud bucal | D | | | | `Z012` |
| 3 | Instrucción de higiene oral | D | 1 | | | `D1330` |
| 4 | Aplicación tópica de flúor barniz | D | 1 | | | `D1206` |

#### Caso 2: Alta Básica Odontológica (ABO) al Concluir Tratamiento
> **Paciente:** DNI: `61968843` | Financ.: `2 (SIS)` | Distrito: `La Victoria` | Edad: `20 Años` | Sexo: `F` | Condición: Estab. `C`, Serv. `C`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMSS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Evaluación oral completa | D | ABO | | | `D0150` |
| 2 | Restauración con resina compuesta en piezas anteriores | D | 11 | | | `D2331` |
| 3 | Instrucción de higiene oral | D | 2 | | | `D1330` |

*Nota en LAB: Registrar `ABO` en el casillero Lab de la evaluación oral para certificar el alta básica odontológica.*

---

## 5. PROCEDIMIENTOS DEL PRODUCTO DE ATENCIÓN ESTOMATOLÓGICA PREVENTIVA (PP0018)

### Paquetes Preventivos por Etapas de Vida

1. **Niños de 6 meses a menores de 2 años:**
   - 02 entregas de Instrucción de Higiene Oral (`D1330`).
   - 02 entregas de Asesoría Nutricional (`D1310`).
   - 02 entregas de Aplicación de Flúor Barniz (`D1206`).
2. **Niños de 2 a 11 años:**
   - 02 entregas de Instrucción de Higiene Oral (`D1330`).
   - 02 entregas de Asesoría Nutricional (`D1310`).
   - 02 entregas de Flúor Barniz (`D1206`) o Flúor Gel (`D1208`).
   - Aplicación de Sellantes en molares sanos libres de caries (`D1351`).
3. **Adolescentes, Jóvenes, Adultos y Adultos Mayores:**
   - 01 Evaluación oral completa (`D0150`).
   - 02 entregas de Instrucción de Higiene Oral (`D1330`).
   - 01 Raspaje dental / destartraje (`D4355`) y pulido dental (`E4110`).

#### Caso: Sesión Preventiva Infantil (Aplicación de Flúor Barniz y Sellante)
> **Paciente:** DNI: `98765432` | Financ.: `2 (SIS)` | Distrito: `Comas` | Edad: `6 Años` | Sexo: `M` | Condición: Estab. `C`, Serv. `C`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMSS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Aplicación tópica de flúor barniz | D | 1 | | | `D1206` |
| 2 | Aplicación de sellante en fosas y fisuras | D | 16 | | | `D1351` |
| 3 | Aplicación de sellante en fosas y fisuras | D | 26 | | | `D1351` |
| 4 | Instrucción de higiene oral | D | 1 | | | `D1330` |

---

## 6. PROCEDIMIENTOS DEL PRODUCTO DE ATENCIÓN ESTOMATOLÓGICA RECUPERATIVA (PP0018)

### 6.1 Subproducto: Raspaje y Pulido Dental (Enfermedad Periodontal Leve/Gingivitis)
> **Paciente:** DNI: `45123789` | Financ.: `2 (SIS)` | Distrito: `Surquillo` | Edad: `32 Años` | Sexo: `M` | Condición: Estab. `C`, Serv. `C`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMSS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Gingivitis crónica | R | | | | `K051` |
| 2 | Raspaje dental; destartraje dental | D | | | | `D4355` |
| 3 | Pulido dental post-raspaje | D | | | | `E4110` |

---

### 6.2 Subproducto: Restauraciones Dentales con Resina e Ionómero de Vidrio

#### Caso 1: Obturación con Resina en Pieza Premolar (Dos Superficies)
> **Paciente:** DNI: `45123789` | Financ.: `2 (SIS)` | Distrito: `Surquillo` | Edad: `32 Años` | Sexo: `M` | Condición: Estab. `C`, Serv. `C`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMSS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Caries de la dentina | D | 24 | | | `K021` |
| 2 | Restauración con resina compuesta en dos superficies, posterior | D | 24 | MO | | `D2392` |

#### Caso 2: Restauración con Ionómero de Vidrio Fotocurable en Pieza Decidua
> **Paciente:** DNI: `89456123` | Financ.: `2 (SIS)` | Distrito: `Ate` | Edad: `4 Años` | Sexo: `F` | Condición: Estab. `C`, Serv. `C`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMSS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Caries de la dentina | D | 64 | | | `K021` |
| 2 | Restauración fotocurable con ionómero de vidrio en dos superficies | D | 64 | DO | | `E2396` |

---

### 6.3 Subproducto: Exodoncia Simple

#### Caso: Exodoncia de Resto Radicular en Adulto
> **Paciente:** DNI: `10234567` | Financ.: `2 (SIS)` | Distrito: `San Juan de Lurigancho` | Edad: `50 Años` | Sexo: `M` | Condición: Estab. `C`, Serv. `C`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMSS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Raíz dental retenida | D | 36 | | | `K083` |
| 2 | Extracción de diente erupcionado o raíz expuesta | D | 36 | | | `D7140` |

---

## 7. ATENCIÓN ESTOMATOLÓGICA EN LA ATENCIÓN PRENATAL REENFOCADA (APN)

La gestante debe recibir como mínimo dos atenciones odontológicas durante el embarazo:
1. **Primera Consulta Estomatológica Prenatal:** Evaluación oral completa (`D0150`), asesoría nutricional (`D1310`), profilaxis/raspaje dental y plan de tratamiento.
2. **Segunda Consulta Estomatológica Prenatal:** Conclusión del plan de tratamiento, fluorización y certificación de Boca Sana / Alta Básica Odontológica de la gestante.

#### Caso: Primera Consulta Odontológica de la Gestante (Semana 14)
> **Paciente:** DNI: `47896521` | Financ.: `2 (SIS)` | Distrito: `Chorrillos` | Edad: `26 Años` | Sexo: `F` | Condición: Estab. `C`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMSS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Supervisión de embarazo normal de 14 semanas | D | 14 | | | `Z3492` |
| 2 | Evaluación oral completa en gestante | D | 1 | | | `D0150` |
| 3 | Gingivitis crónica del embarazo | D | | | | `K051` |
| 4 | Instrucción de higiene oral | D | 1 | | | `D1330` |

---

## 8. TELEMEDICINA Y PROCEDIMIENTOS ESPECIALES EN SALUD BUCAL

### 8.1 Modalidades de Telemedicina en Estomatología

| Modalidad | Descripción | Código CPMSS | Tipo Dx | Campo LAB |
|:---|:---|:---:|:---:|:---:|
| **Teleorientación** | Consejería y orientación en salud bucal mediante llamadas/videollamadas | `D9991` | D | `1`, `2`, `3` |
| **Telemonitoreo** | Seguimiento clínico no presencial post-tratamiento o farmacoterapia | `D9992` | D | `1`, `2`, `3` |
| **Teleinterconsulta** | Consulta a distancia con especialista (Cirujano Maxilofacial, Odontopediatra) | `D9993` | D | `1` (Consultante) / `2` (Consultor) |

---

### 8.2 Atención Estomatológica en Sala de Operaciones (Centro Quirúrgico)

Para pacientes con discapacidad severa, trastornos del neurodesarrollo o fobias dentales refractarias que requieren tratamiento dental integral bajo anestesia general o sedación profunda:
- **Procedimiento Principal:** Tratamiento odontológico integral en sala de operaciones (`D9420`).
- Se acompaña del registro individual de cada restauración, exodoncia o terapia pulpar ejecutada en la sesión con su respectivo código de pieza dental en el campo LAB.
