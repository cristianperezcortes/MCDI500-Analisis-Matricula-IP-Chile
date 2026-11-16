# MCDI500 — Proyecto CNED IP 2025 (Sumativa 1, Fases 1 y 2)

**Asignatura:** Programación para la Ciencia de Datos. **Programa:** Magíster en Ciencia de Datos e Inteligencia Artificial (UNAB). **Docente:** Omar Iván Salinas Silva.
**Grupo 8 — integrantes confirmados por el equipo:** Cristian Pérez Cortés y Claudio Navarrete Sims. Óscar Quezada y Carlos Vergara **no** integran este grupo de trabajo. **Nota administrativa:** la guía menciona grupos de 3–4 estudiantes; se debe comunicar al docente que el Grupo 8 está formado por 2 y solicitar su validación formal, sin atribuir dicha aprobación antes de recibirla.

## Pregunta de investigación
¿Cómo se distribuye y concentra la matrícula de primer año de los Institutos Profesionales en Chile durante 2025, según institución, región y área de conocimiento?

## Objetivo general
Analizar la distribución y la concentración de la matrícula de primer año de los Institutos Profesionales en Chile durante 2025, por institución, región y área de conocimiento, mediante un flujo de procesamiento y análisis descriptivo reproducible en Python.

## Datos y fuente
- Libro suministrado: `Base-INDICES-Matricula-2005-2026.xlsx` — hoja `BaseINDICES_2005_2026`, 260.307 filas y 62 variables.
- Subconjunto IP/2025: 4.731 registros, 27 instituciones, 137.481 matrículas de primer año y 439.607 matrículas totales (pregrado + posgrado, como la entrega original).
- Portal institucional: https://cned.cl/institucional/bases-de-datos/
- **Cautela:** el sitio visible del CNED describe una base 2005–2025; la URL exacta y fecha de descarga de la versión 2005–2026 **no están acreditadas**. No se afirma equivalencia no verificada. El libro original permanece sin modificaciones y su huella SHA-256 está en `docs/metadatos_fase1.json`.

## Estructura
```
F1/F1_Definicion_Cned.ipynb         definición, fuente, perfil y entorno; NO limpia
F2/F2_Preprocesamiento_Cned.ipynb   obtiene, diagnostica, limpia, transforma, valida
src/cned_pipeline.py               funciones reusables y contratos del dato
F3/S2_F3_NucleoAlgoritmico_Cned.ipynb  núcleo POO, benchmarks, pruebas
src/f3_transformaciones.py          clase base y tres transformaciones
src/f3_pipeline.py                  orquestador y equivalencia con F2
src/f3_medicion.py                  timeit y tracemalloc
src/f3_recursion.py                 recursividad de metadatos
scripts/verificar_proyecto.py       auditoría automatizada
validar_dataset.py                  criterios mínimos de dataset
tests/                              pruebas unitarias y de integración
docs/                               informe, mapa, diccionario, metadatos, comparaciones
evidencias/                         pruebas, auditoría y gráfico
data/raw/                           Excel original (NO versionar; sin alterar)
data/interim/                       extracto filtrado generado exclusivamente en F2
data/processed/                     CSV final e indicadores
```

## Requisitos
Python 3.13.5. El archivo `requirements.txt` fija las versiones utilizadas durante esta revisión, incluidas `openpyxl`, `lxml`, `pandas`, `numpy`, `nbclient`, Jupyter y pruebas.

### Windows PowerShell
```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m ipykernel install --user --name mcdi500-cned --display-name "Python (mcdi500-cned)"
python -m jupyterlab
```

### macOS / Linux
```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m ipykernel install --user --name mcdi500-cned --display-name "Python (mcdi500-cned)"
python -m jupyterlab
```

## Ejecución en orden
1. Guardar el Excel original en `data/raw/` con el nombre exacto y **sin modificarlo**.
2. Iniciar Jupyter desde la raíz del repositorio o abrir notebooks desde las carpetas `F1/` y `F2/`. Seleccionar kernel `Python (mcdi500-cned)`.
3. Abrir F1 y ejecutar **Restart Kernel → Run All**: definición, perfil, SHA-256, diccionario y metadatos. **No limpia ni transforma**.
4. Abrir F2 y ejecutar **Restart Kernel → Run All**: obtención, faltantes, atípicos, comparación de cuatro alternativas de ausencia, estimaciones trazables, codificación, escalamiento derivado y validaciones.
5. Ejecutar F3 con Restart Kernel → Run All: POO, equivalencia F2–F3, benchmarks, memoria y recursividad.
6. Ejecutar `python -m pytest -q tests/` y `python scripts/verificar_proyecto.py`. Revisar salidas en `evidencias/` y `docs/`.

## Decisiones y evidencia
- La matrícula y los códigos originales no se imputan. Se conservan 1.576 ceros reales de matrícula de primer año.
- Las variables monetarias CLP y UF se mantienen separadas; los valores UF ausentes no se inventan.
- Se comparan eliminación, media global, mediana global y mediana jerárquica, con enmascaramiento 10%, MAE y desviación antes/después, semilla 42.
- Las variables transformadas derivadas tienen banderas; se generan one-hot de nivel, escala 0–1 y log1p sin alterar los conteos de matrícula.
- Se conservan los 4.731 registros y se documenta la anomalía temporal de IP Santo Tomás mediante sensibilidad.
- F3 y F4 permanecen **proyectadas**, no se afirman realizadas.

## Colaboración GitHub
Repositorio original: https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile

La rama `main` representa la entrega original. Los cambios correctivos F1/F2 están en `fix/sumativa1-cned-guia-integrada-20261114` y PR #1; F3 se integra mediante una rama y PR independientes. Solo se registran commits con autor y fecha reales. Convención sugerida: `docs:`, `feat:`, `fix:`, `test:`. No se puede reconstruir retrospectivamente el historial original ni acreditar aportes de integrantes no confirmados.

**Pendiente externo:** se requiere clon e instalación por Cristian o Claudio en otro computador, autorización docente de la conformación de dos integrantes (la guía indica 3–4), URL oficial de la versión 2005–2026 y autorización de escritura para publicar los cambios.

## Sumativa 2 (F3) — ejecución y controles

El notebook F3 está en `F3/S2_F3_NucleoAlgoritmico_Cned.ipynb` y su informe final, en `docs/f3_s02_entregable_g8.pdf` (archivo nombrado con 20 caracteres antes de `.pdf`). Requiere ejecutar previamente F2 y disponer del Excel en `data/raw/`. Las pruebas incluyen herencia, polimorfismo, encapsulamiento, casos límite, equivalencia exacta del DataFrame F2/F3, `timeit` y `tracemalloc`; los resultados medidos están en `evidencias/f3_benchmarks.csv`.

El flujo `.github/workflows/validar_mcdi500.yml` ejecuta verificaciones sin Excel en GitHub Actions. **Esta CI no sustituye la prueba real de integración** porque la fuente original no está en el repositorio. Para la validación completa deben ejecutar `python -m pytest -q tests` después de generar el extracto de F2.
