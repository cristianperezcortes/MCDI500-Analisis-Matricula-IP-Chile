# Fase 3 — Núcleo algorítmico, eficiencia y POO (Grupo 8)

**Equipo:** Cristian Pérez Cortés y Claudio Navarrete Sims.  
**Asignatura:** MCDI500, Programación para la Ciencia de Datos, UNAB.  
**Datos:** matrícula de Institutos Profesionales de Chile, 2025 (CNED).

## Alcance académico

La Sumativa 2 exige conservar F2 y demostrar que la nueva arquitectura F3 produce el **mismo conjunto** mediante clases y módulos reutilizables, herencia, polimorfismo, encapsulamiento, comparación de algoritmos con `timeit`, medición de memoria y pruebas normales, límite y excepciones. **No se limpia ni modifica nuevamente el Excel original.**

### Archivos

- `S2_F3_NucleoAlgoritmico_Cned.ipynb`: notebook ejecutado; evidencia de POO, equivalencia, eficiencia y trazabilidad.
- `../src/f3_transformaciones.py`: `TransformadorCNED`, `DepuradorEstructura`, `ImputadorSelectivo` y `ConstructorVariables`.
- `../src/f3_pipeline.py`: composición de etapas con interfaz común y prueba exacta contra F2.
- `../src/f3_medicion.py`: alternativas de agrupación, verificaciones de igualdad, `timeit` y `tracemalloc`.
- `../src/f3_recursion.py`: recursividad útil para metadatos anidados, no forzada sobre matrícula tabular.
- `../tests/test_f3_poo.py` y `../tests/test_f3_integracion.py`: pruebas normales, límite, excepciones y regresión.
- `../docs/f3_s02_entregable_g8.pdf`: informe en formato carta, con índice automático y seis apartados.
- `../evidencias/f3_benchmarks.csv` y `f3_equivalencia_f2.json`: cifras de pruebas.

## Ejecución (desde la raíz del repositorio)

1. Instalar Python 3.13; crear `python -m venv .venv` y activar el ambiente.
2. `python -m pip install -r requirements.txt`.
3. Guardar `Base-INDICES-Matricula-2005-2026.xlsx` en `data/raw/` (fuente suministrada, sin modificar).
4. Ejecutar F1 y luego F2 (F2 genera `data/interim/ip_2025_origen_filtrado.csv` y `data/processed/matricula_ip_2025_procesada_v3.csv`).
5. Ejecutar `F3/S2_F3_NucleoAlgoritmico_Cned.ipynb` con **Restart Kernel and Run All Cells**.
6. Ejecutar `python -m pytest -q tests` y revisar `evidencias/`.

## Validación

Se comprueba **igualdad exacta** entre DataFrames F2 y F3 con `pd.testing.assert_frame_equal`, más conservación de 4.731 filas, 27 IP, 137.481 matrículas de primer año y 439.607 matrículas totales. Se comparan agregación por bucle y `pandas.groupby` con resultados idénticos.

## Colaboración y límites

Los avances se versionan mediante ramas y pull requests con fecha y autor real. La evaluación oficial y la aprobación de una nómina de dos integrantes corresponde al docente; la guía general indica 3–4 estudiantes. Las mediciones de memoria con `tracemalloc` no abarcan toda la memoria nativa NumPy/Pandas.

## Auditoría posterior a la ejecución

- `python scripts/auditar_entrega_f3.py`: verifica notebooks guardados, informe, referencias, cifras del benchmark y archivos; se puede ejecutar en GitHub sin el Excel.
- `python scripts/auditar_entrega_f3.py --integracion`: verifica SHA-256 del Excel local y recomputa la equivalencia completa F2/F3. Requiere haber ejecutado previamente F2.
- `tests/test_f3_regresion_portatil.py`: prueba un conjunto **sintético**, no corresponde a registros reales del CNED.
- Las pruebas sin Excel se distinguen explícitamente de las de integración real; no se declara su aprobación por omisión.
- El informe DOCX/PDF usa las cifras de la misma ejecución registrada en `evidencias/f3_benchmarks.csv`. Si se repite el benchmark, debe actualizarse la tabla y figura del informe antes de enviar.

## Fuente institucional y alcance temporal

La fuente de los registros es el sistema CNED–INDICES, disponible en el [portal oficial del Consejo Nacional de Educación](https://cned.cl/institucional/bases-de-datos/). El equipo utilizó el ejemplar denominado `Base-INDICES-Matricula-2005-2026.xlsx`, cuya integridad se comprueba mediante SHA-256. La página pública consultada identifica una edición de matrícula 2005–2025; no afirmamos tener la URL directa ni la fecha de descarga del ejemplar 2005–2026. **2025 es el año de los datos analizados y 2026 el año de preparación del informe.**
