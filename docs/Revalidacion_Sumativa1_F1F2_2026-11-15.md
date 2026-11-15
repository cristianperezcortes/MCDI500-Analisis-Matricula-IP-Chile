# Revalidación integral Sumativa 1 (F1/F2) — 15 de noviembre de 2026

**Evaluación original:** 60/99; **evaluación interna de la versión corregida:** pruebas técnicas aprobadas, sin atribuir una nota docente.

**Fuente de referencia académica:** enunciado y rúbrica Sumativa 1 (15 criterios, 99 puntos), guía docente Fases 1/2, retroalimentación firmada por Omar Iván Salinas Silva, y notebooks de ejemplo de `magistercienciadatos/Material_Didactico_Semana1`.

## Cotejo requisito → evidencia

| Criterio | Evidencia concreta y decisión | Estado interno |
|---|---|---|
| 1 Portada e índice | `docs/Informe_Sumativa1_F1_F2_Guia_Integrada.pdf` y DOCX, índice y portada | Revisado; cotejo plantilla Canvas pendiente |
| 2 Introducción | Caso CNED IP/2025, relevancia y fases F1–F4 | Documentado |
| 3 Problemática/objetivos | Pregunta específica: matrícula primer año por institución, región y área; alcance y límites | Coherente con F1/F2 |
| 4 Herramientas | pandas, NumPy, Jupyter, funciones en `src/cned_pipeline.py` | Probado |
| 5 Reproducibilidad | `requirements.txt`, kernel, rutas relativas y versiones | Ejecutado localmente; segundo equipo pendiente |
| 6 Control Git | Rama correctiva y PR #1, 3 commits reales | Publicado; revisión colaborativa pendiente |
| 7 Documentación | `docs/Registro_decisiones.md`, metadatos, auditorías y notebooks narrados | Documentado |
| 8 Repositorio | F1/F2, README, pruebas, scripts y evidencias en GitHub | Estructura verificada |
| 9 Codificación | Funciones reutilizables y excepciones explícitas | Probado |
| 10 Preprocesamiento | Cuatro estrategias, estimaciones diferenciadas, 0 legítimos, CLP/UF, banderas e IQR | Probado en 4.731 filas |
| 11 Validación | Reglas de invariantes, casos límite/excepciones, regresión y logs | 23/23 tests F1/F2; 40/40 integrando F3 |
| 12 Notebook F1 | 8 celdas ejecutadas; definición y exploración sin limpieza | Ejecución completa guardada |
| 13 Notebook F2 | 10 celdas ejecutadas; obtención, exploración, limpieza, transformación y validación | Ejecución completa guardada |
| 14 Mapa conceptual | `docs/mapa_conceptual.md`, vínculo F1/F2 y pendientes F3–F4 | Documentado |
| 15 Formato APA | Documento con referencias docentes, técnicas y académicas | Revisado; plantilla oficial pendiente |

## Indicadores de integración (Excel suministrado)

- **Registros:** 4.731 de 27 Institutos Profesionales en 2025; 62 variables de entrada.
- **Matrícula:** primer año 137.481; total 439.607; desgloses por sexo coinciden con el total.
- **Procesado F2:** 4.731 × 68 columnas (columnas auxiliares, no datos observados nuevos).
- **Control de duplicados:** cero filas idénticas; coincidencias de programa y sede no se borran automáticamente.
- **Registro temporal:** un caso de IP Santo Tomás posterior al año de referencia, identificado y conservado para sensibilidad.
- **Validez de NA:** 13 columnas vacías y 2 excluidas por faltantes; la imputación se limita a variables auxiliares cuantitativas, no a identificadores ni matrículas.

## Hallazgos críticos y acciones

1. El registro académico debe llevar **solamente Cristian Pérez Cortés y Claudio Navarrete Sims** como integrantes confirmados; no se atribuirá participación de los otros alumnos nombrados en la evaluación inicial.
2. El README antiguo contenía una advertencia de permisos de GitHub de una fecha anterior. Fue corregido para describir el PR #1 ya creado.
3. **La validación en un segundo equipo aún no está acreditada.** No se dará por cumplida sin que un integrante ejecute el proyecto de manera independiente.
4. La guía exige 3–4 integrantes; la conformación del grupo con dos estudiantes debe contar con confirmación del docente. La respuesta del equipo no equivale a aprobación académica.
5. El Excel `Base-INDICES-Matricula-2005-2026.xlsx` es idéntico al utilizado en las pruebas, pero **falta acreditar el URL y fecha de su descarga oficial**. Se conserva la huella SHA-256.
6. El informe cumple la estructura académica interna, aunque **la plantilla de Canvas** no está disponible para cotejar márgenes/logotipo/campos institucionales exactos.

La revisión es deliberadamente exigente: **código ejecutable no equivale a rúbrica formal completa**. La integración se hará mediante revisión de PR, sin alterar el historial original ni simular contribuciones.
