# Estado verificable del proyecto MCDI500 — revisión posterior a Sumativa 1

**Corte documental:** 16 de noviembre de 2026. **Alcance:** F1/F2 corregidos y F3 desarrollado. **Calificación conocida:** 60/99 en la entrega original; ningún resultado posterior se atribuye al profesor.

## Hechos comprobados

- F1: 8 celdas de código ejecutadas en orden, sin errores guardados; definición, fuente, esquema y metadatos.
- F2: 10 celdas ejecutadas en orden, sin errores guardados; 4.731 × 68, 27 IP, matrícula primer año 137.481 y matrícula total 439.607.
- F3: 10 celdas ejecutadas en Python 3.13.17 Windows, equivalencia exacta F2–F3 y benchmarks medidos por Cristian.
- Validación independiente de Cristian en Windows: 44/44 pruebas aprobadas y 27/27 controles con Excel antes de la última ampliación de pruebas.
- GitHub: PR #1, #2, #3 y #4 aprobados e integrados a `main`, con commits auténticos de ambos integrantes.
- GitHub Actions: validación tras PR #4 aprobada; 41 pruebas ejecutadas, 3 omitidas por no versionar el Excel; auditoría F3 28/28.
- Versión documental vigente: `Informe_Sumativa1_F1_F2_Guia_Integrada.docx/.pdf`, `f3_s02_entregable_g8.docx/.pdf`.

## Pendientes académicos o externos

1. Verificar con la plantilla institucional original de Canvas; no consta acceso a ese archivo.
2. Obtener confirmación docente de la conformación de dos estudiantes en el Grupo 8.
3. Acreditar enlace/fecha exactos de procedencia del libro Excel INDICES 2005–2026.
4. Verificar en Canvas el archivo entregado y el comprobante de recepción; los commits de Git no sustituyen ese envío.

**Control:** `python scripts/verificar_proyecto.py`, `python -m pytest -q tests`, `python scripts/auditar_entrega_f3.py --integracion` en el equipo que dispone del Excel original. El repositorio no debe contener el XLSX crudo.
