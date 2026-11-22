# Revisión académica previa a presentación F4 · Grupo 8
**Corte:** 22/11/2026 · `main` SHA `c3c2c0b41bfe3ae644853fd4d93a571f7083f772`.

## Evidencias confirmadas
- Fuente XLSX cotejada por SHA-256 `0439bc1ed1a6ec018a3bbf4be34861bd33749c81c34c2eeeddbc7dcd2657c48a`; 260.307 registros y 62 columnas. El Excel completo no se publica en Git.
- CSV **sin limpiar** `data/fixtures/ip_2025_origen_filtrado.csv`: 4.731 × 62, hash `dd5f92fd31edc9d5cea40a443646ed899a3857a8e018e78f003bc6de0705080d`. F2 genera 4.731 × 68; la versión anterior de 48 columnas está en `historico/`.
- Matrícula primer año 137.481, matrícula total 439.607, 27 instituciones, 16 regiones y 10 áreas. CR3 institución 53,916 %; región 79,243 %; área 79,806 %. HHI respectivamente 1.348,247; 4.402,463; 2.862,560. No equiparar dimensiones entre sí.
- Notebook F1 8 celdas, F2 10, F3 10, F4 4: salidas versionadas con numeración consecutiva y ningún error guardado.
- Run de [GitHub Actions #45031068962](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/actions/runs/45031068962): F1–F4 desde clon limpio, validación de fuente, equivalencia F2–F3, **67 pruebas aprobadas y 0 omitidas tanto en Ubuntu como Windows**.
- F3 implementa base abstracta y transformadores POO. Medición sobre 4.731 registros: bucles 21,020 ms y groupby 1,889 ms, ~11,1x en esa ejecución; groupby mostró memoria pico mayor en tracemalloc (0,2383 frente a 0,1356 MiB).
- Hallazgos principales: DUOC UC 33.104, AIEP 25.422 e IP Latinoamericano de Comercio Exterior 15.598 (suma 74.124 = 53,92 %). Metropolitana 89.674 (65,23 %); Tecnología y Administración y Comercio 96.884 (70,47 %). Sensibilidad Santo Tomás: solo 39 matrículas (0,0284 %).

## Riesgos residuales y pasos no técnicos
1. La guía recomienda no usar **tres figuras de barras similares**. Las figuras guardadas en el notebook F4 son todas de barras; en la presentación oral es admisible una nueva geometría con los **mismos datos**, y se debe mantener el relato contexto–contraste–resolución. Comprobar si la plantilla exige identidad gráfica literal.
2. El informe Word/PDF F4 fue preparado antes del cierre técnico reproducible; debe cotejarse contra la **plantilla institucional exacta** (29 apartados, máximo 10 páginas, APA 7) y contra la última CI para evitar metadatos de ejecución desactualizados.
3. La fuente original está identificada por hash; la **URL directa y fecha exacta de descarga** del ejemplar 2005–2026 siguen sin acreditación.
4. La video-presentación de **5–8 minutos con ambos estudiantes** y el comprobante Canvas deben producirlos y verificarlos Cristian y Claudio. La validación administrativa de grupo de dos necesita evidencia documental.

**Conclusión:** código y datos reproducibles y validados; la calificación académica final y Canvas no pueden declararse terminados ni garantizados por un workflow verde.
