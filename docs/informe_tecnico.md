# INFORME TÉCNICO – SEMANA 1
## Análisis de la oferta académica y matrícula de los Institutos Profesionales en Chile, año 2025

**Asignatura:** MCDI500 – Programación para la Ciencia de Datos  
**Programa:** Magíster en Ciencia de Datos e Inteligencia Artificial  
**Universidad:** Universidad Andrés Bello (UNAB)  
**Integrantes:** [Completar nombres]  
**Fecha:** Noviembre de 2026

---

## 1. Introducción

El presente proyecto tiene como objetivo analizar la oferta académica y matrícula de los Institutos Profesionales (IP) en Chile durante el año 2025, utilizando información oficial del Consejo Nacional de Educación (CNED).

El trabajo se desarrolla mediante Python, Jupyter Notebook y las bibliotecas Pandas y NumPy, aplicando procedimientos de exploración, limpieza, transformación y validación de datos.

## 2. Definición del problema

La información sobre matrícula y oferta académica de los Institutos Profesionales se encuentra distribuida en múltiples registros que contienen características de instituciones, programas, sedes y estudiantes matriculados.

Para facilitar su análisis, es necesario seleccionar, organizar y procesar los datos, identificando inconsistencias, valores faltantes y variables relevantes.

**Pregunta de investigación:**

¿Cómo se caracteriza la oferta académica y la distribución de matrícula de los Institutos Profesionales en Chile durante 2025?

## 3. Objetivos

### Objetivo general

Caracterizar la oferta académica y matrícula de los Institutos Profesionales de Chile durante 2025 mediante técnicas de procesamiento y análisis descriptivo de datos.

### Objetivos específicos

1. Seleccionar los registros de Institutos Profesionales correspondientes a 2025.
2. Identificar las principales variables institucionales, académicas y de matrícula.
3. Detectar valores faltantes, registros duplicados y posibles inconsistencias.
4. Aplicar procedimientos de limpieza y transformación.
5. Generar un conjunto de datos procesado y verificable.

## 4. Fuente de información

Se utilizó la base **INDICES Matrícula 2005–2026**, publicada por el Consejo Nacional de Educación (CNED).

La base original contiene 260.307 registros y 62 columnas.

Para este proyecto se seleccionaron exclusivamente los registros de Institutos Profesionales correspondientes a 2025.

La selección permitió identificar:

- 4.731 registros.
- 27 Institutos Profesionales.
- 62 variables originales.

Los registros representan ofertas académicas y no necesariamente estudiantes individuales.

## 5. Metodología

### 5.1. Fase 1: definición y exploración inicial

Se configuró el entorno de programación con Python, Jupyter Notebook, Pandas y NumPy.

Se cargó el archivo Excel original y se verificó su disponibilidad y estructura.

Posteriormente, se filtraron los registros correspondientes a Institutos Profesionales durante 2025.

Se identificaron 24 columnas con valores faltantes, de las cuales 13 se encontraban completamente vacías.

También se detectó un registro del IP Santo Tomás con año de inicio de actividades 2026 y matrícula correspondiente a 2025. Se conservó para su revisión posterior.

La revisión de duplicados identificó cero registros completamente idénticos. Las coincidencias por institución, programa y sede requirieron examinar otras variables, como campus y horario, por lo que no se eliminaron registros en esta etapa.

### 5.2. Fase 2: preprocesamiento

Se desarrollaron las siguientes actividades:

1. Identificación y cuantificación de valores faltantes.
2. Eliminación de 13 columnas completamente vacías.
3. Exclusión de 2 columnas adicionales con más del 90 % de valores faltantes.
4. Tratamiento de los valores faltantes restantes.
5. Normalización de variables de texto.
6. Creación de una categoría descriptiva de matrícula.
7. Verificación de la estructura del conjunto procesado.
8. Exportación de los datos a formato CSV.

Para completar los valores faltantes, se utilizó la mediana en las variables numéricas y la categoría «No informado» en las variables categóricas.

Estas sustituciones constituyen decisiones de preprocesamiento y no representan información observada directamente en la fuente original.

## 6. Resultados

### 6.1. Indicadores iniciales

| Indicador | Resultado |
|---|---:|
| Registros seleccionados | 4.731 |
| Institutos Profesionales | 27 |
| Columnas originales | 62 |
| Matrícula de primer año | 137.481 |
| Matrícula total | 439.607 |
| Columnas completamente vacías | 13 |
| Columnas adicionales excluidas | 2 |
| Columnas finales procesadas | 48 |
| Valores faltantes después del tratamiento | 0 |

### 6.2. Distribución de categorías de matrícula

Se creó una variable categórica que clasifica los registros según el nivel de matrícula.

| Categoría | Registros |
|---|---:|
| Baja | 2.583 |
| Media | 1.650 |
| Alta | 465 |
| Muy alta | 33 |
| **Total** | **4.731** |

Esta clasificación permite describir diferencias en el tamaño de las ofertas académicas registradas.

### 6.3. Archivo generado

El procesamiento produjo el archivo:

`data/processed/matricula_ip_2025_procesada.csv`

El archivo contiene 4.731 registros y 48 columnas. Se comprobó su lectura mediante Pandas y se verificaron sus dimensiones.

## 7. Decisiones técnicas y limitaciones

Se mantuvieron todos los registros seleccionados, dado que las coincidencias identificadas no justificaban por sí solas su eliminación.

Se excluyeron variables completamente vacías o con un porcentaje muy elevado de información faltante.

Los valores imputados deberán considerarse al interpretar los indicadores, especialmente cuando correspondan a aranceles, vacantes u otras variables cuantitativas.

El análisis es descriptivo y no pretende establecer relaciones de causalidad.

Asimismo, el conjunto seleccionado no contiene directamente un indicador de deserción estudiantil, por lo que dicho fenómeno queda fuera del alcance del proyecto.

## 8. Conclusiones

El trabajo permitió seleccionar y procesar información oficial sobre la oferta académica y matrícula de los Institutos Profesionales de Chile durante 2025.

Se obtuvo un conjunto de datos con 4.731 registros y 48 columnas, que podrá utilizarse en las siguientes etapas del proyecto.

El proceso permitió identificar dificultades de calidad de datos y documentar las decisiones técnicas adoptadas para su tratamiento.

La utilización de Python, Pandas, NumPy y Jupyter Notebook facilitó la organización y verificación del procesamiento realizado.

## 9. Referencias preliminares

- Consejo Nacional de Educación. (s. f.). *INDICES: Estadísticas y bases de datos de educación superior*. https://www.cned.cl/
- Python Software Foundation. (s. f.). *Python documentation*. https://docs.python.org/3/
- pandas development team. (s. f.). *pandas documentation*. https://pandas.pydata.org/docs/
- NumPy Developers. (s. f.). *NumPy documentation*. https://numpy.org/doc/

**Pendiente:** Completar al menos cinco referencias bibliográficas pertinentes, verificar sus datos y adecuarlas a APA 7 antes de entregar el informe.