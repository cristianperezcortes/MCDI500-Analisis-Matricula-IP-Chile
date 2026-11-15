# Auditoría interna de Sumativa 2 — Fase 3 (69 puntos)

**Equipo confirmado por sus integrantes:** Cristian Pérez Cortés y Claudio Navarrete Sims, Grupo 8. La regla general de 3–4 personas requiere aclaración del docente.

La tabla constituye una **lista de evidencias**, no una nota asignada ni una predicción de la calificación. El profesor evalúa cuatro niveles (Excelente, Bueno, Insuficiente, No cumple); por tanto se exige evidencia para cada descriptor antes de declarar un criterio cerrado.

| N.º | Criterio y máximo | Evidencia de implementación real | Estado técnico / observación |
|---|---|---|---|
| 1 | Portada e índice (3) | `docs/f3_s02_entregable_g8.pdf` y `.docx`; índice generado como índice automático | Completo técnicamente; cotejar plantilla Canvas |
| 2 | Codificación funcional (9) | `src/f3_transformaciones.py`, `src/f3_pipeline.py`; funciones parametrizadas | Implementado; interfaces y copias defensivas |
| 3 | Preprocesamiento (6) | Pipeline original F2 reutilizado en F3, 4.731×68; auditorías F2 | Implementado; no rehacer la base |
| 4 | Validación técnica (6) | `tests/`, `evidencias/f3_equivalencia_f2.json`, F3 §3/§6 | Ejecutado; revisar pruebas locales y otro equipo |
| 5 | Eficiencia (6) | `evidencias/f3_benchmarks.csv`, `evidencias/f3_comparacion_tiempos.png`, F3 §4 | Ejecutado; `timeit`, `tracemalloc` y equivalencia |
| 6 | Diseño estructurado (6) | `src/f3_recursion.py`, módulos especializados y razonamiento de cohesión | Implementado; recursividad solo para metadatos |
| 7 | POO (6) | `TransformadorCNED`, tres subclases; `PipelineCNED` polimórfico | Implementado; 3 principios explícitos |
| 8 | Documentación de arquitectura (6) | Informe §III.b, `docs/f3_arquitectura.csv`, README | Implementado; patrón Template Method justificado |
| 9 | Repositorio (6) | `F2/`, `F3/`, historial separado, README actualizado | Publicación y contribuciones individuales sujetas a verificación GitHub |
| 10 | Notebook F3 (6) | `F3/S2_F3_NucleoAlgoritmico_Cned.ipynb`, 10 celdas de código ejecutadas | Ejecutado; numeración continua y salidas guardadas |
| 11 | Aspectos formales (9) | Informe PDF carta, fuentes docentes/oficiales/libro 2022, citas internas | Documento revisado; verificar plantilla institucional |

## Revisión crítica como evaluador

1. **Validación fuerte:** `assert_frame_equal(..., check_exact=True)` confirma invariantes completos, no solo dimensiones o sumas.
2. **No hay fuga predictiva afirmada:** F3 reproduce un análisis descriptivo, no entrena un predictor. Para inferencia futura se requiere separar fit y test de los parámetros de imputación y cuantiles.
3. **Benchmark limitado:** la medida `tracemalloc` captura memoria Python, no toda la memoria nativa. Las cifras corresponden al equipo y ambiente de prueba; no son promesas de rendimiento universal.
4. **No inventar pruebas colaborativas:** los commits corresponden a autores que realizaron acciones reales. La prueba en otro equipo exige revisión independiente de Cristian.
5. **Pendiente académico real:** la plantilla institucional de Canvas y la aprobación de Grupo 8 con dos integrantes no están acreditadas.
6. **Fuente CNED:** usar el Excel original con hash, pero dejar constancia de que falta URL y fecha exacta de descarga de la edición 2005–2026.

**Restricción de integridad académica:** la redacción y las decisiones deben ser comprendidas y revisadas por los integrantes, conforme a las normas de la universidad sobre ayudas tecnológicas; no se altera el historial ni se simulan actuaciones humanas.

## Auditoría adicional del 15 de noviembre de 2026

Se realizó una segunda revisión de código, evidencias, notebooks, informe y compatibilidad con la rúbrica. Este registro es técnico y no sustituye la calificación del profesor.

| Comprobación | Evidencia observada | Estado |
|---|---|---|
| Pruebas con Excel original | `python -m pytest -q tests`: **44 aprobadas, 0 fallidas, 0 omitidas** | Completo en ambiente de desarrollo |
| Reproducibilidad sin Excel | `tests/test_f3_regresion_portatil.py`: 4 pruebas sobre 120 registros **sintéticos**, con NA/UF, ceros y clases | Completo; no sustituye base real |
| Equivalencia F2–F3 | `pd.testing.assert_frame_equal(check_exact=True)` sobre 4.731 filas y 68 columnas | Completo |
| Integridad de la fuente | SHA-256 del XLSX idéntico al metadato F1 | Completo en ambiente de desarrollo |
| Concordancia informe/benchmark | CSV, tabla DOCX, PDF, figura y salida del notebook ahora comparten la ejecución registrada | **Desacople anterior corregido** |
| Índice y PDF | Word con campo de índice; PDF de 7 páginas, carta 612×792 puntos, sin marcas `**` literales | Completo técnicamente |
| Auditoría automatizada complementaria | `python scripts/auditar_entrega_f3.py --integracion`: **27/27 controles** | Completo en ambiente de desarrollo |
| Acciones en GitHub | Flujo ejecuta pruebas sin Excel más auditoría documental; integración CNED se mantiene local | Confirmar nuevo run después de publicar |

**Benchmark vigente de 4.731 registros:** bucle por grupo = **9.241 ms** y `pandas.groupby` = **0.815 ms** de tiempo mínimo por ejecución, una relación aproximada de **11,3×** en el entorno de ensayo. Memoria pico medida con `tracemalloc`: 0.1356 y 0.2383 MiB, respectivamente. Estas cifras no prueban mejoras universales y deben citarse junto con la versión del archivo `evidencias/f3_benchmarks.csv`.

**Hallazgo corregido:** el informe anterior presentaba otros tiempos derivados de una ejecución distinta del mismo benchmark. Se reemplazaron las seis cifras de la tabla, la frase explicativa y la figura para que coincidan con el notebook y el CSV guardados. El criterio de eficiencia requiere concordancia, no elegir la medición de mayor aceleración.

**Riesgos pendientes antes de entregar:** (1) plantilla institucional descargada en Canvas; (2) consentimiento del docente para dos integrantes; (3) contribuciones y ejecución independientes de Cristian; (4) procedencia exacta de la edición XLSX 2005–2026; (5) entrega efectiva en Canvas. No se certifican estos aspectos sin evidencia humana.
