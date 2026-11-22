# Historial de cambios

## 22 de noviembre de 2026 · Reproducibilidad integral con datos CNED reales

| Mejora aplicada | Justificación y evidencia | Commit |
|---|---|---|
| Se publicó el subconjunto original IP 2025 de 62 columnas y 4.731 registros, sin imputaciones | Permite que el evaluador clone y reproduzca las fases sin Excel local. Fuente XLSX y CSV cotejados por SHA-256 | [2979c6f](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/2979c6f4eb0dbaff1503a9554c69d7bec986de21) |
| Se amplió el cargador para usar Excel o CSV validado, sin perder invariantes | Misma lógica analítica y obligación de comprobar integridad antes de transformar | [b5aeeaa](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/b5aeeaa16e14031cb321e7e6eff57a08c4cec41a) |
| Se adaptaron notebooks F1–F3 para el origen reproducible | Ejecución en clon limpio, sin exigir archivos exclusivos del equipo de Cristian | [9e343d3](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/9e343d3ad87d5343d8a560a7aeca4681f0543448), [0e0ab3f](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/0e0ab3fa0b10a34eb6bec1e27a69905b6dbe8e92), [a54fb4d](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/a54fb4d7764124875b03610d1e3e7d1240cc9b69) |
| Se automatizó F1→F4 y la equivalencia F2–F3 en Windows y Ubuntu | Se sustituyen las omisiones por pruebas reales sobre la fuente publicada | [30f9b4b](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/30f9b4b63170f8cc108e8cbe02f604fbfadc3530), [9c48aa9](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/9c48aa98fa1a31e3c62731759550924907a3f25a) |
| Se corrigió un error específico de Git en Windows (LF/CRLF) y otro de rutas F1 | Evita falsos fallos de huella y rutas cuando el Excel completo no está presente | [9c971fd](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/9c971fd67f3c0c800aecaa979fc924136fc1fe7c), [bb8fc2b](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/bb8fc2b1483b348d43f98773a18d8fe281cf6668) |
| Se auditaron resultados, procedencia y reproducción global | Comprobación de 260.307 registros del XLSX, totales 137.481/439.607 y CR3/HHI, sin atribuir fecha/URL de descarga no verificada | [4353fbe](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/4353fbefd98a137085e4bcfa1d66a76972461341), [b65a143](https://github.com/cristianperezcortes/MCDI500-Analisis-Matricula-IP-Chile/commit/b65a143a26f6b26ee985a0374994a1945cdc0087) |

**Criterio de cierre:** los resultados de CI deben comprobarse en Windows y Ubuntu para el commit final y la reproducción debe quedar integrada en `main`. Las puntuaciones docentes y la entrega de Canvas no se suponen aprobadas.


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
