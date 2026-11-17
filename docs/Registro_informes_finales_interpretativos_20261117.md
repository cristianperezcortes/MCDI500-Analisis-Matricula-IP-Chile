# Control de publicación — versiones finales interpretativas UNAB, Grupo 8

**Estado:** dos PDF finales interpretativos incorporados a la rama del PR #14. README actualizado. Pendiente de revisión final, verificación de integridad y fusión con main.

## Archivos verificados que deben publicarse en `docs/`

| Archivo | Tamaño (bytes) | SHA-256 |
|---|---:|---|
| `UNAB_Informe_Fases_1_y_2_Grupo8_Final.pdf` | 304662 | `9db64da5ee77723aadb3fd78a72b8f069a9c510ed74aa46829b6ff2f56958c5a` |
| `UNAB_Informe_Fase_3_Grupo8_Final.pdf` | 420237 | `59a6387d7448b7e3566489502250898a18cb9646a78ce3afdca8616f8ea40955` |

Verificaciones locales: PDF legibles, páginas tamaño carta (612 × 792 pt); Fases 1–2: **7 páginas** y Fase 3: **8 páginas**; no se observaron bloques de texto fuera de los límites de página. Portadas con Cristian Pérez Cortés y Claudio Navarrete Sims, asignatura MCDI500, docente Omar Iván Salinas Silva. Ambos incorporan interpretación crítica posterior a PR #13 y referencian la CI de `main`.

## Procedimiento de publicación y revisión

1. En esta rama, entrar en `docs/` → **Add file → Upload files**; seleccionar exactamente los dos PDF de la tabla, conservar sus nombres y confirmar commit a la **rama actual**, no a `main`.
2. Comprobar tamaños y SHA-256 contra la tabla, que los documentos abran correctamente y que los 11 apartados respeten el orden de la plantilla.
3. Actualizar `README.md` y `docs/README_VERSIONES.md` para identificar estos dos PDF como las versiones finales interpretativas oficiales, conservando las versiones previas como históricas. Mantener las referencias al Word editable previo sin equipararlo a estos PDF nuevos (no se entregó Word final con el mismo nombre).
4. Verificar `Checks` exitosos para **Windows y Ubuntu** del último commit de la rama.
5. Cristian y Claudio revisan el contenido académico. Pasar de **Draft** a **Ready for review**, registrar revisión genuina y fusionar sólo si los archivos y checks están correctos.
6. Verificar publicación en `main` y entregar los PDF en Canvas de forma independiente.

**No cambiar** `F1/`, `F2/`, `F3/`, `src/`, `tests/`, datasets ni cifras/benchmarks ya validados.

**Control de versiones:** PR #13 ya incorporó documentos previos en `main`; PR #12 sigue abierto y contiene cambios documentales no fusionados. Este PR se limita a agregar las dos versiones PDF finales y actualizar referencias después de su carga. No eliminar los anteriores hasta decidir expresamente la política de archivo histórico.
