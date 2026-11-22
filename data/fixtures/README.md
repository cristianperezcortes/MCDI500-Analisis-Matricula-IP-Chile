# Fuente reproducible IP 2025 — Grupo 8

Este directorio contiene el **subconjunto original filtrado** del libro de matrícula CNED–INDICES usado por el grupo. Se publica **sin imputación, escalamiento ni transformaciones** para ejecutar F1–F4 desde un clon limpio. **No** es el CSV histórico de 48 columnas ni el resultado F2 de 68 columnas.

## Procedencia y verificaciones

- Libro local identificado: `Base-INDICES-Matricula-2005-2026.xlsx`; SHA-256 original `0439bc1ed1a6ec018a3bbf4be34861bd33749c81c34c2eeeddbc7dcd2657c48a`.
- Libro validado a partir del ejemplar suministrado por el equipo: **260.307 filas de datos, 62 columnas, una hoja**.
- Regla de extracción: `Año == 2025` y `Tipo Institución == 'I.P.'`; no se elimina ningún otro registro ni columna del filtro.
- Archivo publicado: `ip_2025_origen_filtrado.csv`, UTF-8, saltos LF, **4.731 filas × 62 columnas**.
- SHA-256 exacta del CSV publicado: `dd5f92fd31edc9d5cea40a443646ed899a3857a8e018e78f003bc6de0705080d`. La normalización de UTF-8 y saltos de línea **no modifica los valores de los campos**.
- Indicadores comprobados: 137.481 matrículas de primer año, 439.607 matrículas totales, 27 IP, 16 regiones, 10 áreas; 1.576 registros con matrícula de primer año cero, uno con inicio posterior a 2025 (IP Santo Tomás: 39 matrículas).
- También se verificaron desgloses por sexo, ausencia de filas idénticas y coincidencia de CR3/HHI con los resultados de F2 para institución, región y área.

## Trazabilidad y límites

El **portal institucional** es https://cned.cl/institucional/bases-de-datos/ . La URL directa y fecha exacta de descarga del ejemplar denominado 2005–2026 **no constan**; la huella identifica la copia utilizada, pero no acredita por sí sola su fecha o lugar de descarga. El repositorio no publica el libro XLSX completo.

El archivo CSV es una **copia de los registros antes de cualquier limpieza**; las fases F1 y F2 lo leen cuando el Excel no está presente y la CI comprueba obligatoriamente su SHA-256 antes de procesar. El Excel original, cuando está disponible y tiene la huella declarada, sigue siendo la fuente preferida.

Se conserva `data/processed/` para los resultados derivados, diferentes de `data/fixtures/`. No modificar manualmente el CSV ni sustituirlo por versiones procesadas.
