# Bitácora de decisiones técnicas — F3

| ID | Decisión | Justificación y efecto verificable |
|---|---|---|
| F3-01 | Conservar la fuente CNED y el dataset F2 | Reproducir la misma unidad de análisis, sin sobrescribir matrícula y códigos |
| F3-02 | `TransformadorCNED` abstracta y tres hijas | Alta cohesión, herencia y estado encapsulado; interfaz uniforme `ajustar` / `transformar` |
| F3-03 | `PipelineCNED` por composición | Agregar/quitar etapas sin reescribir la lógica interna de cada clase |
| F3-04 | Template Method como patrón principal | Validación común, copia defensiva, control de estado y pasos especializados |
| F3-05 | Equivalencia F2–F3 estricta | Mismo DataFrame (4.731 × 68), misma matrícula (137.481/439.607), CSV comparable |
| F3-06 | Agrupación `for` frente a `groupby` | Igualdad de series antes de medir, 3 tamaños, 3 rondas, 3 iteraciones por ronda |
| F3-07 | Elegir `groupby` para explotación | Menor costo temporal medido para 4.731 filas; reconocer mayor memoria Python observada |
| F3-08 | Usar recursividad para metadatos anidados | Tiene problema recursivo natural y caso base; no forzarla en tablas |
| F3-09 | Separar tests completos del kernel | La extracción del Excel es pesada; evitar doble carga dentro de Jupyter |
| F3-10 | Mantener PR de F1/F2 independiente de F3 | Historia y revisión académica trazable por evaluación |

**Fuentes técnicas:** Salinas Silva (2026a, 2026b), Python Software Foundation (s. f.) y McKinney (2022). Medidas y pruebas: `evidencias/f3_benchmarks.csv`, `f3_equivalencia_f2.json` y `f3_resultados_pruebas.txt`.

| F3-11 | Añadir regresión portátil sin Excel | Dataset sintético con faltantes CLP/UF, ceros y niveles; confirma F2=F3 sin publicar datos originales. |
| F3-12 | Unificar métricas del informe con evidencia | Se corrigió el desacople entre PDF antiguo y `f3_benchmarks.csv`; texto, tabla y figura reflejan una misma ejecución. |
| F3-13 | Puerta de calidad reproducible | `scripts/auditar_entrega_f3.py` revisa notebooks, informes, métricas y permite validación con SHA-256 del Excel al usar `--integracion`. |
