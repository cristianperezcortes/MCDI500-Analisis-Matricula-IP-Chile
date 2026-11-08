
# Mapa conceptual técnico – Semana 1

## Proyecto
Análisis de la oferta académica y matrícula de los Institutos Profesionales de Chile durante 2025.

## 1. Problema y datos
- Problema: caracterizar la oferta académica y matrícula.
- Fuente: Consejo Nacional de Educación (CNED).
- Base: INDICES Matrícula 2005-2026.
- Selección: 4.731 registros y 62 columnas.
- Instituciones: 27 Institutos Profesionales.

## 2. Herramientas
- Python: lenguaje de programación.
- Jupyter Notebook: desarrollo y ejecución.
- Pandas: procesamiento de datos.
- NumPy: operaciones numéricas.
- Git y GitHub: control de versiones y colaboración.

## 3. Organización del repositorio
- F1/: definición del problema y exploración.
- F2/: limpieza, transformación y validación.
- data/raw/: archivo original del CNED.
- data/processed/: datos procesados.
- docs/: informe técnico y mapa conceptual.
- README.md: descripción e instrucciones.
- requirements.txt: bibliotecas utilizadas.

## 4. Flujo de procesamiento
Fuente CNED
→ Carga de datos
→ Selección de Institutos Profesionales 2025
→ Exploración
→ Identificación de valores faltantes
→ Limpieza y transformación
→ Validación
→ Archivo CSV procesado

## 5. Control de versiones y documentación
- Registrar los cambios mediante commits de Git.
- Publicar los archivos en GitHub.
- Documentar decisiones técnicas.
- Mantener coherencia entre notebooks, informe y repositorio.
- Registrar la participación de los integrantes.

## 6. Reflexión técnica
La utilización de Python y Jupyter permite desarrollar un procesamiento reproducible.

La organización del repositorio facilita el trabajo colaborativo y la trazabilidad.

La documentación de las decisiones de limpieza permite comprender las transformaciones realizadas y sus limitaciones.

## Referencia
Consejo Nacional de Educación. (s. f.). INDICES: Estadísticas y bases de datos de educación superior. https://www.cned.cl/
