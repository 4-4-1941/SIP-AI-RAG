# MANUAL DE REGISTRO Y CODIFICACIÓN EN LA CONSULTA AMBULATORIA
## COMPONENTE DE PREVENCIÓN Y CONTROL DE DAÑOS NO TRANSMISIBLES
### SISTEMA DE INFORMACIÓN HIS (2025 - 2da Edición)

> **Ministerio de Salud del Perú (MINSA)**  
> Dirección General de Intervenciones Estratégicas en Salud Pública (DGIESP)  
> Dirección de Prevención y Control de Enfermedades No Transmisibles, Raras y Huérfanas (DENOT)  
> Oficina General de Tecnologías de la Información (OGTI) - Oficina de Gestión de la Información (OGEI)  

---

### Autoridades del Ministerio de Salud

- **Dr. César Henry Vásquez Sánchez** — Ministro de Salud
- **Dr. Ricardo Peña Sánchez** — Viceministro de Salud Pública
- **Dr. Herberth Ulises Cuba García** — Viceministro de Prestaciones y Aseguramiento en Salud
- **Dr. Cristian Díaz Vélez** — Director General de la Dirección General de Intervenciones Estratégicas en Salud Pública
- **Dr. José Enrique Pérez Lu** — Director General de la Oficina General de Tecnologías de la Información
- **Dr. Percy Alberto Herrera Añazco** — Director Ejecutivo de Prevención y Control de Enfermedades No Transmisibles, Raras y Huérfanas

### Ficha Catalográfica y Créditos de Elaboración

- **Catalogación:** Biblioteca Central del Ministerio de Salud del Perú.
- **Depósito Legal BNP:** N° 2025-05204.
- **Título Oficial:** *Manual de Registro y Codificación en la Consulta Ambulatoria. Componente de Prevención y Control de Daños No Transmisibles. Sistema de Información HIS.* (MINSA, Lima, 2025).
- **Equipo de Trabajo DGIESP / DENOT:**
  - Dr. Percy Alberto Herrera Añazco (Responsable Nacional del Componente)
  - Lic. Joycy Rojas Vílchez (Equipo Técnico)
  - Dr. Pedro Ernesto Kikushima Alcántara (Equipo Técnico)
- **Equipo de Trabajo OGTI / OGEI:**
  - Lic. Luis Pedro Valeriano Arteaga (Jefe de Equipo)
  - Ing. Marco Polo Bardales Espinoza (Equipo Técnico)
  - Ing. Adhemir Reynel Bellido Delgado (Equipo Técnico)
  - Lic. Julie Guillén Ramos (Diseño)
- **Edición y Depósito:** 1ra Edición (Febrero 2021) / 2da Edición (Mayo 2025). Enlace digital: `https://bvs.minsa.gob.pe/local/MINSA/7691.pdf`.

---

## 1. PRESENTACIÓN Y ESTRUCTURA DEL MANUAL

El presente documento técnico establece las directivas y pautas oficiales para el registro, codificación y procesamiento de datos asistenciales en la consulta ambulatoria del componente de Prevención y Control de Daños No Transmisibles en el Sistema de Información HIS-MINSA a nivel nacional.

Las intervenciones se desarrollan a lo largo de todo el curso de vida (niños, adolescentes, jóvenes, adultos y adultos mayores), centradas en la persona, su familia y comunidad, con un enfoque prioritario en la promoción de la salud, detección temprana y manejo integral oportuno de enfermedades cardiometabólicas y crónicas.

### Índice de Contenidos

| N° | Sección / Procedimiento | Página Ref. |
|:---:|:---|:---:|
| 1 | Componente de Prevención y Control de Daños No Transmisibles: Introducción y Ámbito | 04 |
| 2 | Diagnósticos y Actividades Más Frecuentes (CIE-10 / CPMS) | 07 |
| 3 | Instrucciones para el Registro y Codificación en el HIS | 08 |
| 4 | Cartera de Servicios: Productos y Subproductos Presupuestales | 09 |
| 5 | **Producto 3000015:** Valoración Clínica y Tamizaje Laboratorial de Enfermedades Crónicas No Transmisibles | 11 |
| 5.1 | Subproducto 5001508: Valoración Clínica de Factores de Riesgo en Menores de Edad (5 a 17 años) | 12 |
| 5.2 | Subproducto 5001508: Valoración Clínica de Factores de Riesgo en Jóvenes y Adultos (18 a 39 años) | 14 |
| 5.3 | Subproducto 5001508: Valoración Clínica de Factores de Riesgo en Adultos de 40 años a más | 16 |
| 5.4 | Subproductos 5001509 y 5001510: Tamizaje de Laboratorio de ECNT (Glucosa, Perfil Lipídico, Creatinina) | 18 |
| 6 | **Producto 3000016:** Tratamiento y Control a Personas con Diagnóstico de Hipertensión Arterial | 20 |
| 6.1 | Urgencias y Emergencias Hipertensivas Identificadas en Consultorio | 20 |
| 6.2 | Subproducto 5001608: Tratamiento y Control según Clasificación de Riesgo Cardiovascular Global | 22 |
| 6.3 | Subproducto 5001609: Tratamiento para Persona con Hipertensión sin Daño de Órgano | 24 |
| 6.4 | Subproducto 5001606: Personas Hipertensas con Tratamiento Especializado (Cardiología, Medicina Interna, Nefrología) | 26 |
| 6.5 | Subproducto 5001605: Educación y Grupos de Ayuda Mutua (GAM) en Hipertensión y Diabetes | 32 |
| 7 | **Producto 3000017:** Tratamiento y Control de Personas con Diabetes Mellitus | 35 |
| 7.1 | Manejo Básico de Crisis Hipoglucémica o Hiperglucémica en Consultorio | 35 |
| 7.2 | Subproducto 5001708: Tratamiento para Personas con Diabetes Mellitus sin Daño de Órgano | 36 |
| 7.3 | Tabla Maestra de Códigos CIE-10 para Diabetes Mellitus según Tipo y Complicaciones | 37 |
| 7.4 | Subproducto 5001704: Pacientes Diabéticos con Tratamiento Especializado (Nefrología, Neurología, Oftalmología) | 40 |
| 7.5 | Subproducto 5001705: Valoración de Complicaciones en Personas con Diabetes (Retinopatía y Pie Diabético) | 46 |
| 7.6 | Subproducto 5001707: Manejo de Enfermedad Renal Diabética | 49 |
| 8 | Servicios de Telemedicina en Daños No Transmisibles (Teleorientación, Telemonitoreo y Teleinterconsulta) | 51 |

---

## 2. DIAGNÓSTICOS Y ACTIVIDADES MÁS FRECUENTES EN DAÑOS NO TRANSMISIBLES

A continuación se presenta el catálogo consolidado de códigos CIE-10 y procedimientos CPMS de uso más frecuente en la atención de enfermedades crónicas no transmisibles:

| Código | Diagnóstico / Procedimiento / Actividad de Salud |
|:---|:---|
| `E100` | Diabetes Mellitus tipo 1 con coma |
| `E101` | Diabetes Mellitus tipo 1 con cetoacidosis |
| `E110` | Diabetes Mellitus tipo 2 con coma |
| `E111` | Diabetes Mellitus tipo 2 con cetoacidosis |
| `E112` | Diabetes Mellitus tipo 2 con complicaciones renales |
| `E113` | Diabetes Mellitus tipo 2 con complicaciones oftálmicas |
| `E114` | Diabetes Mellitus tipo 2 con complicaciones neurológicas |
| `E115` | Diabetes Mellitus tipo 2 con complicaciones circulatorias periféricas |
| `E116` | Diabetes Mellitus tipo 2 con otras complicaciones especificadas |
| `E117` | Diabetes Mellitus tipo 2 con complicaciones múltiples |
| `E118` | Diabetes Mellitus tipo 2 con complicaciones no especificadas |
| `E119` | Diabetes Mellitus tipo 2 sin complicaciones |
| `E160` | Hipoglicemia inducida por fármacos sin coma |
| `E162` | Hipoglicemia, no especificada |
| `E65` | Adiposidad localizada |
| `E669` | Obesidad no especificada |
| `E6690` | Sobrepeso |
| `E6691` | Obesidad Grado I |
| `E6692` | Obesidad Grado II |
| `E6693` | Obesidad Grado III |
| `E782` | Hiperlipidemia mixta |
| `E785` | Hiperlipidemia no especificada |
| `I10X` | Hipertensión esencial (primaria) |
| `I11X` | Enfermedad cardíaca hipertensiva |
| `I12X` | Enfermedad renal hipertensiva |
| `I13X` | Enfermedad cardiorrenal hipertensiva |
| `I150` | Hipertensión renovascular |
| `I151` | Hipertensión secundaria a otros trastornos renales |
| `I158` | Otras hipertensiones secundarias |
| `I159` | Hipertensión secundaria no especificada |
| `I209` | Angina de pecho, no especificada |
| `I64` | Accidente cerebrovascular no especificado como hemorragia o infarto |
| `N181` | Enfermedad renal crónica, etapa 1 |
| `N182` | Enfermedad renal crónica, etapa 2 |
| `N183` | Enfermedad renal crónica, etapa 3 |
| `N184` | Enfermedad renal crónica, etapa 4 |
| `N185` | Enfermedad renal crónica, etapa 5 |
| `R030` | Lectura elevada de la presión sanguínea, sin diagnóstico de hipertensión |
| `R730` | Prueba de tolerancia a la glucosa anormal |
| `R739` | Hiperglicemia, no especificada |
| `99199.22` | Tamizaje de la presión arterial |
| `99199.23` | Estratificación del riesgo cardiovascular global |
| `99401.13` | Consejería en estilos de vida saludable |
| `Z017` | Examen de laboratorio para pesquisa de factores de riesgo |
| `Z019` | Examen especial no especificado (Valoración Clínica de Factores de Riesgo) |
| `Z720` | Problemas relacionados con el uso de tabaco |
| `Z721` | Problemas sociales relacionados con el uso de alcohol |
| `Z723` | Problemas relacionados con la falta de ejercicio físico (Sedentarismo) |
| `Z724` | Problemas relacionados con la dieta inadecuada y hábitos alimenticios |
| `Z833` | Antecedentes familiares de diabetes mellitus |
| `Z834` | Antecedentes familiares de otras enfermedades crónicas, nutricionales y metabólicas |

---

## 3. INSTRUCCIONES PARA EL REGISTRO Y CODIFICACIÓN EN EL HIS

1. **Condición del Paciente al Establecimiento y Servicio:**
   - `Nuevo (N)`: Paciente que acude por primera vez en su vida al establecimiento / servicio.
   - `Continuador (C)`: Paciente que ya ha sido atendido previamente en el año en curso.
   - `Reingreso (R)`: Paciente atendido en años anteriores que acude por primera vez en el año evaluado.
2. **Tipo de Diagnóstico:**
   - `Presuntivo (P)`: Sospecha clínica que requiere confirmación o pruebas complementarias.
   - `Definitivo (D)`: Certeza diagnóstica, patología confirmada o procedimiento ejecutado.
   - `Repetido (R)`: Casos de control subsiguiente, seguimiento crónico de hipertensión, diabetes o factores de riesgo ya diagnosticados.
3. **Uso de Campos Lab (Laboratorio):**
   - **Lab 1:** Registra valores cuantitativos o subcódigos según procedimiento (ej. Presión sistólica, resultado numérico, sesión de consejería, entrega de medicación).
   - **Lab 2:** Registra valores cuantitativos complementarios (ej. Presión diastólica, meses de tratamiento dispensado, grupo de riesgo).
   - **Lab 3:** Registra valores específicos o estratos según protocolo ministerial.
4. **Regla de Continuidad de Registro:**
   - Si una atención involucra más de tres diagnósticos o actividades, trace una línea oblicua entre los casilleros de Día hasta Servicio del siguiente bloque y consigne las actividades restantes.

---

## 4. CARTERA DE SERVICIOS Y PRODUCTOS PRESUPUESTALES

| Producto | Actividad Presupuestal | Subproducto | Trazador | Unidad de Medida | Categorías IPRESS |
|:---|:---|:---|:---:|:---:|:---:|
| **3000015** Valoración Clínica y Tamizaje Laboratorial de ECNT | 5000113 Evaluación Clínica y Tamizaje Laboratorial | **5001508** Personas de 5 años a más con valoración clínica de factores de riesgo | Sí | Persona Evaluada | I-1, I-2, I-3, I-4, II-1 |
| **3000015** | 5000113 | **5001509** Tamizaje de laboratorio a personas de 18 a 39 años con riesgo elevado | Sí | Persona Evaluada | I-1, I-2, I-3, I-4, II-1 |
| **3000015** | 5000113 | **5001510** Tamizaje de laboratorio a personas de 40 años a más | Sí | Persona Evaluada | I-1, I-2, I-3, I-4, II-1 |
| **3000016** Tratamiento y Control de Hipertensión Arterial | 5000114 Tratamiento y Control de HTA | **5001608** Tratamiento y control de personas según clasificación de RCV | Sí | Persona Tratada y Controlada | I-2, I-3, I-4, II-1, II-2, III-1 |
| **3000016** | 5000114 | **5001609** Tratamiento para persona con hipertensión sin daño de órgano | Sí | Persona Tratada | I-2, I-3, I-4, II-1 |
| **3000016** | 5000114 | **5001606** Personas hipertensas con tratamiento especializado | Sí | Persona Tratada | II-1, II-2, III-1, III-E |
| **3000016** | 5000114 | **5001605** Pacientes con enfermedad cardiometabólica organizados que reciben educación | No | Persona Capacitada | I-1, I-2, I-3, I-4 |
| **3000017** Tratamiento y Control de Diabetes Mellitus | 5000115 Tratamiento y Control de Diabetes | **5001708** Tratamiento para personas con Diabetes Mellitus sin daño de órgano | Sí | Persona Tratada | I-2, I-3, I-4, II-1 |
| **3000017** | 5000115 | **5001704** Pacientes diabéticos con tratamiento especializado | Sí | Persona Tratada | II-1, II-2, III-1, III-E |
| **3000017** | 5000115 | **5001705** Valoración de complicaciones en personas con diabetes | Sí | Persona Evaluada | I-3, I-4, II-1, II-2, III-1 |
| **3000017** | 5000115 | **5001707** Manejo de enfermedad renal diabética | Sí | Persona Tratada | I-4, II-1, II-2, III-1 |

---

## 5. PRODUCTO 3000015: VALORACIÓN CLÍNICA Y TAMIZAJE LABORATORIAL

### 5.1 Subproducto 5001508: Valoración Clínica de Factores de Riesgo en Menores (5 a 17 años)

#### Caso 1: Menor de edad sin factores de riesgo identificados
> **Paciente:** DNI: `85274136` | Financ.: `2 (SIS)` | Distrito: `Huancayo` | Edad: `9 Años` | Sexo: `M` | Peso: `30 kg` | Talla: `135 cm` | Condición: Estab. `N`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Examen especial NE (Valoración Clínica de Factores de Riesgo) | D | | | | `Z019` |
| 2 | Consejería en estilos de vida saludable | D | | | | `99401.13` |

#### Caso 2: Menor de edad con factores de riesgo identificados (Sobrepeso)
> **Paciente:** DNI: `85274136` | Financ.: `2 (SIS)` | Distrito: `Paras` | Edad: `9 Años` | Sexo: `M` | Peso: `37 kg` | Talla: `135 cm` | Perím. Abd.: `74 cm` | Condición: Estab. `N`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Examen especial NE (Valoración Clínica de Factores de Riesgo) | D | ALT | | | `Z019` |
| 2 | Sobrepeso | D | | | | `E6690` |
| 3 | Examen de laboratorio | D | | | | `Z017` |
| 4 | Consejería en estilos de vida saludable | D | | | | `99401.13` |

---

### 5.2 Subproducto 5001508: Valoración Clínica en Jóvenes y Adultos (18 a 39 años)

#### Caso 1: Adulto joven sin factores de riesgo
> **Paciente:** DNI: `12345678` | Financ.: `2 (SIS)` | Distrito: `Lince` | Edad: `20 Años` | Sexo: `M` | Peso: `60 kg` | Talla: `168 cm` | Perím. Abd.: `80 cm` | Condición: Estab. `N`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Examen especial NE (Valoración Clínica de Factores de Riesgo) | D | | | | `Z019` |
| 2 | Tamizaje de la presión arterial | D | 110 | 70 | | `99199.22` |
| 3 | Consejería en estilos de vida saludable | D | | | | `99401.13` |

#### Caso 2: Adulto joven con factores de riesgo identificados (Obesidad y Sedentarismo)
> **Paciente:** DNI: `12345678` | Financ.: `2 (SIS)` | Distrito: `Lince` | Edad: `28 Años` | Sexo: `F` | Peso: `82 kg` | Talla: `158 cm` | Perím. Abd.: `92 cm` | Condición: Estab. `N`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Examen especial NE (Valoración Clínica de Factores de Riesgo) | D | ALT | | | `Z019` |
| 2 | Obesidad I | D | | | | `E6691` |
| 3 | Problemas relacionados con la falta de ejercicio físico | D | | | | `Z723` |
| 4 | Examen de laboratorio | D | | | | `Z017` |
| 5 | Tamizaje de la presión arterial | D | 120 | 80 | | `99199.22` |
| 6 | Consejería en estilos de vida saludable | D | | | | `99401.13` |

---

### 5.3 Subproducto 5001508: Valoración Clínica en Adultos de 40 años a más

#### Caso 1: Persona de 40 años a más sin factores de riesgo
> **Paciente:** DNI: `45678912` | Financ.: `2 (SIS)` | Distrito: `Trujillo` | Edad: `48 Años` | Sexo: `M` | Peso: `67 kg` | Talla: `169 cm` | Perím. Abd.: `82 cm` | Condición: Estab. `N`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Examen especial NE (Valoración Clínica de Factores de Riesgo) | D | | | | `Z019` |
| 2 | Examen de laboratorio | D | | | | `Z017` |
| 3 | Tamizaje de la presión arterial | D | 115 | 75 | | `99199.22` |
| 4 | Consejería en estilos de vida saludable | D | | | | `99401.13` |

#### Caso 2: Persona de 40 años a más con factores de riesgo y estratificación de Riesgo Cardiovascular
> **Paciente:** DNI: `45678912` | Financ.: `2 (SIS)` | Distrito: `Trujillo` | Edad: `55 Años` | Sexo: `M` | Peso: `84 kg` | Talla: `165 cm` | Perím. Abd.: `98 cm` | Condición: Estab. `N`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Examen especial NE (Valoración Clínica de FR) | D | ALT | | | `Z019` |
| 2 | Obesidad | D | | | | `E669` |
| 3 | Examen de laboratorio | D | | | | `Z017` |
| 4 | Tamizaje de la presión arterial | D | 135 | 85 | | `99199.22` |
| 5 | Estratificación del riesgo cardiovascular global | D | RCVB | | | `99199.23` |
| 6 | Consejería en estilos de vida saludable | D | | | | `99401.13` |

*Nota en LAB para `99199.23`: Consignar `RCVB` (Riesgo Bajo <5%), `RCVM` (Riesgo Moderado 5-9%), `RCVA` (Riesgo Alto 10-19%), o `RCVMY` (Riesgo Muy Alto >=20%).*

---

### 5.4 Subproductos 5001509 y 5001510: Entrega y Evaluación de Resultados de Tamizaje de Laboratorio

#### Caso 1: Entrega de resultados normales en persona de 18 a 39 años (Subproducto 5001509)
> **Paciente:** DNI: `12345678` | Financ.: `2 (SIS)` | Distrito: `Lince` | Edad: `28 Años` | Sexo: `F` | Condición: Estab. `C`, Serv. `C`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Examen especial NE (Valoración de Factores de Riesgo) | R | | | | `Z019` |
| 2 | Examen de laboratorio | D | | | | `Z017` |
| 3 | Consejería en estilos de vida saludable | D | | | | `99401.13` |

#### Caso 2: Entrega de resultados patológicos en persona de 40 años a más (Subproducto 5001510)
> **Paciente:** DNI: `45678912` | Financ.: `2 (SIS)` | Distrito: `Trujillo` | Edad: `55 Años` | Sexo: `M` | Condición: Estab. `C`, Serv. `C`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Hiperlipidemia mixta | D | | | | `E782` |
| 2 | Examen de laboratorio | D | | | | `Z017` |
| 3 | Consejería nutricional | D | | | | `99403` |

---

## 6. PRODUCTO 3000016: TRATAMIENTO Y CONTROL DE HIPERTENSIÓN ARTERIAL

### 6.1 Urgencias y Emergencias Hipertensivas Identificadas en Consultorio

#### Caso 1: Urgencia Hipertensiva en Consultorio (PA >= 180/120 mmHg sin daño agudo de órgano)
> **Paciente:** DNI: `54255123` | Financ.: `2 (SIS)` | Distrito: `Chilca` | Edad: `57 Años` | Sexo: `M` | Peso: `60 kg` | Talla: `160 cm` | Perím. Abd.: `89 cm` | Condición: Estab. `N`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Lectura elevada de la presión sanguínea | D | URG | | | `R030` |
| 2 | Tamizaje de la presión arterial | D | 190 | 120 | | `99199.22` |
| 3 | Administración de tratamiento farmacológico antihipertensivo | D | | | | `99199.25` |

#### Caso 2: Emergencia Hipertensiva Detectada en Consultorio (PA >= 180/120 mmHg con daño de órgano)
> **Paciente:** DNI: `54255123` | Financ.: `2 (SIS)` | Distrito: `Chilca` | Edad: `57 Años` | Sexo: `M` | Peso: `67 kg` | Talla: `160 cm` | Perím. Abd.: `92 cm` | Condición: Estab. `N`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Lectura elevada de la presión sanguínea | D | EMG | | | `R030` |
| 2 | Tamizaje de la presión arterial | D | 210 | 130 | | `99199.22` |
| 3 | Procedimiento de referencia de urgencia/emergencia | D | | | | `99096` |

---

### 6.2 Subproducto 5001608: Tratamiento y Control según Riesgo Cardiovascular

#### Caso 1: Paciente hipertenso con Riesgo Cardiovascular Muy Alto (Inicio de tratamiento)
> **Paciente:** DNI: `12347890` | Financ.: `2 (SIS)` | Distrito: `Callao` | Edad: `65 Años` | Sexo: `M` | Peso: `80 kg` | Talla: `164 cm` | Perím. Abd.: `95 cm` | Condición: Estab. `N`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Hipertensión esencial (primaria) | D | | | | `I10X` |
| 2 | Estratificación del riesgo cardiovascular global | D | RCVMY | | | `99199.23` |
| 3 | Tamizaje de la presión arterial | D | 150 | 95 | | `99199.22` |
| 4 | Tratamiento médico de la hipertensión arterial | D | 1 | | | `99199.24` |

---

### 6.3 Subproducto 5001609: Tratamiento para Persona con Hipertensión sin Daño de Órgano

#### Caso 1: Consulta médica de seguimiento y control con meta alcanzada (<130/80 mmHg)
> **Paciente:** DNI: `12347890` | Financ.: `2 (SIS)` | Distrito: `Callao` | Edad: `65 Años` | Sexo: `M` | Peso: `78 kg` | Talla: `164 cm` | Perím. Abd.: `93 cm` | Condición: Estab. `C`, Serv. `C`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Hipertensión esencial (primaria) | R | | | | `I10X` |
| 2 | Tamizaje de la presión arterial | D | 125 | 75 | | `99199.22` |
| 3 | Paciente hipertenso controlado | D | CTM | | | `U129` |
| 4 | Tratamiento médico de la hipertensión arterial | D | 3 | | | `99199.24` |

*Nota: Consignar `CTM` en LAB cuando el paciente alcanza metas terapéuticas.*

---

### 6.4 Subproducto 5001606: Personas Hipertensas con Tratamiento Especializado

#### Caso 1: Atención en UPSS Cardiología por Hipertensión Resistente
> **Paciente:** DNI: `78912345` | Financ.: `2 (SIS)` | Distrito: `Lima` | Edad: `62 Años` | Sexo: `F` | Condición: Estab. `N`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Hipertensión esencial (primaria) | R | HTR | | | `I10X` |
| 2 | Ecocardiografía transtorácica | D | | | | `93306` |
| 3 | Electrocardiograma de 12 derivaciones con informe | D | | | | `93000` |
| 4 | Monitoreo ambulatorio de presión arterial (MAPA) | D | | | | `93784` |

---

### 6.5 Subproducto 5001605: Educación y Grupos de Ayuda Mutua (GAM)

| N° | Actividad Educativa / Comunitaria | Código HIS | Tipo Dx | Lab 1 | Lab 2 | Lab 3 |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Sesión educativa en prevención y control de Hipertensión | `APP100` | D | ED | HTA | 1 |
| 2 | Sesión educativa en prevención y control de Diabetes | `APP100` | D | ED | DM | 1 |
| 3 | Sesión demostrativa en alimentación y estilos de vida (HTA) | `APP100` | D | SD | HTA | 1 |
| 4 | Sesión demostrativa en alimentación y estilos de vida (Diabetes) | `APP100` | D | SD | DM | 1 |
| 5 | Sesión de Grupo de Ayuda Mutua (GAM) - Hipertensión Arterial | `APP100` | D | GAM | HTA | 1 |
| 6 | Sesión de Grupo de Ayuda Mutua (GAM) - Diabetes Mellitus | `APP100` | D | GAM | DM | 1 |

*En el campo Historia Clínica registrar `APP100` y consignar el número de participantes en el casillero correspondiente.*

---

## 7. PRODUCTO 3000017: TRATAMIENTO Y CONTROL DE DIABETES MELLITUS

### 7.1 Manejo Básico de Crisis Hipoglucémica o Hiperglucémica en Consultorio

#### Caso 1: Crisis Hipoglucémica identificada en consulta externa
> **Paciente:** DNI: `32145698` | Financ.: `2 (SIS)` | Distrito: `Arequipa` | Edad: `54 Años` | Sexo: `M` | Condición: Estab. `N`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Hipoglicemia, no especificada | D | 52 | | | `E162` |
| 2 | Dosaje de glucosa en sangre rápida (glucómetro) | D | | | | `82948` |
| 3 | Diabetes Mellitus tipo 2 sin complicaciones | R | | | | `E119` |

---

### 7.2 Subproducto 5001708: Tratamiento para Diabetes Mellitus sin Daño de Órgano

#### Definición Operacional:
Persona de 18 años a más con diagnóstico de Diabetes Mellitus sin complicaciones que cumple con:
1. Al menos cuatro (4) controles de glicemia en el año.
2. Al menos cuatro (4) atenciones médicas especializadas o no especializadas de seguimiento.
3. Evaluación de factores de riesgo y dosaje de hemoglobina glicosilada (HbA1c).

#### Caso 1: Consulta de Seguimiento y Evaluación de Glicemia en Paciente Diabético
> **Paciente:** DNI: `32145698` | Financ.: `2 (SIS)` | Distrito: `Arequipa` | Edad: `54 Años` | Sexo: `M` | Peso: `74 kg` | Talla: `168 cm` | Condición: Estab. `C`, Serv. `C`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Diabetes Mellitus tipo 2 sin complicaciones | R | | | | `E119` |
| 2 | Dosaje de hemoglobina glicosilada (HbA1c) | D | 6.8 | | | `83036` |
| 3 | Paciente diabético controlado | D | CTM | | | `U129` |
| 4 | Tratamiento médico de la diabetes mellitus | D | 3 | | | `99199.27` |

---

### 7.3 Tabla Maestra de Códigos CIE-10 para Diabetes Mellitus

| Condición / Complicación | Tipo 1 (DM1) | Tipo 2 (DM2) | Otras Especificadas | No Especificada |
|:---|:---:|:---:|:---:|:---:|
| **Con coma (cetoacidótico / hiperosmolar)** | `E100` | `E110` | `E130` | `E140` |
| **Con cetoacidosis sin coma** | `E101` | `E111` | `E131` | `E141` |
| **Con complicaciones renales (nefropatía)** | `E102` | `E112` | `E132` | `E142` |
| **Con complicaciones oftálmicas (retinopatía)** | `E103` | `E113` | `E133` | `E143` |
| **Con complicaciones neurológicas (neuropatía)** | `E104` | `E114` | `E134` | `E144` |
| **Con complicaciones circulatorias periféricas (pie diabético)** | `E105` | `E115` | `E135` | `E145` |
| **Con otras complicaciones especificadas** | `E106` | `E116` | `E136` | `E146` |
| **Con complicaciones múltiples** | `E107` | `E117` | `E137` | `E147` |
| **Con complicaciones no especificadas** | `E108` | `E118` | `E138` | `E148` |
| **Sin mención de complicación** | `E109` | `E119` | `E139` | `E149` |

---

### 7.4 Subproducto 5001704: Pacientes Diabéticos con Tratamiento Especializado

- **UPS Nefrología:** Dosaje de creatinina sérica, estimación de tasa de filtración glomerular (TFG), albuminuria/proteinuria en orina de 24 horas y manejo de enfermedad renal diabética estadios 1 a 5 (`N181`-`N185`).
- **UPS Neurología:** Evaluación de polineuropatía sensitivo-motora distal, test de monofilamento de Semmes-Weinstein, velocidad de conducción nerviosa (`E114`).
- **UPS Cardiología:** Evaluación de cardiopatía isquémica silente, ecocardiograma, prueba de esfuerzo (`I209`, `I259`).
- **UPS Oftalmología:** Fondo de ojo con midriasis farmacológica, retinografía digital, angiografía con fluoresceína, fotocoagulación láser (`E113`, `92225`, `92250`).

---

### 7.5 Subproducto 5001705: Valoración de Complicaciones (Retinopatía y Pie Diabético)

#### Caso 1: Despistaje de Retinopatía Diabética mediante Fondo de Ojo
> **Paciente:** DNI: `23456789` | Financ.: `2 (SIS)` | Distrito: `Cusco` | Edad: `58 Años` | Sexo: `F` | Condición: Estab. `C`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Diabetes Mellitus tipo 2 sin complicaciones | R | | | | `E119` |
| 2 | Examen de fondo de ojo | D | NORM | | | `92225` |
| 3 | Consejería en prevención de complicaciones oculares | D | | | | `99401` |

*Nota en LAB: Registrar `NORM` si el fondo de ojo es normal o `ALT` si presenta signos de retinopatía diabética no proliferativa o proliferativa.*

#### Caso 2: Evaluación Integral de Pie Diabético (Riesgo Ulcerativo)
> **Paciente:** DNI: `23456789` | Financ.: `2 (SIS)` | Distrito: `Cusco` | Edad: `58 Años` | Sexo: `F` | Condición: Estab. `C`, Serv. `N`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Diabetes Mellitus tipo 2 con complicaciones circulatorias | D | | | | `E115` |
| 2 | Evaluación integral de los pies en el paciente diabético | D | R1 | | | `99199.28` |
| 3 | Consejería en autocuidado y calzado adecuado | D | | | | `99401` |

*Nota en LAB para `99199.28`: `R0` (Sin pérdida de sensibilidad ni vasculopatía), `R1` (Pérdida de sensibilidad protectora), `R2` (Deformidad o vasculopatía), `R3` (Antecedente de úlcera o amputación).*

---

### 7.6 Subproducto 5001707: Manejo de Enfermedad Renal Diabética

#### Caso 1: Paciente con Nefropatía Diabética Incipiente (Microalbuminuria positiva)
> **Paciente:** DNI: `87654321` | Financ.: `2 (SIS)` | Distrito: `Ica` | Edad: `60 Años` | Sexo: `M` | Condición: Estab. `C`, Serv. `C`

| N° | Diagnóstico / Actividad de Salud | Tipo Dx | Lab 1 | Lab 2 | Lab 3 | Código CIE / CPMS |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | Diabetes Mellitus tipo 2 con complicaciones renales | D | | | | `E112` |
| 2 | Enfermedad renal crónica, etapa 2 | D | | | | `N182` |
| 3 | Dosaje de microalbúmina en orina | D | POS | | | `82043` |
| 4 | Estimación de TFG por fórmula | D | 75 | | | `82565.01` |

---

## 8. SERVICIOS DE TELEMEDICINA EN DAÑOS NO TRANSMISIBLES

| Modalidad | Descripción Operacional | Código CPMS | Tipo Dx | Lab Teleconsultante | Lab Teleconsultor |
|:---|:---|:---:|:---:|:---:|:---:|
| **Teleorientación** | Consejería y orientación en salud a distancia mediante TIC | `99499.01` | D | - | - |
| **Telemonitoreo** | Seguimiento y transmisión de parámetros clínicos (PA, glucosa) | `99499.02` | D | - | - |
| **Teleinterconsulta** | Consulta médica especializada sincrónica o asincrónica entre IPRESS | `99499.03` | D | `1` | `2` |

#### Ejemplo de Teleinterconsulta en Hipertensión Arterial Refractaria:
- **IPRESS Consultante (Primer Nivel):**
  - Fila 1: `I10X` (Hipertensión esencial) — Tipo Dx: `R`
  - Fila 2: `99499.03` (Teleinterconsulta) — Tipo Dx: `D` — LAB: `1`
- **IPRESS Consultora (Hospital II / III Nivel):**
  - Fila 1: `I10X` (Hipertensión esencial) — Tipo Dx: `R`
  - Fila 2: `99499.03` (Teleinterconsulta) — Tipo Dx: `D` — LAB: `2`
