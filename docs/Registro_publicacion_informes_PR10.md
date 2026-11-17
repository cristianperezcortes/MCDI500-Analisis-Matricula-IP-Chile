# PR #10 — Registro de publicación de informes oficiales UNAB (Grupo 8)

**Estado: PREPARACIÓN — los cuatro archivos DOCX/PDF aún deben adjuntarse a esta rama antes de fusionar.**

**Curso:** MCDI500, Programación para la Ciencia de Datos. **Integrantes confirmados por el docente:** Cristian Pérez Cortés y Claudio Navarrete Sims. **Fecha de documentos:** 16 de noviembre de 2026.

## Archivos definitivos aprobados por el equipo para publicar

Guardar cada archivo directamente bajo `docs/`, **sin cambiar su nombre**:

| Archivo | Tamaño (bytes) | SHA-256 esperado |
|---|---:|---|
| `UNAB_Informe_Fases_1_y_2_Grupo8.docx` | 175746 | `dbe61c38fb699694ec7b467174df856b2247e502ff2ea7e7e373c18b532566d1` |
| `UNAB_Informe_Fases_1_y_2_Grupo8.pdf` | 302773 | `faaec37ba69a4a91770707c2ce0625a9c54a58e711b3800ef3046b38c34d1919` |
| `UNAB_Informe_Fase_3_Grupo8.docx` | 258632 | `28b104912c7eb84ce37d09735af3101188ef2b11c730a2ffc8d1c3d8f64255a7` |
| `UNAB_Informe_Fase_3_Grupo8.pdf` | 416877 | `8eb3e2c41a320d0270f71694e3b273038a3105478d2c64d149f1342a386b1798` |

Los archivos locales se inspeccionaron: DOCX como contenedores ZIP válidos y PDF legibles con 7 páginas (F1/F2) y 8 páginas (F3). Los SHA-256 identifican **exactamente** las versiones recibidas del equipo, no acreditan envío a Canvas.

## Checklist antes de aprobar PR #10

- [ ] Confirmar que los **cuatro archivos** estén disponibles en la rama `docs/pr10-informes-unab-definitivos-20261116` dentro de `docs/`
- [ ] Comparar sus hashes SHA-256 con la tabla anterior; no generar archivos alternativos con el mismo nombre
- [ ] Actualizar `README.md` con vínculos a los cuatro documentos vigentes y una nota que preserve los anteriores como históricos; hacerlo **después** de subirlos
- [ ] Verificar los 11 apartados institucionales, las portadas de dos integrantes, figuras, páginas y legibilidad
- [ ] Comprobar las diferencias del PR: sólo documentos finales, este registro y README; **sin editar notebooks, `src/`, `tests/` ni datos**
- [ ] Confirmar GitHub Actions en Windows y Ubuntu; el CI no valida exhaustivamente el contenido de Word/PDF
- [ ] Cristian registra su revisión genuina; seleccionar Ready for review y fusionar `main` sólo después del control

**Importante:** la subida a GitHub no equivale a la entrega oficial en Canvas. Evitar declarar PR #10 terminado antes de acreditar los cuatro archivos y la CI.
