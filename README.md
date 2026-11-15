# MCDI500 — Proyecto CNED IP 2025 (Sumativa 1, Fases 1 y 2)

**Asignatura:** Programación para la Ciencia de Datos. **Programa:** Magíster en Ciencia de Datos e Inteligencia Artificial (UNAB). **Docente:** Omar Iván Salinas Silva.
**Equipo declarado en entrega original:** Cristian Pérez Cortés y Claudio Navarrete Sims. **Confirmación Grupo 8:** verificar Óscar Quezada y Carlos Vergara con el docente; no se atribuye participación que no esté acreditada.

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
5. Ejecutar `python -m pytest -q tests/` y `python scripts/verificar_proyecto.py`. Revisar salidas en `evidencias/` y `docs/`.

## Decisiones y evidencia
- La matrícula y los códigos originales no se imputan. Se conservan 1.576 ceros reales de matrícula de primer año.
- Las variables monetarias CLP y UF se mantienen separadas; los valores UF ausentes no se inventan.
- Se comparan eliminación, media global, mediana global y mediana jerárquica, con enmascaramiento 10%, MAE y desviación antes/después, semilla 42.
- Las variables transformadas derivadas tienen banderas; se generan one-hot de nivel, escala 0–1 y log1p sin alterar los conteos de matrícula.
- Se conservan los 4.731 registros y se documenta la anomalía temporal de IP Santo Tomás mediante sensibilidad.
- F3 y F4 permanecen **proyectadas**, no se afirman realizadas.

## Colaboración GitHub
Repositorio original: https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile

La rama `main` representa la entrega original. La versión mejorada debe publicarse en una rama nueva, con commits reales de cada integrante y una solicitud de integración (pull request). Convención sugerida: `docs:`, `feat:`, `fix:`, `test:`. No se puede reconstruir retrospectivamente el historial original ni acreditar aportes de integrantes no confirmados.

**Pendiente externo:** se requiere clon e instalación por un segundo integrante, confirmación de integrantes, URL oficial de la versión 2005–2026 y autorización de escritura para publicar los cambios.
