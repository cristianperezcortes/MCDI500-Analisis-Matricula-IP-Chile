# Fase 4 · Visualización y comunicación

El notebook [F4_Visualizacion_Comunicacion.ipynb](F4_Visualizacion_Comunicacion.ipynb) genera las tres figuras de la Sumativa 3. Usa los [agregados de F2](../data/processed/README.md), los [metadatos F2](../docs/metadatos_fase2.json) y los [indicadores de concentración](../docs/indicadores_concentracion.csv) versionados. Las tres dimensiones concilian **137.481 matrículas de primer año**. F4 puede ejecutarse desde un clon con esos agregados. La reproducción previa de F1–F3 utiliza la fuente CNED validada: el subconjunto sin limpiar de 62 columnas publicado en `data/fixtures/` o, si está disponible, el Excel completo identificado mediante SHA-256.

## Ejecución

Desde la raíz del repositorio, activar el entorno de Python 3.13 e instalar `requirements.txt`. Abrir el notebook con Jupyter y reiniciar el núcleo para ejecutar todas sus celdas. Para una ejecución por consola desde la raíz:

```sh
python -m jupyter nbconvert --to notebook --execute --inplace F4/F4_Visualizacion_Comunicacion.ipynb
```

| Objetivo | Figura exportada |
| --- | --- |
| Describir la distribución institucional | [Figura 1 · Diez instituciones con mayor matrícula](../evidencias/F4_top10_instituciones.png) |
| Interpretar la concentración por región y área | [Figura 2 · Región y área en dos paneles](../evidencias/F4_matricula_region_area.png) |
| Evaluar la sensibilidad al registro de IP Santo Tomás | [Figura 3 · Escenarios con y sin el registro](../evidencias/F4_sensibilidad_santo_tomas.png) |

La Figura 3 reproduce una variación de **39 matrículas (0,0284 %)** a partir del metadato versionado de F2. El notebook verifica CR3 y HHI por separado para cada dimensión.

## Entregables

- Informe integrado de la Sumativa 3 en [Word](../docs/f4_s03_entregable_g8.docx) y [PDF](../docs/f4_s03_entregable_g8.pdf).
- [Historial de cambios](../changelog.md) y [evidencia transcrita de las pruebas locales](../evidencias/pytest_58_pruebas.txt).
- El enlace de la presentación en Canvas Studio está pendiente.

## Validación de la integración

**Evidencia histórica del 20/11:** la ejecución inicial de F4 guardó cuatro celdas consecutivas y tres figuras; entonces las pruebas portátiles registraron **55 aprobadas y 3 omitidas**, y una ejecución local independiente en Windows documentó 58 aprobadas. Estos resultados son antecedentes, **no el estado técnico actual**.

**Verificación vigente del 22/11 (rama `main`, commit `c3c2c0b41bfe3ae644853fd4d93a571f7083f772`):** el flujo [GitHub Actions 45031068962](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/actions/runs/45031068962) finalizó exitosamente en Windows y Ubuntu. Ejecutó F1, F2, F3 y F4 desde clon limpio con el subconjunto CNED IP 2025 de 62 columnas publicado y verificado por SHA-256, además de **67 pruebas aprobadas y 0 omitidas por sistema**. La comprobación de la huella del XLSX completo sigue siendo independiente de la procedencia documental (fecha y enlace directos pendientes).

**Presentación audiovisual:** cualquier rediseño gráfico de los mismos agregados debe indicar que conserva los valores del notebook F4. Para el video, usar títulos que comuniquen resultados, interpretación y límites; las cifras no deben diferir entre PowerPoint, informe y notebook.

## Controles automáticos de F4 (22/11/2026)

La suite `tests/test_f4_datos_publicados.py` comprueba independientemente los tres agregados versionados, las matrículas y registros conciliados con F2, los indicadores CR3 y HHI, la anomalía temporal de 39 matrículas y la presencia de evidencias ejecutadas.

El comando siguiente **ejecuta de nuevo** las cuatro celdas de F4 usando `nbclient` y verifica la generación de sus tres figuras; no modifica el notebook almacenado en Git:

```sh
python scripts/verificar_f4_publicada.py
```

El workflow GitHub Actions ejecuta ambas comprobaciones sobre Windows y Ubuntu tras un cambio. No necesita el Excel original para esta **subfase de comunicación**. La reproducción integral F1–F4 está automatizada adicionalmente usando el CSV CNED original filtrado publicado en `data/fixtures/`, y no debe confundirse con la verificación de los 260.307 registros del Excel completo.

La auditoría de los 26 criterios está en [Auditoría de cierre F1–F4](../docs/Auditoria_cierre_F1_F4_20261122.md). El video Canvas Studio y la verificación de la plantilla oficial deben quedar acreditados antes de afirmar que la entrega final está cerrada.


## Nota de interpretación obligatoria para la presentación final

**Tecnología sola**: 61.423 matrículas de primer año, **44,68 %** del total de 137.481. **Administración y Comercio sola**: 35.461 matrículas, **25,79 %**. **Ambas áreas juntas**: 96.884, **70,47 %**. En ninguna figura ni texto atribuir 70,47 % exclusivamente a Tecnología. El CR3 de áreas suma además Salud y asciende a 79,806 %; no debe confundirse con dos categorías.

Ver [nota de cálculo](../docs/Nota_F4_porcentajes_areas_20261122.md) y los tests [porcentajes](../tests/test_f4_areas_precisas.py). Las tres figures F4 originales están respaldadas por los agregados CNED; las visualizaciones de apoyo audiovisual pueden variar de geometría sin variar valores ni denominadores.

**Estado actual evaluable:** la rama oficial `main` contiene F1–F4, el CSV original IP 2025 no depurado de 62 columnas, el pipeline F2 que produce 68 columnas, y controles de integración reproducibles. El registro de 55 aprobadas y 3 omitidas de una etapa inicial es histórico, no corresponde a la ejecución final de 67 aprobadas por sistema ya registrada. La fecha y URL directas del ejemplar XLSX 2005–2026 siguen sin acreditación.

\n## Figura 2 para el informe y el video\n\nLa Figura 2 original del notebook (barras) conserva la evidencia histórica. La versión de **puntos** utilizada en el informe final se reproduce con `python scripts/generar_figura2_publicacion.py` usando los mismos agregados de F2, sin cambiar números. El cambio de geometría mejora el contraste y evita tres gráficos de barras idénticos. Ver [procedimiento y denominadores](../docs/F4_figura_contraste_reproducible.md).\n