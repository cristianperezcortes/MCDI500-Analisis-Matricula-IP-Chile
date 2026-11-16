# Auditoría técnica y científica independiente posterior al PR #8

**Fecha:** 16-11-2026. **Rama base auditada:** `main`, commit `f993704206e84b16a259c523cf819b4be4d97c2a`. **Grupo 8:** Cristian Pérez Cortés y Claudio Navarrete Sims.

## Dictamen de ejecución

- PR #8 **fusionado** en `main` el 16-11-2026 (commit `f993704`).
- GitHub Actions PR #8: [ejecución 43917494813](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/actions/runs/43917494813), resultado **success** para Windows y Ubuntu.
- GitHub Actions después del merge: [ejecución 43921690832](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/actions/runs/43921690832), resultado **success** para ambos sistemas.
- Logs del último run: **55 passed, 3 skipped**, tanto en Windows como en Ubuntu. Los tres `skipped` requieren fuente Excel original ausente deliberadamente de CI. **No representan fallos.** Ya existe evidencia previa de validación local con Excel; esta auditoría no repitió esa ejecución.
- Pipeline CI incluye instalación de dependencias, sintaxis, `pytest`, auditoría F3 notebook/CSV/PDF y auditoría académica F1/F2. El archivo `tests/test_documentacion_pr8.py` está incluido en el descubrimiento estándar de `pytest`.

## Revisión crítica de ciencia de datos

| Hallazgo | Evaluación y acción prudente |
|---|---|
| **Coherencia de CR3/HHI** | La definición del HHI en `src/cned_pipeline.py` utiliza escala 0–10.000; el CR3 expresa porcentaje. La nota del PR #8 reconoce correctamente que institución (27 grupos), región (16) y área (10) tienen particiones diferentes. **Observación menor:** el segundo objetivo canónico aún dice «medir y comparar la concentración ... entre instituciones, regiones y áreas». Debe interpretarse como calcular por separado, no realizar comparación directa de magnitudes entre dimensiones. En una próxima revisión académica, cambiar su formulación de manera sincronizada en F1, F2, DOCX y PDF y luego ejecutar `scripts/auditar_consistencia_academica.py`. No editar solo el objetivo canónico porque se rompería la consistencia automatizada. |
| **Imputación y validez estadística** | `comparar_imputaciones` oculta 10% de datos observados con semilla 42 y escoge MAE mínimo. Es una comparación reproducible, pero **una sola partición** no mide estabilidad del ranking de métodos y el comportamiento de faltantes naturales puede diferir del ocultamiento artificial. Para profundización futura: validación con múltiples semillas/repeticiones, intervalos de MAE y análisis de patrón de ausencia (MCAR/MAR/MNAR como hipótesis, nunca como certeza). No rehacer la Sumativa ya validada para introducir resultados no solicitados. |
| **Unidad y cobertura** | Se analizan registros agregados de programas/sedes y sumas de matrícula; **no 4.731 estudiantes**. La selección conservó pregrado y 17 registros de posgrado según la bitácora, por continuidad con la entrega original. Si la pauta exige exclusivamente primer año de pregrado, reportar un análisis de sensibilidad específico, sin alterar la muestra de forma silenciosa. |
| **Fuente y reproducibilidad** | Se comprobó documentación de procedencia CNED–INDICES y SHA-256 `0439bc1ed1a6ec018a3bbf4be34861bd33749c81c34c2eeeddbc7dcd2657c48a`. Ese hash verifica identidad del ejemplar **si se dispone del archivo**, no demuestra URL de descarga ni equivalencia con la base anunciada como 2005–2025. Conservar declaración de incertidumbre; no fabricar metadatos. |
| **Benchmarks F3** | Los tiempos documentados son dependientes de hardware y carga del equipo, por tanto **no son una constante del algoritmo**. Conservar resultados medidos auténticamente; usar benchmarking repetido y análisis de dispersión si se amplía el estudio. |
| **Cobertura de pruebas del PR #8** | Las cinco pruebas nuevas comprueban principalmente presencia de términos, fechas y metadatos. Demuestran consistencia documental básica, **no prueban por sí mismas que los valores numéricos, tablas y figuras de DOCX/PDF coincidan semánticamente**. Para una siguiente iteración, automatizar extracción y comparación de métricas críticas contra CSV con tolerancia documentada. |

## Cierre y límites

**Dictamen:** PR #8 integrado y CI final aprobada en Windows y Ubuntu. **No se detectó un defecto de ejecución que justifique repetir F1/F2/F3 o modificar sus métricas.** Las oportunidades identificadas son mejoras científicas y de documentación; no suponen que el trabajo actualmente entregado sea incorrecto. Se conserva el material histórico y no se alteran notebooks, resultados, CSV, PDF, DOCX ni fuentes crudas.

**Excluido por instrucción:** plantilla institucional, autorización del docente para equipo de dos y verificación de entrega Canvas. El enlace/fecha precisa del ejemplar CNED continúa sin acreditación; no puede derivarse del repositorio.
