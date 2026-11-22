"""Control de separación física de versiones históricas exigida por el docente."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]


def test_notebooks_historicos_separados_y_vigentes_intactos():
    pares = [
        ("F1/F1_Definición.ipynb", "historico/F1/F1_Definición.ipynb"),
        ("F2/F2_procesamiento.ipynb", "historico/F2/F2_procesamiento.ipynb"),
    ]
    for original, archivado in pares:
        assert not (ROOT / original).exists(), original
        archivo = ROOT / archivado
        assert archivo.is_file() and archivo.stat().st_size > 1000
    for vigente in ("F1/F1_Definicion_Cned.ipynb",
                    "F2/F2_Preprocesamiento_Cned.ipynb",
                    "F3/S2_F3_NucleoAlgoritmico_Cned.ipynb",
                    "F4/F4_Visualizacion_Comunicacion.ipynb"):
        assert (ROOT / vigente).is_file()


def test_csv_48_columnas_solo_en_archivo_historico():
    original = ROOT / "data/processed/matricula_ip_2025_procesada.csv"
    archivado = ROOT / "historico/data/processed/matricula_ip_2025_procesada.csv"
    assert not original.exists()
    assert archivado.is_file() and archivado.stat().st_size > 10000
    with archivado.open(encoding="utf-8-sig", newline="") as f:
        columnas = next(csv.reader(f))
    assert len(columnas) == 48, f"Esperadas 48 columnas históricas, observado {len(columnas)}"
    assert (ROOT / "data/processed/README.md").is_file()
