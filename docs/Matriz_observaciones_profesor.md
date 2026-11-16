# Auditoría de correcciones posteriores a la Sumativa 1

**Fuente de control:** guía docente de 10 páginas, rúbrica de 15 criterios / 99 puntos y retroalimentación de Omar Salinas. **No equivale a nota obtenida**.

1. **Informe:** reordenado según 4.1–4.15, con portada, índice, evidencia y bibliografía APA 7; plantilla institucional exacta pendiente.
2. **Problema/objetivos:** una pregunta focalizada sobre concentración de matrícula de primer año y cinco objetivos medibles idénticos en README, informe y F1.
3. **F1 sin invadir F2:** no limpia ni imputa ni escribe el extracto; F2 crea `data/interim/ip_2025_origen_filtrado.csv`.
4. **Entorno verificable:** versiones exactas y prueba individual de cada dependencia; sin celdas que instalen librerías.
5. **Datos originales:** Excel preservado y hash SHA-256 documentado; fuente oficial exacta 2005–2026 pendiente.
6. **Faltantes:** conteo por variable previo a limpieza, 13 vacías y otras dos >90% documentadas.
7. **Imputación:** comparación de eliminación, media global, mediana global y jerárquica, con MAE enmascarando 10% y medición de desviación.
8. **Códigos y monedas:** identificadores y matrículas sin imputar; CLP y UF no mezclados; flags de estimación.
9. **Transformaciones:** cuartiles `qcut` justificados, escala y log1p derivados, one-hot nominal, orden explícito ordinal.
10. **Atípicos:** diagnóstico IQR para variables cuantitativas; no se eliminan máximos legítimos sin evidencia.
11. **Anomalía temporal:** IP Santo Tomás (inicio 2026) marcada, sensibilidad de 39 matrículas de primer año.
12. **Pruebas:** casos normales, límite y excepciones documentados; ejecución limpia de notebooks y guardado de salidas.
13. **Funciones:** módulo `src/cned_pipeline.py` reutilizado por F1 y F2.
14. **Mapa conceptual:** tabla de seis tipos, con estado implementado/proyectado y evidencia.
15. **GitHub:** procedimiento de ramas, commits, PR y autoría. Pendiente de ejecución por los integrantes, no simulado.
16. **Bibliografía:** 2 fuentes del profesor, ≥2 documentación oficial y ≥1 artículo publicado en los últimos cinco años, con citas internas.

Ver correspondencia completa de la guía en `docs/matriz_15_criterios.csv`. No se adjudican 99 puntos sin verificación externa de Git, integrantes y plantilla.
