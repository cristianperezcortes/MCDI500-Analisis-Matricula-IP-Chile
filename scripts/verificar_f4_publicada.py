"""Ejecuta F4 desde los agregados públicos y comprueba sus tres salidas.

No requiere ni sustituye el Excel original CNED necesario para F1-F3.
La ejecución se hace en memoria; no modifica el notebook versionado.
"""
from pathlib import Path
import json
import sys
import nbformat
from nbclient import NotebookClient

RAIZ = Path(__file__).resolve().parents[1]
F4 = RAIZ / "F4" / "F4_Visualizacion_Comunicacion.ipynb"
EVIDENCIAS = RAIZ / "evidencias"
FIGURAS = (
    "F4_top10_instituciones.png",
    "F4_matricula_region_area.png",
    "F4_sensibilidad_santo_tomas.png",
)


def main():
    if not F4.exists():
        raise FileNotFoundError(F4)
    notebook = nbformat.read(F4, as_version=4)
    resultado = NotebookClient(
        notebook,
        timeout=180,
        kernel_name="python3",
        resources={"metadata": {"path": str(RAIZ)}},
    ).execute()
    celdas = [c for c in resultado.cells if c.cell_type == "code"]
    esperados = list(range(1, len(celdas) + 1))
    assert [c.execution_count for c in celdas] == esperados, "Celdas sin ejecución correlativa"
    for celda in celdas:
        assert celda.outputs, "Celda de código sin salida"
        assert not any(o.get("output_type") == "error" for o in celda.outputs)
    for nombre in FIGURAS:
        archivo = EVIDENCIAS / nombre
        assert archivo.is_file() and archivo.stat().st_size > 5000, nombre
    print(json.dumps({
        "fase": "F4",
        "estado": "ejecucion_satisfactoria",
        "celdas_ejecutadas": len(celdas),
        "figuras": list(FIGURAS),
        "requiere_excel_original": False,
        "advertencia": "La ejecución de F4 sobre agregados no certifica F1-F3 desde el XLSX",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"[ERROR] F4 no reproducible: {error}", file=sys.stderr)
        raise
