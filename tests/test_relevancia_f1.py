"""Comprobaciones de la observación docente sobre problema y supuestos en F1."""
from pathlib import Path
import nbformat

ROOT = Path(__file__).resolve().parents[1]


def test_f1_declara_relevancia_externa_y_tres_categorias():
    nb = nbformat.read(ROOT / "F1" / "F1_Definicion_Cned.ipynb", as_version=4)
    texto = "\n".join(c.source for c in nb.cells if c.cell_type == "markdown")
    for expresion in (
        "Relevancia del problema y utilidad externa",
        "planificación de oferta educativa",
        "**Alcance decidido:**",
        "**Restricciones:**",
        "**Supuestos:**",
        "Objetivos específicos analíticos",
    ):
        assert expresion in texto, expresion
    assert "acceso, equidad, calidad" in texto


def test_f1_conserva_salidas_y_numeracion_de_codigo():
    nb = nbformat.read(ROOT / "F1" / "F1_Definicion_Cned.ipynb", as_version=4)
    celdas = [c for c in nb.cells if c.cell_type == "code"]
    assert [c.execution_count for c in celdas] == list(range(1, len(celdas) + 1))
    assert not any(o.get("output_type") == "error" for c in celdas for o in c.outputs)
