# Auditoría de correcciones académicas F1/F2 — 16 de noviembre de 2026

**Objeto:** resolver las observaciones posteriores a la primera evaluación de 60/99, conservando la autoría y el historial auténticos. No se atribuye una recalificación.

## Modificaciones verificables

1. **Índice del informe:** se insertó un índice real actualizable de Word con páginas (TOC de niveles 1–2), verificado también en PDF de 9 páginas tamaño carta.
2. **Problema:** se reescribió como situación de investigación sobre distribución y concentración de matrícula de primer año. La pregunta y el objetivo general son idénticos a F1 y F2.
3. **Mapa conceptual:** se añadió una figura que explica F1 → F2 → F3 implementada → F4 pendiente, con fuente DOT reproducible.
4. **Presentación:** se eliminaron marcas Markdown `**` visibles y referencias desactualizadas a PR pendientes; anexo presentado en página independiente.
5. **Versiones:** el README y `docs/README_VERSIONES.md` distinguen claramente la primera entrega de 48 columnas de la salida corregida de 68 columnas.
6. **Trazabilidad Git:** se documentan los cuatro PR integrados, las revisiones y commits auténticos de ambos integrantes.
7. **Control de datos completo:** nueva función `auditar_columnas_originales_completas` para auditar la conservación exacta de columnas numéricas completas, y de etiquetas textuales completas después de normalizar espacios. Los placeholders como `Null` cuentan como ausentes semánticos.
8. **Pruebas:** seis pruebas unitarias nuevas en `tests/test_f2_conservacion_columnas.py`; batería local con Excel original: **50/50 aprobadas**. No se cambió ni reescribió la fuente.

## Condiciones que siguen fuera del alcance de la automatización

- Obtener y aplicar la plantilla institucional exacta desde Canvas.
- Confirmar formalmente por el docente la conformación del Grupo 8 con dos personas.
- Acreditar fecha, URL o mecanismo verificable de la versión del Excel INDICES 2005–2026.
- Revisar el comprobante del envío realizado en Canvas. Un merge de GitHub no equivale a la entrega académica.

Las versiones corregidas no sustituyen la primera entrega histórica ni alteran la nota original. Los archivos anteriores se mantienen identificados como **históricos**, para demostrar continuidad del proyecto.
