# Control de versiones académicas — MCDI500 / Grupo 8

Este documento diferencia la primera entrega evaluada (60/99 puntos), las correcciones posteriores y la última versión integrada. **Una mejora del repositorio no modifica retroactivamente la nota anterior.**

| Elemento | Versión vigente | Evidencia histórica no vigente |
|---|---|---|
| F1 | `F1/F1_Definicion_Cned.ipynb` | `F1/F1_Definición.ipynb` |
| F2 | `F2/F2_Preprocesamiento_Cned.ipynb` | `F2/F2_procesamiento.ipynb` |
| F3 | `F3/S2_F3_NucleoAlgoritmico_Cned.ipynb` (salidas reales de Cristian) | Salidas anteriores conservadas en Git |
| Dataset | `data/processed/matricula_ip_2025_procesada_v3.csv`, generado localmente por F2, 68 columnas | `data/processed/matricula_ip_2025_procesada.csv`, 48 columnas, de la primera entrega |
| Informe F1/F2 | `docs/Informe_Sumativa1_F1_F2_Guia_Integrada.pdf` | `docs/Informe_Tecnico_Semana1.pdf`, `docs/informe_tecnico.md` |
| Informe F3 | `docs/f3_s02_entregable_g8.pdf` | Documentos previos visibles en historial Git |
| Calidad del dato | `docs/Registro_decisiones.md`, auditorías y pruebas | `docs/Revision_calidad_datos.md` (48 columnas históricas) |

El lector de datos y su pipeline no deben mezclar la base histórica procesada de 48 columnas con la nueva salida de 68. La ruta de entrada F3 es la salida **generada por F2**, no el archivo histórico versionado.

**Contribuciones:** ambos integrantes efectuaron acciones auténticas en GitHub. PR #1–7 fueron integrados al corte del 16/11/2026. La fecha/URL exacta de la versión INDICES 2005–2026, plantilla Canvas y aceptación docente del grupo de dos quedan sin acreditar.

## Actualización de reproducibilidad (16/11/2026)

El proyecto fija Notebook 7.5.3, separa los objetivos analíticos de la metodología y mantiene los archivos de la primera entrega como evidencia histórica. El PR #7 incorporó estos ajustes en `main` y GitHub Actions aprobó Windows/Ubuntu. Para correcciones posteriores debe consultarse su PR correspondiente, sin dar por integrados cambios pendientes. Los resultados con Excel no se sustituyen por los controles CI sin datos.

**Fechas:** 2025 designa el año de matrícula estudiado, no la fecha de creación de los informes, elaborados/revisados en noviembre de 2026. **Fuente:** CNED–INDICES (portal institucional); la identificación exacta de la copia local 2005–2026 está delimitada en `docs/Proveniencia_CNED_INDICES.md`.
