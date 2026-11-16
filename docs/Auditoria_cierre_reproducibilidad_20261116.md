# Auditoría de cierre — reproducibilidad y consistencia

**Grupo 8:** Cristian Pérez Cortés y Claudio Navarrete Sims. **Fecha:** 16/11/2026.

## Controles técnicos ejecutados
- **50/50 pruebas portátiles** aprobadas en la validación local sin ejecutar tests pesados de integración.
- **53/53 pruebas** aprobadas con el Excel suministrado y sus validaciones de integración.
- **F1 → F2 → F3** ejecutados sin errores en una copia temporal del proyecto; F2 entregó 4.731 filas y 68 columnas, totales 137.481 y 439.607.
- Verificación del SHA-256 de la fuente Excel y de las versiones de paquetes en el entorno Python 3.13.
- Se insertaron **dos figuras reales** en el Word/PDF local corregido de F1/F2 y se cambiaron los objetivos específicos (distribución, CR3/HHI y sensibilidad). **La versión Word/PDF fue sincronizada automáticamente** en el commit `5d84232e` de esta rama. Las comprobaciones finales aprobaron y el PR #7 fue integrado en `main`. La versión F1/F2 contiene las figuras y objetivos analíticos.

## Modificaciones propuestas
1. requirements.txt fija Jupyter Notebook 7.5.3 (junto a JupyterLab 4.5.3).
2. README describe instalación en Windows CMD y macOS/Linux desde GitHub.
3. Workflow crea instalaciones limpias independientes en Ubuntu y Windows.
4. F1 y F2 contienen exactamente los tres objetivos específicos del archivo canónico; la limpieza queda como metodología.
5. Scripts de preflight, copia temporal reproducible y auditoría de consistencia, además de pruebas portátiles adicionales.
6. Informe F1/F2 sincronizado en Word/PDF en PR #7 integrado. Cualquier versión posterior se revisa mediante su PR y CI.

## Qué NO se afirma
- Los tests CI sin Excel no sustituyen los tres tests de datos reales omitidos.
- Las pruebas locales se hicieron con dependencias del entorno ya instalado: la instalación limpia nueva la comprobará GitHub Actions.
- No se ha certificado el diseño institucional hasta obtener la plantilla Canvas.
- La aprobación final de la rúbrica y la entrega oficial dependen del profesor y Canvas.

## Aclaración del período y fuente

La fuente primaria de los datos de matrícula es **CNED–INDICES**, portal institucional https://cned.cl/institucional/bases-de-datos/. La copia usada por el equipo se denomina `Base-INDICES-Matricula-2005-2026.xlsx`, con SHA-256 registrado; la publicación visible en el sitio oficial corresponde a 2005–2025. El enlace directo, la fecha de descarga y la equivalencia precisa de esa copia no han sido recuperados. **2025** es el año analizado, mientras los informes se prepararon en **noviembre de 2026**.
