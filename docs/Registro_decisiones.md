# Bitácora actualizada de decisiones — Sumativa 1 F1/F2

| ID | Problema técnico | Decisión y criterio | Evidencia / impacto |
|---|---|---|---|
| D01 | Unidad de análisis | Registro agregado de programa/sede/campus, no estudiante individual | 4.731 filas frente a 137.481 matrículas de primer año |
| D02 | Cobertura | IP/2025, se conservan pregrado y posgrado por comparabilidad | 4.714 + 17 registros |
| D03 | Fuente original | Excel 2005–2026 suministrado, SHA-256 en metadatos, no modificar | 260.307 × 62, versión de descarga exacta pendiente |
| D04 | Alcance F1/F2 | F1 solo define/explora; F2 obtiene/limpia/transforma | Extracto `data/interim/` escrito solo en F2 |
| D05 | Valores faltantes textuales | Tratar `Null` como ausente sin convertir 0 en NA | 13 columnas enteramente vacías |
| D06 | Campos con >90% NA | Excluir las 2 columnas identificadas, sin tocar matrícula | Grado Académico y Mención o Especialidad |
| D07 | Eliminar filas frente a imputar | Medir filas que se perderían; mantener registros para matrícula | 1.571 filas elegibles faltantes en arancel CLP, 896 en vacantes |
| D08 | Selección imputación | Comparar media, mediana global y mediana jerárquica mediante MAE con 10% enmascarado y semilla 42 | Tabla `docs/comparacion_imputaciones.csv` |
| D09 | Efecto imputación | Medir dispersión antes/después; no inferir MNAR resuelto | Variación de desviación en `comparacion_imputaciones.csv` |
| D10 | Monedas | No estimar UF con distribución de pesos | 5 aranceles UF sin estimar |
| D11 | Identificadores y matrícula | No imputar códigos ni las variables objetivo; dejar 0 legítimos | 1.576 ceros de primer año preservados |
| D12 | Transformaciones | Tipos, flags, MinMax/log1p auxiliares, one-hot de nivel y categoría ordinal explícita | 68 columnas; conteos originales intactos |
| D13 | Atípicos | Diagnóstico IQR, sin exclusión automática de ofertas grandes | `docs/diagnostico_atipicos.csv` |
| D14 | Cuartiles matrícula | `qcut` de matrícula total, conserva empates, no tramos arbitrarios | 1.223 / 1.169 / 1.165 / 1.174 registros |
| D15 | Anomalía temporal | Retener caso IP Santo Tomás, medir sensibilidad sin eliminarlo | 1 caso; 39 matrículas, 0,0284% |
| D16 | Duplicaciones | No eliminar por coincidencias de programa/sede sin verificar campus/jornada | 0 duplicados idénticos |
| D17 | Concentración | Participaciones, CR3 e HHI sobre primer año **observado** | Instituciones CR3 53,916%; regiones 79,243%; áreas 79,806% |
| D18 | Reproducibilidad | Versiones exactas, kernel, rutas relativas, pruebas con salida guardada | `requirements.txt`, F1/F2, `evidencias/` |
| D19 | Colaboración | Nuevos commits reales por autor, rama y PR, nunca retrofechar | Pendiente de autorización Git y contribuciones del equipo |

## Riesgos residuales

No se conoce el mecanismo de ausencia de datos monetarios; MAE sobre valores observados ocultados no permite probar validez causal ni ausencia aleatoria. La versión 2005–2026 necesita URL y fecha de descarga acreditadas. La instalación en otro equipo y la autoría colaborativa requieren acciones humanas verificables.
