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
