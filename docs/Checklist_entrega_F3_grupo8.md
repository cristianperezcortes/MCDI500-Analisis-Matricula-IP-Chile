# Checklist de cierre — Sumativa 2 F3, Grupo 8

**Evaluación:** MCDI500, Fase 3 / Semana 2 · 69 puntos · 20% del módulo.  
**Entrega declarada en Canvas:** domingo 15 de noviembre de 2026, 23:59 (Chile). Confirmar el plazo en la cuenta del estudiante antes de subir.  
**Integrantes declarados por el equipo:** Cristian Pérez Cortés y Claudio Navarrete Sims. La autorización docente del grupo de dos no consta en las evidencias disponibles.

## Validaciones automatizables completadas

- [x] Las funciones F2 y las clases F3 están organizadas en `src/`.
- [x] Notebook F1 y F2 con ejecución guardada, sin errores y orden de celdas continuo.
- [x] Notebook F3 con ejecución guardada, sin errores y orden de celdas continuo.
- [x] Tests portátiles de F2/F3 sobre datos **sintéticos** en CI, sin compartir el Excel.
- [x] Tests de datos reales en el equipo de desarrollo; el dataset original permanece fuera de GitHub.
- [x] Benchmark `timeit` y memoria `tracemalloc`, con igualdad de resultados.
- [x] Texto, tabla de seis filas y gráfico del informe sincronizados con `evidencias/f3_benchmarks.csv`.
- [x] Portada, índice Word, PDF tamaño carta, seis apartados y bibliografía del informe.
- [x] Auditoría automática: `python scripts/auditar_entrega_f3.py`.

## Revisión de Cristian (acciones reales)

- [x] Cristian ejecutó el proyecto con el Excel original en Windows, desde una copia descargada; la instalación desde clon Git con carpeta `.git` permanece como verificación adicional opcional.
- [x] Cristian ejecutó F1, F2 y F3 desde Jupyter en Windows; F3 actualizado con sus salidas reales en PR #4.
- [x] Ejecutó 44/44 pruebas y 27/27 controles con el Excel antes de ampliar las pruebas; posteriormente se agregaron seis casos sintéticos (50/50 en revisión local).
- [x] PR #1–4 revisados, aprobados e integrados en `main` con la cuenta real de Cristian.
- [x] Cristian realizó commits y revisiones con su cuenta real sin modificar la autoría histórica.

## Documentos y aprobación académica

- [ ] Obtener la plantilla institucional original de Canvas y comparar sus estilos, campos, portada y página de referencias.
- [ ] Recibir confirmación docente de que el Grupo 8 puede estar integrado por dos estudiantes.
- [ ] Acreditar fecha y URL de origen de la versión CNED 2005–2026, si el profesor lo requiere.
- [ ] Comprobar que la versión aprobada de `docs/f3_s02_entregable_g8.pdf` coincide con el archivo destinado a Canvas.
- [ ] Subir el PDF oficial desde la cuenta del integrante responsable y registrar acuse de recepción.

## Orden seguro de integración GitHub

1. Revisar y aprobar F1/F2 en PR #1; integrar primero esa base en `main`.
2. Revisar y aprobar F3 en PR #2; cambiar su base de la rama F1/F2 a `main` cuando corresponda.
3. Integrar los ajustes de auditoría adicionales tras revisión, conservando los commits y sin forzar el historial.

**Criterio de salida:** que el código se ejecute, que los datos e informes coincidan, que cada integrante comprenda y respalde las decisiones, y que la entrega respete las normas institucionales. Ninguna auditoría interna equivale a una nota docente.

## Resultado de la auditoría complementaria

- **44/44 pruebas locales aprobadas**, con datos reales y pruebas sintéticas.
- **27/27 controles documentales/de datos aprobados**, incluyendo formato y cifras del PDF.
- **No se declara todavía una nota**: la plantilla externa, la autorización del grupo y la revisión independiente siguen pendientes.
