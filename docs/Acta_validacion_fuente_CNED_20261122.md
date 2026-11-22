# Acta técnica de validación del archivo CNED – Grupo 8

**Fecha de análisis:** 22 de noviembre de 2026  
**Asignatura:** MCDI500 – Programación para la Ciencia de Datos  
**Participantes:** Cristian Pérez Cortés y Claudio Navarrete Sims (autoría del trabajo académico); el registro de cambios conserva el usuario autenticado que creó cada commit.

## 1. Identidad del ejemplar revisado

- Archivo suministrado: `Base-INDICES-Matricula-2005-2026.xlsx` (libro completo, no publicado en Git).
- SHA-256 calculada de los bytes del archivo: `0439bc1ed1a6ec018a3bbf4be34861bd33749c81c34c2eeeddbc7dcd2657c48a`.
- SHA-256 previa en `docs/metadatos_fase1.json`: **idéntica**.
- Estructura examinada: una hoja, 260.307 registros de datos, 62 columnas (`A1:BJ260308`, con encabezado).
- La identidad de bits verifica que no se está sustituyendo inadvertidamente la versión analizada, pero no acredita lugar o fecha exactos de descarga.

## 2. Extracción sin limpieza previa

Se conservaron exclusivamente los registros donde `Año = 2025` y `Tipo Institución = I.P.`, leyendo los valores del XLSX y preservando las 62 variables.

| Control | Resultado |
|---|---:|
| Registros IP 2025 | 4.731 |
| Columnas antes de transformar | 62 |
| Instituciones IP | 27 |
| Regiones | 16 |
| Áreas de conocimiento | 10 |
| Matrículas de primer año | 137.481 |
| Matrículas totales | 439.607 |
| Matrículas de primer año iguales a cero | 1.576 |
| Pregrado / posgrado (registros) | 4.714 / 17 |
| Filas duplicadas exactas | 0 |
| Filas con desgloses hombre/mujer/no binario incoherentes | 0 |
| Registro con inicio de actividades en 2026 | 1 (IP Santo Tomás, 39 matrículas) |

## 3. Indicadores contrastados con F2

| Dimensión | Grupos | CR3 (%) | HHI |
|---|---:|---:|---:|
| Instituciones | 27 | 53,916 | 1.348,247 |
| Regiones | 16 | 79,243 | 4.402,463 |
| Áreas | 10 | 79,806 | 2.862,560 |

Los agregados completos concilian exactamente **4.731 registros y 137.481 matrículas** en cada dimensión; los indicadores coinciden con el reporte previo F2.

## 4. Archivo publicado en GitHub

- `data/fixtures/ip_2025_origen_filtrado.csv` (UTF-8, 4.731 registros y 62 variables).
- SHA-256: `dd5f92fd31edc9d5cea40a443646ed899a3857a8e018e78f003bc6de0705080d`.
- Git blob SHA del archivo almacenado: `d33644f84ebef273946af0a554339b27b0efa6f9`; comprobado contra el archivo normalizado, sin diferencias.
- La versión en CSV representa los registros **originales filtrados**, no un reemplazo del Excel ni el CSV analítico F2 de 68 columnas.
- Los cambios de F1/F2 permiten seleccionar el Excel original cuando está presente o el subconjunto publicado con comprobación obligatoria de SHA cuando no está.

## 5. Reproducibilidad y límites del cierre

La rama de esta mejora incorpora un workflow que exige la fuente publicada, ejecuta F1 → F2 → F3 → F4 desde copia limpia y valida los resultados con pruebas unitarias/de integración en Windows y Ubuntu.

**El cumplimiento final se supedita a que esas ejecuciones concluyan satisfactoriamente tras el commit correspondiente.** El original completo permanece en resguardo externo al repositorio. El enlace directo y fecha exacta de descarga del ejemplar 2005–2026 siguen sin acreditarse, y la entrega del video y del informe en Canvas es independiente de estas comprobaciones.
