"""Prueba real del subconjunto CNED publicado y, si existe, del Excel original.

La CI debe ejecutar esta prueba; no se permite omitirla cuando está la fuente
versionada. El Excel sigue siendo fuente preferente cuando está disponible.
"""
from pathlib import Path
import pytest
from src.cned_pipeline import (
    cargar_cned_ip, validar_fase1, preparar_fase2, validar_fase2,
    sha256_archivo, CSV_IP_2025_SHA256, XLSX_ORIGEN_SHA256,
)

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data/raw/Base-INDICES-Matricula-2005-2026.xlsx'
CSV = ROOT / 'data/fixtures/ip_2025_origen_filtrado.csv'


def test_base_real_completa():
    assert RAW.is_file() or CSV.is_file(), "Falta tanto el Excel original como el CSV versionado"
    fuente = RAW if RAW.is_file() else CSV
    if fuente.suffix.lower() == ".csv":
        assert sha256_archivo(fuente) == CSV_IP_2025_SHA256
    else:
        assert sha256_archivo(fuente) == XLSX_ORIGEN_SHA256
    original, meta = cargar_cned_ip(fuente)
    assert meta['columnas_origen'] == 62
    assert meta['filas_origen'] == (260307 if fuente.suffix == ".xlsx" else 4731)
    assert (len(original), original.shape[1]) == (4731, 62)
    v = validar_fase1(original)
    assert v['matricula_primer_anio'] == 137481
    assert v['matricula_total'] == 439607
    assert v['instituciones'] == 27
    assert v['registro_inicio_posterior'] == 1
    assert v['matricula_primer_anio_cero'] == 1576
    limpio, a = preparar_fase2(original)
    assert limpio.shape == (4731,68)
    assert len(a['columnas_vacias']) == 13
    assert set(a['columnas_excluidas_por_umbral']) == {'Grado Académico','Mención o Especialidad'}
    assert limpio['categoria_matricula_total'].notna().all()
    assert validar_fase2(original, limpio, a)['filas_sin_perdidas'] == 4731


def test_csv_publicado_rechaza_huella_alterada(tmp_path):
    assert CSV.is_file(), "El CSV es indispensable para el clon limpio"
    alterado = tmp_path / "ip_2025_modificado.csv"
    alterado.write_bytes(CSV.read_bytes() + b"\n")
    with pytest.raises(ValueError,match="SHA-256"):
        cargar_cned_ip(alterado)
