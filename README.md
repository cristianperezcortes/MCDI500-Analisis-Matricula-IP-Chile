# MCDI500 — Proyecto CNED IP 2025 (Fases 1, 2 y 3)

**Asignatura:** Programación para la Ciencia de Datos. **Programa:** Magíster en Ciencia de Datos e Inteligencia Artificial (UNAB). **Docente:** Omar Iván Salinas Silva.
**Grupo 8 — integrantes confirmados por el equipo:** Cristian Pérez Cortés y Claudio Navarrete Sims. Óscar Quezada y Carlos Vergara **no** integran este grupo de trabajo. **Nota administrativa:** la guía menciona grupos de 3–4 estudiantes; se debe comunicar al docente que el Grupo 8 está formado por 2 y solicitar su validación formal, sin atribuir dicha aprobación antes de recibirla.

## Pregunta de investigación
¿Cómo se distribuye y concentra la matrícula de primer año de los Institutos Profesionales en Chile durante 2025, según institución, región y área de conocimiento?

## Objetivo general
Analizar la distribución y la concentración de la matrícula de primer año de los Institutos Profesionales en Chile durante 2025, por institución, región y área de conocimiento, mediante un flujo de procesamiento y análisis descriptivo reproducible en Python.

## Datos y fuente
- **Fuente institucional primaria:** portal oficial CNED–INDICES del Consejo Nacional de Educación (https://cned.cl/institucional/bases-de-datos/), señalado por el equipo como origen de sus datos. **Copia analizada:** `Base-INDICES-Matricula-2005-2026.xlsx`, hoja `BaseINDICES_2005_2026`, 260.307 filas y 62 variables, identificada con SHA-256. **Año estudiado: 2025; edición documental: noviembre de 2026.**
- Subconjunto IP/2025: 4.731 registros, 27 instituciones, 137.481 matrículas de primer año y 439.607 matrículas totales (pregrado + posgrado, como la entrega original).
- Portal institucional: https://cned.cl/institucional/bases-de-datos/
- **Trazabilidad de procedencia:** CNED–INDICES es la fuente primaria institucional; el equipo trabajó con una copia identificada como 2005–2026. El portal oficial consultado muestra actualmente la edición de matrícula 2005–2025. La URL directa, fecha de descarga y equivalencia entre ambas copias **no están acreditadas**. No se altera el Excel; su SHA-256 consta en `docs/metadatos_fase1.json`. Ver `docs/Proveniencia_CNED_INDICES.md`.

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

## Archivos vigentes e históricos (evitar confusiones académicas)

- **Informe Sumativa 1 corregido:** `docs/Informe_Sumativa1_F1_F2_Guia_Integrada.pdf` (y su DOCX editable).
- **Informe Sumativa 2 F3 definitivo:** `docs/f3_s02_entregable_g8.pdf` (y su DOCX editable).
- **Notebooks vigentes:** `F1/F1_Definicion_Cned.ipynb`, `F2/F2_Preprocesamiento_Cned.ipynb`, `F3/S2_F3_NucleoAlgoritmico_Cned.ipynb`.
- **Versión histórica de Sumativa 1 (60/99):** `F1/F1_Definición.ipynb`, `F2/F2_procesamiento.ipynb`, `docs/Informe_Tecnico_Semana1.pdf`, `docs/informe_tecnico.md`, `docs/Revision_calidad_datos.md` y `data/processed/matricula_ip_2025_procesada.csv` (**48 columnas**, resultado original). No usarlos como dataset vigente.
- **Resultado corregido:** ejecutar F2 para generar `data/processed/matricula_ip_2025_procesada_v3.csv` (**68 columnas**). El XLSX original nunca debe alterarse ni publicarse.
- **Bitácora de cambios:** `docs/README_VERSIONES.md`; mapa de fases actualizado `docs/mapa_conceptual.md`.
- **Integración Git:** PR #1–7 integrados a `main` al corte del 16/11/2026; para cambios posteriores consultar los PR y checks vigentes. Se conserva la autoría real de cada participante.

## Reproducibilidad y versiones exactas

El proyecto utiliza **Python 3.13.x** y versiones directas fijadas en `requirements.txt`, incluido **Jupyter Notebook 7.5.3**, **JupyterLab 4.5.3** y `openpyxl`. No se instalan librerías desde notebooks.

### Windows: CMD, desde un clon limpio

```cmd
cd /d C:\mcdi500
git clone https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile.git
cd MCDI500-Analisis-Matricula-IP-Chile
py -3.13 -m venv "%USERPROFILE%\venvs\mcdi500"
"%USERPROFILE%\venvs\mcdi500\Scripts\activate.bat"
python -m pip install --upgrade pip
python -m pip install --only-binary=:all: -r requirements.txt
python -m pip check
python scripts/verificar_entorno.py
python -m ipykernel install --user --name mcdi500-cned --display-name "Python 3.13 - MCDI500"
python -m notebook
```

En CMD trabajar desde una carpeta local corta fuera de OneDrive. En Jupyter seleccionar el kernel **Python 3.13 - MCDI500**.

### macOS / Linux

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip check
python scripts/verificar_entorno.py
python -m ipykernel install --user --name mcdi500-cned --display-name "Python 3.13 - MCDI500"
python -m notebook
```

### Secuencia de las fases con el Excel original

1. Colocar el archivo `Base-INDICES-Matricula-2005-2026.xlsx` en `data/raw/`, sin modificarlo.
2. Ejecutar los notebooks F1 → F2 → F3 con **Restart Kernel and Run All Cells**, cada uno desde la raíz del repositorio o su carpeta.
3. Ejecutar los controles:

```cmd
python scripts/verificar_entorno.py --exigir-excel
python -m pytest -q tests
python scripts/verificar_proyecto.py
python scripts/auditar_entrega_f3.py --integracion
python scripts/auditar_consistencia_academica.py
```

4. Para un ensayo que **no sobrescriba las métricas oficiales de Cristian**, ejecutar `python scripts/reproducir_desde_cero.py --ejecutar`. Crea y borra una copia temporal con la misma fuente original. Los tiempos de `timeit` varían por computador.

**Dos niveles de evidencia:** GitHub Actions valida instalación y pruebas en Windows y Ubuntu desde checkout limpio, **sin** la fuente original; tres pruebas de datos reales se omiten explícitamente en GitHub. La reproducción con Excel y comprobación SHA-256 se hace localmente. No se atribuye una nota académica a ninguna prueba.

## Decisiones y evidencia
- La matrícula y los códigos originales no se imputan. Se conservan 1.576 ceros reales de matrícula de primer año.
- Las variables monetarias CLP y UF se mantienen separadas; los valores UF ausentes no se inventan.
- Se comparan eliminación, media global, mediana global y mediana jerárquica, con enmascaramiento 10%, MAE y desviación antes/después, semilla 42.
- Las variables transformadas derivadas tienen banderas; se generan one-hot de nivel, escala 0–1 y log1p sin alterar los conteos de matrícula.
- Se conservan los 4.731 registros y se documenta la anomalía temporal de IP Santo Tomás mediante sensibilidad.
- **F3 implementada y revisada:** núcleo POO, equivalencia estricta F2–F3, benchmarks y pruebas sintéticas autónomas; **F4 permanece pendiente**.

## Colaboración GitHub
Repositorio original: https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile

La rama `main` integra las correcciones y la implementación F3; la entrega original se conserva en los commits y archivos históricos. Los cambios correctivos F1/F2 están en `fix/sumativa1-cned-guia-integrada-20261114` y PR #1; F3 y auditoría se integraron mediante PR #2–4; F1/F2 se reforzaron en PR #5; el control de versiones se actualizó en PR #6 y el cierre de reproducibilidad e informes en PR #7. Solo se registran commits con autor y fecha reales. Convención sugerida: `docs:`, `feat:`, `fix:`, `test:`. No se puede reconstruir retrospectivamente el historial original ni acreditar aportes de integrantes no confirmados.

**Pendiente externo:** confirmación del docente sobre el equipo de dos integrantes, procedencia exacta de la versión XLSX 2005–2026, plantilla Canvas y comprobante de entrega oficial. La instalación independiente de Cristian en Windows ya se verificó. La escritura en las ramas de revisión ya fue verificada y los PR están publicados.

## Sumativa 2 (F3) — ejecución y controles

El notebook F3 está en `F3/S2_F3_NucleoAlgoritmico_Cned.ipynb` y su informe final, en `docs/f3_s02_entregable_g8.pdf` (archivo nombrado con 20 caracteres antes de `.pdf`). Requiere ejecutar previamente F2 y disponer del Excel en `data/raw/`. Las pruebas incluyen herencia, polimorfismo, encapsulamiento, casos límite, equivalencia exacta del DataFrame F2/F3, `timeit` y `tracemalloc`; los resultados medidos están en `evidencias/f3_benchmarks.csv`. La auditoría interna adicional se ejecuta con `python scripts/auditar_entrega_f3.py` (sin Excel) o `python scripts/auditar_entrega_f3.py --integracion` (con los datos reales generados por F2).

El flujo `.github/workflows/validar_mcdi500.yml` ejecuta verificaciones sin Excel en GitHub Actions, incluida una prueba de integración F2–F3 sobre un dataset **sintético**. **Esta CI no sustituye la prueba real de integración** porque la fuente original no está en el repositorio. Para la validación completa deben ejecutar `python -m pytest -q tests` después de generar el extracto de F2.

## Precaución sobre indicadores de concentración

Los índices **CR3 y HHI** se interpretan por separado para instituciones, regiones y áreas de conocimiento. Las tres dimensiones tienen números y definiciones de grupos diferentes; comparar sus valores directamente no constituye, por sí solo, evidencia de que una dimensión esté «más concentrada» en sentido estructural. Ver `docs/Nota_metodologica_concentracion.md`.
