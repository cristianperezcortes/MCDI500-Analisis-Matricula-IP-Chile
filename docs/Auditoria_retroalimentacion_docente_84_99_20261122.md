# Auditoría de cierre tras retroalimentación docente — 22/11/2026

## Evidencia docente recibida
El profesor Omar Salinas informó una **recalificación de Sumativa 1 a 84/99** (comunicación aportada por el equipo). El texto docente reconoce alineación de pregunta, objetivos e indicadores; preprocesamiento fundamentado y pruebas aprobadas con el entorno declarado. Esta calificación **no se deduce del repositorio**: debe corroborarse en Canvas para constancia oficial.

## Cuatro observaciones del docente y estado verificable
| Observación | Evidencia actual | Estado |
|---|---|---|
| 1. Clon limpio con subconjunto IP 2025 **o enlace exacto y fecha de descarga** | `data/processed/matricula_ip_2025_procesada.csv` existe, **pero es versión histórica de 48 columnas**. `data/processed/matricula_ip_2025_procesada_v3.csv` de 68 columnas no está publicado en `main`. El enlace y la fecha exactos del Excel original aún no están documentados. | **Pendiente** |
| 2. Ejecutar F1 y F2 dentro del repositorio, salidas y metadatos asociados a commit | Notebooks versionados y metadatos JSON en `docs/`; existe evidencia histórica de ejecución local. No equivale a una reproducción certificada desde un clon limpio actual con el archivo fuente. | **Parcial** |
| 3. Separar históricos de vigentes en F1, F2 y data | `F1/F1_Definición.ipynb`, `F2/F2_procesamiento.ipynb` y el CSV de 48 columnas siguen junto a los archivos vigentes; `README.md` los diferencia, pero **no hay separación física completa**. | **Parcial** |
| 4. Relevancia y supuestos explícitos en el informe | Existen informes finales interpretativos y nota metodológica, pero falta cotejar cada sección con la nueva observación y la versión entregada en Canvas. | **Por verificar** |

## Estado de la implementación
- F1, F2 y F3: integrados en `main`, sin necesidad demostrada de rehacer algoritmos.
- F4: preparada en PR #15, **no integrada** al cierre de esta auditoría. Su notebook usa agregados de F2 versionados para gráficos y sensibilidad.
- GitHub Actions: PR #15 con ejecución reportada en verde en Windows y Ubuntu (https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/actions/runs/44746767759); la CI no verifica el Excel original.
- PR #9 y #12: abiertos; antes de integrarlos, comparar con el estado más reciente de `main` para evitar retrocesos de documentos.

## Secuencia mínima de cierre
1. Elegir una estrategia de reproducibilidad: publicar **solo** el subconjunto derivado IP/2025 autorizado y verificado (68 columnas, 4.731 filas), **o** acreditar URL exacta + fecha de descarga de la fuente original. No confundir el CSV histórico de 48 columnas con el vigente.
2. Comprobar SHA-256 de la fuente local frente a `docs/Proveniencia_CNED_INDICES.md`; ejecutar F1 y F2 desde un clon limpio, capturar las salidas y verificar metadatos, 4.731 filas, 68 columnas, sumas 137.481/439.607; registrar commit y entorno. **No introducir archivos de origen de manera inadvertida**.
3. Trasladar o archivar en carpetas `historico/` los notebooks de primera entrega y el CSV de 48 columnas; actualizar rutas que dependan de ellos antes de fusionar. Mantener trazabilidad y evitar borrar evidencia.
4. Revisar relevancia, supuestos, limitaciones y figura(s) del informe vigente frente a la retroalimentación y la pauta institucional.
5. Revisar PR #15 y solo fusionarlo si se valida el contenido, CI y entregables; confirmar con el profesor la autorización de equipo de dos integrantes.

## Cautelas
Un archivo de datos cargado en el computador de Cristian no significa que esté versionado en GitHub. Una prueba CI en verde sin Excel original no garantiza la reproducción íntegra. La presente auditoría no altera notebooks, resultados numéricos ni historial de autoría.
