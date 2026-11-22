# Aclaración metodológica: Tecnología individual y participación conjunta

**Proyecto:** MCDI500, Grupo 8 · Análisis de matrícula IP de primer año 2025.

## Denominador único
El universo estudiado suma **137.481 matrículas de primer año** (no equivale a personas únicas). Los CSV agrupados de F2 son una partición del mismo universo; se obtienen desde `data/fixtures/ip_2025_origen_filtrado.csv` mediante el pipeline reproducible.

| Área | Matrículas | Participación del total |
|---|---:|---:|
| **Tecnología** | **61.423** | **44,6774 % ≈ 44,68 %** |
| Administración y Comercio | 35.461 | 25,7934 % ≈ 25,79 % |
| **Ambas áreas sumadas** | **96.884** | **70,4708 % ≈ 70,47 %** |

**Regla obligatoria:** nunca rotular «Tecnología: 70,47 %». Esa cifra corresponde exclusivamente a la suma de Tecnología y Administración y Comercio. Tampoco es el CR3 de áreas, que suma los tres mayores grupos: Tecnología, Administración y Comercio, y Salud (**79,806 %**).

## Qué significa cada concentración
- **CR3 de áreas = 79,806 %:** suma de las tres categorías de conocimiento con mayor matrícula; NO solo dos.
- **HHI de áreas = 2.862,560:** suma de participaciones al cuadrado sobre las diez áreas.
- La Región Metropolitana concentra **89.674** matrículas (**65,2265 % ≈ 65,23 %**).
- CR3/HHI institucional, territorial y por áreas describen **particiones diferentes**, por lo que no se usan para inferir causas, calidad educativa o tasas de acceso.

## Evidencias y control automático
Fuente: `data/processed/matricula_por_area.csv`, `data/processed/matricula_por_region.csv`, `docs/metadatos_fase2.json`; test `tests/test_f4_areas_precisas.py`. Presentación y guion deben distinguir siempre los tres porcentajes y mostrar fuente, unidad y límite del estudio.

La copia completa del Excel se identifica por SHA-256, pero la URL y fecha exactas de descarga del ejemplar 2005–2026 no están acreditadas; no afirmar que el hash pruebe esos extremos.
