
# MCDI500 - Análisis de Matrícula de Institutos Profesionales en Chile

## Descripción del proyecto

Proyecto de la asignatura Programación para la Ciencia de Datos del Magíster en Ciencia de Datos e Inteligencia Artificial.

El objetivo es analizar la oferta académica y matrícula de los Institutos Profesionales de Chile durante el año 2025, utilizando información oficial del Consejo Nacional de Educación (CNED).

## Fuente de datos

- Institución: Consejo Nacional de Educación (CNED).
- Base de datos: INDICES Matrícula 2005-2026.
- Registros seleccionados: 4.731.
- Institutos Profesionales identificados: 27.
- Columnas originales: 62.
- Columnas del archivo procesado: 48.

El archivo Excel original no se incluye en GitHub debido a su tamaño. Puede obtenerse desde el sitio oficial del CNED: https://www.cned.cl/

## Estructura del proyecto

- F1/F1_Definición.ipynb: definición del problema y exploración inicial.
- F2/F2_procesamiento.ipynb: limpieza, transformación y validación.
- data/processed/: archivo CSV procesado.
- docs/: informe técnico y mapa conceptual.
- requirements.txt: dependencias de Python.
- .gitignore: exclusiones del control de versiones.

## Herramientas

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Git y GitHub

## Instrucciones de ejecución

1. Descargar el repositorio.
2. Crear un entorno virtual: `python -m venv .venv`
3. Activarlo en Windows: `.venv\Scripts\activate`
4. Instalar las dependencias: `pip install -r requirements.txt`
5. Descargar la base original del CNED y guardarla en `data/raw/Base-INDICES-Matricula-2005-2026.xlsx`.
6. Iniciar Jupyter Notebook: `jupyter notebook`
7. Ejecutar primero `F1/F1_Definición.ipynb`.
8. Ejecutar después `F2/F2_procesamiento.ipynb`.

## Resultados de la Semana 1

Se seleccionaron 4.731 registros de Institutos Profesionales correspondientes a 2025.

Durante el procesamiento se identificaron y excluyeron 13 columnas completamente vacías y otras 2 columnas con alta proporción de valores faltantes.

Se aplicaron transformaciones adicionales, obteniendo un archivo final de 4.731 registros y 48 columnas.

El archivo procesado se encuentra en `data/processed/matricula_ip_2025_procesada.csv`.

## Documentación

El informe técnico y el mapa conceptual están disponibles en la carpeta `docs`.

## Equipo de Trabajo
Cristian Pérez Cortés 
Claudio Navarrete Sims

## Fuente y alcance de los datos

El proyecto utiliza información oficial del Consejo
Nacional de Educación (CNED), correspondiente a la
matrícula de Institutos Profesionales de Chile
durante el año 2025.

El conjunto de datos seleccionado contiene 4.731
registros de 27 Institutos Profesionales.

El análisis considera procesos de selección,
limpieza, transformación y validación de datos,
documentados en los notebooks del proyecto.
