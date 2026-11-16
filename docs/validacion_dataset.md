# Informe de validación del dataset CNED IP 2025

Adaptación del procedimiento didáctico del curso, aplicada al subconjunto objetivo, no a los 260.307 registros históricos.

- Archivo: `Base-INDICES-Matricula-2005-2026.xlsx` (versión exacta de descarga 2005–2026 pendiente de confirmación).
- Filas del archivo: **260307**; columnas: **62**.
- IP/2025: **4731** filas; **27** instituciones.
- Matrícula de primer año: **137481**; matrícula total: **439607**.

## Requisitos del curso

| Criterio | Estado |
|---|---|
| Al menos 2000 registros | CUMPLE |
| Al menos 12 columnas | CUMPLE |
| Al menos 3 roles analíticos | CUMPLE |
| Variables numéricas | CUMPLE |
| Variables categóricas | CUMPLE |
| Matrícula no negativa | CUMPLE |

## Calidad de las variables

- Variables completamente vacías en IP/2025: **13**.
- Las variables con 100% de ausencias no son aptas para analizar: se eliminan en F2, documentando sus nombres.
- Los identificadores no se imputan, aun si Pandas los reconoce como números.
- Ceros observados de matrícula primer año: **1576**.
- Inconsistencias temporales: **1**; se etiqueta y documenta sensibilidad.
- Duplicados exactos: **0**.

## Veredicto

**APTO** para análisis descriptivo y de concentración de matrícula agregada en IP/2025, con las restricciones documentadas.

## Limitación de procedencia

La URL institucional del CNED está identificada; la URL exacta y la fecha de descarga de la versión 2005–2026 siguen sin verificarse.
