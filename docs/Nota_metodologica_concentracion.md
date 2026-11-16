# Nota metodológica — interpretación de CR3 y HHI

**Variable de interés:** matrícula de primer año observada de Institutos Profesionales en Chile, 2025. **Fuente:** CNED–INDICES (ver `docs/Proveniencia_CNED_INDICES.md`).

## Indicadores

- **CR3:** porcentaje de la matrícula que concentran los tres grupos de mayor matrícula dentro de **una misma dimensión**.
- **HHI:** suma de cuadrados de las participaciones de todos los grupos de la dimensión (en la escala utilizada por `src/cned_pipeline.py`). Su magnitud describe la distribución entre esos grupos.

El análisis calcula ambos indicadores por **institución**, **región** y **área de conocimiento**. Esas dimensiones **no son particiones intercambiables**: difieren en su cantidad de grupos, definición y distribución, y un mismo registro contribuye a una categoría de cada dimensión.

## Limitación de comparaciones

**No es correcto concluir, solo porque CR3 o HHI sea más alto en una dimensión, que está «más concentrada» estructuralmente que otra.** En CR3 se comparan tres grupos de universos distintos; en HHI influye también la cantidad total de categorías y su definición.

Para interpretar:
1. Comparar grupos **dentro de la misma dimensión**, con el mismo año y la misma variable de matrícula.
2. Informar el total de grupos, el tamaño de la matrícula, los valores de CR3 y HHI y la distribución que los explica.
3. Si se pretende contrastar dimensiones, definir previamente una normalización apropiada y justificar sus supuestos; no inferir causalidad, calidad de instituciones ni deserción.

**Decisión académica:** mantener las cifras calculadas como resultados descriptivos, sin recalcular ni alterar los datos originales. La presente nota limita su interpretación, no sustituye las tablas del informe.
