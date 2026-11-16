"""Impide regresiones entre objetivos y notebooks del proyecto MCDI500."""
import nbformat
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_versiones_academicas_fijadas():
    req=(ROOT/"requirements.txt").read_text(encoding="utf-8")
    assert "notebook==7.5.3" in req and "openpyxl==3.1.5" in req
def test_objetivos_mismos_en_f1_y_f2():
    objetivos=(ROOT/"docs/objetivos_analiticos_f1f3.txt").read_text(encoding="utf-8").splitlines()
    assert len(objetivos)==3
    for rel in ("F1/F1_Definicion_Cned.ipynb","F2/F2_Preprocesamiento_Cned.ipynb"):
        nb=nbformat.read(ROOT/rel,as_version=4)
        md="\n".join(c.source for c in nb.cells if c.cell_type=="markdown")
        assert all(x in md for x in objetivos)
def test_no_instalar_en_notebooks():
    for rel in ("F1/F1_Definicion_Cned.ipynb","F2/F2_Preprocesamiento_Cned.ipynb","F3/S2_F3_NucleoAlgoritmico_Cned.ipynb"):
        nb=nbformat.read(ROOT/rel,as_version=4)
        source="\n".join(c.source for c in nb.cells if c.cell_type=="code")
        assert "%pip install" not in source and "!pip install" not in source
