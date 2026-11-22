# Historial de cambios

## 22 de noviembre de 2026 · Cierre de relevancia y continuidad entre fases

- F1: se explicitó la relevancia externa del análisis de concentración y se distinguió de afirmaciones sobre calidad, acceso o causalidad ([453891c](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/453891c7082553c05209667874febbc265d1569e)).
- F1: se añadieron pruebas de sus objetivos, alcance, restricciones, supuestos y salidas de notebook ([77479a7](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/77479a7a9da3aec374e9df3c2aafda200e863894)).
- F4: se cotejó la evidencia versionada de equivalencia F2–F3 antes de generar visualizaciones; no equivale a reproducir el Excel original ([abc39cf](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/abc39cf8fd54239c3f1f7d07bebba5b6ec45ed0e)).
- F4: se documentó por qué se visualizan agregados en unidades originales y no una matriz transformada ([26c8d7c](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/26c8d7c00ee7e778d07347596b8f3d7d622179bb)).
- Tests: se controla automáticamente la coherencia entre el registro histórico de equivalencia F3 y F4 ([fdb4b06](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/fdb4b06ae7f5d6f69a3ff9ba15f4d7082d4b7081)).


## 22 de noviembre de 2026 · Validación autónoma F4

- Se añadieron pruebas de integridad de agregados y metadatos de F2 para F4; commit [4b96457](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/4b9645702196e466311afdc3dd772076c6bb3fdf).
- Se incorporó un ejecutor reproducible de notebook F4 usando `nbclient`; commit [617d954](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/617d954d4f03362c886637f5e89a59000fe0860b).
- Se extendió CI para ejecutar F4 automáticamente en Windows y Ubuntu; commit [5db16c2](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/5db16c256c9d4487d89826b3fd578e200c9e0fde).
- Se publicó auditoría de 26 criterios con brechas de fuente y entrega declaradas; commit [575e88f](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/575e88fa7548919f1fa722a4a0f1c7b87a998d1b).
- Se explicaron los controles F4 en su README; commit [2e6deb6](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/2e6deb613d067457baae0740464849e4264ce297).


## 20 de noviembre de 2026 · Sumativa 3

- Se integra el notebook ejecutable de F4 sobre los agregados de F2. Las figuras de región y área comparten escala en dos paneles. La comparación con y sin el registro de IP Santo Tomás reproduce el cálculo a partir del metadato de F2.
- Se incorpora el informe integrado F1–F4 en Word y PDF, con las figuras generadas por el notebook, el alcance del ensayo y la matriz de mejoras.
- Se incorpora la transcripción del resultado local de 58 pruebas a partir de la captura de consola. La verificación de F4 en un clon usa los agregados versionados.

## F1–F3 · Cambios integrados

| Fecha de integración en Chile | Cambio y justificación | Commit |
| --- | --- | --- |
| 15/11/2026 | Se alinearon los objetivos, el tratamiento de datos y los indicadores de F1–F2 con las observaciones docentes. | [d036944](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/d0369448e5127d67af633c5c1c6def03fca4a5fe) |
| 15/11/2026 | Se modularizó F3 y se compararon algoritmos sobre salidas equivalentes. | [5f017cc](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/5f017cc2560b1d1f7ba09f3c8c9b53de9df22f93) |
| 16/11/2026 | Se documentó la reproducción limpia y se distinguieron los archivos vigentes de los históricos. | [dfd987d](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/dfd987de9d479d62330ffc06261294b58507d0fd) |
| 16/11/2026 | Se precisó el alcance de CR3 y HHI y lo que acredita la huella del archivo de origen. | [f993704](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/f993704206e84b16a259c523cf819b4be4d97c2a) |
| 17/11/2026 | Se publicaron las versiones interpretativas finales de los informes anteriores. | [5b95167](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/5b951672d0a7eeaf9f6080cfbba4f173f00e8494) |
