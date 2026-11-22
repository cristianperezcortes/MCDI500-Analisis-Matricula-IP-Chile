# Fase 4 · Visualización y comunicación

El notebook [F4_Visualizacion_Comunicacion.ipynb](F4_Visualizacion_Comunicacion.ipynb) genera las tres figuras de la Sumativa 3. Usa los [agregados de F2](../data/processed/README.md), los [metadatos F2](../docs/metadatos_fase2.json) y los [indicadores de concentración](../docs/indicadores_concentracion.csv) versionados. Las tres dimensiones concilian **137.481 matrículas de primer año**. F4 puede ejecutarse desde un clon con esos agregados. La reproducción previa de F1–F3 desde el origen requiere el Excel CNED.

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

La ejecución de las cuatro celdas en una sesión IPython nueva (Python 3.13.5) generó las tres figuras con los insumos versionados. La suite existente dio **55 pruebas aprobadas y 3 omitidas** en el clon sin los datos originales. Las omisiones corresponden al Excel CNED y al extracto que se obtiene al ejecutar F2 con ese Excel. El resultado de **58 aprobadas** corresponde a la ejecución separada de Windows con el extracto disponible.

## Controles automáticos de F4 (22/11/2026)

La suite `tests/test_f4_datos_publicados.py` comprueba independientemente los tres agregados versionados, las matrículas y registros conciliados con F2, los indicadores CR3 y HHI, la anomalía temporal de 39 matrículas y la presencia de evidencias ejecutadas.

El comando siguiente **ejecuta de nuevo** las cuatro celdas de F4 usando `nbclient` y verifica la generación de sus tres figuras; no modifica el notebook almacenado en Git:

```sh
python scripts/verificar_f4_publicada.py
```

El workflow GitHub Actions ejecuta ambas comprobaciones sobre Windows y Ubuntu tras un cambio. No necesita el Excel original para esta **subfase de comunicación**, pero **no certifica** la reproducción completa de F1–F3, que siguen requiriendo el origen CNED y su huella de integridad.

La auditoría de los 26 criterios está en [Auditoría de cierre F1–F4](../docs/Auditoria_cierre_F1_F4_20261122.md). El video Canvas Studio y la verificación de la plantilla oficial deben quedar acreditados antes de afirmar que la entrega final está cerrada.

## Contrato documentado entre F3 y F4

Además de recalcular los agregados de F2, F4 consulta `evidencias/f3_equivalencia_f2.json`, cuyo registro histórico confirma que el dataframe F3 se cotejó exactamente con F2 (4.731 × 68 y matrícula inalterada). Esta verificación evita afirmar continuidad de una transformación que no está disponible en los CSV agregados. Los tres gráficos se construyen con categorías y unidades originales; no es necesario ni correcto aplicar una inversión de escalamiento genérica a matrículas que nunca fueron reemplazadas por la escala derivada.

**Límite:** este contrato es una prueba de coherencia documental versionada, no una nueva ejecución F1–F3 desde el XLSX original.
