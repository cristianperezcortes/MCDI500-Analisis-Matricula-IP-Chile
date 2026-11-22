# MCDI500 — Proyecto CNED IP 2025 (Fases 1 a 4)

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
F4/F4_Visualizacion_Comunicacion.ipynb  visualizaciones, interpretación y sensibilidad
src/f3_transformaciones.py          clase base y tres transformaciones
src/f3_pipeline.py                  orquestador y equivalencia con F2
src/f3_medicion.py                  timeit y tracemalloc
src/f3_recursion.py                 recursividad de metadatos
scripts/verificar_proyecto.py       auditoría automatizada
validar_dataset.py                  criterios mínimos de dataset
tests/                              pruebas unitarias y de integración
docs/                               informe, mapa, diccionario, metadatos, comparaciones
evidencias/                         pruebas, auditoría y gráfico
data/raw/                           Excel original opcional (no versionado)
data/fixtures/                      Subconjunto CNED IP/2025 62 columnas con SHA-256
data/interim/                       extracto filtrado generado exclusivamente en F2
data/processed/                     CSV final e indicadores
```

## Archivos vigentes e históricos (evitar confusiones académicas)

- **Informe Sumativa 1 corregido:** `docs/Informe_Sumativa1_F1_F2_Guia_Integrada.pdf` (y su DOCX editable).
- **Informe Sumativa 2 F3 definitivo:** `docs/f3_s02_entregable_g8.pdf` (y su DOCX editable).
- **Notebooks vigentes:** `F1/F1_Definicion_Cned.ipynb`, `F2/F2_Preprocesamiento_Cned.ipynb`, `F3/S2_F3_NucleoAlgoritmico_Cned.ipynb`.
- **Versión histórica de Sumativa 1 (60/99):** `historico/F1/F1_Definición.ipynb`, `historico/F2/F2_procesamiento.ipynb`, `docs/Informe_Tecnico_Semana1.pdf`, `docs/informe_tecnico.md`, `docs/Revision_calidad_datos.md` y `historico/data/processed/matricula_ip_2025_procesada.csv` (**48 columnas**, resultado original). No usarlos como dataset vigente.
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

### Secuencia de reproducción con Excel original o CSV verificado en GitHub

1. El clon ya contiene `data/fixtures/ip_2025_origen_filtrado.csv` (4.731 × 62) sin transformar, extraído del Excel original cuya huella SHA-256 está documentada. Si se dispone del libro original, situarlo sin modificar en `data/raw/`: se utilizará preferentemente.
2. Ejecutar los notebooks F1 → F2 → F3 con **Restart Kernel and Run All Cells**, cada uno desde la raíz del repositorio o su carpeta.
3. Ejecutar los controles:

```cmd
python scripts/verificar_entorno.py --exigir-fuente
python -m pytest -q tests
python scripts/verificar_proyecto.py
python scripts/auditar_entrega_f3.py --integracion
python scripts/auditar_consistencia_academica.py
```

4. Para una reproducción completa sin alterar el historial de mediciones de Cristian, ejecutar `python scripts/reproducir_desde_cero.py --ejecutar`. Repite F1–F4 en una carpeta temporal con el CSV publicado o, si está disponible, el Excel original. Para dejar derivados preparados para tests en CI usar `--mantener-derivados-ci`. Los tiempos de `timeit` varían por computador.

**Evidencia diferenciada:** la CI de esta actualización ejecuta F1 → F2 → F3 → F4 y pruebas de integración contra el subconjunto CNED publicado, verificando su huella y sus 4.731 × 62 registros. Si se dispone del Excel íntegro identificado por SHA-256, también puede reproducirse el filtrado de los 260.307 registros originales. La URL y fecha exactas de descarga siguen pendientes de acreditación. La CI verde no reemplaza el control académico de Canvas.

## Decisiones y evidencia
- La matrícula y los códigos originales no se imputan. Se conservan 1.576 ceros reales de matrícula de primer año.
- Las variables monetarias CLP y UF se mantienen separadas; los valores UF ausentes no se inventan.
- Se comparan eliminación, media global, mediana global y mediana jerárquica, con enmascaramiento 10%, MAE y desviación antes/después, semilla 42.
- Las variables transformadas derivadas tienen banderas; se generan one-hot de nivel, escala 0–1 y log1p sin alterar los conteos de matrícula.
- Se conservan los 4.731 registros y se documenta la anomalía temporal de IP Santo Tomás mediante sensibilidad.
- **F3 implementada y revisada:** núcleo POO, equivalencia estricta F2–F3, benchmarks y pruebas sintéticas autónomas. **F4:** visualizaciones e interpretación desde los agregados versionados.

## Colaboración GitHub
Repositorio original: https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile

La rama `main` integra las correcciones y la implementación F3; la entrega original se conserva en los commits y archivos históricos. Los cambios correctivos F1/F2 están en `fix/sumativa1-cned-guia-integrada-20261114` y PR #1; F3 y auditoría se integraron mediante PR #2–4; F1/F2 se reforzaron en PR #5; el control de versiones se actualizó en PR #6 y el cierre de reproducibilidad e informes en PR #7. Solo se registran commits con autor y fecha reales. Convención sugerida: `docs:`, `feat:`, `fix:`, `test:`. No se puede reconstruir retrospectivamente el historial original ni acreditar aportes de integrantes no confirmados.

**Pendiente externo:** confirmación del docente sobre el equipo de dos integrantes, procedencia exacta de la versión XLSX 2005–2026, plantilla Canvas y comprobante de entrega oficial. La instalación independiente de Cristian en Windows ya se verificó. La escritura en las ramas de revisión ya fue verificada y los PR están publicados.

## Sumativa 2 (F3) — ejecución y controles

El notebook F3 está en `F3/S2_F3_NucleoAlgoritmico_Cned.ipynb` y su informe final, en `docs/f3_s02_entregable_g8.pdf` (archivo nombrado con 20 caracteres antes de `.pdf`). Requiere ejecutar previamente F2 y disponer de **una fuente CNED validada**, bien el Excel íntegro en `data/raw/` o el subconjunto original publicado en `data/fixtures/`. Las pruebas incluyen herencia, polimorfismo, encapsulamiento, casos límite, equivalencia exacta del DataFrame F2/F3, `timeit` y `tracemalloc`; los resultados medidos están en `evidencias/f3_benchmarks.csv`. La auditoría interna adicional se ejecuta con `python scripts/auditar_entrega_f3.py` (sin Excel) o `python scripts/auditar_entrega_f3.py --integracion` (con los datos reales generados por F2).

El flujo `.github/workflows/validar_mcdi500.yml` ejecuta la reproducción real F1–F4, comparación exacta F2–F3 y pruebas unitarias e integración en Windows y Ubuntu con el **subconjunto original 2025 versionado**. El libro Excel íntegro de 58 MB no se sube al repositorio y puede validarse por separado mediante su SHA-256.

## Precaución sobre indicadores de concentración

Los índices **CR3 y HHI** se interpretan por separado para instituciones, regiones y áreas de conocimiento. Las tres dimensiones tienen números y definiciones de grupos diferentes; comparar sus valores directamente no constituye, por sí solo, evidencia de que una dimensión esté «más concentrada» en sentido estructural. Ver `docs/Nota_metodologica_concentracion.md`.

## Sumativa 3 (F4) — visualización y comunicación

- [Guía de ejecución y vínculo entre objetivos y figuras](F4/README.md).
- [Notebook F4 ejecutado](F4/F4_Visualizacion_Comunicacion.ipynb) con tres figuras exportadas y análisis de sensibilidad.
- [Informe integrado en PDF](docs/f4_s03_entregable_g8.pdf) y [Word editable](docs/f4_s03_entregable_g8.docx).
- [Historial de cambios](changelog.md) y [transcripción de las 58 pruebas locales](evidencias/pytest_58_pruebas.txt).
- Presentación audiovisual en Canvas Studio, con enlace pendiente.

## Informes académicos oficiales — Grupo 8

### Versiones finales interpretativas

Los siguientes documentos PDF corresponden a las versiones finales interpretativas de los informes académicos del proyecto MCDI500 de la Universidad Andrés Bello, elaborados por el Grupo 8.

| Entregable | PDF final |
|---|---|
| Informe Fases 1 y 2 | [Ver PDF final](docs/UNAB_Informe_Fases_1_y_2_Grupo8_Final.pdf) |
| Informe Fase 3 | [Ver PDF final](docs/UNAB_Informe_Fase_3_Grupo8_Final.pdf) |

### Versiones anteriores e históricas

Se conservan los informes publicados anteriormente mediante el PR #13, para mantener la trazabilidad documental y el historial de versiones del proyecto.

| Entregable | Word | PDF anterior |
|---|---|---|
| Informe Fases 1 y 2 | [Descargar Word](docs/UNAB_Informe_Fases_1_y_2_Grupo8.docx) | [Ver PDF](docs/UNAB_Informe_Fases_1_y_2_Grupo8.pdf) |
| Informe Fase 3 | [Descargar Word](docs/UNAB_Informe_Fase_3_Grupo8.docx) | [Ver PDF](docs/UNAB_Informe_Fase_3_Grupo8.pdf) |

Las versiones finales interpretativas se incorporan mediante el PR #14, sin modificar los notebooks, el código Python ni los resultados analíticos previamente validados.

La entrega oficial en Canvas se realiza de forma independiente.

## Reproducibilidad IP 2025 incorporada en noviembre de 2026

Ver [fuente versionada y sus huellas](data/fixtures/README.md) y [auditoría de F1–F4](docs/Auditoria_cierre_F1_F4_20261122.md). El CSV original filtrado de 62 columnas y su SHA-256 están publicados; **no confundir** con el dataset procesado de 68 columnas generado por F2 ni con el histórico de 48 columnas. El origen Excel se verificó con 260.307 registros y el mismo hash del trabajo anterior, pero la fecha y URL directas de descarga de ese ejemplar CNED 2005–2026 no están acreditadas.


## Precisión final para la evaluación F4 (22/11/2026)

- **Repositorio evaluable:** la rama `main` (no una rama antigua ni un PR abierto). El Excel de 260.307 filas permanece externo a GitHub; `data/fixtures/ip_2025_origen_filtrado.csv` es el subconjunto IP/2025 **original filtrado sin limpiar**, 4.731 × 62, con SHA-256. F2 genera el derivado de 68 columnas durante la reproducción limpia.
- **Reproducción:** consultar los checks de GitHub Actions del commit que se entregue; los workflows ejecutan F1→F4 sobre el CSV publicado con tests en Ubuntu y Windows. El Excel completo solo se necesita para repetir además la extracción desde los 260.307 registros.
- **Porcentajes sin ambigüedad:** Tecnología representa 44,68 %, Administración y Comercio 25,79 %, ambas áreas suman 70,47 % del total de 137.481; el CR3 de áreas (tres grupos) es 79,806 %. Ver `docs/Nota_F4_porcentajes_areas_20261122.md`.
- **Entregables de Canvas:** el PDF final de Sumativa 3 y el video en Canvas Studio se entregan por la vía institucional, independientemente del repositorio. No afirmar video entregado, aprobación docente ni fecha/URL exacta del ejemplar XLSX mientras no exista evidencia.
