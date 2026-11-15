# Manual de registro y codificacion consulta ambulatoria

## Metadatos del documento

| Campo | Valor |
|---|---|
| Título | Manual de Registro y Codificación en la Consulta Ambulatoria. Componente de Prevención y Control de Daños No Transmisibles. Sistema de Información HIS |
| Institución | Ministerio de Salud del Perú (MINSA) |
| Edición | 2.ª edición, mayo de 2025 |
| Extensión de la fuente | 58 páginas PDF |
| Tipo de contenido | Manual técnico de registro y codificación HIS para prevención y control de daños no transmisibles |
| Archivo fuente | `Manual de registro y codificacion consulta ambulatoria.pdf` |
| Método de extracción | Extracción de la capa textual del PDF con preservación de disposición; OCR español + inglés a 300 dpi para páginas de imagen sin capa textual (portada y contraportada). |
| Tratamiento de tablas | Tablas legibles estructuradas en Markdown cuando la extracción tabular fue fiable; el texto original por página se conserva como respaldo. |

## Criterios de uso para RAG

- Cada página está delimitada con un encabezado `Página N`, que permite recuperar y citar el origen.
- Se conserva la terminología, los códigos, las cifras, las edades, los criterios y los ejemplos del documento fuente.
- Las tablas normalizadas se incluyen en la sección de tablas de su página. En caso de discrepancia visual, prevalece la consulta del PDF original.
- No se han completado datos ausentes ni corregido silenciosamente posibles erratas del documento.
- La portada y la contraportada son páginas escaneadas; su texto se transcribe mediante OCR y puede contener errores puntuales.

---

## Página 1 — Portada (OCR)

```text
Manual de Registro y Codificación Y
en la Consulta Ambulatoria y iV
COMPONENTE bz
PREVENCIÓN y CONTROL
pe DANOS NO TRANSMISIBLES
S
| Sy A
Ml SISTEMA DE INFORMACIÓN HIS 2025
```

## Página 2

Catalogación hecha por la Biblioteca del Ministerio de Salud

  Manual de registro y codificación en la consulta ambulatoria: Componente de prevención y control de daños
  no transmisibles. Sistema de información HIS / Ministerio de Salud. Dirección General de Intervenciones
  Estratégicas en Salud Pública. Dirección de Prevención y Control de Enfermedades No Transmisibles, Raras y
  Huérfanas. Oficina General de Tecnologías de la Información. Oficina de Gestión de la Información-- Lima:
  Ministerio de Salud; 2025.
    59 p.; ilus.

  ENFERMEDADES NO TRANSMISIBLES / ATENCIÓN AMBULATORIA / ENFERMEDADES RARAS / ATENCIÓN
  INTEGRAL DE SALUD / SISTEMAS DE INFORMACIÓN / CLASIFICACIÓN INTERNACIONAL DE ENFERMEDADES /
  CODIFICACIÓN CLÍNICA / SISTEMA DE REGISTROS / SISTEMAS DE REGISTROS MÉDICOS COMPUTARIZADOS

Hecho el Depósito Legal en la Biblioteca Nacional del Perú N° 2025 – 05204

“Manual de Registro y Codificación en la Consulta Ambulatoria. Componente de Prevención y
Control de Daños No transmisibles. Sistema de Información HIS”

Ministerio de Salud. Dirección General de Intervenciones Estratégicas en Salud Pública. Dirección de
Prevención y Control de Enfermedades No Transmisibles, Raras y Huérfanas - Oficina General de
Tecnologías de la Información. Oficina de Gestión de la Información ( MINSA / DGIESP / DENOT-
OGTI/ OGEI)

Equipo de Trabajo DGIESP:
Percy Alberto Herrera Añazco, Director Ejecutivo de Prevención y Control de Enfermedades No
Transmisibles, Raras y Huérfanas
Percy Alberto Herrera Añazco, Responsable Nacional del Componente de Daños No transmisibles
Joycy Rojas Vilchez, Equipo Técnico del Componente de Prevención y Control de Daños No
Transmisibles
Pedro Ernesto Kikushima Alcántara, Equipo Técnico del Componente de Prevención y Control de Daños
No Transmisibles

Equipo de Trabajo de la Oficina de Gestión de la Información:
Luis Pedro Valeriano Arteaga, Jefe de Equipo de la Oficina Gestión de la Información
Marco Polo Bardales Espinoza, Equipo Técnico de la Oficina Gestión de la Información
Adhemir Reynel Bellido Delgado, Equipo Técnico de la Oficina Gestión de la Información

Diseño:
Lic. Julie Guillen Ramos, Equipo técnico de la Oficina de Gestión de la Información

© MINSA, Mayo, 2025

Ministerio de Salud
Av. Salaverry N° 801, Lima 11, Perú
Telf.: (51-1) 315-6600
www.gob.pe/minsa
webmaster@minsa.gob.pe

1ra. Edición, Febrero 2021
2da. Edición, Mayo 2025

Enlace digital: https://bvs.minsa.gob.pe/local/MINSA/7691.pdf

---

## Página 3

CÉSAR HENRY VÁSQUEZ SÁNCHEZ
          Ministro de Salud

       RICARDO PEÑA SÁNCHEZ
     Viceministro de Salud Pública

    HERBERTH ULISES CUBA GARCÍA
      Viceministro de Prestaciones
       y Aseguramiento en Salud

   MOISÉS IVÁN GUILLÉN CÁRDENAS
         Secretario General

         CRISTIAN DIAZ VÉLEZ
    Director General de la Dirección
       General de Intervenciones
     Estratégicas en Salud Pública

        JOSÉ ENRIQUE PÉREZ LU
     Director General de la Oficina
General de Tecnologías de la Información

---

## Página 4

PRESENTACIÓN
El Componente de Prevención y Control de Daños No Transmisibles, pertenece
a la Dirección de Prevención y Control de Enfermedades No Transmisibles,
Raras y Huérfanas (DENOT)-Dirección General de Intervenciones Estratégicas
en Salud Pública-DGIESP del Ministerio de Salud.
Las intervenciones para la prevención y control de enfermedades no
transmisibles se desarrollan en todo el curso de la vida, en niños, adolescentes,
jóvenes, adultos y adultos mayores, colocando en el centro a la persona y sus
múltiples enfermedades no transmisibles.
Además, son parte de las intervenciones estratégicas en las redes integrales
de salud a nivel nacional, promueven el acceso oportuno a través de la
telemedicina, y desarrollan acciones de tamizaje en poblaciones vulnerables,
en coordinación con los actores sociales y la participación de las asociaciones
de pacientes, las sociedades científicas y la cooperación internacional.
Este componente identifica y desarrolla intervenciones estratégicas con los
siguientes objetivos: a reducción de los factores de riesgo de las enfermedades
no transmisibles y la identificación precoz y el tratamiento oportuno y efectivo
de la obesidad, las enfermedades cardiovasculares, la diabetes mellitus y la
enfermedad renal crónica, controlando la enfermedad, así como evitando y
retrasando el inicio de complicaciones.

Asimismo, consideramos que el sistema de información en consulta
ambulatoria (HIS), es un sistema de información necesaria para la toma de
decisiones en la solución de problemas sanitarios relacionados al componente
ya que los datos generados se almacenan, se procesan y se interpretan para:
llevar un control de los servicios prestados a los usuarios, obtener estadísticas,
obtener datos epidemiológicos, elaborar perfiles y establecer los costos de la
atención prestada a cada paciente, etc.

En este contexto, esperamos que este Manual, basado en los documentos
normativos actualizados, sea una herramienta útil y de consulta permanente
por los profesionales de la salud y estadísticos que laboran en los
establecimientos de salud de los diferentes niveles de atención a nivel
nacional.

---

## Página 5

Tabla de Contenidos
COMPONENTE DE PREVENCIÓN Y CONTROL DE DAÑOS NO TRANSMISIBLES………………………………. 09
Actividades más frecuentes…………………………………………………………………………………………………………..… 09

INSTRUCCIONES PARA EL REGISTRO Y CODIFICACIÓN DE LAS ACTIVIDADES DE LA COMPONENTE
DE PREVENCIÓN Y CONTROL DE DAÑOS NO TRANSMISIBLES…………………………………………………….. 10
Atención de salud………………………………………………………………………………………………………………………….. 10

VALORACIÓN CLÍNICA Y TAMIZAJE LABORATORIAL DE ENFERMEDADES CRÓNICAS NO
TRANSMISIBLES – (PRODUCTO 3000015)…………………………………………………………………………………….. 11
   Valoración Clínica de Factores de Riesgo………………………………………………………………………………. 13
   Subproducto 5001508: Personas de 5 años a más con Valoración Clínica de Factores de
   Riesgo…………………………………………………………………………………………………………………………………... 13
   Valoración clínica en personas menores de edad……………………………………………………………………... 14
   Valoración clínica en personas mayores de edad hasta los 39 años……………………………………….…. 16
   Valoración clínica en personas de 40 años a más……………………………………………………………………... 18

   Subproducto 5001509 Tamizaje de laboratorio a Personas de 18 a 39 años con riesgo elevado.. 20
   Subproducto 5001510 Tamizaje de laboratorio a Personas de 40 años a más………………………… 20

  TRATAMIENTO Y CONTROL A PERSONAS CON DIAGNÓSTICO DE HIPERTENSIÓN ARTERIAL
 (PRODUCTO 3000016)………………………………………………………………….……………………………………………. 21
    Urgencia hipertensiva identificada en consultorio……………………………………………………………………. 22
    Emergencia hipertensiva detectada en consultorio………………………………………………………………….. 23

   Subproducto 5001608: Tratamiento y control de personas según clasificación de riesgo
   cardiovascular………………………………………………………………………………………………………………………. 24
   Registro de la medición del riesgo cardiovascular……………………………………………………………..……... 24
   Manejo del riesgo cardiovascular……………………………………………………………………………………………... 25

   Subproducto 5001609: Tratamiento para persona con hipertensión sin daño de órgano……… 26
   Controles de la presión arterial…………………………………………………………………………………………….. 27
   Consulta para tratamiento y evaluación del paciente hipertenso…………………………………………. 27

   Subproducto 5001606: Personas Hipertensas Con Tratamiento Especializado………………………. 28
   UPSS Cardiología/Medicina Interna/Medicina familiar……………………………………………………………... 29
   Manejo Integral Especializado………………………………………………………………………………………………….. 31
     UPSS Cardiología……………………………………………………………………………………………………………..…… 31
     UPSS Cirugía Cardiovascular……………………………………………………………………………….………………… 31
     UPSS Endocrinología…………………………………………………………………………………………….………….….. 32
     UPSS Nefrología…………………………………………………………………………………………………………….…….. 32
     UPSS Neurología………………………………………………………………………………………………………………….. 32
     UPSS Rehabilitación…………………………………………………………………………………………………………….. 32
   Registro de otros procedimientos en personas con hipertensión……………………………………………… 32

### Tablas estructuradas de la página

| Columna 1 | Columna 2 |
| --- | --- |
|  | 10 |
| Atención de salud………………………………………………………………………………………………………………………….. |  |
| VALORACIÓN CLÍNICA Y TAMIZAJE LABORATORIAL DE ENFERMEDADES CRÓNICAS NO | 1 |
|  | 1 |
| TRANSMISIBLES – (PRODUCTO 3000015)…………………………………………………………………………………….. |  |
| Valoración Clínica de Factores de Riesgo………………………………………………………………………………. | 13 |
| Subproducto 5001508: Personas de 5 años a más con Valoración Clínica de Factores de | 1 |
| Riesgo…………………………………………………………………………………………………………………………………... | 3 |
| Valoración clínica en personas menores de edad……………………………………………………………………... | 14 |
| Valoración clínica en personas mayores de edad hasta los 39 años……………………………………….…. | 16 |
| Valoración clínica en personas de 40 años a más……………………………………………………………………... | 18 |
| S ubproducto 5001509 Tamizaje de laboratorio a Personas de 18 a 39 años con riesgo elevado.. | 2 0 |
| Subproducto 5001510 Tamizaje de laboratorio a Personas de 40 años a más………………………… | 20 |

| S ubproducto 5001606: Personas Hipertensas Con Tratamiento Especializado………………………. | 2 8 |
| --- | --- |
| UPSS Cardiología/Medicina Interna/Medicina familiar……………………………………………………………... | 29 |
| Manejo Integral Especializado………………………………………………………………………………………………….. | 31 |
| UPSS Cardiología……………………………………………………………………………………………………………..…… | 31 |
| UPSS Cirugía Cardiovascular……………………………………………………………………………….………………… | 31 |
| UPSS Endocrinología…………………………………………………………………………………………….………….….. | 32 |
| UPSS Nefrología…………………………………………………………………………………………………………….…….. | 32 |
| UPSS Neurología………………………………………………………………………………………………………………….. |  |
|  | 32 |
| UPSS Rehabilitación…………………………………………………………………………………………………………….. |  |
|  | 32 |

---

## Página 6

Subproducto 5001605: Pacientes Con Enfermedad Cardiometabólica organizados que reciben
    educación para el control de la enfermedad…………………………………………………………………………. 34
    Registro de Sesión educativa con tema de prevención de Hipertensión…………………………………….. 34
    Registro de Sesión educativa con tema de prevención de Diabetes………………………………………….. 35
    Registro de Sesión Demostrativa con tema de prevención de Hipertensión……………………………… 35
    Registro de Sesión Demostrativa con tema de prevención de Diabetes……………………………………. 35
    Registro de Sesión de Grupo de Ayuda Mutua con tema de prevención de Hipertensión…………… 36
    Registro de Sesión de Grupo de Ayuda Mutua con tema de prevención de Diabetes…………………. 37

TRATAMIENTO Y CONTROL DE PERSONAS CON DIABETES ( PRODUCTO 3000017)…………………………. 37
    Registro de manejo básico de crisis hipoglucémica o hiperglucémica ………………………………………
                                                                                       37
    Subproducto 5001708: Tratamiento Para Personas Con Diabetes Mellitus Sin Daño De
    Órgano…………………………………………………………………………………………………………………………………. 38
    Tabla de códigos CIE10 correspondientes a Diabetes Mellitus según tipo de diabetes y tipo de
    complicaciones…………………………………………………………………………………………………………………………. 39
    Atención de seguimiento de la glicemia del paciente Diabético……………………………………………….. 40
    Registro de consulta para tratamiento y evaluación del paciente diabético……………………………… 41

    Subproducto 5001704: Pacientes Diabéticos Con Tratamiento Especializado………………………. 42
    Registro de consulta para tratamiento y evaluación del paciente diabético……………………………..
                                                                                           43
    Atención integral especializada según especialidades………………………………………………………………
                                                                                           44
       UPS Nefrología……………………………………………………………………………………………………………………..
                                                                                           44
       UPS Neurología…………………………………………………………………………………………………………………….. 46
       UPS Cardiología o cardiovascular………………………………………………………………………………………….. 46
       UPS Oftalmología……………………………………………..………………………………………………………….………. 47
    Pacientes en manejo especializado por otras comorbilidades ……………………………..…………………… 47

    Subproducto 5001705 valoración de complicaciones en personas con diabetes…………………... 48
    Registro para la indicación de despistaje de retinopatía diabética…………………………………………… 50

    Subproducto 5001707: Manejo De Enfermedad Renal Diabética…………………………………………. 51
    Pacientes con nefropatía diabética incipiente sin proteinuria………………………………………………….. 52

    Registro los servicios de teleorientación y telemonitoreo…………………………………………………….. 53

    Valoración Clínica y Tamizaje laboratorial de Enfermedades Crónicas No Transmisibles
    (Valoración Clínica De Factores De Riesgo)………………………………………………………………………….. 53
    Teleconsultante…………………………………………………………………………………………………………….………… 54
    Teleconsultor…………………………………………………………………………………………………………………………… 54
    Evaluación y entrega de Resultados a través de Telemonitoreo………………………………………………. 54

    Seguimiento de pacientes con diagnóstico de Hipertensión arterial a través de Telemedicina   55

    Seguimiento de pacientes con diagnóstico de Diabetes Mellitus a través de Telemedicina…. 56
    Registro de servicios de teleconsulta…………………………………………………………………….………….…. 58
    Registro de servicios de teleinterconsulta……………………………………………….…………………………… 58

---

## Página 7

COMPONENTE DE PREVENCIÓN Y CONTROL DE DAÑOS NO TRANSMISIBLES
                               Actividades más frecuentes

Código        Diagnóstico / Actividad                  Código       Diagnóstico / Actividad

E100        Diabetes Mellitus tipo 1 con coma           I209       Angina de pecho, no
                                                                   especificada
E101        Diabetes Mellitus con cetoacidosis          I64        Accidente cerebrovascular no
E110        Diabetes Mellitus tipo 2, con coma                     especificado como hemorragia o
E111        Diabetes Mellitus tipo 2, con cetoaci                  infarto
            dosis                                       N181       Enfermedad renal crónica etapa
                                                                   1
E112        Diabetes      Mellitus   tipo   2,   con    N182       Enfermedad renal crónica etapa
                                                                   2
            complicaciones renales                      N183       Enfermedad renal crónica etapa
                                                                   3
E113        Diabetes      Mellitus   tipo   2,   con    N184       Enfermedad renal crónica etapa
                                                                   4
            Complicaciones Oftálmicas                   N185       Enfermedad renal crónica etapa
                                                                   5
E114        Diabetes Mellitus tipo 2, con               R030       Lectura elevada de la presión
            complicaciones neurológicas                            sanguínea, sin diagnóstico de
E115        Diabetes Mellitus tipo 2,            con               hipertensión
            Complicaciones Circulatorias                R730       Prueba de tolerancia a la
                                                                   glucosa anormal
            Periféricas
E116        Diabetes Mellitus tipo 2, con otras         R739       Hiperglicemia, no especificada
            Complicaciones         Especificadas        99199.22   Tamizaje de la presión arterial
E117        Diabetes    Mellitus      tipo    2,        Z017       Examen de laboratorio
            con     Complicaciones     Múltiples        Z019       Valoración Clínica de Factores
                                                                   de Riesgo
E118        Diabetes Mellitus tipo 2, con
            complicaciones no especificadas             99199.23   Estratificación del riesgo
E119        Diabetes Mellitus tipo 2, sin                          cardiovascular global
            complicaciones                              Z720       Problemas relacionados con el
                                                                   uso de tabaco
E160        Hipoglicemia Inducida por fármacos
            sin coma                                    Z721       Problemas sociales relacionados
E162        Hipoglicemia, no especificada                          con el uso de alcohol
E65         Adiposidad localizada                       Z723       Problemas relacionados con la
                                                                   falta
E669        Obesidad                                               de ejercicio físico
E6691       Obesidad I                                  Z724       Problemas relacionados con la
                                                                   dieta
E6692       Obesidad II                                            inadecuada y hábitos
                                                                   alimenticios
E6693       Obesidad III                                Z833       Antecedente familiares de
E6690       Sobrepeso                                              diabetes mellitus
E782        Hiperlipidemia Mixta                        Z834       Antecedentes familiares de
E785        Hiperlipidemia no          especificada                otras

### Tablas estructuradas de la página

| Columna 1 | Columna 2 | Columna 3 | Columna 4 |
| --- | --- | --- | --- |
|  |  | Actividades más frecuentes |  |
| Código | Diagnóstico / Actividad | Código | Diagnóstico / Actividad |
| E100 | Diabetes Mellitus tipo 1 con coma | I209 | Angina de pecho, no |
|  |  |  | especificada |
| E101 | Diabetes Mellitus con cetoacidosis | I64 | Accidente cerebrovascular no |
| E110 | Diabetes Mellitus tipo 2, con coma |  | especificado como hemorragia o |
|  |  |  | infarto |
| E111 | Diabetes Mellitus tipo 2, con cetoaci |  |  |
|  | dosis | N181 | Enfermedad renal crónica etapa |
|  |  |  | 1 |
| E112 | Diabetes Mellitus tipo 2, con | N182 | Enfermedad renal crónica etapa |
|  |  |  | 2 |
|  | complicaciones renales | N183 | Enfermedad renal crónica etapa |
|  |  |  | 3 |
| E113 | Diabetes Mellitus tipo 2, con | N184 | Enfermedad renal crónica etapa |
|  |  |  | 4 |
|  | Complicaciones Oftálmicas | N185 | Enfermedad renal crónica etapa |
|  |  |  | 5 |
| E114 | Diabetes Mellitus tipo 2, con | R030 | Lectura elevada de la presión |
|  | complicaciones neurológicas |  | sanguínea, sin diagnóstico de |
|  |  |  | hipertensión |
| E115 | Diabetes Mellitus tipo 2, con |  |  |
|  | Complicaciones Circulatorias | R730 | Prueba de tolerancia a la |
|  |  |  | glucosa anormal |
|  | Periféricas |  |  |
| E116 | Diabetes Mellitus tipo 2, con otras | R739 | Hiperglicemia, no especificada |
|  | Complicaciones Especificadas | 99199.22 | Tamizaje de la presión arterial |
| E117 | Diabetes Mellitus tipo 2, | Z017 | Examen de laboratorio |
|  | con Complicaciones Múltiples | Z019 | Valoración Clínica de Factores |
|  |  |  | de Riesgo |
| E118 | Diabetes Mellitus tipo 2, con |  |  |
|  | complicaciones no especificadas | 99199.23 | Estratificación del riesgo |
| E119 | Diabetes Mellitus tipo 2, sin |  | cardiovascular global |
|  | complicaciones | Z720 | Problemas relacionados con el |
|  |  |  | uso de tabaco |
| E160 | Hipoglicemia Inducida por fármacos |  |  |
|  | sin coma | Z721 | Problemas sociales relacionados |
| E162 | Hipoglicemia, no especificada |  | con el uso de alcohol |
| E65 | Adiposidad localizada | Z723 | Problemas relacionados con la |
|  |  |  | falta |
| E669 | Obesidad |  | de ejercicio físico |
| E6691 | Obesidad I | Z724 | Problemas relacionados con la |
|  |  |  | dieta |
| E6692 | Obesidad II |  | inadecuada y hábitos |
|  |  |  | alimenticios |
| E6693 | Obesidad III | Z833 | Antecedente familiares de |
| E6690 | Sobrepeso |  | diabetes mellitus |
| E782 | Hiperlipidemia Mixta | Z834 | Antecedentes familiares de |
| E785 | Hiperlipidemia no especificada |  | otras |

---

## Página 8

enfermedades endocrinas,
                 (Dislipidemia)                                            nutricionales y metabólicas.
G632             Polineuropatía diabética                  93000           Electrocardiograma
H360             Retinopatía diabética                     99401.13        Consejería en estilos de vida
H420             Glaucoma en enfermedades                                  saludable
                 endocrinas                               C0009            Sesión educativa
I10              Hipertensión Esencial (Primaria)          C0010           Sesión demostrativa
I110             Enfermedad Cardíaca Hipertensiva          C0012           Sesión de ayuda mutua
                 con Insuficiencia Cardíaca               99499.09         Teleorientación síncrona
                 (Congestiva)                             99499.10         Telemonitoreo
I119             Enfermedad Cardíaca Hipertensiva          83036           Dosaje de Hemoglobina;
                 sin Insuficiencia                                         glucosilada (HBA1C)
                 Cardíaca (Congestiva)                      82947          Dosaje de glucosa
I499             Arritmia Cardíaca, no Especificada

           INSTRUCCIONES PARA EL REGISTRO Y CODIFICACIÓN DE LAS ACTIVIDADES
           DE LA COMPONENTE DE PREVENCIÓN Y CONTROL DE DAÑOS NO
           TRANSMISIBLES

        ✓ Este Componente desarrolla actividades de atenciones de salud, orientadas a la detección
          temprana, prevención primaria, tratamiento oportuno y manejo de las enfermedades no
          transmisibles priorizadas para el Componente de Prevención y Control de Daños No
          Transmisibles.
       ✓ El registro de los datos generales se hace siguiendo las indicaciones pertinentes y no
          presenta características especiales.

           A. ATENCIÓN DE SALUD

             Los ítems referidos al día, historia clínica, DNI, financiador, pertenencia étnica, distrito
             de procedencia, edad, sexo, establecimiento y servicio se registran siguiendo las
             indicaciones planteadas en los capítulos posteriores del presente Documento Técnico.

             En el ítem: Tipo de diagnóstico se debe tener en cuenta las siguientes consideraciones
             al momento de registrar: Marcar con un aspa (X)
             P: (Diagnóstico presuntivo) Únicamente cuando no existe certeza del diagnóstico y/o
                                         éste requiere de algún resultado de Laboratorio. Su carácter
                                         es provisional.

             D: (Diagnóstico definitivo) Cuando se tiene certeza del diagnóstico por evaluación clínica
                                          y/o por exámenes auxiliares y debe ser escrito una sola vez
                                          para el mismo evento (episodio de la enfermedad cuando se
                                          trate de enfermedades agudas y solo una vez para el caso
                                          de enfermedades crónicas) en un mismo paciente.

             R: (Diagnóstico repetido) Cuando el paciente vuelve a ser atendido para el seguimiento
                                        de un mismo episodio o evento de la enfermedad en
                                        cualquier otra oportunidad posterior a aquella en que
                                        estableció el diagnóstico definitivo.

### Tablas estructuradas de la página

| Columna 1 | Columna 2 | Columna 3 | Columna 4 |
| --- | --- | --- | --- |
|  |  |  | enfermedades endocrinas, |
|  | (Dislipidemia) |  | nutricionales y metabólicas. |
| G632 | Polineuropatía diabética | 93000 | Electrocardiograma |
| H360 | Retinopatía diabética | 99401.13 | Consejería en estilos de vida |
| H420 | Glaucoma en enfermedades |  | saludable |
|  | endocrinas | C0009 | Sesión educativa |
| I10 | Hipertensión Esencial (Primaria) | C0010 | Sesión demostrativa |
| I110 | Enfermedad Cardíaca Hipertensiva | C0012 | Sesión de ayuda mutua |
|  | con Insuficiencia Cardíaca | 99499.09 | Teleorientación síncrona |
|  | (Congestiva) |  |  |
|  |  | 99499.10 | Telemonitoreo |
| I119 | Enfermedad Cardíaca Hipertensiva | 83036 | Dosaje de Hemoglobina; |
|  | sin Insuficiencia |  | glucosilada (HBA1C) |
|  | Cardíaca (Congestiva) | 82947 | Dosaje de glucosa |
| I499 | Arritmia Cardíaca, no Especificada |  |  |

---

## Página 9

Si son más de tres (03) los diagnósticos y/o actividades los que se van a registrar, continúe
            en el siguiente registro y trace una línea oblicua entre los casilleros de los ítems día hasta
            servicio y utilice los siguientes tres (03) ítems del campo “diagnósticos y/o actividades”
            para completar el registro de la atención.

            Los ítems diagnóstico motivo de consulta, tipo de diagnóstico y Lab presentan algunas
            particularidades que se revisará en detalle a continuación.

VALORACIÓN CLÍNICA Y TAMIZAJE LABORATORIAL DE ENFERMEDADES CRÓNICAS NO
TRANSMISIBLES – (PRODUCTO 3000015)

                                                      Cartera de Servicios

                                                                                                 Unidad de
    Producto              Actividad                       Sub Producto                Trazador                    Categorías
                                                                                                  Medida

                                          5001508 Personas de 5 años a más con                    PERSONA
                                                                                         X                   I1   I2   I3   I4 II1
                                          valoración clínica de factores de riesgo.              EVALUADA
                     5000113 Evaluación
3000015 Valoración
                       Clínica Y Tamizaje
 Clínica Y Tamizaje                       5001509 Tamizaje de laboratorio a
                        Laboratorial De                                                           PERSONA
  Laboratorial De
                     Personas Con Riesgo Personas de 18 a 39 años con riesgo             X
                                                                                                 EVALUADA
                                                                                                             I1   I2   I3   I4 II1
   Enfermedades                           elevado.
                           De Padecer
    Crónicas No
                    Enfermedades Crónicas
   Transmisibles
                       No Transmisibles
                                          5001510 Tamizaje de laboratorio a                       PERSONA
                                                                                         X                   I1   I2   I3   I4 II1
                                          Personas de 40 años a más.                             EVALUADA

        Definición Operacional. - Conjunto de actividades dirigidas a la población general que se
        desarrollan en establecimientos de salud con población adscrita para la identificación de
        personas con factores de riesgo para diabetes e hipertensión arterial y diagnóstico
        temprano. Incluye la valoración clínica de factores de riesgo, tamizaje de la presión arterial
        y exámenes de laboratorio en población priorizada y consulta por profesional de la salud
        para la entrega de resultados y manejo. Se brinda en E.E.S.S de las categorías I-1, I-2, I-3, I-
        4 y II-1 con población adscrita, con enfoque de curso de vida desde los 5 años en adelante.

        El producto incluye: Valoración clínica inicial, indicación de tamizaje cuando se cumple con
        los criterios descritos y la lectura de resultados.
        ✔ La valoración clínica incluye cálculo del Índice de Masa Corporal (IMC), medición del
            perímetro abdominal, valoración de estilos de vida, factores de riesgo y cuando aplique
            toma de presión arterial. Se realiza a todas las personas que acudan al establecimiento
            de salud de manera rutinaria, en triaje o en consultorio por personal de salud
            capacitado.

        ✔ Junto a la valoración clínica y de factores de riesgo, se brinda intervención breve sobre
               estilos de vida saludables personalizada. Puede incluir: brindar información general
               para modificación de conductas, entrevista motivacional, reforzar hábitos saludables u
               otros que se consideren pertinentes.

        ✔ El tamizaje laboratorial incluye: dosaje de glucemia en plasma venoso y perfil lipídico
               (colesterol total, HDL, LDL calculado y triglicéridos), según corresponda al grupo de
               edad y valoración de riesgo. La entrega del servicio (producto) culmina con la lectura

### Tablas estructuradas de la página

| Producto | Actividad / subproducto | Trazador | Unidad de medida | Categorías |
| --- | --- | --- | --- | --- |
| 3000015 Valoración clínica y tamizaje laboratorial de enfermedades crónicas no transmisibles | 5000113 Evaluación clínica y tamizaje laboratorial de personas con riesgo de padecer enfermedades crónicas no transmisibles | X | PERSONA EVALUADA | I1, I2, I3, I4, II1 |
| 3000015 | 5001508 Personas de 5 años a más con valoración clínica de factores de riesgo | X | PERSONA EVALUADA | I1, I2, I3, I4, II1 |
| 3000015 | 5001509 Tamizaje de laboratorio a personas de 18 a 39 años con riesgo elevado | X | PERSONA EVALUADA | I1, I2, I3, I4, II1 |
| 3000015 | 5001510 Tamizaje de laboratorio a personas de 40 años a más | X | PERSONA EVALUADA | I1, I2, I3, I4, II1 |

---

## Página 10

de resultados.
       ✔ Se puede complementar a través de actividades extramurales y telemedicina.
       ✔ Se emplea aproximadamente 25 minutos en la consulta de valoración clínica.
       ✔ El personal que ejecuta la actividad: Equipo multidisciplinario.

       *Para las evaluaciones de triaje o en campañas de extramural, se recomienda usar
       formatos estructurados como FINDRISK ó una lista de chequeo con personal capacitado.
          ❖ Se considera a la persona evaluada con una Valoración de Riesgo Alterada cuando:
                                            Factores de Riesgo a evaluar
                 Indagar en la valoración anual la presencia de los siguientes factores de riesgo:
                 • Historia Familiar de Dislipidemia Familiar, enfermedad coronaria prematura
                    o Diabetes Mellitus en familiares de primer grado o segundo grado.
                 • Diagnóstico previo de Diabetes Mellitus, Examen previo de glucosa alterada,
                    Enfermedad Cardiovascular, Enfermedad Renal Crónica o Hipertensión
                    Arterial
                 • Obesidad (IMC igual o mayor a 30) o Sobrepeso.
                 • Perímetro abdominal (> 88 cm en mujeres y > 102 en varones)
                 • Sedentarismo
                 • Tabaquismo
                 En poblaciones específicas también indagar por:
                 • Preeclampsia
                 • Antecedentes de Diabetes Gestacional
                 • Menopausia precoz

                 Cuando se encuentren los siguientes signos o diagnósticos previos, también se
                 les debe considerar como factores que aumentan el riesgo y realizar el tamizaje
                 de laboratorio para ENT:
                 • Signos clínicos de resistencias a la insulina (acros cordones,
                     acantosis nigricans)
                 • Signos clínicos de Hipercolesterolemia familiar (arco corneal, xantelasmas o
                     xantomas)
                 • Diagnóstico previo de hipotiroidismo
                 • Diagnóstico previo de enfermedades autoinmunes (LES, AR)
                 • Diagnóstico previo de infección por VIH y/o Tuberculosis
                 • Síndrome de Ovario Poliquístico.

Valoración Clínica de Factores de Riesgo
Subproducto 5001508: Personas de 5 años a más con Valoración Clínica de Factores de Riesgo.

       Definición Operacional. - Conjunto de actividades realizadas por profesional de salud o
       personal de salud capacitado, para la identificación de población con factores de riesgo
       para diabetes, hipertensión o dislipidemia en personas de 5 años a más.
       Incluye:
               a) cálculo del índice de masa corporal (IMC)
              b) medición del perímetro abdominal
              c) valoración de estilos de vida
              d) medición de presión arterial en mayores de 18 años
              e) Consejería en estilos de vida saludable

---

## Página 11

f) Identificar factores de riesgo no modificables priorizados
      e) Indagar por otros factores de riesgo

En caso tener diagnóstico previo o encontrar el diagnóstico durante la intervención de una
enfermedad no transmisible como hipertensión y diabetes, deben ser derivados para
manejo por el equipo multidisciplinario según pautas de productos, vías de abordaje HEARTS
y otros documentos normativos vigentes.

La evaluación del índice de masa corporal se realiza según la edad:
                       • En personas de 5 a 17 años se usarán las tablas de IMC para la
                          edad

                   CIE10            Punto de Corte                       Clasificación
                   E669               97 percentil                         Obesidad
                   E6690             > 85 percentil                        Sobrepeso
                                   >Percentil 3 <85                          Normal
                                      Percentil
                                        Fuente: RM 1120-2017/MINSA. GT para la
                              identificación, tamizaje y manejo de factores de riesgo
                                  cardiovasculares y de diabetes mellitus tipo 2.

                        •    En personas de 18 a 60 años según tabla estandarizada para
                             adultos

                     Evaluación del Índice de Masa Corporal (IMC) en
                                     personas adultas
                     Código                Punto De Corte (IMC)                         Clasificación
                   -------                           18.5<28                            Peso Normal

                   E6690                            25 a < 30                            Sobrepeso

                   E6691                            30 a < 35                            Obesidad I

                   E6692                            35 a < 40                           Obesidad II
                   E6693                              ≥ a 40                            Obesidad III

               Fuente: Adaptado de la OMS, 1995. El estado físico: Uso e interpretación de la
               Antropometría. Informe del Comité de Expertos de la OMS, Serie de Informes técnicos
               854, Ginebra, Suiza.

                        •    En personas de 60 a más según tabla estandarizada para adultos
                             mayores

                       Clasificación de la Valoración Nutricional de las Personas Adultas
                       Mayores según Índice de Masa Corporal (IMC)
                                IMC                          Clasificación                              CIE10
                               ≤ 23,0                               Delgadez                            E46X
                             >23 a < 28                              Normal
                             ≥ 28 a < 32                           Sobrepeso                            E6690

                                 ≥ 32                               Obesidad                            E669

### Tablas estructuradas de la página

| Columna 1 | Columna 2 | Columna 3 |
| --- | --- | --- |
|  | Evaluación del Índice de Masa Corporal (IMC) en |  |
|  | personas adultas |  |
| Código | Punto De Corte (IMC) | Clasificación |
| ------- | 18.5<28 | Peso Normal |
| E6690 | 25 a < 30 | Sobrepeso |
| E6691 | 30 a < 35 | Obesidad I |
| E6692 | 35 a < 40 | Obesidad II |
| E6693 | ≥ a 40 | Obesidad III |

---

## Página 12

Fuente: Organización Panamericana de la Salud (OPS). Guía Clínica para Atención Primaria a las
                                                             Personas Adultas Mayores. Módulo 5. Valoración Nutricional del Adulto Mayor Washington, DC 2002.

                                No es necesaria una codificación para las personas que tienen peso normal.

                Valoración clínica en personas menores de edad:

                Para las personas entre los 5 a 17 años, no es obligatoria la toma de la presión arterial.

                 Para este grupo poblacional no se recomienda tomar muestras para tamizaje de
                 laboratorio sistemáticamente. Indicar el tamizaje de forma individualizada, con toma de
                 decisiones conjunta en consulta médica para la población con más de un factor de riesgo
                 identificado.

                                         ➢ Cuando no se identifican factores de riesgo

                                 En el ítem peso, talla y perímetro abdominal registrar en valores
                                 numéricos, peso(kg), talla(cm) y Pab(cm).

                                 En el ítem Diagnóstico motivo de consulta y/o actividad de salud
                                 anote:
                                 • En el 1º casillero Valoración Clínica de Factores de Riesgo (Examen especial no
                                   especificado Z019)
                                 • En el 2º casillero Consejería en estilos de vida saludable (99401.13)

                                 En el ítem Tipo de diagnóstico
                                 • En el 1º, y 2º casilleros marque “D” de diagnóstico definitivo.

               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION   ESTA- SER-                                                  TIPO DE          VALOR
                              FINANC.                                             CEFALICO-                                 DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                 CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRICA BLEC VICIO                                               DIAGNÓSTICO          LAB
                                                                                                                                        Y ACTIVIDADES DE SALUD                                           CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL      HEMOGLOBINA                                                             P    D R      1º      2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                  FECHA DE ULTIMA REGLA: ____/____/______

             85274136
                                 2            Huancayo              A    M
                                                                                PC                PESO     30      N    N 1. Examen especial NE (Valoración Clínica de FR)   P   D   R                     Z019

               45320                                        9     M            Pab                TALLA    135     C    C   2. Consejería en estilos de vida saludable       P   D   R                   99401.13
                                40                                       F
                                                                    D          Ppreg               Hb              R    R   3.                                               P   D   R

               •        No se necesita colocar código que indique IMC Normal.
               •        Es importante el registro de la variable de pertenencia étnica en el HIS

               ➢        Cuando se identifican factores de riesgo
               En el ítem peso, talla y perímetro abdominal registrar en valores numéricos,
               peso(kg), talla(cm) y P. ab(cm).

                  En el ítem Diagnóstico motivo de consulta y/o actividad de salud anote:
                • En el 1º casillero Valoración Clínica de Factores de Riesgo (Examen especial no
                  especificado Z019) registrando en la casilla de LAB el código ALT (alterado)

---

## Página 13

• En el 2º casillero cuando esté presente, registrar cualquiera de los diagnósticos
                    siguientes (máximo 2 en caso de identificar más de uno):
                     - Adiposidad localizada(E65)
                     - Obesidad (E669)
                     - Obesidad I(E6691)
                     - Obesidad II (E6692)
                     - Obesidad III (EE693)
                     - Sobrepeso(E6690)
                     - Problemas relacionados con el uso de tabaco (Z720)
                     - Problemas sociales relacionados con el uso de alcohol (Z721).
                     - Problemas relacionados con la falta de ejercicio físico (Z723)
                     - Problemas relacionados con la dieta inadecuada y hábitos alimenticios(Z724)
                     - Antecedente familiares de diabetes (Z833)
                     - Antecedentes familiares de otras enfermedades crónicas, nutricionales y
                       metabólicas(Z834)

                  • En el 3º casillero examen de laboratorio(Z017) si el personal médico a cargo de la
                    atención lo ha considerado necesario
                  • En el 4 º casillero la consejería en estilos de vida saludable (99401.13)

                  En el ítem Tipo de diagnóstico anote:
                  • En el 1º, 2º, 3º y 4º casilleros corresponden “D” de diagnóstico definitivo.

               D.N.I.                           DISTRITO DE                               PERIM ETRO         EVALUACION   ESTA- SER-                                                  TIPO DE                            VALOR
                              FINANC.                                                      CEFALICO-                                 DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                                         CÓDIGO
 DIA      HISTORIA CLINICA                     PROCEDENCIA         EDAD       SEXO      ABDOM INAL -PESO   ANTROPOMETRICA BLEC VICIO                                               DIAGNÓSTICO                            LAB
                                                                                                                                                 Y ACTIVIDADES DE SALUD                                                                   CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                             PREGESTACIONAL      HEMOGLOBINA                                                             P    D R                        1º      2º 3º
NOMBRES Y APELLIDOS PACIENTE:
         (*)FECHA DE NACIMIENTO: _____/____/______               FECHA ULTIMO RESULTADO DE Hb: _____/____/______                               FECHA DE ULTIMA REGLA: ____/____/______

               85274136
                                    2                Paras                A       M
                                                                                           PC              PESO         30         N       N 1. Examen especial NE (Valoración Clínica de FR)       P   D   R   ALT                         Z019

                 45320                                            9       M                Pab             TALLA        135        C       C   2. Sobrepeso                                         P   D   R                              E6690
                                   58                                             F
                                                                          D             Ppreg               Hb                     R       R   3. Examen de laboratorio                             P   D   R                               Z017
NOMBRES Y APELLIDOS PACIENTE:
         (*)FECHA DE NACIMIENTO: _____/____/______               FECHA ULTIMO RESULTADO DE Hb: _____/____/______                               FECHA DE ULTIMA REGLA: ____/____/______

                                                                          A       M
                                                                                           PC              PESO                    N       N 1. Consejería en estilos de vida saludable             P   D   R                             99401.13

                                                                          M                Pab             TALLA                   C       C   2.                                                   P   D   R
                                                                                  F
                                                                          D             Ppreg               Hb                     R       R   3.                                                   P   D   R

                  ✓ Cuando se identifican factores de riesgo para enfermedades no transmisibles no
                    incluida en la lista de condiciones a registrar, como por ejemplo cuando la persona
                    reporta un diagnóstico previo de lupus eritematoso sistémico (LES)
                    Registrar en código Z019 y en el casillero de LAB “Alt”

                  D.N.I.                           DISTRITO DE                                 PERIM ETRO         EVALUACION   ESTA- SER-                                                  TIPO DE                             VALOR
                                 FINANC.                                                        CEFALICO-                                 DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                                       CÓDIGO
       DIA   HISTORIA CLINICA                     PROCEDENCIA         EDAD            SEXO   ABDOM INAL -PESO   ANTROPOMETRICA BLEC VICIO                                               DIAGNÓSTICO                             LAB
                                                                                                                                                      Y ACTIVIDADES DE SALUD                                                                 CIE/CPMSS
           GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                               PREGESTACIONAL      HEMOGLOBINA                                                             P    D R                        1º       2º 3º
   NOMBRES Y APELLIDOS PACIENTE:
   NOMBRES Y APELLIDOS PACIENTE:
             (*)FECHA DE NACIMIENTO: _____/____/______              FECHA ULTIMO RESULTADO DE Hb: _____/____/______                                 FECHA DE ULTIMA REGLA: ____/____/______

                   85274136
                                        2                Paras                A        M
                                                                                                 PC             PESO          37       N       N 1. Examen especial NE (Valoración Clínica de FR)       P   D   R        ALT                   Z019

                    45320                                             9       M                 Pab             TALLA        140       C       C    2. Examen de laboratorio                            P   D   R                              Z017
                                        58                                             F
                                                                              D              Ppreg               Hb                    R       R    3. Consejería en estilos de vida saludable          P   D   R                           99401.13
   NOMBRES Y APELLIDOS PACIENTE:
             (*)FECHA DE NACIMIENTO: _____/____/______              FECHA ULTIMO RESULTADO DE Hb: _____/____/______                                 FECHA DE ULTIMA REGLA: ____/____/______

                                                                              A        M
                                                                                                 PC             PESO                   N       N 1.                                                     P   D   R

                                                                              M                 Pab             TALLA                  C       C    2.                                                  P   D   R
                                                                                       F
                                                                              D              Ppreg               Hb                    R       R    3.                                                  P   D   R

---

## Página 14

Para esta población cuando hay dos o más factores de riesgo se debe evaluar la necesidad de
                           tamizaje de laboratorio, con toma de decisiones conjunta en consulta médica.

                Valoración clínica en personas mayores de edad hasta los 39 años:

                En este grupo poblacional, si se encuentra un factor de riesgo, está indicado el realizar un
                tamizaje de laboratorio para enfermedades no transmisibles. (Corresponde con el
                subproducto 5001509 Tamizaje de laboratorio a Personas de 18 a 39 años con riesgo
                elevado.)

                Cuando no se identifican factores de riesgo

                En el ítem Diagnóstico motivo de consulta y/o actividad de salud anote:
                • En el 1º casillero Z019 Examen especial no especificado (Valoración Clínica de Factores
                  de Riesgo)
                • En el 2º casillero el Tamizaje de la Presión arterial (99199.22)
                • En el 3° casillero la consejería en estilos de vida saludable (99401.13).

                En el ítem Tipo de Diagnóstico
                • Usar el tipo de diagnóstico “D” de diagnóstico definitivo.

                En el ítem Lab anote:
                • En el 2º casillero registrar valor de presión arterial.
                  En la primera columna registrar el valor de la presión arterial sistólica.
                  En la segunda columna registrar el valor de la presión arterial diastólica.

               D.N.I.                        DISTRITO DE                               PERIM ETRO         EVALUACION   ESTA- SER-                                                  TIPO DE        VALOR
                              FINANC.                                                   CEFALICO-                                 DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                               CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA            EDAD       SEXO   ABDOM INAL -PESO
                                                                                                        ANTROPOMETRICA BLEC VICIO                                               DIAGNÓSTICO        LAB
                                                                                                                                              Y ACTIVIDADES DE SALUD                                         CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                             PREGESTACIONAL      HEMOGLOBINA                                                             P    D R      1º    2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______                 FECHA ULTIMO RESULTADO DE Hb: _____/____/______                  FECHA DE ULTIMA REGLA: ____/____/______

             12345678
                                 2      San Juan de Miraflores            A    M
                                                                                      PC                PESO     60      N    N 1. Examen especial NE (Valoración Clínica de FR)   P   D   R                   Z019

               1234                                               20 M               Pab       80       TALLA    165     C    C   2. Tamizaje de la presión arterial               P   D   R   120   80      99199.22
                                58                                             F
                                                                          D          Ppreg               Hb              R    R   3. Consejería en estilos de vida saludable       P   D   R                 99401.13

                      Registrar evaluación de presión arterial en pacientes sin antecedentes de hipertensión arterial
                      confirmada o que no estén tomando medicamentos antihipertensivos.
                       No  es necesario
                        tomando         colocar
                                medicamentos       código que indique IMC normal.
                                             antihipertensivos.

                ➢                Cuando se identifican factores de riesgo

                En el ítem Diagnóstico motivo de consulta y/o actividad de salud anote:

---

## Página 15

• En el 1º casillero Z019 Examen especial no especificado (Valoración Clínica de Factores
                 de Riesgo)

                  Registrar el en el casillero LAB que se encuentra alterado ALT
                • En el 2º casillero cuando esté presente, registrar cualquiera de los diagnósticos
                  siguientes:
                  − Adiposidad localizada(E65)
                  − Obesidad (E669)
                  − Obesidad(E6691)
                  − Obesidad (E6692)
                  − Obesidad (EE693)
                  − Sobrepeso(E6690)
                  − Problemas relacionados con el uso de tabaco(Z720).
                  − Problemas sociales relacionados con el uso de alcohol (Z721).
                  − Problemas relacionados con la falta de ejercicio físico (Z723).
                  − Problemas relacionados con la dieta inadecuada y hábitos alimenticios(Z724)
                  − Antecedente familiares de diabetes (Z833)
                  − Antecedentes familiares de otras enfermedades crónicas, nutricionales y
                      metabólicas(Z834).

               • En el 3º casillero el examen de laboratorio(Z017).
               • En el 4º casillero el Tamizaje de la presión arterial (99199.22)

               En el item Lab registrar el valor de presión arterial.
                En la primera columna colocar el valor de la presión arterial sistólica.
                En la segunda columna colocar el valor de la presión arterial diastólica.

                • En el 5º casillero la Consejería en estilos de vida saludable (99401.13)

               En el ítem Tipo de Diagnóstico marcar “D” de diagnóstico definitivo.
               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION   ESTA- SER-                                                  TIPO DE           VALOR
                              FINANC.                                             CEFALICO-                                 DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                  CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRICA BLEC VICIO                                               DIAGNÓSTICO           LAB
                                                                                                                                        Y ACTIVIDADES DE SALUD                                            CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL      HEMOGLOBINA                                                             P    D R      1º       2º 3º
NOMBRES Y APELLIDOS PACIENTE:

       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                  FECHA DE ULTIMA REGLA: ____/____/______

             12345678                                               A           PC                PESO     82      N    N 1. Examen especial NE (Valoración Clínica de FR)   P   D   R   ALT                Z019
                                 2             Huaráz                    M
               1234                                         48 M               Pab      105       TALLA    163     C    C   2. Obesidad                                      P   D   R                      E669
                                58                                       F
                                                                    D          Ppreg               Hb              R    R   3. Examen de laboratorio                         P   D   R                      Z017
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                  FECHA DE ULTIMA REGLA: ____/____/______
                                                                  A      M      PC                PESO             N    N 1. Tamizaje de la presión arterial                 P   D   R   120     80       99199.22
                                                                  M            Pab                TALLA            C    C 2. Consejería en estilos de vida saludable         P   D   R                    99401.13
                                                                    D    F     Ppreg               Hb              R    R   3.                                               P   D   R

                ✓ Cuando se identifican factores de riesgo sin un código identificado en el CIE10
                Es suficiente registrar que la valoración clínica Z019, se registre el LAB de alterado “ALT”

### Tablas estructuradas de la página

| Columna 1 | Columna 2 |
| --- | --- |
| • En el 2º casillero cuando esté presente, registrar cualquiera de los diagnósticos |  |
| siguientes: |  |
| − | Adiposidad localizada(E65) |
| − | Obesidad (E669) |
| − | Obesidad(E6691) |
| − | Obesidad (E6692) |
| − | Obesidad (EE693) |
| − | Sobrepeso(E6690) |
| − | Problemas relacionados con el uso de tabaco(Z720). |
| − | Problemas sociales relacionados con el uso de alcohol (Z721). |
| − | Problemas relacionados con la falta de ejercicio físico (Z723). |
| − | Problemas relacionados con la dieta inadecuada y hábitos alimenticios(Z724) |
| − | Antecedente familiares de diabetes (Z833) |
| − | Antecedentes familiares de otras enfermedades crónicas, nutricionales y |
|  | metabólicas(Z834). |

---

## Página 16

D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION   ESTA- SER-                                                  TIPO DE           VALOR
                              FINANC.                                             CEFALICO-                                 DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                  CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRICA BLEC VICIO                                               DIAGNÓSTICO           LAB
                                                                                                                                        Y ACTIVIDADES DE SALUD                                            CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL      HEMOGLOBINA                                                             P    D R      1º       2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                  FECHA DE ULTIMA REGLA: ____/____/______
             12345678                                               A           PC                PESO     67      N    N 1. Examen especial NE (Valoración Clínica de FR)   P   D   R   ALT                Z019
                                 2             Huaráz                    M
               1234                                         49 M               Pab       82       TALLA    169     C    C   2. Examen de laboratorio                         P   D   R                      Z017
                                58                                  D    F     Ppreg               Hb              R    R   3. Tamizaje de la presión arterial               P   D   R   120     80       99199.22
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                  FECHA DE ULTIMA REGLA: ____/____/______
                                                                  A      M  PC               PESO                  N    N 1. Consejería en estilos de vida saludable         P   D   R                    99401.13
                                                                  M            Pab                TALLA            C    C   2.                                               P   D   R
                                                                         F
                                                                    D          Ppreg               Hb              R    R   3.                                               P   D   R

                Valoración clínica en personas de 40 años a más:
                Se recomienda que la valoración clínica sea de forma anual, evaluando cambios en el nivel de riesgo
                individual como aparición de nuevos factores de riesgo. En esta población corresponde
                complementar la actividad con el subproducto 5001510 Tamizaje de laboratorio a Personas de 40
                años a más.

                En personas de 40 años o más se debe iniciar el tamizaje de laboratorio aun cuando no hay
                otros factores de riesgo identificados, y la periodicidad de la próxima toma de muestra
                puede ser variable según el nivel de riesgo:
                  • Sin factores de riesgo: se puede repetir el laboratorio hasta dentro de los próximos 3
                     años
                  • En caso de encontrar factores de riesgo asociados: se recomienda que los controles
                     sean más seguidos de manera anual, o incluso en los casos de mayor riesgo se puede
                     repetir la prueba a los 6 meses según criterio médico.

                ❖               Cuando no se identifican factores de riesgo
                                En el ítem perímetro abdominal, peso y talla,
                                registrar en valores numéricos el peso(kg), talla(cm)
                                y perímetro abdominal (cm)
                                En el ítem: Diagnóstico motivo de consulta y/o
                                actividad de salud anote:
                                • En el 1º casillero Valoración Clínica de Factores de Riesgo (Examen especial no
                                   especificado Z019).
                                • En el 2º casillero cuando se indique según plan de salud individual, el examen de
                                   laboratorio(Z017).

                                • En el 3º casillero Tamizaje de la presión arterial (99199.22) En el ítem Lab registre
                                   el resultado de presión arterial:
                                En la primera columna colocar el valor de la presión arterial sistólica.
                                En la segunda columna colocar el valor de la presión arterial diastólica
                                •       En el 4º Consejería integral (99401.13)

                                •                  Para el ítem: Tipo de diagnóstico siempre es “D” de diagnóstico definitivo.

---

## Página 17

*En casos en los que el riesgo evaluado ha sido bajo, no es necesario registrar cada
                        año el código Z017, sólo registrarlo cuando corresponde según plan de seguimiento
                        (cada 3 años como mínimo)
               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION   ESTA- SER-                                                  TIPO DE        VALOR
                              FINANC.                                             CEFALICO-                                 DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                 CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO   ANTROPOMETRICA BLEC VICIO                                               DIAGNÓSTICO        LAB
                                                                                                                                        Y ACTIVIDADES DE SALUD                                           CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL      HEMOGLOBINA                                                             P    D R      1º    2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                  FECHA DE ULTIMA REGLA: ____/____/______

             12345678
                                 2             Camaná               A    M
                                                                                PC                PESO     60      N    N 1. Examen especial NE (Valoración Clínica de FR)   P   D   R                     Z019

               1234                                         68 M               Pab       95       TALLA    164     C    C   2. Tamizaje de la presión arterial               P   D   R   120   80        99199.22
                                58                                       F
                                                                    D          Ppreg               Hb              R    R   3. Examen de laboratorio                         P   D   R                     Z017
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                  FECHA DE ULTIMA REGLA: ____/____/______

                                                                    A    M
                                                                                PC                PESO             N    N 1. Consejería en estilos de vida saludable         P   D   R                   99401.13

                                                                  M            Pab                TALLA            C    C   2.                                               P   D   R
                                                                         F
                                                                    D          Ppreg               Hb              R    R   3.                                               P   D   R

       ❖       Cuando se identifican factores de riesgo
       En el ítem Diagnóstico motivo de consulta y/o actividad de salud registrar
       • En el 1º casillero Valoración Clínica de Factores de Riesgo (Examen especial no especificado
         Z019).
         En el campo LAB colocar ALT
       • En el 2º casillero anote los factores de riesgo identificados:
          − Adiposidad localizada(E65)
          − Obesidad (E669)
          − Obesidad(E6691)
          − Obesidad (E6692)
          − Obesidad (EE693)
          − Sobrepeso(E6690)
          − Problemas relacionados con el uso de tabaco(Z720).
          − Problemas sociales relacionados con el uso de alcohol (Z721).
          − Problemas relacionados con la falta de ejercicio físico (Z723).
          − Problemas relacionados con la dieta inadecuada y hábitos alimenticios(Z724)
          − Antecedente familiares de diabetes (Z833)
          − Antecedentes familiares de otras enfermedades crónicas, nutricionales y
               metabólicas(Z834).

       • En el 3º casillero anote Examen de laboratorio(Z017).
       • En el 4º casillero anote Tamizaje de la presión arterial (99199.22). Registrar el campo Lab
         En la primera columna colocar el valor de la presión arterial sistólica.
         En la segunda columna colocar el valor de la presión arterial diastólica
       • En el 5º Consejería integral (99401.13).

---

## Página 18

D.N.I.                                                                    PERIM ETRO          EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                                FINANC. DISTRITO DE PROCEDENCIA                           CEFALICO-                                 DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                           CÓDIGO
 DIA      HISTORIA CLINICA                                          EDAD        SEXO   ABDOM INAL -PESO    ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                Y ACTIVIDADES DE SALUD                                                     CIE/CPMSS
         GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                              PREGESTACIONAL      A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:

       (*)FECHA DE NACIMIENTO: _____/____/______                  FECHA ULTIMO RESULTADO DE Hb: _____/____/______                          FECHA DE ULTIMA REGLA: ____/____/______

             12345678                                                      A            PC                 PESO     82     N       N 1. Examen especial NE (Valoración Clínica de FR)       P       D       R ALT            Z019
                                   2            Huaráz                           M
               1234                                                48 M                Pab      105        TALLA    163    C       C       2. Obesidad                                      P       D       R                E669
                                  58                                             F
                                                                           D           Ppreg                Hb             R       R       3. Examen de laboratorio                         P       D       R                Z017
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______                  FECHA ULTIMO RESULTADO DE Hb: _____/____/______                          FECHA DE ULTIMA REGLA: ____/____/______
                                                                         A       M      PC                 PESO            N       N 1. Tamizaje de la presión arterial                     P       D       R 120 80       99199.22
                                                                         M             Pab                 TALLA           C       C 2. Consejería en estilos de vida saludable             P       D       R              99401.13
                                                                           D     F     Ppreg                Hb             R       R       3.                                               P       D       R

               Para el ítem Tipo de diagnóstico marque “D” de diagnóstico definitivo.
               ✓ Cuando se identifican factores de riesgo sin un código identificado en el CIE10
               En el ítem LAB
                   •         En el primer casillero colocar ALT.

               D.N.I.                                                                     PERIM ETRO          EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC. DISTRITO DE PROCEDENCIA                              CEFALICO-                                 DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                            CÓDIGO
 DIA      HISTORIA CLINICA                                           EDAD       SEXO    ABDOM INAL -PESO
                                                                                                            ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                 Y ACTIVIDADES DE SALUD                                                      CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                                PREGESTACIONAL      A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______                  FECHA ULTIMO RESULTADO DE Hb: _____/____/______                           FECHA DE ULTIMA REGLA: ____/____/______
             12345678                                                       A            PC                 PESO     67        N       N 1. Examen especial NE (Valoración Clínica de FR)       P       D       R ALT          Z019
                                   2               Huaráz                        M
               1234                                                 49 M                Pab       82        TALLA    169       C       C    2. Examen de laboratorio                            P       D       R              Z017
                                  58                                        D     F    Ppreg                 Hb                R       R    3. Tamizaje de la presión arterial                  P       D       R 120 80     99199.22
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______                  FECHA ULTIMO RESULTADO DE Hb: _____/____/______                           FECHA DE ULTIMA REGLA: ____/____/______
                                                                         A       M PC              PESO                        N       N 1. Consejería en estilos de vida saludable             P       D       R            99401.13
                                                                           M            Pab                 TALLA              C       C    2.                                                  P       D       R
                                                                                  F
                                                                            D          Ppreg                 Hb                R       R    3.                                                  P       D       R

Registro de entrega de resultados de laboratorio
Subproducto 5001509 Tamizaje de laboratorio a Personas de 18 a 39 años con riesgo elevado.
Subproducto 5001510 Tamizaje de laboratorio a Personas de 40 años a más.

               El tamizaje de laboratorio se registra durante la consulta de seguimiento para la lectura de
               resultados. Si no se hace la lectura de resultados no se considera que el subproducto ha
               sido entregado. El modelo aplica para todas las edades, incluso de 5 a 17 años.

               La entrega de resultados se puede realizar de forma presencial como intra o extramural, o
               mediante telemonitoreo.
               En la primera casilla registre:
               • En la consulta de seguimiento para la Valoración Clínica de Factores de Riesgo (Examen
                 especial no especificado Z019), con tipo de diagnóstico R de repetitivo
               • Luego registre los resultados de las pruebas realizadas:
               Siempre realizar por lo menos una evaluación de glucosa en ayunas y colesterol:
       -       *Glucosa en sangre (82947) ó Glucosa en tira reactiva (82948)
       -       Colesterol Total (82465)
               Si se realizaron las pruebas de colesterol LDL y triglicéridos, también registrarlas
       -       Colesterol LDL (83721)
       -       Triglicéridos (84478)
               Para todas las pruebas de laboratorio se coloca diagnóstico D de definitivo y se registra el

---

## Página 19

valor obtenido en números en el campo LAB.

                Ejemplo de registro de personas de 18 a 39 años con riesgo elevado:
                Con lectura de resultado de laboratorio

               D.N.I.                                                                    PERIM ETRO          EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                                FINANC. DISTRITO DE PROCEDENCIA                           CEFALICO-                                 DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                               CÓDIGO
  DIA     HISTORIA CLINICA                                          EDAD       SEXO    ABDOM INAL -PESO    ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                Y ACTIVIDADES DE SALUD                                                         CIE/CPMSS
         GESTANTE/PUERPERA       ETNIA      CENTRO POBLADO                             PREGESTACIONAL      A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:

        (*)FECHA DE NACIMIENTO: _____/____/______                 FECHA ULTIMO RESULTADO DE Hb: _____/____/______                    FECHA DE ULTIMA REGLA: ____/____/______

              12345678                                                     A              PC               PESO     65      N    N 1. Examen especial NE (Valoración Clínica de FR)       P     D       R ALT                      Z019
                                   2                Paras                        M
                1234                                               27 M                   Pab    90        TALLA   164      C    C   2. Glucosa                                           P     D       R 110                      82947
                                   58                                      D     F     Ppreg                Hb              R    R   3. Colesterol LDL                                    P     D       R 200                      83721
NOMBRES Y APELLIDOS PACIENTE:

        (*)FECHA DE NACIMIENTO: _____/____/______                 FECHA ULTIMO RESULTADO DE Hb: _____/____/______                    FECHA DE ULTIMA REGLA: ____/____/______

                                                                           A              PC               PESO             N    N 1. Colesterol Total                                    P     D       R 250                      82465
                                                                                 M
                                                                          M               Pab              TALLA            C    C   2. Triglicéridos                                     P     D       R 185                      84478

                                                                           D     F     Ppreg                Hb              R    R   3.                                                   P     D       R

                Ejemplo de registro de personas de 40 años a más con riesgo elevado:
                Con lectura de resultado de laboratorio
               D.N.I.                         DISTRITO DE                               PERIM ETRO          EVALUACION   ESTA- SER-                                                  TIPO DE                      VALOR
                                FINANC.                                                  CEFALICO-                                  DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                               CÓDIGO
 DIA      HISTORIA CLINICA                   PROCEDENCIA           EDAD        SEXO   ABDOM INAL -PESO    ANTROPOMETRICA BLEC VICIO                                               DIAGNÓSTICO                      LAB
                                                                                                                                                Y ACTIVIDADES DE SALUD                                                         CIE/CPMSS
         GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                             PREGESTACIONAL       HEMOGLOBINA                                                             P    D R                 1º       2º 3º
NOMBRES Y APELLIDOS PACIENTE:

        (*)FECHA DE NACIMIENTO: _____/____/______             FECHA ULTIMO RESULTADO DE Hb: _____/____/______                        FECHA DE ULTIMA REGLA: ____/____/______

              12345678                                                    A            PC                 PESO     70       N   N 1. Examen especial NE (Valoración Clínica de FR)    P       D     R                              Z019
                                   2                Paras                       M
                1234                                              52 M                Pab       91        TALLA    166      C   C    2. Glucosa                                       P       D     R       105                    82947
                                  58                                      D     F     Ppreg                Hb               R   R    3. Colesterol LDL                                P       D     R       140                    83721
NOMBRES Y APELLIDOS PACIENTE:

        (*)FECHA DE NACIMIENTO: _____/____/______             FECHA ULTIMO RESULTADO DE Hb: _____/____/______                        FECHA DE ULTIMA REGLA: ____/____/______

                                                                          A            PC                 PESO              N   N 1. Colesterol Total                                 P       D     R       200                    82465
                                                                                M
                                                                        M             Pab                 TALLA             C   C    2. Triglicéridos                                 P       D     R       165                    84478

                                                                          D     F     Ppreg                Hb               R   R    3.                                               P       D     R

                TRATAMIENTO Y CONTROL A PERSONAS CON DIAGNÓSTICO DE HIPERTENSIÓN ARTERIAL
                (PRODUCTO 3000016)
                                            Cartera de servicios

                                                                                                     CODIGO              UNIDAD DE
                       SUB PRODUCTOS                                      TRAZADORES                                                                                  CATEGORIAS
                                                                                                       UM                 MEDIDA

 Tratamiento y control de personas según                                                                                PERSONA
                                                                                                         087                                            I2    I3        I4      II1       II2           III1       III2      IIE        IIIE
 Clasificación de Riesgo Cardiovascular                                                                                 ATENDIDA
 Tratamiento para persona con Hipertensión                                                                              PERSONA
                                                                                      X                  087                                            I2    I3        I4
 sin daño de órgano                                                                                                     ATENDIDA
 5001605 Pacientes Con Enfermedad
 Cardiometabolica Organizados Que Reciben                                                                            PERSONA
                                                                                                         088                                            I2    I3        I4      II1       II2           III1       III2      IIE        IIIE
 Educación Para El Control De La                                                                                    CAPACITADA
 Enfermedad
 5001606 Personas Hipertensas Con                                                                                       PERSONA
                                                                                      X                  087                                                                    II1       II2           III1       III2      IIE        IIIE
 Tratamiento Especializado                                                                                              ATENDIDA

---

## Página 20

Registro de las urgencias hipertensivas

No asociado a subproducto, sólo sirve para identificar los casos de emergencia o urgencia
hipertensiva encontrados en las actividades de consulta externa.

 •   No tiene una meta de programación
 •   Cuando el caso ha sido identificado en emergencias o en hospitalizaciones, el registro
     se hace según los sistemas de registro vigentes en dichas áreas

  Urgencia hipertensiva es una situación en la que la presión arterial se ve gravemente
  elevada (180 o superior para la presión sistólica o 110 o superior para la presión
  diastólica), pero no hay daño orgánico asociado. Aquellos que experimentan urgencia
  hipertensiva pueden o no experimentar uno o más de estos síntomas: dolor de cabeza
  intenso, dificultad para respirar, hemorragias nasales o ansiedad severa. La atención de
  la urgencia hipertensiva incluye el control de las funciones vitales.
  El tratamiento de la urgencia hipertensiva generalmente requiere reajuste y/o
  dosificación adicional de medicamentos por vía oral, pero no requiere hospitalización
  para la reducción rápida de la presión arterial. Puede ser manejada inicialmente en los
  establecimientos de primer nivel y en casos extremos, referir a establecimientos de
  mayor capacidad resolutiva.

       Emergencia hipertensiva cuando la presión arterial alcanza niveles que dañan
       órganos. Ocurren generalmente en los niveles de presión arterial superiores o
       iguales a 180 sistólica o 120 diastólica, pudiendo ocurrir a niveles más bajos en
       pacientes cuya presión arterial no había sido previamente alta. Se define la
       emergencia cuando la presión elevada se acompaña de un daño a órgano como:
       Ictus, pérdida de consciencia, pérdida de la memoria, ataque al corazón, daño a los
       ojos y los riñones, pérdida de la función renal, disección aórtica, angina de pecho
       (dolor de pecho inestable) edema pulmonar (acumulación de líquido en los
       pulmones) entre otros.

  La atención de la emergencia hipertensiva no corresponde al primer nivel de atención
  y requiere derivación a emergencia y manejo hospitalario. Sólo se registra cuando ha
  sido identificado en consultorio para su referencia.

  Urgencia hipertensiva identificada en consultorio

   En el ítem: Diagnóstico motivo de consulta y/o actividad de salud:
 • En el 1º casillero registrar Lectura Elevada de la Presión Sanguínea(R030)
   En el casillero LAB registrar “URG” de urgencia

 • En el 2º casillero registre cualquiera de los siguientes diagnósticos:

  • Hipertensión esencial (primaria) (I10X)
  • Crisis hipertensiva (I16)
  • Enfermedad Cardiaca Hipertensiva (I11)
  • Enfermedad renal crónica hipertensiva (I12)
  • Enfermedad Cardiaca y renal crónica hipertensiva (I13)

---

## Página 21

Para el ítem: Tipo de diagnóstico anote:
                         • En el 1º casillero marque “D” de definitivo.

                         En el ítem Lab:
                         • En el 1º casillero registrar “URG” de urgencia.

               D.N.I.                           DISTRITO DE                               PERIM ETRO              EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                                      CEFALICO-                                     DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                    CÓDIGO
 DIA      HISTORIA CLINICA                     PROCEDENCIA         EDAD       SEXO      ABDOM INAL -PESO
                                                                                                                ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                     Y ACTIVIDADES DE SALUD                                              CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                             PREGESTACIONAL          A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
         (*)FECHA DE NACIMIENTO: _____/____/______               FECHA ULTIMO RESULTADO DE Hb: _____/____/______                                     FECHA DE ULTIMA REGLA: ____/____/______

               65256251
                                   2             Chiclayo                 A    M
                                                                                           PC                   PESO         60          N       N 1. Lectura elevada de la presión sanguínea       P   D   R URG          R030

                 54255                                            57 M                  Pab           89        TALLA        155         C       C   2. Hipertensión esencial (primaria)            P   D   R              I10X
                                   58                                             F
                                                                          D            Ppreg                     Hb                      R       R   3.                                             P   D   R

                         La urgencia hipertensiva con o sin diagnóstico previo no requiere referencia a otro
                         establecimiento de salud.

                         Emergencia hipertensiva detectada en consultorio

                         En el ítem: Diagnóstico motivo de consulta y/o actividad de salud:
                          • En el 1º casillero registrar Lectura elevada de la presión sanguínea. R030

                          En el 2°casillero registrar cualquier de los siguientes diagnósticos:
                          • Hipertensión esencial (primaria) (I10X).
                          • Enfermedad Cardiaca Hipertensiva (I11).
                          • Enfermedad renal crónica hipertensiva(I12)
                          • Enfermedad Cardiaca y renal crónica hipertensiva (I13)

                         Para el ítem Tipo de diagnóstico:
                         • En el 1º casillero registrar “D” de definitivo.
                         • En el 2° casillero registrar “R”

                         En el ítem Lab:
                         • En el 1º casillero registrar “EMG”

                 En el siguiente casillero registrar “RF” si el paciente fue referido a otro establecimiento
                 de salud.
                  D.N.I.                           DISTRITO DE                                    PERIM ETRO            EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                                 FINANC.                                                           CEFALICO-                                   DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                 CÓDIGO
       DIA   HISTORIA CLINICA                     PROCEDENCIA          EDAD           SEXO      ABDOM INAL -PESO
                                                                                                                      ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                           Y ACTIVIDADES DE SALUD                                           CIE/CPMSS
           GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                                  PREGESTACIONAL        A HEMOGLOBINA                                                           P    D R 1º 2º 3º
   NOMBRES Y APELLIDOS PACIENTE:
             (*)FECHA DE NACIMIENTO: _____/____/______              FECHA ULTIMO RESULTADO DE Hb: _____/____/______                                       FECHA DE ULTIMA REGLA: ____/____/______

                   65256251
                                        2            Chiclayo                 A        M
                                                                                                 PC                   PESO         67        N       N 1. Lectura elevada de la presión sanguínea       P   D   R EMG         R030

                    54255                                            57 M                       Pab        92      TALLA           161       C       C    2. Enfermedad cardiaca hipertensiva           P   D   R   RF        I11X
                                        58                                             F
                                                                              D              Ppreg                     Hb                    R       R    3.                                            P   D   R

                  Subproducto 5001608: Tratamiento y control de personas según clasificación de riesgo

---

## Página 22

cardiovascular

Definición operacional. - Intervención dirigida a personas de 18 años o más con
hipertensión arterial y/o dislipidemia. La estratificación se realiza al menos una vez al año
utilizando la calculadora de riesgo HEARTS en personas entre los 40 a 75 años.
Para personas de 18 a 39 años, la evaluación del riesgo cardiovascular y su manejo se
realiza de manera individualizada, considerando los factores de riesgo cardiovascular y
presencia de comorbilidades, en el contexto de decisiones médicas compartidas con el
paciente. No es necesario hacerlo de forma sistemática, ni se usa la calculadora de riesgo
HEARTS, ni se debe programar metas en este grupo de edades.
Para las personas mayores de 75 años, se puede usar la calculadora de riesgo HEARTS
fijando la edad con la máxima permitida por la calculadora (75 años). Se debe considerar
que el riesgo/beneficio para iniciar tratamiento farmacológico con estatinas no es claro
por encima de los 75, por lo que la decisión debe ser individualizada.

Riesgo Cardiovascular: Es la probabilidad que tiene un individuo de sufrir muerte o
enfermedad cardiovascular durante un periodo de tiempo, generalmente a 10 años, el cual
va a depender del número de factores de riesgo que estén presentes en el individuo. El
riesgo cardiovascular se estratifica de la siguiente manera:

                          Valoración de Riesgo Cardiovascular
                                    Nivel de
                                                      Porcentaje
                                     Riesgo
                                                        Colocar
                              Bajo                        <5%
                              Moderado                5% - <10%
                              Alto                    10% - <20%
                              Muy Alto                20% - <30%
                              Crítico                    ≥30%

     •    Esta actividad implica definir claramente el riesgo cardiovascular inicial y revalorar
          el riesgo de forma periódica según plan de seguimiento y manejo de acuerdo al
          nivel de riesgo (incluye a las personas referidas de otros establecimientos de menor
          nivel resolutivo).

 •       Para personas que están continuando tratamientos instaurados previamente para la
         prevención primaria de enfermedad cardiovascular, siempre que el paciente tolere
         el tratamiento, se recomienda mantener la medicación.

El personal que ejecuta la actividad puede ser: médico, enfermera, técnico de enfermería
o personal de laboratorio.

---

## Página 23

Registro de la medición del riesgo cardiovascular

En el ítem Diagnóstico motivo de consulta y/o actividad de salud:
• En el 1º casillero registre el diagnóstico de:
     Hipertensión esencial (primaria) I10X
     Ó
      El cualquiera de los diagnósticos, según la dislipidemia identificada:
                                            •       Hipercolesterolemia Pura (E780)
                                            •       Hipercolesterolemia Pura (E781)
                                            •       Hiperlipidemia Mixta (E782)
                                            •       Otra hiperlipidemia (E784)
                                            •       Dislipidemia (E785)

• En el 2º casillero registre valoración de riesgo cardiovascular 99199.23 en el campo LAB
  se registra valor numérico

               D.N.I.                        DISTRITO DE                               PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                                   CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                               CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA            EDAD       SEXO   ABDOM INAL -PESO
                                                                                                        ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                             Y ACTIVIDADES DE SALUD                                         CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                             PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______                 FECHA ULTIMO RESULTADO DE Hb: _____/____/______                FECHA DE ULTIMA REGLA: ____/____/______

             12345678
                                 2      San Juan de Lurigancho            A    M
                                                                                      PC                PESO    80     N    N 1. Hipertensión esencial (primaria)                     P   D   R               I10X

               1234                                               65 M               Pab       95       TALLA   164    C    C   2. Estratificación del riesgo cardiovascular global   P   D   R   15        99199.23
                                56                                             F
                                                                          D          Ppreg               Hb            R    R   3.                                                    P   D   R

Manejo del riesgo cardiovascular:

Según el nivel de riesgo, considerar iniciar tratamiento farmacológico (estatinas y/o ácido
acetilsalicílico) según documentos técnicos vigentes Vías de Abordaje HEARTS, Guías de
Práctica Clínica u otros dirigidos a personas con hipertensión arterial y/o dislipidemia.

Para pacientes con hipertensión y riesgo cardiovascular alto o más, se recomienda que el
seguimiento del tratamiento preventivo con estatinas sea en conjunto con el manejo de la
medicación antihipertensiva. Para mayor detalle consultar las vías de abordaje HEARTS,
guías de práctica clínica vigentes u otros documentos.

❖              Registro de consultas de seguimento
En caso de reevaluación del riesgo cardiovascular en personas con dislipidemia y riesgo
cardiovascular alto o superior, se registra al momento de la reevaluación.
En el ítem Diagnóstico motivo de consulta y/o actividad de salud:
• En el 1º casillero registrar cualquiera de los siguientes diagnósticos:
   − Hipercolesterolemia Pura (E780)
   − Hipercolesterolemia Pura (E781)
   − Hiperlipidemia Mixta (E782)
   − Otra hiperlipidemia (E784)
   − Dislipidemia(E785).

### Tablas estructuradas de la página

| Columna 1 | Columna 2 |
| --- | --- |
| El cualquiera de los diagnósticos, según la dislipidemia identificada: |  |
| • | Hipercolesterolemia Pura (E780) |
| • | Hipercolesterolemia Pura (E781) |
| • | Hiperlipidemia Mixta (E782) |
| • | Otra hiperlipidemia (E784) |
| • | Dislipidemia (E785) |

---

## Página 24

• En el 2º casillero registrar Tamizaje de presión sanguínea (99199.22).
           En la primera columna colocar el valor de la presión arterial sistólica.
           En la segunda columna colocar el valor de la presión arterial diastólica

         Para el ítem: Tipo de diagnóstico anote:
          En todos los casilleros corresponde marcar “D” de definitivo.

         En el ítem Lab:
         • En el 3º casillero registre valoración de riesgo cardiovascular 99199.23 en el campo LAB
           se registra valor numérico

               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                 CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                           CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                FECHA DE ULTIMA REGLA: ____/____/______

             65321452
                                 2             Camaná               A    M
                                                                                PC                PESO    60     N    N 1. Dislipidemia                                         P   D   R                 E785

               35745                                        48 M               Pab       80       TALLA   178    C    C   2. Tamizaje de la presión arterial                    P   D   R 120 80    99199.22
                                58                                       F
                                                                    D          Ppreg               Hb            R    R   3. Estratificación del riesgo cardiovascular global   P   D   R   12      99199.23

         Subproducto 5001609: Tratamiento para persona con hipertensión sin daño de órgano

         Definición Operacional. - Intervención dirigida a personas con hipertensión arterial que no
         presentan daño establecido de órgano diana como complicación de la enfermedad, se
         brinda en establecimientos de salud con población asignada de las categorías I-2, I-3 y I-4,
         con la finalidad de brindar tratamiento integral para el control de su enfermedad.

         Incluye las medidas farmacológicas y no farmacológicas establecidas dentro de la Vía de
         abordaje HEARTS, guía de práctica clínica u otro documento correspondiente del MINSA.
         Incluye el manejo de complicaciones y multimorbilidades según riesgo cardiovascular.

         Para el tratamiento integral de la hipertensión se considera el desarrollo de los siguientes
         procedimientos e intervenciones:
            • Control de la presión arterial
            • Cálculo del IMC (registro de peso y talla en el HIS)
            • Medición del perímetro abdominal.
            • Evaluación de efectos adversos, adherencia terapéutica y prescripción farmacológica.
            • Consejerías no farmacológicas, priorizar según criterio:
                       • Consejería nutricional.
                       • Consejería/ prescripción de actividad física.
                       • Recomendaciones para la cesación de consumo de tabaco y alcohol
            • Electrocardiograma, idealmente una vez al año (priorizar en personas con alto riesgo
               cardiovascular)

                 El personal que ejecuta la actividad: médico, enfermera, nutricionista, técnico de
                 enfermería y personal de laboratorio.

---

## Página 25

El resultado deseado del tratamiento integral lograr el control de la enfermedad, para ello
            se define:

                       Paciente controlado: Es aquel que, teniendo el tratamiento instaurado, reporta sus
                       últimos 3 controles dentro de la meta de tratamiento.

                              •         Presión arterial menor de 140/90 mmHg en población general

                              •         Meta terapéutica individualizada establecida según el caso (menor a 130/80 en
                                        casos de alto riesgo cardiovascular).

            ❖ Controles de la Presión arterial
            Cuando se programan citas de seguimiento con enfermería, técnico de enfermería u otro
            personal no médico para evaluar el control de la enfermedad según meta de tratamiento,
            presión arterial < 140/90 mmHg u otro valor establecido según la evaluación médica. Se
            registra de la siguiente manera:

            En el ítem Diagnóstico motivo de consulta y/o actividad de salud anote:
            • En el 1º casillero Hipertensión Esencial (Primaria).
            • En el 2º casillero Tamizaje de presión arterial.

            En el ítem Tipo de Diagnóstico:
            • En el 1º casillero marcar “R” de repetido.
            • En el 2º casillero marcar “D” de definitivo.

            En el ítem Lab:
            • En el 2º casillero colocar valor de presión arterial.
              En la primera columna colocar el valor de la presión arterial sistólica.
              En la segunda columna colocar el valor de la presión arterial diastólica.

               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                       CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                 CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                FECHA DE ULTIMA REGLA: ____/____/______

             65321452
                                  2           Los Olivos            A    M
                                                                                PC                PESO    67     N    N 1. Hipertensión esencial (primaria)          P   D   R                  I10X

               35745                                        61 M               Pab       95       TALLA   161    C    C   2. Tamizaje de la presión arterial         P   D   R 120 80         99199.22
                                  58                                     F
                                                                    D          Ppreg               Hb            R    R   3.                                         P   D   R

            ❖                Consulta para tratamiento y evaluación del paciente hipertenso:

                    En pacientes no controlados se recomienda la prescripción y control mensual o un
                    tiempo menor hasta lograr el control de la enfermedad según las metas terapéuticas
                    establecidas según documentos referenciales del MINSA.

                  Una vez alcanzada la meta terapéutica, con tres controles consecutivos dentro de rango
                  se recomienda espaciar los controles y prescripción a cada 3 meses o según lo
                  establezca el documento normativo vigente.

---

## Página 26

En el ítem Diagnóstico motivo de consulta y/o actividad de salud anote:
       • En el 1º casillero Hipertensión Esencial (Primaria)
       • En el 2º casillero Examen de presión arterial

       En el ítem Tipo de Diagnóstico:
       • En el 1º casillero marcar “R” de repetido, sólo se puede registrar “D” si en esa
         consulta se ha establecido el diagnóstico por primera vez.
       • En el 2º casillero marcar “D” de definitivo.

       En el ítem Lab:
       • En el 1º casillero registrar “PC” de paciente que recibe controles en LAB 1 y en la
         segunda columna LAB2 registrar el número de meses para los que se ha prescrito el
         tratamiento.
         P Ejem: 2 meses de tratamiento = PC/2
         Actualmente el máximo valor a registrar será “3” que indica que se ha prescrito medicación
         para los próximos 3 meses.
         La evaluación anual usa los valores registrados en LAB2 para evaluar la continuidad de
         tratamiento a lo largo del tiempo.

       • En el 2º casillero marcar registrar valor de presión arterial.
         En la primera columna colocar el valor de la presión arterial sistólica.
         En la segunda columna colocar el valor de la presión arterial diastólica.

               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE          VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                   CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO          LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                             CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R     1º       2º   3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______

             16070602
                                 2            Los Olivos            A    M
                                                                                PC                PESO    56      N    N 1. Hipertensión esencial (primaria)             P   D   R     PC      2            I10X

               15212                                        61 M               Pab       89       TALLA   167     C    C   2. Tamizaje de la presión arterial            P   D   R     120     80         99199.22
                                58                                       F
                                                                    D          Ppreg               Hb             R    R   3.                                            P   D   R

Subproducto 5001606: Personas Hipertensas Con Tratamiento Especializado

Definición Operacional. –

Intervención dirigida a personas con diagnóstico de hipertensión arterial, con daño de órgano diana
(retinopatía, Enfermedad Renal Crónica, cardiopatía o Enfermedad Cardiovascular) que se les da
seguimiento por consultorio externo en el segundo o tercer nivel de atención.

También puede incluir a pacientes con comorbilidades importantes que requieran una valoración
integral especializada. La visita a cada médico especialista a cargo debe hacerse una vez al año
como mínimo según los daños de órgano diana que tenga el paciente e incluye valoración con
exámenes auxiliares en caso de requerirlo. También se cuentan para la entrega del subproducto
las consultas por telemedicina.

Se puede incluir a personas con Hipertensión Arterial con alto riesgo cardiovascular, muy alto
riesgo y riesgo crítico, con una o varias complicaciones. También se incluye a los pacientes
con hipertensión arterial resistente al tratamiento.

---

## Página 27

El manejo se realiza en establecimientos de salud de categorías II-1, II-2, II-E, III-1 y III-2,
con acceso a equipos especializados.

La intervención al paciente Hipertenso se debe llevar a cabo los siguientes procedimientos:
La consulta médica tiene una duración de 20 minutos y se debe realizar al menos cada 3
meses. Se realiza la prescripción farmacológica, valoración de la adherencia, evaluación de
efectos adversos y daño de órgano blanco. Dependiendo de la especialidad, la evaluación
puede incluir:

1. Cardiología: control de presión arterial, evaluación del IMC, perímetro abdominal,
    electrocardiograma, ecocardiograma, monitorización ambulatoria de la presión
    arterial, índice brazo-tobillo, ecografía doppler arterial (carótidas y miembros
    inferiores).
2. Endocrinología: control de glucemia plasmática y/o hemoglobina glucosilada,
    evaluación de causas endocrinológicas de hipertensión arterial secundaria.
3. Nefrología: creatinina y cociente albúmina/creatinina en orina.
4. Oftalmología: evaluación de fondo de ojo.
5. Incluye la consulta o consejería nutricionales por profesional capacitado, consulta de
    prescripción/indicación de actividad física y consulta para la cesación del consumo de
    tabaco y alcohol.
6. Se debe realizar interconsultas para valoración de otras complicaciones y comorbilidades
    (Retinopatía hipertensiva, cardiopatía y vasculopatía, coagulación y vasculopatía,
    dislipidemia, daño hepático u otro), incluye exámenes de laboratorio según criterio
    médico, si el establecimiento no cuente con el especialista deberá ser referir a un
    establecimiento de salud con la capacidad resolutiva correspondiente.

El resultado deseado del tratamiento integral es lograr el control de la enfermedad, para
ello se define:

    Paciente controlado: Es aquel que, teniendo el tratamiento instaurado, reporta sus
    últimos 3 controles dentro de la meta de tratamiento.

        •   Presión arterial menor de 140/90 mmHg en población general

        •   Meta terapéutica individualizada establecida según el caso (menor a 130/80 en
            casos de riesgo cardiovascular Alto o más).

   UPSS Cardiología/Medicina Interna/Medicina familiar*

   *En establecimientos especializados que no cuenten con servicios de cardiología, P.Ej
   Institutos de salud mental, de contar con área de medicina familiar para el manejo de
   comorbilidades, siempre que el personal cuente con las capacidades específicas para
   la intervención, esta UPSS puede brindar la atención especializada

❖ Controles de la Presión arterial
 Intervención que puede ser realizada por enfermera, técnica en enfermería capacitada u
 otro personal no médico, orientada a identificar los valores de presión arterial en
 personas hipertensas y si han logrado la meta terapéutica: presión arterial sistólica <
 140 mmHg o <130mmHg, según el caso, se registra de la siguiente manera:

---

## Página 28

En el ítem Diagnóstico motivo de consulta y/o actividad de salud anote:
            • En el 1º casillero Hipertensión Esencial (Primaria)
            • En el 2º casillero Tamizaje de presión arterial.

            En el ítem Tipo de Diagnóstico:
            • En el 1º casillero marcar “R” de repetido.
            • En el 2º y 3º casillero marcar “D” de definitivo.

          En el ítem Lab:
         En el 2º casillero registrar EL valor de presión arterial.
         En la primera columna colocar el valor de la presión arterial sistólica.
         En la segunda columna colocar el valor de la presión arterial diastólica.
               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE          VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                   CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO          LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                             CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R     1º       2º   3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______

             16070602
                                 2            Los Olivos            A    M
                                                                                PC                PESO    67      N    N 1. Hipertensión esencial (primaria)             P   D   R                          I10X

               15212                                        61 M               Pab       95       TALLA   161     C    C   2. Tamizaje de la presión arterial            P   D   R     130     70         99199.22
                                58                                       F
                                                                    D          Ppreg               Hb             R    R   3.                                            P   D   R

       ❖               Consulta para tratamiento y evaluación del paciente hipertenso:

            En el ítem Diagnóstico motivo de consulta y/o actividad de salud anote:
            • En el 1º casillero cualquiera de los siguientes diagnósticos:
            • Hipertensión esencial (primaria) (I10X).
            • Enfermedad Cardiaca Hipertensiva (I11).
            • Enfermedad renal crónica hipertensiva (I12)
            • Enfermedad Cardiaca y renal crónica hipertensiva (I13)

            • En el 2º registre casillero Examen de presión arterial (99199.22)

            En el ítem Tipo de Diagnóstico:
            • En el 1º casillero marcar “R” de repetido.
            • En el 2º casillero marcar “D” de definitivo.

            En el ítem Lab:
            • En el 1º casillero registrar “PC” de paciente que recibe controles en LAB 1 y en la
              segunda columna LAB2 registrar el número de meses para los que se ha prescrito el
              tratamiento.
              P Ejem: 1 mes de tratamiento = PC/1
                Actualmente el máximo valor a registrar será “3” que indica que se ha prescrito medicación
                para los próximos 3 meses.
                La evaluación anual usa los valores registrados en LAB2 para evaluar la continuidad de
                tratamiento a lo largo del tiempo.

            • En el 2º casillero marcar registrar valor de presión arterial.

---

## Página 29

En la primera columna colocar el valor de la presión arterial sistólica.
                         En la segunda columna colocar el valor de la presión arterial diastólica.

               D.N.I.                           DISTRITO DE                                   PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                                          CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                              CÓDIGO
 DIA      HISTORIA CLINICA                     PROCEDENCIA            EDAD        SEXO      ABDOM INAL -PESO
                                                                                                               ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                    Y ACTIVIDADES DE SALUD                                                        CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                                 PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
        (*)FECHA DE NACIMIENTO: _____/____/______                   FECHA ULTIMO RESULTADO DE Hb: _____/____/______                       FECHA DE ULTIMA REGLA: ____/____/______

              16070602
                                  2             Los Olivos                   A     M
                                                                                             PC                PESO       56     N   N 1. Hipertensión esencial (primaria)                         P     D       R       PC   1     I10X

               15212                                                 61 M                   Pab        89      TALLA     167     C   C    2. Tamizaje de la presión arterial                       P     D       R 130 70         99199.22
                                 58                                                 F
                                                                             D              Ppreg               Hb               R   R    3.                                                       P     D       R

              Manejo Integral especializado
              El manejo integral especializado involucra los servicios de cardiología o medicina interna,
              nefrología, oftalmología, endocrinología, y nutrición; incluye consulta médica,
              hospitalización, evaluaciones complementarias multidisciplinarias, exámenes bioquímicos
              y otras pruebas según criterio médico para valorar y controlar complicaciones,
              morbilidades asociadas y manifestaciones tardías de la enfermedad.

              En el ítem Diagnóstico motivo de consulta y/o actividad de salud anote:
              • En el 1º casillero colocar Hipertensión esencial (primaria) (I10X)
              • En el 2º casillero colocar cualquiera de los siguientes diagnósticos:

                                                                                    DIAGNOSTICOS MAS FRECUENTES
                         ESPECIALIDAD                                                                                                     CÓDIGOS
            Cardiología                                         Enfermedad cardiaca hipertensiva con insuficiencia cardiaca (I110)
                                                                Trastorno de la válvula aórtica (I359)
            Cirugía Cardiovascular                              Enfermedad vascular periférica (I739)
                                                                Arteriosclerosis de la aorta (I700)
            Endocrinología                                      Diabetes tipo 2 con complicaciones múltiples (E117)
            Nefrología                                          Enfermedad renal hipertensiva (I129)
            Neurología                                          Accidente cerebrovascular no especificado como hemorragia o infarto (I64)
            Oftalmología                                        Retinopatía hipertensiva (H350)
            Rehabilitación                                      Secuelas de accidente vascular encefálico, no especificado como hemorrágico o
                                                                isquémico (I694)

              Para el ítem Tipo de diagnóstico
              • En el 1º casillero marque “R” según sea el diagnóstico del especialista.
              • En el 2º casillero marque “D” o “R” según sea el diagnóstico del especialista.

              En el ítem Lab:

              No aplica en este ejemplo.

              UPSS Cardiología
                      D.N.I.                           DISTRITO DE                                    PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                                     FINANC.                                                           CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                            CÓDIGO
        DIA      HISTORIA CLINICA                     PROCEDENCIA                EDAD       SEXO    ABDOM INAL -PESO
                                                                                                                       ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                            Y ACTIVIDADES DE SALUD                                                      CIE/CPMSS
               GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                                  PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
       NOMBRES Y APELLIDOS PACIENTE:
              (*)FECHA DE NACIMIENTO: _____/____/______                   FECHA ULTIMO RESULTADO DE Hb: _____/____/______                          FECHA DE ULTIMA REGLA: ____/____/______

                    16070602
                                         2             Los Olivos                       A    M
                                                                                                     PC                PESO    60     N        N 1. Hipertensión esencial (primaria)                         P       D    R                I10X

                       15212                                                 58 M                   Pab        90      TALLA   170    C        C   2. Trastorno de la válvula aórtica, no especificado       P       D    R                I359
                                        58                                                    F
                                                                                        D           Ppreg               Hb            R        R   3.                                                        P       D    R

### Tablas estructuradas de la página

| ESPECIALIDAD | CÓDIGOS |
| --- | --- |
| Cardiología | Enfermedad cardiaca hipertensiva con insuficiencia cardiaca (I110) |
|  | Trastorno de la válvula aórtica (I359) |
| Cirugía Cardiovascular | Enfermedad vascular periférica (I739) |
|  | Arteriosclerosis de la aorta (I700) |
| Endocrinología | Diabetes tipo 2 con complicaciones múltiples (E117) |
| Nefrología | Enfermedad renal hipertensiva (I129) |
| Neurología | Accidente cerebrovascular no especificado como hemorragia o infarto (I64) |
| Oftalmología | Retinopatía hipertensiva (H350) |
| Rehabilitación | Secuelas de accidente vascular encefálico, no especificado como hemorrágico o |
|  | isquémico (I694) |

---

## Página 30

UPSS Cirugía Cardiovascular
                      D.N.I.                            DISTRITO DE                                     PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                                     FINANC.                                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                   CÓDIGO
        DIA      HISTORIA CLINICA                      PROCEDENCIA                 EDAD       SEXO    ABDOM INAL -PESO
                                                                                                                         ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                              Y ACTIVIDADES DE SALUD                                             CIE/CPMSS
               GESTANTE/PUERPERA      ETNIA          CENTRO POBLADO                                   PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
       NOMBRES Y APELLIDOS PACIENTE:
              (*)FECHA DE NACIMIENTO: _____/____/______                     FECHA ULTIMO RESULTADO DE Hb: _____/____/______                          FECHA DE ULTIMA REGLA: ____/____/______

                    16070602
                                         2                  Iquitos                       A    M
                                                                                                       PC                PESO    60     N        N 1. Hipertensión esencial (primaria)                     P       D   R            I10X

                       15212                                                   58 M                   Pab        90      TALLA   170    C        C   2. Arterioesclerosis de la aorta                      P       D   R            I700
                                         7                                                      F
                                                                                          D           Ppreg               Hb            R        R   3.                                                    P       D   R

              UPSS Endocrinología
                      D.N.I.                            DISTRITO DE                                     PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                                     FINANC.                                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                   CÓDIGO
        DIA      HISTORIA CLINICA                      PROCEDENCIA                 EDAD       SEXO    ABDOM INAL -PESO
                                                                                                                         ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                              Y ACTIVIDADES DE SALUD                                             CIE/CPMSS
               GESTANTE/PUERPERA      ETNIA          CENTRO POBLADO                                   PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
       NOMBRES Y APELLIDOS PACIENTE:
              (*)FECHA DE NACIMIENTO: _____/____/______                     FECHA ULTIMO RESULTADO DE Hb: _____/____/______                          FECHA DE ULTIMA REGLA: ____/____/______

                    16070602
                                         2                  Iquitos                       A    M
                                                                                                       PC                PESO    65     N        N 1. Hipertensión esencial (primaria)                     P       D   R            I10X

                       15212                                                   58 M                   Pab        90      TALLA   167    C        C   2. Diabetes tipo 2 con complicaciones múltiples       P       D   R            E117
                                        58                                                      F
                                                                                          D           Ppreg               Hb            R        R   3.                                                    P       D   R

                   UPSS Nefrología
               D.N.I.                           DISTRITO DE                                     PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                                            CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                     CÓDIGO
 DIA      HISTORIA CLINICA                     PROCEDENCIA              EDAD        SEXO      ABDOM INAL -PESO
                                                                                                                 ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                      Y ACTIVIDADES DE SALUD                                               CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                                   PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
        (*)FECHA DE NACIMIENTO: _____/____/______                     FECHA ULTIMO RESULTADO DE Hb: _____/____/______                       FECHA DE ULTIMA REGLA: ____/____/______

              85274136
                                  2                 Nauta                      A     M
                                                                                               PC                PESO       65     N   N 1. Hipertensión esencial (primaria)                       P   D       R             I10X

               65471                                                   58 M                   Pab        90      TALLA     173     C   C    2. Enfermedad renal hipertensiva                       P   D       R             I129
                                 58                                                   F
                                                                               D              Ppreg               Hb               R   R    3.                                                     P   D       R

                   UPSS Neurología
               D.N.I.                           DISTRITO DE                                     PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                                            CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                     CÓDIGO
 DIA      HISTORIA CLINICA                     PROCEDENCIA              EDAD        SEXO      ABDOM INAL -PESO
                                                                                                                 ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                      Y ACTIVIDADES DE SALUD                                               CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                                   PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
        (*)FECHA DE NACIMIENTO: _____/____/______                     FECHA ULTIMO RESULTADO DE Hb: _____/____/______                       FECHA DE ULTIMA REGLA: ____/____/______

              85274136
                                  2             Punchana                       A     M
                                                                                               PC                PESO       60     N   N 1. Hipertensión esencial (primaria)                       P   D       R             I10X
                                                                                                                                                  Accidente cerebrovascular no especificado como
               65471                                                   58 M                   Pab        90      TALLA     173     C   C    2.
                                                                                                                                                  hemorragia o infarto
                                                                                                                                                                                                   P   D       R             I64X
                                 58                                                   F
                                                                               D              Ppreg               Hb               R   R    3.                                                     P   D       R

                   UPSS Rehabilitación
               D.N.I.                           DISTRITO DE                                     PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                                            CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                     CÓDIGO
 DIA      HISTORIA CLINICA                     PROCEDENCIA              EDAD        SEXO      ABDOM INAL -PESO   ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                      Y ACTIVIDADES DE SALUD                                               CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                                   PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
        (*)FECHA DE NACIMIENTO: _____/____/______                     FECHA ULTIMO RESULTADO DE Hb: _____/____/______                       FECHA DE ULTIMA REGLA: ____/____/______

              85274136                                                         A               PC                PESO       60     N   N 1. Hipertensión esencial (primaria)                       P   D       R             I10X
                                  2              Iquitos                             M
                                                                                                                                               Secuelas de accidente cerebrovascular
               65471                                                   58 M                   Pab        90      TALLA     170     C   C    2. encefálico, no especificado como hemorrágico o      P   D       R             I694
                                                                                                                                               isquémico
                                 58                                                   F
                                                                               D              Ppreg               Hb               R   R    3.                                                     P   D       R

              ❖ Registro de otros procedimientos en personas con hipertensión

                   Como parte de los cuidados brindados a personas con hipertensión, se puede realizar de
                   forma rutinaria pruebas auxiliares dirigidas a la atención de la persona con Hipertensión.

                   Electrocardiograma
                   Se deben priorizar los recursos para los pacientes al momento del diagnóstico cuando
                   nunca han recibido la evaluación y para el seguimiento de pacientes con alto riesgo
                   cardiovascular o enfermedad cardiovascular establecida.
                       • En el primer casillero registrar el código del tipo de hipertensión

---

## Página 31

•         Hipertensión esencial (primaria) (I10X).
                              •         Enfermedad Cardiaca Hipertensiva (I11X).
                              •         Enfermedad renal crónica hipertensiva (I12X)
                              •         Enfermedad Cardiaca y renal crónica hipertensiva (I13X)

                              • En el segundo casillero registrar según corresponda

                             Toma de electrocardiograma e interpretación                                                                                                        93000
                             Toma de electrocardiograma, sin interpretación ni informe                                                                                          93005
                             Sólo interpretación e informe de electrocardiograma                                                                                                93010

               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                          CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                    CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                FECHA DE ULTIMA REGLA: ____/____/______

             85274136
                                  2            Iquitos              A    M
                                                                                PC                PESO    60     N    N 1. Hipertensión esencial (primaria)                     P   D   R          I10X
                                                                                                                               Toma de electrocardiograma, sin interpretación
               65471                                        58 M               Pab       90       TALLA   170    C    C   2.
                                                                                                                               ni informe
                                                                                                                                                                                P   D   R         93000
                                58                                       F
                                                                    D          Ppreg               Hb            R    R   3.                                                    P   D   R

                 Tamizaje de función renal
         Se realiza acorde a lo planteado en las vías de abordaje HEARTS y otros documentos normativos
         vigentes.
                 • En el 1º registrar cualquiera de los siguientes diagnósticos.
         −        Hipertensión esencial primaria I10X tipo de diagnóstico R

               • Realizar según pautas de documento normativo
                 A. 2° casilla: Dosaje de creatinina en sangre (82565) llenar en el campo LAB la TFG estimada mediante
                            fórmula
                            3° casilla: Dosaje de albúmina en orina, microalbúmina semicuantitativa (p ej ensayo con tira reactiva)
                            82044 llenar en el campo lab el número de cruces encontrados
                       Ó
                    B. 2° casilla Dosaje de creatinina en sangre (82565) llenar en el campo LAB la TFG estimada mediante
                            fórmula
                            3° casilla Dosaje de Albúmina en orina, microalbúmina, cuantitativa 82043 llenar en el campo LAB el
                            valor del Ratio Albumina Creatinuria

               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                          CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                    CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                FECHA DE ULTIMA REGLA: ____/____/______

             85274136
                                  2          Cajamarca              A    M
                                                                                PC                PESO    70     N    N 1. Hipertensión esencial (primaria)                     P   D   R          I10X

               65471                                        70 M               Pab       91       TALLA   167    C    C   2. Dosaje de creatinina en sangre                     P   D   R   78    82565
                                58                                       F                                                     Dosaje de albúmina en orina, microalbúmina
                                                                    D          Ppreg               Hb            R    R   3.                                                    P   D   R   14    82043
                                                                                                                               cuantitativa

---

## Página 32

Subproducto 5001605: Pacientes Con Enfermedad Cardiometabólica organizados que reciben
educación para el control de la enfermedad.

Definición Operacional. - Intervención que se brinda en establecimientos de salud de las
categorías I-2, I-3, I-4, II-1, II-2, III-1 y III-2 que brindan regularmente servicios para el tratamiento y
control de pacientes con enfermedad hipertensiva o diabética.

                       Incluye el desarrollo de los siguientes procedimientos:
                       • Sesión Educativa: Participan como máximo de 15 personas por actividad, tiene una
                         duración aproximada de 30 minutos.
                       • Sesión Demostrativa: Participan entre 8 y 15 personas por evento, tiene una
                         duración estimada de 45 minutos.
                       • Sesión de Grupo de Ayuda Mutua: Participan por lo menos 8 personas, tiene una
                         duración estimada de 30 minutos.

                       Registro de Sesión educativa con tema de prevención de Hipertensión

                       Posibles temas para la sesión educativa: alimentación saludable, reducir el consumo de
                       sal, mantener peso adecuado, actividad física, evitar el tabaquismo, limitar el consumo
                       de alcohol. https://www.cdc.gov/bloodpressure/prevent.htm

                       Los ítems: Documento de Identidad, Financiador, Pertenencia Étnica, Edad, Sexo,
                       Establecimiento y Servicio no se registran por tratarse de una actividad grupal.

                       En el ítem: Historia Clínica anote siempre APP100 de Actividades en Establecimiento de
                       Salud
                       En el ítem: Diagnóstico Motivo de Consulta y/o Actividad de Salud:
                       • En el 1º casillero registrar Sesión Educativa
                       • En el 2º casillero registrar el tema que corresponde la sesión educativa
                         • Hipertensión arterial

                       Para el ítem Tipo de diagnóstico
                       • En el 1º casillero marque “D” de diagnóstico definitivo.
                       • En el 2º casillero marque “R” de diagnóstico repetido.

                       En el ítem Lab anote:
                       • En el 1º casillero el número de personas que participan de la sesión

               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                       CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                 CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                FECHA DE ULTIMA REGLA: ____/____/______

              APP100
                                               Iquitos              A    M
                                                                                PC                PESO           N    N 1. Sesión educativa                          P   D   R   15            C0009

                                                                  M            Pab                TALLA          C    C   2. Hipertensión esencial (primaria)        P   D   R                  I10X
                                                                         F
                                                                    D          Ppreg               Hb            R    R   3.                                         P   D   R

---

## Página 33

Registro de Sesión educativa con tema de prevención de Diabetes
                       En el ítem: Historia Clínica anote siempre APP100 de Actividades en Establecimiento
                       de Salud
                       En el ítem: Diagnóstico Motivo de Consulta y/o Actividad de Salud:
                       • En el 1º casillero registrar Sesión Educativa
                       • En el 2º casillero registrar: Diabetes Mellitus tipo 2 sin complicaciones

                       • En el 1º casillero marque “D” de diagnóstico definitivo.
                       • En el 2º casillero marque “R” de diagnóstico repetido.

                       En el ítem Lab anote:
                       • En el 1º casillero el número de personas que participan de la sesión.
                        D.N.I.                         DISTRITO DE                                    PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                                       FINANC.                                                         CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                        CÓDIGO
           DIA     HISTORIA CLINICA                   PROCEDENCIA               EDAD         SEXO   ABDOM INAL -PESO
                                                                                                                       ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                            Y ACTIVIDADES DE SALUD                                                  CIE/CPMSS
                 GESTANTE/PUERPERA      ETNIA       CENTRO POBLADO                                  PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
         NOMBRES Y APELLIDOS PACIENTE:
                 (*)FECHA DE NACIMIENTO: _____/____/______                    FECHA ULTIMO RESULTADO DE Hb: _____/____/______                    FECHA DE ULTIMA REGLA: ____/____/______

                        APP100
                                                         Iquitos                       A      M
                                                                                                     PC                PESO            N    N 1. Sesión educativa                                     P   D    R   15                C0009

                                                                                      M             Pab                TALLA           C    C    2. Diabetes mellitus tipo 2 sin complicaciones       P   D    R                      E119
                                                                                              F
                                                                                       D            Ppreg               Hb             R    R    3.                                                   P   D    R

                  Registro de Sesión Demostrativa con tema de prevención de Hipertensión
                 Los ítems Documento de Identidad, Financiador, Pertenencia Étnica, Edad, Sexo,
                 Establecimiento y Servicio; no se registran por tratarse de una actividad grupal.

                 En el ítem Historia Clínica anote siempre APP100 de Actividades en Establecimiento de
                 Salud
                 En el ítem Diagnóstico Motivo de Consulta y/o Actividad de Salud
                 • En el 1º casillero registre Sesión Demostrativa
                 • En el 2º casillero registre: Hipertensión Arterial

                 Para el ítem Tipo de diagnóstico
                 • En el 1º casillero marque “D” de diagnóstico definitivo.
                 • En el 2º casillero marque “R” de diagnóstico repetido.

                 En el ítem Lab anote:
                 • En el 1º casillero registre el número de personas que participan de la sesión
                   demostrativa.
               D.N.I.                        DISTRITO DE                                 PERIM ETRO           EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                                     CEFALICO-                                  DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                       CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA            EDAD        SEXO    ABDOM INAL -PESO
                                                                                                            ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                 Y ACTIVIDADES DE SALUD                                                 CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                               PREGESTACIONAL       A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______               FECHA ULTIMO RESULTADO DE Hb: _____/____/______                         FECHA DE ULTIMA REGLA: ____/____/______

              APP100
                                             Moyobamba                    A     M
                                                                                        PC                  PESO               N   N 1. Sesión demostrativa                                 P     D   R   15             C0010

                                                                      M                Pab                  TALLA              C   C   2. Hipertensión esencial (primaria)                  P     D   R                   I10X
                                                                                 F
                                                                          D           Ppreg                  Hb                R   R   3.                                                   P     D   R

                 Registro de Sesión Demostrativa con tema de prevención de Diabetes

                 En el ítem Historia Clínica anote siempre APP100 de Actividades en Establecimiento de
                 Salud

---

## Página 34

En el ítem Diagnóstico Motivo de Consulta y/o Actividad de Salud
                 • En el 1º casillero registre Sesión Demostrativa
                 • En el 2º casillero registre lo que corresponde:
                 • Diabetes Mellitus tipo 2 sin complicaciones

                  Para el ítem Tipo de diagnóstico
                  • En el 1º casillero marque “D” de diagnóstico definitivo.
                  • En el 2º casillero marque “R” de diagnóstico repetido

                  En el ítem Lab
                  • En el 1º casillero el número de personas que participan de la sesión demostrativa.
               D.N.I.                           DISTRITO DE                               PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                                      CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                               CÓDIGO
 DIA      HISTORIA CLINICA                     PROCEDENCIA         EDAD       SEXO      ABDOM INAL -PESO
                                                                                                           ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                Y ACTIVIDADES DE SALUD                                         CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                             PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
         (*)FECHA DE NACIMIENTO: _____/____/______               FECHA ULTIMO RESULTADO DE Hb: _____/____/______                        FECHA DE ULTIMA REGLA: ____/____/______

                APP100
                                                  Iquitos                 A       M
                                                                                           PC              PESO             N       N 1. Sesión demostrativa                             P   D   R   15         C0010

                                                                        M                  Pab             TALLA            C       C   2. Diabetes mellitus tipo 2 sin complicaciones   P   D   R               E119
                                                                                  F
                                                                          D             Ppreg               Hb              R       R   3.                                               P   D   R

Registro de Sesión de Grupo de Ayuda Mutua con tema de prevención de Hipertensión

                  Los ítems Documento de Identidad, Financiador, Pertenencia Étnica, Edad, Sexo,
                  Establecimiento y Servicio; no se registran por tratarse de una actividad grupal.

                  En el ítem Historia Clínica anote siempre APP100 de Actividades en Establecimiento de
                  Salud
                  En el ítem Diagnóstico Motivo de Consulta y/o Actividad de Salud
                  • En el 1º casillero registre Sesión de Grupo de Ayuda Mutua
                  • En el 2º casillero registre:
                    • Hipertensión Arterial

                  Para el ítem Tipo de diagnóstico
                  • En el 1º casillero marque “D” de diagnóstico definitivo.
                  • En el 2º casillero marque “R” de diagnóstico repetido.

                  En el ítem Lab anote:
                  • En el 1º casillero registre el número de personas que participan de la Sesión de Grupo de
                    Ayuda Mutua.
                  D.N.I.                           DISTRITO DE                                 PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                                 FINANC.                                                        CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                             CÓDIGO
       DIA   HISTORIA CLINICA                     PROCEDENCIA         EDAD            SEXO   ABDOM INAL -PESO
                                                                                                                ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                     Y ACTIVIDADES DE SALUD                                       CIE/CPMSS
           GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                               PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
   NOMBRES Y APELLIDOS PACIENTE:
             (*)FECHA DE NACIMIENTO: _____/____/______              FECHA ULTIMO RESULTADO DE Hb: _____/____/______                          FECHA DE ULTIMA REGLA: ____/____/______

                   85274136
                                       2             Iquitos                  A        M
                                                                                                 PC             PESO            N       N 1. Sesión de grupo de ayuda mutua                  P   D   R    15       C0012

                    65471                                                     M                 Pab             TALLA           C       C    2. Hipertensión esencial (primaria)             P   D   R              I10X
                                      58                                               F
                                                                              D              Ppreg               Hb             R       R    3.                                              P   D   R

---

## Página 35

Registro de Sesión de Grupo de Ayuda Mutua con tema de prevención de Diabetes

               En el ítem: Historia Clínica anote siempre APP100 de Actividades en Establecimiento de
               Salud
               En el ítem: Diagnóstico Motivo de Consulta y/o Actividad de Salud:
               • En el 1º casillero registrar Sesión de Grupo de Ayuda Mutua
               • En el 2º casillero registrar el tema que corresponde la sesión educativa
                 • Diabetes Mellitus tipo 2 sin complicaciones
               En el ítem: Tipo de diagnóstico marcar siempre “D” en
               ambos casilleros En el ítem Lab anote:
               • En el 1º casillero el número de personas que participan de la Sesión de Grupo de Ayuda
                 Mutua
                D.N.I.                        DISTRITO DE                         PERIM ETRO   EVALUACION   ESTA- SER-                                                  TIPO DE  VALOR
                             FINANC.                                               CEFALICO-                           DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                     CÓDIGO
DIA        HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO                ANTROPOMETRIC BLEC VICIO
                                                                                ABDOM INAL -PESO
                                                                                                                                                                     DIAGNÓSTICO  LAB
                                                                                                                                     Y ACTIVIDADES DE SALUD                                             CIE/CPMSS
         GESTANTE/PUERPERA     ETNIA       CENTRO POBLADO                                    A HEMOGLOBINA
                                                                                PREGESTACIONAL                                                                        P    D R 1º 2º 3º
       (*)FECHA DE NACIMIENTO: _____/____/______            FECHA ULTIMO RESULTADO DE Hb: _____/____/______            FECHA DE ULTIMA REGLA: ____/____/______

            85274136
                                2            Iquitos                 A    M
                                                                                 PC                PESO    N   N 1. Sesión de grupo de ayuda mutua                  P        D   R    15                 C0012

              65471                                               M             Pab                TALLA   C   C   2. Diabetes mellitus tipo 2 sin complicaciones   P        D   R                        E119
                               58                                         F
                                                                     D          Ppreg               Hb     R   R   3.                                               P        D   R

               TRATAMIENTO Y CONTROL DE PERSONAS CON DIABETES (PRODUCTO 3000017)
                                           Cartera de servicios
                                                                                                                                                     Unidad de
                                      Actividad                                           Sub Producto                           Trazador                                                     Categorías
       Producto                                                                                                                                       Medida
                                                            5001704 PACIENTES DIABETICOS CON TRATAMIENTO                                              PERSONA
                                                                                                                                       X                                                    II1   II2     III1      III2   IIE   IIIE
                                                            ESPECIALIZADO                                                                            CAPACITADA

                                                            5001705 VALORACIÓN DE COMPLICACIONES EN PERSONAS                                          PERSONA
          3000017                    5000115 BRINDAR                                                                                                                                   I4   II1   II2     III1      III2   IIE   IIIE
                                                            CON DIABETES                                                                              ATENDIDA
      TRATAMIENTO Y                   TRATAMIENTO A
        CONTROL DE                     PERSONAS CON                                                                                                   PERSONA
                                                            5001707 MANEJO DE LA ENFERMEDAD RENAL DIABETICA                                                             I2       I3    I4   II1
      PERSONAS CON                   DIAGNOSTICO DE                                                                                                   ATENDIDA
         DIABETES                   DIABETES MELLITUS

                                                            5001708 TRATAMIENTO PARA PERSONA CON DIABETES                                             PERSONA
                                                                                                                                       X                                I2       I3    I4
                                                            MELLITUS SIN DAÑO DE ÓRGANO                                                               ATENDIDA

           Registro de manejo básico de crisis hipoglucémica o hiperglucémica

           No asociado a subproducto, sólo sirve para identificar los casos de emergencia o urgencia en
           diabetes encontrados en las actividades de consulta externa.

           • No tiene una meta de programación.
           • Cuando el caso ha sido identificado en emergencias o en hospitalizaciones, el registro se
           hace según los sistemas de registro vigentes en dichas áreas, no duplicar registros.

           La hipoglucemia se define como una concentración de glucemia menor a 70 mg/dl, con o sin
           síntomas.

           Las crisis hiperglucémicas son los episodios que cursan con elevadas concentraciones
           plasmáticas de glucemia, generalmente mayor de 250 ó 200 mg/dl y que ponen en riesgo la
           vida del paciente. Las dos formas de presentación de descompensación hiperglicemia severa
           son:
           • Estado hiperosmolar hiperglucémico (EHH)
           • Cetoacidosis diabética (CAD)
           • O una combinación de ambas.

---

## Página 36

En el ítem: Diagnóstico motivo de consulta y/o actividad de salud.

                                                    Diabetes con                        Cetoacidosis                  Hipoglucemia por Medicamentos                                  Otras Hipoglucemias
                                                       coma                              Diabética                                (E16.0)                                                   (E16.2)
                                                                                                                                                                                 E162+ (E100 con coma ó E108 sin
       Diabetes Mellitus tipo 1                             E100                                E101                    E160+ (E100 con coma ó E108 sin coma)
                                                                                                                                                                                              coma)

                                                                                                                                                                                 E162+ (E110 con coma ó E118 sin
       Diabetes Mellitus tipo 2                             E110                                E111                    E160+ (E110 con coma ó E118 sin coma)
                                                                                                                                                                                              coma)

 Otras diabetes: E13 cuando se                                                                                                                                                   E162+ (E130 con coma ó E138 sin
                                                            E130                                E131                    E160+ (E130 con coma ó E138 sin coma)
  conoce el tipo de diabetes                                                                                                                                                                  coma)

                En los casos de coma diabético sea este por hipoglucemia severa o hiperglucemia de
                cualquier tipo, o en los casos de cetoacidosis sólo se requiere un código pues este
                identifica el tipo de diabetes.
                Ejemplo 1
                Para registrar hipoglicemia en general o hipoglicemia inducida por alimentos, es necesario
                incluir el código para el tipo de diabetes con el cuarto carácter siendo 0 si es con coma u 8
                de lo contrario.
                Ejemplo 2
                Para el ítem Tipo de diagnóstico
                • En el 1º casillero marque “D” de diagnóstico definitivo.

               D.N.I.                         DISTRITO DE                              PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                                   CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                         CÓDIGO
 DIA      HISTORIA CLINICA                   PROCEDENCIA           EDAD       SEXO   ABDOM INAL -PESO
                                                                                                        ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                             Y ACTIVIDADES DE SALUD                                   CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA       CENTRO POBLADO                            PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
        (*)FECHA DE NACIMIENTO: _____/____/______             FECHA ULTIMO RESULTADO DE Hb: _____/____/______                   FECHA DE ULTIMA REGLA: ____/____/______
                                                                                                                                     Diabetes mellitus tipo 2 con cetoacidosis
              84521475
                                  2            Los Olivos                 A    M
                                                                                      PC                PESO    80     N    N 1.                                                 P   D   R              E111
                                                                                                                                     diabética
               15212                                           61 M                  Pab       98       TALLA   179    C    C   2.                                               P   D   R
                                 58                                            F
                                                                          D          Ppreg               Hb            R    R   3.                                               P   D   R

En el 2º casillero marque “R” de diagnóstico repetido.
               D.N.I.                         DISTRITO DE                              PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                                   CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                         CÓDIGO
 DIA      HISTORIA CLINICA                   PROCEDENCIA           EDAD       SEXO   ABDOM INAL -PESO
                                                                                                        ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                             Y ACTIVIDADES DE SALUD                                   CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA       CENTRO POBLADO                            PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
        (*)FECHA DE NACIMIENTO: _____/____/______             FECHA ULTIMO RESULTADO DE Hb: _____/____/______                   FECHA DE ULTIMA REGLA: ____/____/______

              84521475
                                  2            Los Olivos                 A    M
                                                                                      PC                PESO    80     N    N 1. Hipoglicemia por medicamentos                   P   D   R              E160

               15212                                           61 M                  Pab       98       TALLA   179    C    C   2. Diabetes mellitus tipo 1                      P   D   R              E108
                                 58                                            F
                                                                          D          Ppreg               Hb            R    R   3.                                               P   D   R

                Subproducto 5001708: Tratamiento Para Personas Con Diabetes Mellitus Sin Daño De
                Órgano

                Definición Operacional. - Intervención que se brinda a personas con diabetes mellitus sin
                complicaciones en establecimientos de salud con población asignada de las categorías I-2,
                I-3 y I-4, con la finalidad de brindar tratamiento integral para el control de su enfermedad.

                Incluye las medidas farmacológicas y no farmacológicas establecidas dentro de la Vía de
                abordaje HEARTS, guía de práctica clínica u otro documento correspondiente del MINSA.
                Incluye el manejo de complicaciones y multimorbilidades según riesgo cardiovascular.

### Tablas estructuradas de la página

|  | Diabetes con | Cetoacidosis | Hipoglucemia por Medicamentos | Otras Hipoglucemias |
| --- | --- | --- | --- | --- |
|  | coma | Diabética | (E16.0) | (E16.2) |
|  |  |  |  | E162+ (E100 con coma ó E108 sin |
| Diabetes Mellitus tipo 1 | E100 | E101 | E160+ (E100 con coma ó E108 sin coma) |  |
|  |  |  |  | coma) |
|  |  |  |  | E162+ (E110 con coma ó E118 sin |
| Diabetes Mellitus tipo 2 | E110 | E111 | E160+ (E110 con coma ó E118 sin coma) |  |
|  |  |  |  | coma) |
| Otras diabetes: E13 cuando se |  |  |  | E162+ (E130 con coma ó E138 sin |
|  | E130 | E131 | E160+ (E130 con coma ó E138 sin coma) |  |
| conoce el tipo de diabetes |  |  |  | coma) |

---

## Página 37

Paciente diabético no complicado: se define como las personas con diabetes que cumplen
     con las tres condiciones siguientes:
     1. Sin retinopatía o retinopatía no proliferativa Leve,
     2. Tasa de filtración glomerular mayor o igual a 60ml/min y sin proteinuria
     3. Pie diabético con clasificación de Wagner 0 ó 1.
     4. No historia de enfermedad cardiovascular conocida

     Procedimientos e intervenciones que se deben realizar en la consulta para tratamiento y
     seguimiento:
         • Control de la presión arterial
         • Evaluar control glucémico
         • Cálculo del IMC (registro de peso y talla en el HIS)
         • Medición del perímetro abdominal.
         • Evaluación de efectos adversos, adherencia terapéutica y prescripción farmacológica.
         • Consejerías no farmacológicas, priorizar según criterio:
                   • Consejería nutricional.
                   • Consejería/ prescripción de actividad física.
                   • Recomendaciones para la cesación de consumo de tabaco y alcohol
     El resultado que se espera de la intervención es el control de la enfermedad según metas
     terapéuticas, para lo que se considera:

     Paciente controlado: Es aquel que, teniendo el tratamiento instaurado, reporta
     • Controles con glucemia en sangre o capilar ayunas 70 a 130 mg/dl y en caso de tomas
       post prandial 180 mg/dl ó
     • Hemoglobina glucosilada menor de 7% (o según meta terapéutica de Hb1Ac) cada 3
       meses en no controlados y cada 6 meses en pacientes controlados
     • Niveles de presión arterial <130/80

                  Tabla de códigos CIE10 correspondientes a Diabetes Mellitus
                         según tipo de diabetes y tipo de complicaciones

  Diabetes           Diabetes         DM otros tipos
                                                                     Diagnósticos
Mellitus tipo 1    Mellitus tipo 2     identificada
    E100                E110               E130                Diabetes Mellitus con coma

    E101                E111               E131                     Con cetoacidosis.
                                                           Con complicaciones renales (incluye
    E102                E112               E132
                                                              enfermedad renal diabética)
                                                             Con complicaciones oftálmicas.
    E103                E113               E133
                                                              (incluye retinopatía diabética)
    E104                E114               E134             Con complicaciones neurológicas

    E105                E115               E135             Con complicaciones circulatorias

---

## Página 38

periféricas.

E106               E116                   E136             Con otras complicaciones especificadas.

E107              E117                   E137                     Con complicaciones múltiples.

E108              E118                   E138                 Con complicaciones no especificadas.

                                                                Diabetes Mellitus sin mención de
E109              E119                   E139
                                                                         complicación

❖ Atención de seguimiento de la glicemia del paciente Diabético

Actividades realizadas por personal de salud para tomas de muestra de glucosa capilar, se
deben registrar en Historia Clínica del paciente con fecha y hora. Siempre que sea posible
registrar en cartilla de control de paciente.

En el ítem Diagnóstico motivo de consulta y/o actividad de salud:
• En el 1º casillero registre cualquiera de los siguientes diagnósticos:
    − Diabetes mellitus insulinodependiente, sin mención de complicación (E109).
    − Diabetes mellitus no insulinodependiente, sin mención de complicación (E119).
    − Diabetes mellitus especificada, sin mención de complicación (E139)*
       *Usar cuando se cuenta con un diagnóstico de otros tipos de diabetes identificadas como MODY,
       Neonatal, etc

• En el 2º casillero registre cualquiera de los siguientes diagnósticos:
• Glucosa de tira reactiva (82948) En el valor de LAB colocar el resultado numérico.
  En los casos en los que el valor excede los parámetros del glucómetro registrar: ALT

• En el 3º casillero registre Examen de presión arterial (99199.22)
• En el casillero de LAB registre valor de presión arterial.

 En la primera columna colocar el valor de la presión arterial sistólica y en la segunda
 columna colocar el valor de la presión arterial diastólica

Para el ítem Tipo de diagnóstico anote:
• En el 1º casillero marque “R” de diagnóstico repetido.
• En el 2º y 3º casillero marque “D” de diagnóstico definitivo.

En el ítem Lab
• En el 2º casillero en la primera columna registre Valor de glucosa en mg/dl

### Tablas estructuradas de la página

| Columna 1 | Columna 2 | Columna 3 | Columna 4 |
| --- | --- | --- | --- |
|  |  |  | periféricas. |
| E106 | E116 | E136 | Con otras complicaciones especificadas. |
| E107 | E117 | E137 | Con complicaciones múltiples. |
| E108 | E118 | E138 | Con complicaciones no especificadas. |
|  |  |  | Diabetes Mellitus sin mención de |
| E109 | E119 | E139 |  |
|  |  |  | complicación |

---

## Página 39

D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE         VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                               CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO   ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO         LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                         CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R     1º     2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______

             52146387
                                 2           Cajamarca              A    M
                                                                                PC                PESO    95      N    N 1. Diabetes Mellitus tipo 2, sin complicaciones   P   D   R                    E119

              854255                                        56 M               Pab      102       TALLA   174     C    C   2. Glucosa de tira reactiva                     P   D   R   89              82948
                                58                                       F
                                                                    D          Ppreg               Hb             R    R   3. Tamizaje de la presión arterial              P   D   R 110 70           99199.22

  ❖ Registro de consulta para tratamiento y evaluación del paciente Diabético

  En el ítem Diagnóstico motivo de consulta y/o actividad de salud:
  • En el 1º casillero registre cualquiera de los siguientes diagnósticos:
    − Diabetes mellitus insulinodependiente, sin mención de complicación (E109).
    − Diabetes mellitus no insulinodependiente, sin mención de complicación (E119).
    − Diabetes mellitus especificada, sin mención de complicación (E139).

       En el casillero LAB registrar “PC” de paciente que recibe controles en LAB 1 y en la
       segunda columna LAB2 registrar el número de meses para los que se ha prescrito el
       tratamiento.
          P Ejem: 2 meses de tratamiento = PC/2
            Actualmente el máximo valor a registrar será “3” que indica que se ha prescrito medicación
            para los próximos 3 meses.
            La evaluación anual usa los valores registrados en LAB2 para evaluar la continuidad de
            tratamiento a lo largo del tiempo

  • En el 2º casillero registre:
    - Glucosa en sangre (82947) en Ayunas
               ó
    - Dosaje de hemoglobina glucosilada (83036) *prueba de elección

  En el ítem Lab Colocar Valor de
              •        Glucosa en mg/dl
                       ó
          • Hb A1c% x10
       Ejemplo: HbA1c%: 8.7=87

  • En el 3º casillero registre Examen de presión arterial (99199.22)
       En el campo LAB registre el valor de la presión arterial.
       En la primera columna colocar el valor de la presión arterial sistólica.
       En la segunda columna colocar el valor de la presión arterial diastólica.

  Para el ítem Tipo de diagnóstico anote:
  En el 1º casillero marque “R” de diagnóstico repetido.
  En el 2º y 3º casillero marque “D” de diagnóstico definitivo.
    En el ítem Lab

---

## Página 40

D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE       VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                  CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO       LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                            CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R     1º   2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______

             52146387
                                 2           Cajamarca              A    M
                                                                                PC                PESO    95      N    N 1. Diabetes Mellitus tipo 2, sin complicaciones   P   D   R   PC   2              E119

              854255                                        56 M               Pab      102       TALLA   174     C    C   2. Dosaje de glucosa en sangre                  P   D   R   89                 82947
                                58                                       F
                                                                    D          Ppreg               Hb             R    R   3. Tamizaje de la presión arterial              P   D   R 120 80          99199.22

         Subproducto 5001704: Pacientes Diabéticos Con Tratamiento Especializado

         Definición Operacional. - Intervención dirigida a personas con diagnóstico de diabetes, con
         alguna o varias complicaciones, tipificada para su manejo en establecimientos de salud de
         categorías II-,1, II-2, III-1 y III-2, que se encuentran clínicamente estables.

         El manejo integral del paciente puede incluir:

         -Pacientes con complicaciones micro y macrovasculares producto de la enfermedad

         -Pacientes con comorbilidades que requieren un manejo diferenciado por médicos
         especialistas

         La intervención al paciente diabético complicado consiste en los siguientes
         procedimientos:

            1. Al menos una consulta médica cada 3 meses para reevaluar la adherencia al
               tratamiento, evaluación de efectos adversos y prescripción farmacológica, control de
               la glucemia o hemoglobina glucosilada, control de presión arterial

          2. Consultas de enfermería, seguimiento de la glicemia, cálculo del IMC, medición del
              perímetro abdominal, educación o consejería en control de diabetes

          3. Consulta por especialista según el tipo de complicación que condicione su manejo
              especializado y consulta con otros servicios como nutrición, psicología y odontología.
          4. Consejerías no farmacológicas, priorizar según criterio:
             • Consejería nutricional.
             • Consejería/ prescripción de actividad física.
             • Recomendaciones para la cesación de consumo de tabaco y alcohol

         El resultado que se espera de la intervención es el control de la enfermedad según metas
         terapéuticas, para lo que se considera:

         Paciente controlado: Es aquel que, teniendo el tratamiento instaurado, reporta
         • Controles con glucemia en sangre o capilar ayunas 70 a 130 mg/dl y en caso de tomas
           post prandial 180 mg/dl
           ó
         • Hemoglobina glucosilada menor de 7% (o según meta terapéutica de Hb1Ac) cada 3
           meses en no controlados y cada 6 meses en pacientes controlados
         • Niveles de presión arterial <130/80

---

## Página 41

En las consultas de tratamiento especializado se debe incluir una evaluación de enfermedad,
educación al paciente y un manejo integral de la enfermedad. La consulta incluye en caso de
presencia de comorbilidades el derivar al especialista adecuado para evaluación y manejo. La
frecuencia de control se debe orientar por los documentos normativos vigentes, considerándose
adecuado en pacientes en meta terapéutica un control metabólico por 3 a 6 meses.

             ❖ Registro de consulta de control y medicación
             Actividades realizadas por personal de salud para tomas de muestra de glucosa capilar, se
             deben registrar en Historia Clínica del paciente con fecha y hora. Siempre que sea posible
             en cartilla de control de paciente
             En el ítem Diagnóstico motivo de consulta y/o actividad de salud:
             • En el 1º casillero registre cualquiera de los siguientes diagnósticos:
               − Diabetes mellitus Tipo 1 (E102-E108).
               − Diabetes mellitus Tipo 2 (E112-E118).
               − Diabetes mellitus especificada (E132-138).
                        *Los códigos de elección deben ser los comprendidos entre E102-E108,

              • En el 2º casillero registre cualquiera de los siguientes diagnósticos:
              • Glucosa de tira reactiva (82948) Valor de glucosa en mg/dl LAB
                En los casos en los que el valor excede los parámetros del glucómetro escribir: ALT

              • En el 3º casillero registre Examen de presión arterial (99199.22)
                En el casillero de LAB
                  En la primera columna colocar el valor de la presión arterial sistólica.
                  En la segunda columna colocar el valor de la presión arterial diastólica.

              Para el ítem Tipo de diagnóstico anote:
              • En el 1º casillero marque “R” de diagnóstico repetido.
              • En el 2º, 3º y 4º casillero marque “D” de diagnóstico definitivo.

                D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE               VALOR
                               FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                     CÓDIGO
  DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                   ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO               LAB
                                                                                                                                        Y ACTIVIDADES DE SALUD                                               CIE/CPMSS
         GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R           1º     2º 3º
 NOMBRES Y APELLIDOS PACIENTE:
        (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______
                                                                                                                                Diabetes Mellitus tipo 2, con complicaciones no
              52146387
                                  2           Cajamarca              A    M
                                                                                 PC                PESO    78      N    N 1.                                                      P   D   R                    E118
                                                                                                                                especificadas
               854255                                        56 M               Pab       92       TALLA   160     C    C   2. Dosaje de glucosa en sangre                        P   D   R   89              82947
                                 58                                       F
                                                                     D          Ppreg               Hb             R    R   3. Tamizaje de la presión arterial                    P   D   R 110 70           99199.22

Registro de consulta para tratamiento y evaluación del paciente diabético

             En el ítem Diagnóstico motivo de consulta y/o actividad de salud:
             • En el 1º casillero registre cualquiera de los siguientes diagnósticos:
               − Diabetes mellitus insulinodependiente, sin mención de complicación (E109).
               − Diabetes mellitus no insulinodependiente, sin mención de complicación (E119).
               − Diabetes mellitus especificada, sin mención de complicación (E139).

                  En el casillero LAB registrar “PC” de paciente que recibe controles en LAB 1 y en la

---

## Página 42

segunda columna LAB2 registrar el número de meses para los que se ha prescrito el
                 tratamiento.
                    P Ejem: 2 meses de tratamiento = PC/2
                        Actualmente el máximo valor a registrar será “3” que indica que se ha prescrito medicación
                        para los próximos 3 meses.
                        La evaluación anual usa los valores registrados en LAB2 para evaluar la continuidad de
                        tratamiento a lo largo del tiempo
               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE               VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                     CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO               LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                               CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R           1º     2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______
                                                                                                                               Diabetes Mellitus tipo 2, con complicaciones no
             52146387
                                 2           Cajamarca              A    M
                                                                                PC                PESO    78      N    N 1.                                                      P   D   R   PC     3         E118
                                                                                                                               especificadas
              854255                                        56    M            Pab       92       TALLA   160     C    C   2. Dosaje de Hemoglobina glicosilada                  P   D   R   92              83036
                                58                                       F
                                                                    D          Ppreg               Hb             R    R   3. Tamizaje de la presión arterial                    P   D   R 110 70           99199.22

            • En el 2º casillero registre:
              - Glucosa en sangre (82947) en Ayunas
                         ó
              - Dosaje de hemoglobina glucosilada (83036) *prueba de elección

            En el ítem Lab Colocar Valor de
                  - Glucosa en mg/dl
                      ó
                  - Hb A1c% x10
              Ejemplo: HbA1c%: 9.2=92

            • En el 3º casillero registre Examen de presión arterial 99199.22
                En el campo LAB registre el valor de la presión arterial.
                En la primera columna colocar el valor de la presión arterial sistólica.
                En la segunda columna colocar el valor de la presión arterial diastólica.

            Para el ítem Tipo de diagnóstico anote:
            En el 1º casillero marque “R” de diagnóstico repetido.
            En el 2º y 3º casillero marque “D” de diagnóstico definitivo.
              En el ítem Lab

             Atención integral especializada según especialidades

                 UPS NEFROLOGÍA

               En el ítem Diagnóstico motivo de consulta y/o actividad de salud
             • En el 1º casillero registre la complicación o complicaciones de diabetes por la que acude
               el paciente:
             − Diabetes Mellitus tipo 1 con complicaciones renales(E102)

---

## Página 43

− Diabetes Mellitus tipo 2 con complicaciones renales(E112)
                 − Otra Diabetes Mellitus especificada con complicaciones renales(E132)

                 ▪        Pacientes con nefropatía diabética incipiente y proteinuria:
                          En el 2° Casillero cuando se tiene proteinuria A2
                           • Estadio 1 TFG >90 (N181)
                           • Estadio 2 TFG 60- (N182)

                          En el 3° Casillero colocar Albuminuria (R80)

                          Para el ítem Tipo de diagnóstico
                           • En el 1º casillero marque “R” de diagnóstico repetido.
                           • En el 2º casillero marque “D” de diagnóstico definitivo.
                           • En el 3º casillero marque “D” de diagnóstico definitivo.

                          En el ítem Lab: No aplica en este ejemplo.
               D.N.I.                          DISTRITO DE                           PERIM ETRO          EVALUACION  ESTA- SER-                                                  TIPO DE              VALOR
                              FINANC.                                                 CEFALICO-                                 DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                    CÓDIGO
  DIA     HISTORIA CLINICA                    PROCEDENCIA       EDAD       SEXO    ABDOM INAL -PESO
                                                                                                       ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO              LAB
                                                                                                                                            Y ACTIVIDADES DE SALUD                                              CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA        CENTRO POBLADO                         PREGESTACIONAL      A HEMOGLOBINA                                                           P    D R          1º     2º 3º
NOMBRES Y APELLIDOS PACIENTE:
         (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                     FECHA DE ULTIMA REGLA: ____/____/______
                                                                                                                                      Diabetes Mellitus tipo 2, con complicaciones
               52146387
                                   2           Cajamarca               A    M
                                                                                    PC                 PESO    78      N    N 1.                                                     P   D   R                     E112
                                                                                                                                      renales
                854255                                         56     M            Pab       92       TALLA    160     C    C    2. Enfermedad renal crónica etapa 3                 P   D   R                    N183
                                  58                                         F
                                                                       D          Ppreg                 Hb             R    R    3. Albuminuria                                      P   D   R                    R80X

                ▪ Pacientes con nefropatía diabética establecida:

                • En el 2º casillero registre el estadio 3, 4 o 5.
                • Estadio 3 cuando la tasa de Filtración Glomerular (TFG) está entre 30-59 mL/min (N183)
                • Estadio 4, cuando las tasas de Filtración Glomerular (TFG) está entre 15-29 mL/min
                  (N184)
                • Estadio 5 cuando la TFG es <15 (N185)

                En el 3° casillero con o Sin R80 según presencia de Albuminuria asociada

                Para el ítem Tipo de diagnóstico
                • En el 1º casillero marque “R” de diagnóstico repetido.
                • En el 2º casillero marque “D” de diagnóstico definitivo.

               D.N.I.                         DISTRITO DE                           PERIM ETRO          EVALUACION  ESTA- SER-                                                  TIPO DE               VALOR
                              FINANC.                                                CEFALICO-                                 DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                     CÓDIGO
 DIA      HISTORIA CLINICA                   PROCEDENCIA       EDAD        SEXO   ABDOM INAL -PESO
                                                                                                      ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO               LAB
                                                                                                                                           Y ACTIVIDADES DE SALUD                                               CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA       CENTRO POBLADO                         PREGESTACIONAL      A HEMOGLOBINA                                                           P    D R           1º     2º 3º
NOMBRES Y APELLIDOS PACIENTE:
        (*)FECHA DE NACIMIENTO: _____/____/______            FECHA ULTIMO RESULTADO DE Hb: _____/____/______                    FECHA DE ULTIMA REGLA: ____/____/______
                                                                                                                                     Diabetes Mellitus tipo 2, con complicaciones
              52146387
                                  2           Cajamarca               A     M
                                                                                   PC                 PESO    78      N    N 1.                                                      P   D   R                    E112
                                                                                                                                     renales
               854255                                         56 M                Pab       92        TALLA   160     C    C    2. Enfermedad renal crónica etapa 3                  P   D   R                    N183
                                 58                                         F
                                                                      D           Ppreg                Hb             R    R    3.                                                   P   D   R

                Registro de pruebas de laboratorio para evaluación de la función renal
                Evaluación de la función renal
                     a. 2° casilla Dosaje de creatinina en sangre (82565) llenar en el campo LAB la TFG estimada

---

## Página 44

mediante fórmula
                                  3° casilla Dosaje de Albúmina en orina, microalbúmina, cuantitativa 82043 llenar en el
                                  campo LAB el valor del Ratio Albumina Creatinuria

               UPS Neurología

                       En el ítem Diagnóstico motivo de consulta y/o actividad de salud
                       • En el 1º casillero registre la complicación o complicaciones de diabetes por la que acude
                         el paciente:
                          − Diabetes Mellitus tipo 1 con complicaciones neurológicas(E104)
                          − Diabetes Mellitus tipo 2 con complicaciones neurológicas (E114)
                          − Otra Diabetes Mellitus especificada con complicaciones neurológicas (E134)

                   • En el 2º casillero registre la complicación o complicaciones de diabetes por la que acude
                          el paciente:
                       - Mononeuropatía diabética ( G590 )
                       - Polineuropatía Diabética (G632-Componente de pie diabético)
                       - Neuropatía autonómica en enfermedades Metabólicas y endocrinas (G990)
               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE             VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                   CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO             LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                             CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R         1º     2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______
                                                                                                                                Diabetes Mellitus tipo 2, con complicaciones
             52146387
                                 2           Cajamarca              A    M
                                                                                PC                PESO    78      N    N 1.                                                    P   D   R                    E114
                                                                                                                                neurológicas
              854255                                        56 M               Pab       92       TALLA   160     C    C   2. Mononeuropatía diabética                         P   D   R                    G632
                                58                                       F
                                                                    D          Ppreg               Hb             R    R   3.                                                  P   D   R

                  UPS cardiología o cardiovascular

                  En el ítem Diagnóstico motivo de consulta y/o actividad de salud
                  • En el 1º casillero registre la complicación o complicaciones de diabetes por la que acude
                  el paciente:
                  − Diabetes Mellitus tipo 1 con complicaciones Cardiológicas (E105 ó E106)
                  − Diabetes Mellitus tipo 2 con complicaciones Cardiológicas (E115 ó E106)
                  − Otra Diabetes Mellitus especificada con complicaciones Cardiológicas (E135 ó E106)

                  • En el 2º casillero registre la complicación o complicaciones de diabetes por la que acude
                  el paciente:
                  - Angiopatía periférica en enfermedades clasificadas en otra parte (I79.2)
                  - Enfermedad isquémica crónica del corazón (I25)
                  - Enfermedad cardiovascular, no especificada (I56.1)
               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE             VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                   CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO             LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                             CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R         1º     2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______
                                                                                                                                Diabetes Mellitus tipo 2, con otras
             52146387
                                 2           Cajamarca              A    M
                                                                                PC                PESO    78      N    N 1.                                                    P   D   R                    E116
                                                                                                                                complicaciones especificadas
              854255                                        56 M               Pab       92       TALLA   160     C    C   2. Enfermedad ateroesclerótica del corazón          P   D   R                   I125.1
                                58                                       F
                                                                    D          Ppreg               Hb             R    R   3.                                                  P   D   R

---

## Página 45

UPS Oftalmología

   •        Diagnóstico de Retinopatía Diabética (RD)
                En el ítem: Diagnóstico motivo de consulta y/o Actividad de Salud, se registra por ejemplo:
                *PARA MAYOR DETALLE CONSULTAR EL MANUAL DEL COMPONENTE DE SALUD OCULAR EN LO CORRESPONDIENTE A
                RETINOPATÍA DIABÉTICA:

           •       En la 1° fila, registrar el diagnóstico:
                   - Diabetes mellitus tipo 1, con complicaciones oftálmicas (E103)
                   - Diabetes mellitus tipo 2, con complicaciones oftálmicas (E113)
                   - Diabetes mellitus no especificada, con complicaciones oftálmicas (E143)
                   - Desprendimiento de retina por tracción (H334)
                   - Trastorno de la retina, no especificado (H359)
                   - Hemorragia retiniana (H356)
                   - Retinopatía diabética (H360)
                   - Hemorragia del vítreo (H431)

           •       En la 2° fila, registrar el procedimiento realizado:
                   - Oftalmoscopia indirecta (92226)
                   - Fotografía de la Retina o Retino grafía (92250)
                   - Angiografía con fluoresceína (92235)
                   - Tomografía de Coherencia Óptica - OCT (92133)

                            En el ítem: Tipo de diagnóstico, marcar:
                               •         En la 1° fila, marque siempre “D” cuando se diagnóstica por primera vez y en los controles
                                         marque “R”.
                               •         En la 2° fila, marque siempre “D” por actividad y procedimiento realizado
                D.N.I.                         DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE             VALOR
                               FINANC.                                              CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                   CÓDIGO
  DIA      HISTORIA CLINICA                   PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                    ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO             LAB
                                                                                                                                         Y ACTIVIDADES DE SALUD                                             CIE/CPMSS
         GESTANTE/PUERPERA      ETNIA       CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R         1º     2º 3º
 NOMBRES Y APELLIDOS PACIENTE:
         (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______

               52146387
                                    2          Cajamarca              A    M
                                                                                  PC                PESO    70      N    N 1. Hemorragia retiniana                              P   D    R                    H356

                854255                                        62      M           Pab      89       TALLA   154     C    C   2. Oftalmoscopía indirecta                         P   D    R                   92226
                                   58                                      F
                                                                      D          Ppreg               Hb             R    R                                                         P D
                                                                                                                             3. Diabetes mellitus tipo 2 con complicaciones oftálmicas   R                    E113

               D.N.I.                          DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE             VALOR
                              FINANC.                                               CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                    CÓDIGO
 DIA      HISTORIA CLINICA                    PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                    ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO             LAB
                                                                                                                                         Y ACTIVIDADES DE SALUD                                              CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA        CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R         1º     2º 3º
NOMBRES Y APELLIDOS PACIENTE:
        (*)FECHA DE NACIMIENTO: _____/____/______            FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______

               15925865
                                   1                 Lima             A    M
                                                                                  PC                PESO    54      N    N 1. Retinopatía diabética                             P    D   R                    H36.0

                26582                                         18 M               Pab       78       TALLA   160     C    C   2. Retinografía                                    P    D   R                    92250
                                   58                                      F
                                                                      D          Ppreg               Hb             R    R                                                         P D
                                                                                                                             3. Diabetes mellitus tipo 1 con complicaciones oftálmicas   R                     E103

                    Pacientes en manejo especializado por otras comorbilidades
                    Para pacientes manejados en hospitales o institutos por comorbilidades no asociadas a la
                    diabetes, pero que puedan complicar la enfermedad, el responsable del manejo del
                    paciente debe registrar el tipo de problema asociado, y se debe asegurar una atención por
                    la UPSS correspondiente.

                   En el 1° Casillero colocar según el tipo de Diabetes Mellitus

### Tablas estructuradas de la página

| Columna 1 | Columna 2 |
| --- | --- |
| RETINOPATÍA DIABÉTICA: |  |
| En la 1° fila, registrar el diagnóstico: |  |
| - | Diabetes mellitus tipo 1, con complicaciones oftálmicas (E103) |
| - | Diabetes mellitus tipo 2, con complicaciones oftálmicas (E113) |
| - | Diabetes mellitus no especificada, con complicaciones oftálmicas (E143) |
| - | Desprendimiento de retina por tracción (H334) |
| - | Trastorno de la retina, no especificado (H359) |
| - | Hemorragia retiniana (H356) |
| - | Retinopatía diabética (H360) |
| - | Hemorragia del vítreo (H431) |

---

## Página 46

•       Diabetes Tipo 1 E108
            •       Diabetes Tipo2 E118

             • En el 2° Casillero Colocar el diagnóstico que complica el manejo del paciente en el primer
               nivel
               Por Ejemplo: Esquizofrenia Paranoide (F200)
               Enfermedad de Parkinson (G20)

                 En ítem LAB
                 En 2° casillero colocar C (comorbilidad).
                 D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE       VALOR
                                FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                              CÓDIGO
   DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                    ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO       LAB
                                                                                                                                         Y ACTIVIDADES DE SALUD                                        CIE/CPMSS
          GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R     1º   2º 3º
  NOMBRES Y APELLIDOS PACIENTE:
         (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______

                15925865
                                   1           Cajamarca              A    M
                                                                                  PC                PESO    70      N    N 1. Diabetes mellitus tipo 2 sin complicaciones    P   D   R                     E118

                 26582                                        56 M               Pab       88       TALLA   169     C    C   2. Enfermedad de parkinson                      P   D   R   C                 G20X
                                  58                                       F
                                                                      D          Ppreg               Hb             R    R   3.                                              P   D   R

Subproducto 5001705: Valoración de complicaciones en personas con diabetes

     Intervención dirigida a personas con diagnóstico definitivo de diabetes que requieren recibir
     la valoración inicial o anual de sus complicaciones/comorbilidades tardías de la enfermedad.

     Al menos 1 vez al año, se realizarán una consulta para valoración de complicaciones y
     comorbilidades en el servicio correspondiente, incluido mediante referencia o teleapoyo
     diagnóstico.

      Se brinda en establecimientos de salud categoría a partir del I-4.
     Incluye:
     -Al menos 1 vez al año creatinina en sangre, creatinina en orina, albuminuria
     -Fondo de ojo al momento del diagnóstico y luego según plan cada 1 o 2 años, valoración de
     agudeza visual 1 vez al año
     -Al menos 1 vez al año valoración de pie diabético
     -Seguimiento de colesterol en sangre

     Otros procedimientos según criterio médico.

                         Procedimiento                                                          Códigos a usar                                                         Actividades incluye

                                                                                                                                                     Inspección de pie, palpar pulsos
                                                                                           Evaluación del pie                                        periféricos y test de monofilamento y
                                                                                                                                                     diapasón
              Evaluación de pie diabético                                                 diabético (99214.07)
                                                                                                                                                          •    En el registro de LAB registrar
                                                                                                                                                               N si el examen es normal
                                                                                                                                                          •    Registrar A si el examen es
                                                                                                                                                               anormal

---

## Página 47

Dosaje de creatinina y cálculo de la
                                                                            Tasa de filtración glomerular con
                                                                            fórmula (CKD -EPI 2021 ó MDRD4)
                                                                            + Dosaje de albuminuria
                                    1.   Dosaje de creatinina en sangre
                                                                                 •    En caso de recursos
                                         (82565)
                                                                                      limitados se puede usar tira
                                    2.   Dosaje de albúmina con
                                                                                      reactiva 82044
                                         cualquiera de las siguientes
                                                                                 •     El test de elección es el
                                              a. Dosaje de albúmina en
                                                                                       dosaje de albúmina en orina
                                                   orina, microalbúmina
 Evaluación de función renal                                                           y creatinina en orina,
                                                   semicuantitativa (p ej
                                                                                       calculando el RACo 82043
                                                   ensayo con tira
                                                                            Registrar los valores en el campo LAB
                                                   reactiva) 82044
                                                                                 •    Valor de la TFG en 82565
                                              b. Dosaje de Albúmina en
                                                                                      prueba de creatinina
                                                   orina, microalbúmina,
                                                                                 •    0, 1, 2 o 3 si es prueba
                                                   cuantitativa 82043
                                                                                      semicuantitativa (82044)
                                                                                 •    El valor de laboratorio RACo
                                                                                      (82043)

                                                                            Es preferible la evaluación por
                               Fotografía de la Retina ó Retinografía       oftalmología, se puede emplear
 Evaluación de retinopatía
                               (92250)                                      tecnologías de telemedicina siempre
 diabética
                               Ó Oftalmoscopia indirecta (92226)            que esté disponible.
                                                                            Temporalidad de 1 o 2 veces al año

                               Determinacion directa de lipoproteina de     Registrar los valores en el campo LAB
 Evaluación de dislipidemia    baja densidad (LDL colesterol) (83721)       del
                                                                                 •    LDL colesterol 83721

En el ítem Diagnóstico motivo de consulta y/o actividad de salud
• En el 1º registrar cualquiera de los siguientes diagnósticos.
     −    Diabetes Mellitus tipo 1 (E10)
     −    Diabetes Mellitus tipo 2 (E11)
     −    Otras Diabetes Mellitus Especificadas (E13)
     −    Diabetes Mellitus, no Especificada (E14)

   • En el 2º y demás casilleros registre los diagnósticos de las complicaciones si estas son renales,
   oftalmológicas o polineuropatía diabética.
   1 vez al año realizar
       A. Evaluación del pie diabético (99214.07)
       B. Tamizaje de función renal
           a. 2° casilla: Dosaje de creatinina en sangre (82565) llenar en el campo LAB la TFG
                estimada mediante fórmula
                    3° casilla: Dosaje de albúmina en orina, microalbúmina semicuantitativa (p ej
                    ensayo con tira reactiva) 82044 llenar en el campo lab el número de cruces
                    encontrados
                    Ó
           b. 2° casilla Dosaje de creatinina en sangre (82565) llenar en el campo LAB la TFG estimada

---

## Página 48

mediante fórmula
                             3° casilla Dosaje de Albúmina en orina, microalbúmina, cuantitativa 82043 llenar
                             en el campo LAB el valor del Ratio Albumina Creatinuria
                 C. Determinacion directa de lipoproteina de baja densidad (LDL colesterol) (83721)

                 D. Paciente referido a Oftalmología llenar según manual de Salud Ocular Pejmp: Fotografía de la
                    Retina ó Retinografía (92250) o
                     Evaluación con oftalmoscopio en el establecimiento: Oftalmoscopia indirecta (92226)

            Para el ítem Tipo de diagnóstico
               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE           VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                 CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO           LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                           CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R       1º     2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______
                                                                                                                                Diabetes mellitus tipo 2 sin mención de
             15925865
                                 1           Cajamarca              A    M
                                                                                PC                PESO    70      N    N 1.                                                  P   D   R                    E119
                                                                                                                                complicaciones
               26582                                        56 M               Pab       88       TALLA   167     C    C   2. Evaluación del pie diabético                   P   D   R   N              99214.07
                                58                                       F
                                                                    D          Ppreg               Hb             R    R   3.                                                P   D   R

            En el 1º y 2º casilleros marque “D” de diagnóstico definitivo

               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE           VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                 CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO           LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                           CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R       1º     2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______
                                                                                                                                Diabetes mellitus tipo 2 sin mención de
             15925865
                                 2           Cajamarca              A    M
                                                                                PC                PESO    70      N    N 1.                                                  P   D   R                    E119
                                                                                                                                complicaciones
               26582                                        70 M               Pab       88       TALLA   167     C    C   2. Dosaje de creatinina en sangre                 P   D   R   78              82565
                                58                                       F                                                      Dosaje de albúmina en orina, microalbúmina
                                                                    D          Ppreg               Hb             R    R   3.                                                P   D   R   2               82044
                                                                                                                                semicuantitativa

               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE           VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                 CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO           LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                           CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R       1º     2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______
                                                                                                                                Diabetes mellitus tipo 2 sin mención de
             15925865
                                 2           Cajamarca              A    M
                                                                                PC                PESO    70      N    N 1.                                                  P   D   R                   H36.0
                                                                                                                                complicaciones
               26582                                        70 M               Pab       88       TALLA   167     C    C   2. Dosaje de creatinina en sangre                 P   D   R   78              82565
                                58                                       F                                                      Dosaje de albúmina en orina, microalbúmina
                                                                    D          Ppreg               Hb             R    R   3.                                                P   D   R   14              82043
                                                                                                                                cuantitativa

            Registro para la indicación de despistaje de retinopatía diabética
         Pacientes que son evaluados en un establecimiento de salud sin capacidad instalada para
         evaluar retina, registra el examen de agudeza visual y el diagnóstico del tipo de diabetes,
         con la indicación de referencia
            En el ítem: Diagnóstico motivo de consulta y/o Actividad de Salud, registrar:

       •       En la 1° fila, registrar el diagnóstico:
                - Diabetes mellitus tipo 1, sin mención de complicación (E109)
                - Diabetes mellitus tipo 1, con complicaciones oftálmicas (E103)
                - Diabetes mellitus tipo 1, con complicaciones no especificadas (E108)
                - Diabetes mellitus tipo 2, sin mención de complicación (E119)
                - Diabetes mellitus tipo 2, con complicaciones oftálmicas (E113)
                - Diabetes mellitus tipo 2, con complicaciones no especificadas (E118)
                - Diabetes mellitus especificada, con complicaciones oftálmicas (E133)
                - Diabetes mellitus especificada, sin mención de complicación (E139)
                - Retinopatía diabética (Reevaluación de caso, se registra como “R” ) (H360)

                         Si el paciente es referido a otro establecimiento en el ítem LAB registrar RF

---

## Página 49

•       En la 2° fila, registrar el procedimiento realizado:
                   Determinación de la agudeza visual (99173)
           En la 2° fila, columna 1 se registra el resultado de la evaluación del OD y en la columna se
           registra el resultado de la evaluación del OI, usando las nomenclaturas de agudeza visual.

  •        En caso se haya realizado en la 3° fila registrar el tipo de examen realizado
             - Fotografía de la Retina ó Retino grafía (92250) o
             - Oftalmoscopia directa (92225)
       *Cabe señalar que se puede considerar otros procedimientos u actividades según criterio médico y capacidad resolutiva.

       En el ítem: Tipo de diagnóstico, marcar:
           •     En la 1° fila, marque “D” para el diagnóstico de la morbilidad por tratarse de caso.
           •     En la 2º fila, marque siempre “D” por actividad y procedimiento realizado.

       En el ítem: Lab, registrar:
        • En la 1° fila, columna 1 Lab. registre “RF” para indicar la referencia realizada.
        • En la 2° fila, columna 1 Lab. registre el resultado de la evaluación del OJO DERECHO y en
           la columna 2 Lab. registre el resultado de la evaluación del OJO IZQUIERDO según
           corresponda, usando las nomenclaturas: A= Anormal o N= Normal

               D.N.I.                         DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE              VALOR
                              FINANC.                                              CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                     CÓDIGO
 DIA      HISTORIA CLINICA                   PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                   ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO              LAB
                                                                                                                                        Y ACTIVIDADES DE SALUD                                               CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA       CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R          1º     2º 3º
NOMBRES Y APELLIDOS PACIENTE:
        (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______
                                                                                                                               Diabetes mellitus tipo 2, con complicaciones no
               15925865
                                  2             Camaná               A    M
                                                                                 PC                PESO    50      N    N 1.                                                     P   D   R   RF                  E118
                                                                                                                               especificadas
                26582                                        52    M            Pab       80       TALLA   152     C    C   2. Agudeza visual                                    P   D   R   20 400              99173
                                 58                                       F
                                                                     D          Ppreg               Hb             R    R   3. Retinografía                                      P   D   R                       92250

           Subproducto 5001707: Manejo De Enfermedad Renal Diabética

           Definición Operacional: Atenciones del primer nivel de atención, orientada al seguimiento
           y manejo de pacientes con Nefropatía diabética en sus etapas iniciales. Los pacientes con
           TFG >60 sin proteinuria deben ser manejados en el primer nivel de atención por personal
           capacitado.
           *Las pautas para el manejo de la nefropatía diabética se realiza según lo consignado en las vías de abordaje
           HEARTS y en otros documentos técnicos vigentes.
           **Para el registro de manejo especializado, considerar lo planteado en el subproducto de “PACIENTES
           DIABETICOS CON TRATAMIENTO ESPECIALIZADO”

           ✓ Pacientes con TFG>45 (ERC IIIa) cuando no tengan otros factores de riesgo, ni
             proteinuria pueden ser seguidos en el Primer nivel de atención

               En el ítem Diagnóstico motivo de consulta y/o actividad de salud
               En el 1º casillero registre la complicación o complicaciones de diabetes por la que acude el
               paciente:
                • Diabetes Mellitus tipo 1 con complicaciones renales(E102)

### Tablas estructuradas de la página

| * | Cabe señalar que se puede considerar otros procedimientos u actividades según criterio médico y capacidad resolutiva. |  |
| --- | --- | --- |
|  | En el ítem: Tipo de diagnóstico, marcar: |  |
|  | • | En la 1° fila, marque “D” para el diagnóstico de la morbilidad por tratarse de caso. |
|  | • | En la 2º fila, marque siempre “D” por actividad y procedimiento realizado. |
|  | En el ítem: Lab, registrar: |  |
|  | • | En la 1° fila, columna 1 Lab. registre “RF” para indicar la referencia realizada. |
|  | • | En la 2° fila, columna 1 Lab. registre el resultado de la evaluación del OJO DERECHO y en |
|  |  | la columna 2 Lab. registre el resultado de la evaluación del OJO IZQUIERDO según |
|  |  | corresponda, usando las nomenclaturas: A= Anormal o N= Normal |

---

## Página 50

• Diabetes Mellitus tipo 2 con complicaciones renales(E112)
                    • Otra Diabetes Mellitus especificada con complicaciones renales(E132)
                    • Diabetes Mellitus no especificada, con complicaciones renales (E142)

               Pacientes con nefropatía diabética incipiente sin proteinuria
               En el 2° Casillero cuando se tiene proteinuria categoría A1, A2 ó A3 según tabla de Vía
               Hearts
                • Estadio 1 TFG >90                                  (N181)
                • Estadio 2 TFG 60-89                                ( N182)
                • Estadio 3 cuando (TFG) está entre 30-59 mL/min (N183)

                        Pacientes con nefropatía diabética establecida por debajo de 45 deben ser referidos
                        Como parte de la evaluación al menos una valoración de función renal al año.

                       En el 3er casillero: Dosaje de creatinina en sangre (82565) en el valor LAB se registra el
                       valor de TFG calculada

                       En el 4to casillero:
                             •          Dosaje de albúmina en orina, microalbúmina semicuantitativa (p ej ensayo con tira
                                        reactiva) 82044 En el valor LAB registrar (0, 1, 2, 3 ó 4) según valor de cruces en
                                        tira reactiva
                                        Ó

                             • Dosaje de Albúmina en orina, microalbúmina, cuantitativa 82043 En el valor LAB
                                        registrar RACo medido

                       Para el ítem Tipo de diagnóstico
                       • En el 1º casillero marque “R” de diagnóstico repetido.
                       • En el 2º casillero marque “D” de diagnóstico definitivo si es diagnóstico o “R” si es
                         repetitivo
                       • En la 3° casilla marcar D

               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE             VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                   CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO   ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO             LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                             CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R         1º     2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______
                                                                                                                                Diabetes Mellitus tipo 2, con complicaciones
             15925865
                                 1                 Lima             A    M
                                                                                PC                PESO    70      N    N 1.                                                    P   D   R                    E112
                                                                                                                                renales
               26582                                        48 M               Pab       82       TALLA   167     C    C   2. Enfermedad renal crónica etapa 3                 P   D   R                    N181
                                 58                                      F
                                                                    D          Ppreg               Hb             R    R   3. Dosaje de creatinina en sangre                   P   D   R   78              82565
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                 FECHA DE ULTIMA REGLA: ____/____/______
                                                                                                                                Dosaje de albúmina en orina, microalbúmina
                                                                    A    M
                                                                                PC                PESO            N    N 1.                                                    P   D   R   14              82043
                                                                                                                                cuantitativa
                                                                  M            Pab                TALLA           C    C   2.                                                  P   D   R   78
                                                                         F
                                                                    D          Ppreg               Hb             R    R   3.                                                  P   D   R   14

---

## Página 51

REGISTRO LOS SERVICIOS DE TELEORIENTACIÓN Y TELEMONITOREO

      A. Valoración Clínica y Tamizaje laboratorial de Enfermedades Crónicas No Transmisibles
         (Valoración Clínica De Factores De Riesgo)

        Definición Operacional. - Conjunto de actividades para completar la valoración clínica
        de factores de riesgo, orientados a dar mayor flexibilidad al sistema de salud y a los
        beneficiarios. Comprende dos grandes actividades:

            •   La valoración clínica incluye: valoración del índice de masa corporal (IMC),
                medición del perímetro abdominal, valoración de estilos de vida y medición de
                presión arterial. Se emplea 25 minutos.

            •   El tamizaje laboratorial incluye: dosaje de glucosa (idealmente en suero
                plasmático) y perfil lipídico (colesterol total, HDL, LDL calculado y triglicéridos),
                según corresponda al grupo de edad así como la lectura de resultados.

        El tamizaje de laboratorio se le debe iniciar a todos los mayores de 40 años. La
        frecuencia de este tamizaje puede variar según lo especificado por los documentos
        normativos vigentes.

        Para los adultos menores de 40 años en caso se identifique algún factor de riesgo según
        GPC también se debe realizar. Para menores de edad, la necesidad de tomar
        laboratorios se determina de manera individualizada y no se debe hacer de forma
        sistemática.

        Se puede realizar el apoyo mediante teleconsulta, telemonitoreo, teleinterconsulta
        sincrónica o asincrona como la valoración individualizada de factores de riesgo en
        menores de edad o la lectura de resultados en los establecimientos, entre otros.

        Ejemplo:
        Cuando se requiere apoyo en la valoración de riesgo de menores de edad
        En el ítem Diagnóstico motivo de consulta y/o actividad de salud anote:
        • En el 1º casillero Valoración Clínica de Factores de Riesgo Z019 y en el Lab 1 se registra
          ALT indicando que en la Valoración se ha encontrado una alteración
        • En el 2º casillero Consejería en estilos de vida saludable
        • En el 3º casillero Teleinterconsulta sincrónica y según corresponda registrar en el
          primer casillero LAB
          Lab “1” Teleconsultante
          Lab “2” Teleconsultor

      Si es la primera evaluación que recibe el paciente en el año, se registra con tipo de
      diagnóstico “D” de definitivo por parte de la unidad teleconsultante. El teleconsultor
      siempre registra con tipo de diagnóstico “R” de repetitivo

      En los casos en que sea la segunda evaluación a modo de seguimiento, se registra con tipo

---

## Página 52

de diagnóstico “R” de Repetitivo en ambas IPRES

                Teleconsultante
                       D.N.I.                             DISTRITO DE                                     PERIM ETRO          EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                                      FINANC.                                                              CEFALICO-                                 DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                                 CÓDIGO
          DIA     HISTORIA CLINICA                       PROCEDENCIA               EDAD        SEXO     ABDOM INAL -PESO
                                                                                                                            ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                                 Y ACTIVIDADES DE SALUD                                                           CIE/CPMSS
                GESTANTE/PUERPERA      ETNIA           CENTRO POBLADO                                   PREGESTACIONAL      A HEMOGLOBINA                                                           P    D R 1º 2º 3º
        NOMBRES Y APELLIDOS PACIENTE:
                 (*)FECHA DE NACIMIENTO: _____/____/______                 FECHA ULTIMO RESULTADO DE Hb: _____/____/______                                     FECHA DE ULTIMA REGLA: ____/____/______

                       85274136
                                              2           Huancayo                        A     M
                                                                                                         PC                 PESO        40       N        N 1. Examen especial NE (Valoración Clínica de FR)        P       D   R ALT                 Z019

                          45320                                                10 M                      Pab                TALLA       140      C        C    2. Consejería en estilos de vida saludable           P       D   R                 99401.13
                                           58                                                      F
                                                                                          D             Ppreg                Hb                  R        R    3. Teleinterconsulta síncrona                        P       D   R       1         99499.08

                Teleconsultor
                      D.N.I.                             DISTRITO DE                                     PERIM ETRO          EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                                     FINANC.                                                              CEFALICO-                                 DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                                 CÓDIGO
        DIA      HISTORIA CLINICA                       PROCEDENCIA            EDAD           SEXO     ABDOM INAL -PESO
                                                                                                                           ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                                Y ACTIVIDADES DE SALUD                                                           CIE/CPMSS
               GESTANTE/PUERPERA      ETNIA           CENTRO POBLADO                                   PREGESTACIONAL      A HEMOGLOBINA                                                           P    D R 1º 2º 3º
       NOMBRES Y APELLIDOS PACIENTE:
                (*)FECHA DE NACIMIENTO: _____/____/______                 FECHA ULTIMO RESULTADO DE Hb: _____/____/______                                     FECHA DE ULTIMA REGLA: ____/____/______

                      85274136
                                          2              Huancayo                     A        M
                                                                                                        PC                 PESO        40        N    N 1. Examen especial NE (Valoración Clínica de FR)        P       D       R ALT                Z019

                       45320                                               10 M                        Pab                 TALLA       140       C    C       2. Consejería en estilos de vida saludable        P       D       R                99401.13
                                         58                                                    F
                                                                                      D                Ppreg                Hb                   R    R       3. Teleinterconsulta síncrona                     P       D       R   2            99499.08

                Cuando el paciente ha sido evaluado previamente por personal no médico y se determina
                que es necesaria un tamizaje de laboratorio:

                En el ítem: Diagnóstico motivo de consulta y/o Actividad de salud registrar:
                • En el 1° casillero se colocará la Valoración Clínica de Factores de Riesgo, según
                  corresponda.
                • En el 2° se consignarán los factores de riesgo que se identifiquen. (sobrepeso, obesidad)
                • En el 3° casillero, registra la solicitud de exámenes de laboratorio (glucosa y perfil
                  lipídico).
                • En el último casillero, registrar el servicio realizado Telemonitoreo 99499.10 ó
                  teleinterconsulta 99499. según sea el caso

                En el ítem: Tipo de diagnóstico
                • En el 1° casillero marque “R” de diagnóstico definitivo

                En el ítem LAB anote:

               D.N.I.                                DISTRITO DE                                PERIM ETRO           EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                                            CEFALICO-                                  DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                                    CÓDIGO
 DIA      HISTORIA CLINICA                          PROCEDENCIA         EDAD        SEXO      ABDOM INAL -PESO     ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                        Y ACTIVIDADES DE SALUD                                                              CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA              CENTRO POBLADO                              PREGESTACIONAL       A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
         (*)FECHA DE NACIMIENTO: _____/____/______                   FECHA ULTIMO RESULTADO DE Hb: _____/____/______                                 FECHA DE ULTIMA REGLA: ____/____/______

                85274136
                                     2               Huancayo                  A     M
                                                                                               PC                  PESO          70          N   N 1. Examen especial NE (Valoración Clínica de FR)         P   D       R ALT                 Z019

                  45320                                                68 M                    Pab                TALLA          166         C   C   2. Sobrepeso                                           P   D       R                    E6690
                                    58                                                F
                                                                               D              Ppreg                 Hb                       R   R   3. Solicitud de examen de laboratorio                  P   D       R                     Z017
NOMBRES Y APELLIDOS PACIENTE:
         (*)FECHA DE NACIMIENTO: _____/____/______                   FECHA ULTIMO RESULTADO DE Hb: _____/____/______                                 FECHA DE ULTIMA REGLA: ____/____/______

                                                                               A     M
                                                                                               PC                  PESO                      N   N 1. Consejería en estilos de vida saludable               P   D       R                   99401.13

                                                                            M                  Pab                TALLA                      C   C   2. Telemonitoreo                                       P   D       R                   99499.10
                                                                                      F
                                                                               D              Ppreg                 Hb                       R   R   3.                                                     P   D       R

                  Evaluación y entrega de Resultados a través de Telemonitoreo

                      Segunda Atención luego de haber encontrado factores de riesgo en la
                      teleorientación:

---

## Página 53

En el ítem Diagnóstico motivo de consulta y/o Actividad de salud registrar:
                       • Registre cualquiera de los siguientes códigos según corresponda:

                       En la 1° fila registrar el seguimiento de la valoración clínica Z019 con tipo de Dx “R”

                       Luego registrar los valores y códigos disponibles
                       Glucosa en sangre (82947) ó Glucosa en tira reactiva (82948)
                        - Colesterol LDL (83721)
                        - Colesterol Total (82465)
                        - Triglicéridos (84478)

                        En el ítem Lab:
                          • Colocar resultado de laboratorio En el 3° casillero se registrará el servicio realizado
                            Telemonitoreo

En el ítem: Tipo de diagnóstico
          • En el 1° casillero marque “R” de repetido
          • En el 2° casillero marque “D”, de definitivo
          • En el 3° casillero maque “D” de definitivo
               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                       CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO   ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                 CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                FECHA DE ULTIMA REGLA: ____/____/______

             85274136
                                 2            Huancayo              A    M
                                                                                PC                PESO    58     N    N 1. Examen especial NE (Valoración Clínica de FR)   P   D   R ALT        Z019

               45320                                        39 M               Pab       90       TALLA   148    C    C   2. Glucosa en sangre                             P   D   R 110       82947
                                58                                       F
                                                                    D          Ppreg               Hb            R    R   3. Colesterol LDL                                P   D   R 200       83721
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                FECHA DE ULTIMA REGLA: ____/____/______

                                                                    A    M
                                                                                PC                PESO           N    N 1. Colesterol total                                P   D   R 250       82465

                                                                  M            Pab                TALLA          C    C   2. Triglicéridos                                 P   D   R 185       84478
                                                                         F
                                                                    D          Ppreg               Hb            R    R   3. Telemonitoreo                                 P   D   R          99499.10

               B. Seguimiento de pacientes con diagnóstico de Hipertensión arterial a través de
                       Telemedicina

                       Intervención dirigida a personas con hipertensión arterial, con la finalidad de
                       complementar el tratamiento integral para el control de su enfermedad que han sido
                       tipificados como controlados. Incluye el manejo de complicaciones y multimorbilidades
                       según riesgo cardiovascular

                       Cuando no tiene tensiómetro para la toma de presión arterial
                       En este tipo de pacientes las consultas de telemonitoreo se realizan orientadas a
                       continuar tratamiento en pacientes controlados, se puede pactar visitas domiciliarias,
                       se programan las citas de control presencial según riesgo cardiovascular y en casos
                       especiales de pacientes bien controlados evidenciados, se puede prescribir medicación.

                       En el ítem: Diagnóstico motivo de consulta y/o Actividad de salud registrar:
                       • En el 1° casillero se colocará el diagnostico Hipertensión arterial.
                       • En el 2° casillero Telemonitoreo

---

## Página 54

En el ítem: Tipo de diagnóstico
                    • Marcar siempre “D”
              Si al paciente se le ha llamado para agendar una cita o como seguimiento
                  D.N.I.                           DISTRITO DE                                   PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                                 FINANC.                                                          CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                             CÓDIGO
       DIA   HISTORIA CLINICA                     PROCEDENCIA           EDAD           SEXO    ABDOM INAL -PESO
                                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                       Y ACTIVIDADES DE SALUD                                                       CIE/CPMSS
           GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                                 PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
   NOMBRES Y APELLIDOS PACIENTE:
             (*)FECHA DE NACIMIENTO: _____/____/______               FECHA ULTIMO RESULTADO DE Hb: _____/____/______                                  FECHA DE ULTIMA REGLA: ____/____/______

                   7622210
                                        2                Paras                 A        M
                                                                                                  PC               PESO        71       N       N 1. Hipertensión esencial (primaria)               P       D       R                  I10X

                    85421                                              38 M                       Pab             TALLA     168         C       C     2. Telemonitoreo                              P       D       R               99499.10
                                        58                                              F
                                                                               D              Ppreg                Hb                   R       R     3.                                            P       D       R

                  En casos de contingencia específicos para personas consideradas como controladas, se
                  puede prescribir continuidad de medicación
                  D.N.I.                           DISTRITO DE                                   PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                                 FINANC.                                                          CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                             CÓDIGO
       DIA   HISTORIA CLINICA                     PROCEDENCIA           EDAD           SEXO    ABDOM INAL -PESO
                                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                       Y ACTIVIDADES DE SALUD                                                       CIE/CPMSS
           GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                                 PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
   NOMBRES Y APELLIDOS PACIENTE:
             (*)FECHA DE NACIMIENTO: _____/____/______               FECHA ULTIMO RESULTADO DE Hb: _____/____/______                                  FECHA DE ULTIMA REGLA: ____/____/______

                   16070602
                                        2            Los Olivos                A        M
                                                                                                  PC               PESO        67       N       N 1. Hipertensión esencial (primaria)               P       D       R    PC   2        I10X

                    15212                                              61 M                       Pab             TALLA     161         C       C     2. Telemonitoreo                              P       D       R               99499.10
                                        58                                              F
                                                                               D              Ppreg                Hb                   R       R     3.                                            P       D       R

                         Cuando tiene tensiómetro para la toma de presión arterial
                         Si el paciente cuenta con tensiómetro en el momento de realizar el telemonitoreo, se
                         registra los valores encontrados en el campo LAB y se realiza el registro igual que en los
                         subproductos de tratamiento de la hipertensión en caso de brindar receta electrónica.

                         En el ítem: Diagnóstico motivo de consulta y/o Actividad de salud registrar:
                         • En el 1° casillero se colocará el diagnostico de enfermedad hipertensiva
                         • En el 3° casillero se registrará el servicio realizado Telemonitoreo

                           En el ítem: Tipo de diagnóstico
                         • En el 1° casillero marcar “R”
                         • En el 2° casillero marcar “D”

                         En el ítem LAB anote:
                          Ejemplo: paciente que recibe control y receta por telemonitoreo
               D.N.I.                           DISTRITO DE                                   PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                                          CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                              CÓDIGO
 DIA      HISTORIA CLINICA                     PROCEDENCIA          EDAD       SEXO         ABDOM INAL -PESO
                                                                                                               ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                    Y ACTIVIDADES DE SALUD                                                        CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                                 PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:

         (*)FECHA DE NACIMIENTO: _____/____/______                FECHA ULTIMO RESULTADO DE Hb: _____/____/______                                   FECHA DE ULTIMA REGLA: ____/____/______

               16070602                                                    A                 PC                PESO       67        N       N 1. Hipertensión esencial (primaria)               P       D       R   PC    2         I10X
                                   2            Los Olivos                      M
                 15212                                             61 M                     Pab                TALLA      161       C       C       2. Tamizaje de presión arterial             P       D       R                 99199.22
                                   58                                              F
                                                                           D             Ppreg                    Hb                R       R       3. Telemonitoreo                            P       D       R                 99499.10

                 C. Seguimiento de pacientes con diagnóstico de Diabetes Mellitus a través de
                         Telemedicina

                         Definición Operacional. - Intervención que se brinda a personas con diabetes mellitus
                         sin complicaciones (personas con diabetes sin retinopatía, examen simple de orina con
                         proteínas negativo o microalbuminuria categoría A1 y pie diabético con evaluación de

---

## Página 55

monofilamento negativa), que han logrado alcanzar las siguientes metas de control
                       cardiometabólico:
                       Glucemia en ayunas 70 a 130 mg/dl en dos mediciones, o hemoglobina glucosilada
                       menor de 7% (o según meta terapéutica de Hb1Ac), y Presión arterial menor de 140/80
                       mmHg.

                       Cuando se identifica que no tiene exámenes de control
                       Si el paciente no cuenta con glucómetro en domicilio para realizar la medición, se le
                       solicita examen de laboratorio y se programa una atención domiciliaria para la toma de
                       muestra.

                       En el ítem Diagnóstico motivo de consulta y/o Actividad de salud registrar:
                       • En el 1° casillero se colocar el diagnóstico DM2 sin complicaciones
                       • En el 2° casillero colocar solicitud de examen de laboratorio
                       • En el 3° casillero se registrará el servicio realizado Telemonitoreo

                       En el ítem: Tipo de diagnóstico
                       • En el 1° casillero marque “R” de repetido
                       • En el 2° casillero marque “D”, de definitivo
                       • En el 3° casillero maque “D” de definitivo

               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                       CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                 CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                FECHA DE ULTIMA REGLA: ____/____/______
                                                                                                                             Diabetes mellitus tipo 2, sin mención de
             85274136
                                 2            Huancayo              A    M
                                                                                PC                PESO    70     N    N 1.                                              P   D   R               E119
                                                                                                                             complicación
               45320                                        68    M            Pab                TALLA   166    C    C   2. Solicitud de examen de laboratorio         P   D   R               Z017
                                58                                       F
                                                                    D          Ppreg               Hb            R    R   3. Telemonitoreo                              P   D   R             9949910

                        Cuando tiene resultados de laboratorio

                        Luego de haber solicitado los exámenes de laboratorio y obtener los resultados se
                        registra los valores. Sin embargo, si el paciente cuenta con glucómetro en el momento
                        de realizar el telemonitoreo, se registra los valores encontrados como N o A.

                       En el ítem: Diagnóstico motivo de consulta y/o Actividad de salud registrar:
                       • En el 1° casillero se coloca el diagnostico.
                       • En el 2° - 5°casillero registrar las actividades que se hayan realizado: entrega de
                         resultados, consejerías, etc
                       • En el último casillero se registrará el servicio realizado Telemonitoreo

---

## Página 56

D.N.I.                           DISTRITO DE                                   PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                                          CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                           CÓDIGO
 DIA      HISTORIA CLINICA                     PROCEDENCIA            EDAD        SEXO      ABDOM INAL -PESO   ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                    Y ACTIVIDADES DE SALUD                                                     CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                                 PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
        (*)FECHA DE NACIMIENTO: _____/____/______                   FECHA ULTIMO RESULTADO DE Hb: _____/____/______                       FECHA DE ULTIMA REGLA: ____/____/______
                                                                                                                                                Diabetes mellitus tipo 2, sin mención de
              85274136
                                  2             Huancayo                     A     M
                                                                                             PC                PESO      70      N   N 1.                                                      P    D       R                    E119
                                                                                                                                                complicación
               45320                                                 68 M                   Pab                TALLA     168     C   C    2. Examen de glucosa                                 P    D       R 130               82947
                                 58                                                 F
                                                                             D              Ppreg               Hb               R   R    3. Sólo interpretación e informe de electrocardiogramaP   D       R                   93010
NOMBRES Y APELLIDOS PACIENTE:
        (*)FECHA DE NACIMIENTO: _____/____/______                   FECHA ULTIMO RESULTADO DE Hb: _____/____/______                       FECHA DE ULTIMA REGLA: ____/____/______

                                                                             A     M
                                                                                             PC                PESO              N   N 1. Consejería en estilos de vida saludable              P    D       R                  99401.13

                                                                           M                Pab                TALLA             C   C    2. Telemonitoreo                                     P    D       R                  99499.10
                                                                                    F
                                                                             D              Ppreg               Hb               R   R    3.                                                   P    D       R

              D. Registro de servicios de teleconsulta

                En el ítem: Diagnóstico motivo de consulta y/o Actividad de salud registrar:
                • En el 1° casillero se colocará el diagnostico de enfermedad hipertensiva(I10) o Diabetes
                  Mellitus (E10, E11, E13, E14)
                • En el 2° y 3° casillero se registran los códigos correspondientes a toma de presión y/o
                  exámenes de laboratorio según corresponde. Cotejar con sección dedicada a cada
                  patología.
                • En el último casillero se registrará el servicio realizado Teleconsulta.

                En el ítem: Tipo de diagnóstico
                • En el 1° casillero marcar “R”
                • En el 2° casillero marcar “D”

                      D.N.I.                           DISTRITO DE                                    PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                                     FINANC.                                                           CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                                         CÓDIGO
        DIA      HISTORIA CLINICA                     PROCEDENCIA                EDAD       SEXO    ABDOM INAL -PESO
                                                                                                                       ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                                            Y ACTIVIDADES DE SALUD                                                   CIE/CPMSS
               GESTANTE/PUERPERA      ETNIA         CENTRO POBLADO                                  PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
       NOMBRES Y APELLIDOS PACIENTE:
              (*)FECHA DE NACIMIENTO: _____/____/______                   FECHA ULTIMO RESULTADO DE Hb: _____/____/______                          FECHA DE ULTIMA REGLA: ____/____/______

                    85274136
                                         2             Los Olivos                       A    M
                                                                                                     PC                PESO    67     N        N 1. Hipertensión esencial (primaria)                    P       D   R                   I10X

                       45320                                                 61 M                   Pab                TALLA   161    C        C   2. Tamizaje de presión arterial                      P       D   R 130 70         99199.22
                                        58                                                   F
                                                                                        D           Ppreg               Hb            R        R   3. Teleconsulta                                      P       D   R                99499.01

                E. Registro de servicios de teleinterconsulta

                En el cuidado de la hipertensión o diabetes, puede surgir la necesidad de consultar en
                tiempo real o diferido sobre un paciente a un médico especialista de un mayor nivel de
                atención. Para ello se registran

                En el ítem: Diagnóstico motivo de consulta y/o Actividad de salud registrar:
                • En el 1° casillero se colocará el diagnostico de enfermedad hipertensiva(I10) o Diabetes
                  Mellitus (E10, E11, E13, E14)
                • En el 2°, 3°, 4° o hasta 5° casillero se registran los códigos correspondientes a toma de
                  presión y/o exámenes auxiliares según corresponde.
                         El servicio que realiza la prueba es el que registra los exámenes auxiliares.
                         El servicio interconsultor puede registrar la lectura de resultados con Z017
                • En el último casillero se registrará el servicio realizado Teleinterconsulta.
                        Teleinterconsulta síncrona 99499.11
                        Teleinterconsulta asíncrona 99499.12
                        En los campos LAB 1 se registra:

---

## Página 57

LAB Teleinterconsultante = “1”
                          LAB Teleinterconsultor = “2”

               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                              CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                        CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                FECHA DE ULTIMA REGLA: ____/____/______

             85274136
                                 2            Los Olivos            A    M
                                                                                PC                PESO    67     N    N 1. Hipertensión esencial (primaria)                     P   D   R              I10X
                                                                                                                               Toma de electrocardiograma, sin interpretación
               45320                                        61 M               Pab                TALLA   161    C    C   2.
                                                                                                                               ni informe
                                                                                                                                                                                P   D   R             93000
                                58                                       F
                                                                    D          Ppreg               Hb            R    R   3. Teleinterconsulta síncrona                         P   D   R   1    99499.11

               D.N.I.                        DISTRITO DE                         PERIM ETRO         EVALUACION  ESTA- SER-                                                  TIPO DE  VALOR
                              FINANC.                                             CEFALICO-                                DIAGNÓSTICO MOTIVO DE CONSULTA, PROCEDIMIENTO                              CÓDIGO
 DIA      HISTORIA CLINICA                  PROCEDENCIA      EDAD       SEXO   ABDOM INAL -PESO
                                                                                                  ANTROPOMETRIC BLEC VICIO                                               DIAGNÓSTICO  LAB
                                                                                                                                       Y ACTIVIDADES DE SALUD                                        CIE/CPMSS
        GESTANTE/PUERPERA      ETNIA      CENTRO POBLADO                       PREGESTACIONAL     A HEMOGLOBINA                                                           P    D R 1º 2º 3º
NOMBRES Y APELLIDOS PACIENTE:
       (*)FECHA DE NACIMIENTO: _____/____/______           FECHA ULTIMO RESULTADO DE Hb: _____/____/______                FECHA DE ULTIMA REGLA: ____/____/______

             85274136
                                 2            Los Olivos            A    M
                                                                                PC                PESO    67     N    N 1. Hipertensión esencial (primaria)                     P   D   R              I10X
                                                                                                                               Sólo interpretación e informe de
               45320                                        61 M               Pab                TALLA   161    C    C   2.
                                                                                                                               electrocardiograma
                                                                                                                                                                                P   D   R             93010
                                58                                       F
                                                                    D          Ppreg               Hb            R    R   3. Teleinterconsulta síncrona                         P   D   R   2    99499.11

---

## Página 58

**Contraportada (OCR):**

```text
A .
/ Rien (
j : eo
es
ie En
& oN a. - ;

PERU | Ministerio
wy de Salud
Ministerio de Salud
Av. Salaverry N° 801 - Jesus Maria - Perú
Telef.: (01) 315 6600
```

---
