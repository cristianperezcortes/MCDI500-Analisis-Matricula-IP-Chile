"""Regresión F4: Tecnología individual NO equivale a Tecnología + Administración."""
import csv
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def test_porcentajes_tecnologia_y_administracion_no_se_confunden():
    ruta = RAIZ / "data" / "processed" / "matricula_por_area.csv"
    with ruta.open(encoding="utf-8-sig", newline="") as archivo:
        filas = list(csv.DictReader(archivo))
    metadatos = json.loads((RAIZ / "docs" / "metadatos_fase2.json").read_text(encoding="utf-8"))
    total = int(metadatos["matricula_primer_anio"])
    areas = {fila["Area Conocimiento"]: int(fila["matricula_primer_anio"]) for fila in filas}
    assert total == sum(areas.values()) == 137481
    tecnologia = areas["Tecnología"]
    administracion = areas["Administración y Comercio"]
    assert tecnologia == 61423
    assert administracion == 35461
    assert round(100 * tecnologia / total, 2) == 44.68
    assert round(100 * administracion / total, 2) == 25.79
    assert round(100 * (tecnologia + administracion) / total, 2) == 70.47
    assert round(100 * tecnologia / total, 2) != 70.47


def test_areas_provienen_de_un_mismo_universo_y_mantienen_cr3():
    with (RAIZ / "data" / "processed" / "matricula_por_area.csv").open(
        encoding="utf-8-sig", newline=""
    ) as archivo:
        datos = list(csv.DictReader(archivo))
    assert len(datos) == 10
    valores = sorted((int(f["matricula_primer_anio"]) for f in datos), reverse=True)
    assert sum(int(f["registros"]) for f in datos) == 4731
    assert round(100 * sum(valores[:3]) / sum(valores), 3) == 79.806
