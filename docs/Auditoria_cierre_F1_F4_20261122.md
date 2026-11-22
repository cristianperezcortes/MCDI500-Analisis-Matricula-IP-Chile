# Auditoría de cierre – Sumativa 3 (Grupo 8)

**Fecha:** 22-11-2026. **Integrantes:** Cristian Pérez Cortés y Claudio Navarrete Sims.
**Objetivo:** documentar lo verificable y los pendientes reales antes de la entrega.
**Nota académica conocida:** el docente informó al grupo que Sumativa 1 fue recalificada a **84/99**. No se afirma que ello equivalga a aprobar Sumativa 3.

## Evidencia técnica observada

- La rama de F4 contiene `F4/F4_Visualizacion_Comunicacion.ipynb` con cuatro celdas de código y numeración guardada 1–4; tres imágenes, informe Word y PDF, README y changelog.
- Los CSV agregados por institución, región y área están versionados; permiten comunicar el universo IP/2025 mediante 4.731 registros y 137.481 matrículas de primer año. El notebook F4 compara CR3 y HHI con el documento de F2.
- `historico/data/processed/matricula_ip_2025_procesada.csv` conserva la entrega histórica de **48 columnas**, separada físicamente en la rama de cierre; **NO** es el dataset vigente F2 de 68 columnas. El CSV v3 de 68 columnas y el libro Excel original no figuran en los árboles de Git examinados.
- F1 y F2 exigen `data/raw/Base-INDICES-Matricula-2005-2026.xlsx`; los agregados publicados **no permiten** repetir toda la limpieza, imputación ni equivalencia F2/F3 desde cero.
- La fuente institucional se atribuye a CNED–INDICES; **fecha y URL exactas de la copia 2005–2026 siguen sin acreditación**.
- Las pruebas portátiles F1–F3 existen y están automatizadas; en esta rama se añaden pruebas específicas de F4 y ejecución real del notebook mediante `nbclient` dentro de CI.

## Control por los 26 criterios

| Apartado | Pts | Evidencia / revisión requerida |
|---|---:|---|
| 1 Portada e índice | 3 | Verificar plantilla institucional exacta e índice actualizado |
| 2 Introducción/contextualización | 6 | Explicar utilidad para interpretación de distribución y concentración, no calidad educativa |
| 3 Problema y objetivos | 6 | Concordar tres objetivos analíticos con tres figuras; separar alcance, restricciones y supuestos |
| 4 Herramientas científicas | 9 | Versiones verificables en `requirements.txt` y notebooks |
| 5 Reproducibilidad | 6 | F4 reproducible con CSV versionados; F1–F3 pendientes de acceso limpio al XLSX |
| 6 Control de versiones | 6 | Commits auténticos, no reconstruir aportes de participantes |
| 7 Documentación del proceso | 6 | README, bitácora y registros de decisiones |
| 8 Repositorio GitHub | 6 | F1–F4 y pruebas en `main` después de integrar PR |
| 10 Codificación funcional | 9 | `src/cned_pipeline.py`; revisar responsabilidades y contratos |
| 11 Preprocesamiento del dataset | 6 | F2, comparación de imputaciones, validaciones; falta reproducción sin fuente |
| 12 Validación técnica | 6 | `tests/`, casos normal/límite/excepción, resultados CI |
| 13 Eficiencia y optimización | 6 | `evidencias/f3_benchmarks.csv`; interpretar tiempo y memoria con cautela |
| 14 Diseño estructurado | 6 | Módulos `src/` y justificativos de arquitectura |
| 15 Notebook final | 3 | F4 ejecutable; verificar secuencia F1–F4 con fuente completa cuando esté disponible |
| 17 Programación orientada a objetos | 6 | `src/f3_transformaciones.py`, clases, estado, contratos |
| 18 Arquitectura | 6 | `docs/f3_arquitectura.csv` y decisiones justificadas |
| 20 Datos para visualizar | 6 | Agregados legibles con unidades originales; no confundir con one-hot/escala 0–1 |
| 21 Tres visualizaciones | 6 | `evidencias/F4_*.png`; revisar título, eje, fuente, valores, límite y objetivo |
| 22 Metodología | 6 | F1–F4, decisiones `X→razón→resultado`, colaboración y benchmarks |
| 23 Validación/reflexión | 3 | Comparar fases e interpretar límites de CI |
| 24 Resultados | 3 | Tres hallazgos respaldados por agregados y metadatos |
| 25 Discusión | 3 | No atribuir causas, desempeño ni calidad educativa a matrícula |
| 26 Conclusiones | 3 | Conclusiones ligadas a objetivos y límites declarados |
| 27 Trazabilidad | 3 | `changelog.md`, vínculo corrección→commit real |
| 28 Presentación audiovisual | 12 | **Pendiente:** video real de ambos integrantes, 5–8 min en Canvas Studio |
| 29 Bibliografía/aspectos formales | 9 | APA 7, ≥2 fuentes del curso, ≥2 técnicas oficiales, ≥1 académica; plantilla y ≤10 páginas |

Los apartados 9, 16 y 19 son encabezados, sin puntuación propia.

## Secuencia para cierre efectivo

1. Validar nuevo workflow de CI Windows/Ubuntu con `scripts/verificar_f4_publicada.py` y `tests/test_f4_datos_publicados.py`; registrar enlace de las ejecuciones.
2. Conseguir el archivo de origen con SHA-256 `0439bc1ed1a6ec018a3bbf4be34861bd33749c81c34c2eeeddbc7dcd2657c48a` **o** la ruta/fecha exactas y trazables; reproducir F1→F2→F3. No reemplazar fuente por un CSV histórico.
3. **Implementado en rama de cierre:** los notebooks F1/F2 históricos y el CSV de 48 columnas se reubicaron en `historico/` conservando los blobs Git originales; README, docs/README_VERSIONES.md y data/processed/README.md actualizados. La integración final requiere CI verde y merge.
4. Confirmar que el PDF final respeta plantilla, 29 apartados, máximo 10 páginas y APA 7. El informe existente se somete a contraste, no a afirmación automática de conformidad.
5. Insertar URL de video Canvas Studio, acreditar participación auténtica y confirmar aceptación administrativa del Grupo 8.
6. Aprobar e integrar cambios verificables en la rama principal; repetir revisión después del merge. Una PR abierta no equivale a entrega.

> Este registro no es una certificación de 150/150 ni un comprobante de Canvas. Los puntos pendientes están declarados para evitar que el informe afirme lo que la fuente o GitHub todavía no demuestran.

## Actualización posterior: fuente reproducible desde GitHub

Se examinó el libro XLSX suministrado por el grupo, cuyo SHA-256 coincide con la fuente de F1–F3. Se comprobó que contiene 260.307 registros y 62 columnas, y se extrajeron los 4.731 registros IP 2025 antes de cualquier transformación, publicados en `data/fixtures/ip_2025_origen_filtrado.csv`. Los agregados coinciden con 137.481 matrículas de primer año, 439.607 totales, CR3 y HHI. El CSV publicado tiene SHA-256 `dd5f92fd31edc9d5cea40a443646ed899a3857a8e018e78f003bc6de0705080d`.

La automatización de esta rama incorpora ejecución integral F1–F4 y pruebas de integración sobre los datos reales filtrados, sin depender de un Excel guardado en el computador. **No afirmar éxito de CI hasta comprobar la última ejecución de Windows y Ubuntu**. Sigue abierta la evidencia documental de fecha/URL exactas de descarga y la entrega de video en Canvas.
