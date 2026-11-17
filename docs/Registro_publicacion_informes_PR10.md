# Registro de publicación de informes oficiales UNAB — PR #10 a PR #12 (Grupo 8)

**Estado verificable al 17-11-2026:** PR #10 integró el manifiesto; PR #11 integró una carga equivocada; PR #12 contiene los cuatro archivos correctos en la rama `docs/correccion-informes-unab`, pero **no se declara integrado en `main` mientras no se fusione**. La comprobación se refiere al commit de la rama revisada.

**Curso:** MCDI500, Programación para la Ciencia de Datos. **Integrantes confirmados por el docente:** Cristian Pérez Cortés y Claudio Navarrete Sims. **Fecha de documentos:** 16 de noviembre de 2026.

## Archivos definitivos aprobados por el equipo para publicar

Archivos presentes en `docs/` de la rama del PR #12, con sus nombres definitivos y huellas verificadas contra los cuatro archivos entregados por el equipo:

| Archivo | Tamaño (bytes) | SHA-256 esperado |
|---|---:|---|
| `UNAB_Informe_Fases_1_y_2_Grupo8.docx` | 175746 | `dbe61c38fb699694ec7b467174df856b2247e502ff2ea7e7e373c18b532566d1` |
| `UNAB_Informe_Fases_1_y_2_Grupo8.pdf` | 302773 | `faaec37ba69a4a91770707c2ce0625a9c54a58e711b3800ef3046b38c34d1919` |
| `UNAB_Informe_Fase_3_Grupo8.docx` | 258632 | `28b104912c7eb84ce37d09735af3101188ef2b11c730a2ffc8d1c3d8f64255a7` |
| `UNAB_Informe_Fase_3_Grupo8.pdf` | 416877 | `8eb3e2c41a320d0270f71694e3b273038a3105478d2c64d149f1342a386b1798` |

Los archivos locales se inspeccionaron: DOCX como contenedores ZIP válidos y PDF legibles con 7 páginas (F1/F2) y 8 páginas (F3). Los SHA-256 identifican **exactamente** las versiones recibidas del equipo, no acreditan envío a Canvas.

## Comprobaciones de la rama PR #12

- [x] Los **cuatro archivos** se encuentran en `docs/` dentro de `docs/correccion-informes-unab` con los nombres exactos.
- [x] Los cuatro SHA-256 y tamaños coinciden con los archivos locales originales aprobados por el equipo. Sus hashes Git blob también coinciden.
- [x] El PR #12 reemplaza/retira los informes cargados erróneamente y no cambia notebooks, `src/`, `tests/`, `requirements.txt` ni conjuntos de datos.
- [x] Se actualizó `README.md` con enlaces a versiones oficiales, referencias históricas y conformación de Grupo 8 confirmada por correo del docente.
- [x] GitHub Actions del commit previo a estos ajustes registró resultado `success` en Windows y Ubuntu.
- [ ] Confirmar **GitHub Actions del nuevo commit** de documentación en ambos sistemas antes del merge.
- [ ] Revisar contenido académico y formateo final de Word/PDF por los integrantes; la CI no evalúa el mérito científico.
- [ ] Registrar revisión genuina y fusionar PR #12 a `main` cuando todas las comprobaciones estén verdes.
- [ ] Verificar los cuatro enlaces en `main` después del merge y efectuar la entrega oficial en Canvas.

**Precisión sobre historial:** PR #10 se fusionó antes de la carga de los informes; PR #11 incorporó los archivos incorrectos; PR #12 reúne la rectificación. No se atribuye al PR #10 una subida que no ocurrió en él.

**Precisión sobre pruebas:** las pruebas de GitHub Actions omiten controles que necesitan el Excel original, mantenido fuera de GitHub; existe evidencia de validaciones locales anteriores. Ninguna prueba automatizada sustituye la revisión académica ni prueba la entrega en Canvas.
