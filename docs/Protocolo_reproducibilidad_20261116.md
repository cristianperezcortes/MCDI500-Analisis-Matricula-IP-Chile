# Protocolo reproducible del Grupo 8 — MCDI500

**Corte:** 16 de noviembre de 2026. Este protocolo es evidencia técnica interna, no una nota del profesor.

## Entorno y dependencia de datos
Python 3.13, Pandas 2.2.3, NumPy 2.3.5, openpyxl 3.1.5, Jupyter Notebook 7.5.3, JupyterLab 4.5.3 y demás dependencias fijadas en requirements.txt.

GitHub Actions parte de un **checkout limpio** con una matriz **Windows y Ubuntu** e instala el entorno completo. Como la fuente CNED no está en GitHub, las pruebas de integración que exigen el Excel se indican **skipped**, no aprobadas.

Para un ensayo completo, copiar el XLSX suministrado en data/raw y comprobar su SHA-256. En un entorno Python 3.13 recién configurado:
    python scripts/verificar_entorno.py --exigir-excel
    python scripts/reproducir_desde_cero.py --ejecutar
    python -m pytest -q tests
    python scripts/verificar_proyecto.py
    python scripts/auditar_entrega_f3.py --integracion

La reproducción crea una copia temporal del proyecto, ejecuta F1→F2→F3 en procesos Jupyter separados y **no sobrescribe** el CSV, las figuras ni las cifras timeit del informe publicado. Es normal obtener otros tiempos en otra máquina.

## Coherencia científica
Los objetivos **analíticos** son distribución, concentración (CR3 y HHI) y sensibilidad del registro atípico IP Santo Tomás. La selección, imputación y limpieza son **actividades metodológicas**, no objetivos de investigación. El archivo docs/objetivos_analiticos_f1f3.txt establece su redacción canónica.

Los notebooks F1, F2 y F3 y el informe F1/F2 deben mantener esa misma formulación. El control scripts/auditar_consistencia_academica.py comprueba su correspondencia. El Word/PDF actualizado fue integrado mediante el PR #7 y su correspondencia académica fue comprobada por CI en Windows y Ubuntu.

## Límites institucionales (pendientes, no aprobados)
1. Plantilla institucional solicitada al profesor, aún no disponible para cotejo.
2. Aceptación docente del grupo integrado por dos estudiantes.
3. Enlace y fecha exactos de descarga CNED 2005–2026; la huella SHA-256 identifica el archivo recibido, no demuestra la URL histórica.
4. Comprobante del envío a Canvas.

El informe F3 conserva las mediciones reales de Windows de Cristian: 21,020 ms y 1,889 ms para el caso de 4.731 filas. No alterar esas cifras sin rehacer y registrar el experimento y regenerar todas las evidencias documentales.

## Procedencia y comparación de concentración

La fuente primaria de los datos es CNED–INDICES: https://cned.cl/institucional/bases-de-datos/. La copia analizada está identificada por SHA-256; el nombre de archivo 2005–2026 no constituye por sí mismo prueba de descarga de esa edición, mientras el portal público muestra 2005–2025. Ver `docs/Proveniencia_CNED_INDICES.md`.

CR3 y HHI se informan por institución, región y área, pero sus valores no deben compararse ingenuamente entre dimensiones con distinto número de grupos. Ver `docs/Nota_metodologica_concentracion.md`.
