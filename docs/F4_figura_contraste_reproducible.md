# Figura 2 alternativa reproducible para la Sumativa 3

La [figura de contraste de publicación](../scripts/generar_figura2_publicacion.py) se genera con una **gráfica de puntos**, usando las mismas matrículas y agregados de la Fase 2 que el notebook F4. Responde al criterio de la guía docente que recomienda evitar entregar tres figuras de barras iguales. No crea un cuarto resultado: es una **representación alternativa de la Figura 2**, con exactamente el mismo universo de 137.481 matrículas.

Para generar desde un clon limpio:

```sh
python scripts/generar_figura2_publicacion.py --output evidencias/F4_region_area_puntos_publicacion.png
```

La imagen exportada se utiliza en el PDF del informe académico y su contenido puede contrastarse con `data/processed/matricula_por_region.csv`, `data/processed/matricula_por_area.csv` y `docs/metadatos_fase2.json`. El notebook `F4/F4_Visualizacion_Comunicacion.ipynb` mantiene además su figura original de barras como evidencia histórica; todas las cifras son idénticas.

**Aclaración de porcentajes:** Región Metropolitana 65,23 %; **Tecnología aislada 44,68 %**; Administración y Comercio 25,79 %; ambas áreas 70,47 %. Ninguno de estos valores representa causalidad o calidad institucional.

Se valida con `tests/test_f4_figura_publicacion.py` y GitHub Actions en la rama principal.
