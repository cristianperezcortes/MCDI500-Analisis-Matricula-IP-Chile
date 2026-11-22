"""Pruebas portátiles de las fuentes PUBLICADAS para F4, sin Excel original."""
from pathlib import Path
import csv
import json
import math
import nbformat
import pytest

RAIZ = Path(__file__).resolve().parents[1]
PROCESADOS = RAIZ / "data" / "processed"
METADATOS = RAIZ / "docs" / "metadatos_fase2.json"
INDICADORES = RAIZ / "docs" / "indicadores_concentracion.csv"
NOTEBOOK = RAIZ / "F4" / "F4_Visualizacion_Comunicacion.ipynb"

DIMENSIONES = {
    "institucion": ("Nombre Institución", 27),
    "region": ("Nombre Region", 16),
    "area": ("Area Conocimiento", 10),
}


def leer_csv(ruta):
    with ruta.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


@pytest.fixture(scope="module")
def metadatos():
    return json.loads(METADATOS.read_text(encoding="utf-8"))


@pytest.mark.parametrize("dimension,columna,grupos", [
    (dimension, columna, grupos)
    for dimension, (columna, grupos) in DIMENSIONES.items()
])
def test_agrupados_reproducen_resultados_f2(dimension, columna, grupos, metadatos):
    tabla = leer_csv(PROCESADOS / f"matricula_por_{dimension}.csv")
    assert len(tabla) == grupos
    assert len({fila[columna] for fila in tabla}) == grupos
    valores = [int(fila["matricula_primer_anio"]) for fila in tabla]
    conteos = [int(fila["registros"]) for fila in tabla]
    assert min(valores) >= 0 and min(conteos) >= 0
    assert sum(valores) == metadatos["matricula_primer_anio"] == 137481
    assert sum(conteos) == metadatos["registros"] == 4731
    indicadores = {fila["dimension"]: fila for fila in leer_csv(INDICADORES)}
    esperado = indicadores[columna]
    participaciones = [v / sum(valores) for v in sorted(valores, reverse=True)]
    cr3 = round(100 * sum(participaciones[:3]), 3)
    hhi = round(10000 * sum(p * p for p in participaciones), 3)
    assert int(esperado["grupos"]) == grupos
    assert int(esperado["total_matricula_primer_anio"]) == sum(valores)
    assert math.isclose(float(esperado["cr3_pct"]), cr3, abs_tol=0.001)
    assert math.isclose(float(esperado["hhi"]), hhi, abs_tol=0.001)


def test_la_anomalia_f2_es_trazable_y_no_se_exagera(metadatos):
    diferencia = int(metadatos["impacto_anomalia_primer_anio"])
    total = int(metadatos["matricula_primer_anio"])
    assert metadatos["validacion"]["filas_anomalia_temporal"] == 1
    assert diferencia == 39
    assert total - diferencia == 137442
    assert round(100 * diferencia / total, 4) == 0.0284


def test_notebook_f4_ejecutado_sin_errores_y_con_tres_figuras():
    assert NOTEBOOK.exists(), "La F4 debe estar en la rama evaluable"
    notebook = nbformat.read(NOTEBOOK, as_version=4)
    codigo = [c for c in notebook.cells if c.cell_type == "code"]
    assert len(codigo) == 4
    assert [c.execution_count for c in codigo] == [1, 2, 3, 4]
    assert all(c.outputs for c in codigo)
    assert not any(
        salida.get("output_type") == "error"
        for celda in codigo for salida in celda.outputs
    )
    archivos = [
        "F4_top10_instituciones.png",
        "F4_matricula_region_area.png",
        "F4_sensibilidad_santo_tomas.png",
    ]
    for nombre in archivos:
        ruta = RAIZ / "evidencias" / nombre
        assert ruta.exists() and ruta.stat().st_size > 5000
        assert ruta.read_bytes()[:8] == bytes.fromhex("89504e470d0a1a0a")



def test_informe_f4_word_y_pdf_en_su_lugar_y_legibles():
    """Evita un PDF que supere el límite de la guía o binarios dañados."""
    from zipfile import ZipFile
    from pypdf import PdfReader

    pdf = RAIZ / "docs" / "f4_s03_entregable_g8.pdf"
    word = RAIZ / "docs" / "f4_s03_entregable_g8.docx"
    assert pdf.is_file() and pdf.stat().st_size > 10000
    assert word.is_file() and word.stat().st_size > 10000
    lector = PdfReader(str(pdf))
    assert 1 <= len(lector.pages) <= 10, "La guía limita el informe a 10 páginas"
    contenido = " ".join(p.extract_text() or "" for p in lector.pages)
    assert "2025" in contenido, "El informe debe identificar el año de análisis"
    with ZipFile(word) as z:
        assert z.testzip() is None
        assert "word/document.xml" in z.namelist()



def test_contrato_de_trazabilidad_f3_f4(metadatos):
    evidencia = json.loads(
        (RAIZ / "evidencias" / "f3_equivalencia_f2.json").read_text(encoding="utf-8")
    )
    assert evidencia["equivalencia_dataframe_exacto"] is True
    assert evidencia["equivalencia_csv"] is True
    assert evidencia["filas"] == metadatos["registros"] == 4731
    assert evidencia["columnas"] == metadatos["columnas_finales"] == 68
    assert evidencia["matricula_primer_anio"] == metadatos["matricula_primer_anio"]
    assert evidencia["matricula_total"] == metadatos["matricula_total"]
    notebook = nbformat.read(NOTEBOOK, as_version=4)
    codigo = "\n".join(c.source for c in notebook.cells if c.cell_type == "code")
    assert "f3_equivalencia_f2.json" in codigo
