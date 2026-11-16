# Procedencia y trazabilidad de la fuente CNED–INDICES — Grupo 8

**Año observado:** 2025. **Informes académicos:** noviembre de 2026.

## Fuente primaria institucional

La fuente primaria de los datos del proyecto corresponde al **Consejo Nacional de Educación (CNED)**, por medio del sistema oficial **INDICES Educación Superior** y su [portal de bases de datos](https://cned.cl/institucional/bases-de-datos/). El equipo informa que el archivo utilizado proviene del sitio original de CNED; esta atribución institucional es coherente con la estructura y las variables del conjunto.

El estudio trabaja con una copia proporcionada al grupo denominada `Base-INDICES-Matricula-2005-2026.xlsx`, hoja `BaseINDICES_2005_2026`, de 260.307 registros y 62 columnas. Se filtraron Institutos Profesionales, año 2025, obteniendo 4.731 filas de 27 instituciones, matrícula de primer año 137.481 y matrícula total 439.607.

**Integridad del ejemplar procesado:** SHA-256 `0439bc1ed1a6ec018a3bbf4be34861bd33749c81c34c2eeeddbc7dcd2657c48a`. El hash permite distinguir si se modificó el archivo con el que trabajó el equipo, pero **no verifica el lugar ni la fecha exacta de su descarga**.

## Alcance de la evidencia y discrepancia de ediciones

Al verificar el portal institucional se observa que la **base histórica de matrícula publicada se identifica como 2005–2025**. En contraste, el nombre de la copia local del grupo indica `2005-2026`. Por ello, **no se afirma** que ambos archivos sean byte por byte idénticos, ni que exista una URL directa actualmente accesible para la versión exacta que sugiere el nombre del XLSX.

La URL directa de descarga, fecha precisa de obtención y eventuales cambios entre ediciones **permanecen sin acreditar documentalmente**. Si se recupera la comunicación de descarga, historial del navegador o enlace original, deberá archivarse la evidencia sin reemplazar silenciosamente la copia analizada.

## Temporalidad del informe

- **2025:** año de matrícula estudiado.
- **15–16 de noviembre de 2026:** fechas de elaboración y revisión de los informes académicos.
- El **2026** en el nombre del XLSX designa su identificación de archivo de trabajo, no prueba por sí mismo un período adicional de observación del presente análisis.

## Reproducibilidad y resguardo

La fuente cruda queda fuera del repositorio GitHub (`data/raw/`). Para reproducir los resultados, un integrante debe usar el ejemplar identificado por SHA-256, verificar su integridad y ejecutar F1 → F2 → F3. Las pruebas de CI emplean datos sintéticos o no dependientes de la fuente y registran explícitamente las pruebas de datos reales que se omiten.

**Referencia institucional:** Consejo Nacional de Educación. (s. f.). *Bases de datos — INDICES*. https://cned.cl/institucional/bases-de-datos/
