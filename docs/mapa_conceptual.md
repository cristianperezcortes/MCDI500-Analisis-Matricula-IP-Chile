# Mapa conceptual técnico — Fases 1 y 2, CNED 2025

```mermaid
flowchart TD
  A[Pregunta: concentración de matrícula de primer año] --> B[Libro CNED aportado y SHA-256]
  B --> C[F1: definición, entorno y reconocimiento sin limpiar]
  C --> D[F2: obtención IP/2025 y perfil]
  D --> E[Normalización de ausentes y columnas inválidas]
  E --> F[Comparar eliminación, media, mediana y grupos]
  F --> G[Estimaciones, banderas y métricas de dispersión]
  G --> H[Codificación, cuartiles y escala auxiliar]
  H --> I[Validaciones y prueba de sensibilidad]
  I --> J[Participaciones CR3 HHI y CSV final]
  J --> K[F3: funciones, clases y algoritmos]
  K --> L[F4: interpretación y comunicación]
  M[Git, versiones y README] --> C
  M --> D
  M --> I
```

| Elemento | Tipo según rúbrica | Estado | Evidencia |
|---|---|---|---|
| Python, pandas, NumPy, lxml, Jupyter | Herramientas | Implementado | F1 §2; F2 §1, requirements.txt |
| Ingesta y auditoría de calidad | Procesos | Implementado | F2 §2-3; src/cned_pipeline.py |
| Fuente→extracción→validación→salida | Flujo reproducible | Implementado local | data/raw, interim, processed; tests/ |
| Ausencia, imputación, monedas, cuartiles | Decisiones técnicas | Implementado | Registro_decisiones.md; comparacion_imputaciones.csv |
| Ramas, estructura F1–F4 y README | Organización repositorio | Preparado, **no publicado** | README; GitHub pendiente |
| Narrativa, código, salidas, métricas | Estructura notebooks | Implementado y ejecutado | F1/*.ipynb; F2/*.ipynb |
| Algoritmos OOP y visualización final | F3/F4 proyectadas | Futuro | F3/README.md; F4/README.md |

**Justificación:** el mapa organiza la planificación conceptual alrededor de evidencias verificables del problema. El pipeline medido responde a esa planificación sin atribuir trabajo de F3/F4 a esta entrega. No se reclama un commit inexistente ni un acceso no acreditado.
