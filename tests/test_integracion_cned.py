"""Validación de integración con el Excel original, si está disponible."""
from pathlib import Path
import pytest
from src.cned_pipeline import cargar_cned_ip, validar_fase1, preparar_fase2, validar_fase2

RAW=Path(__file__).resolve().parents[1]/'data/raw/Base-INDICES-Matricula-2005-2026.xlsx'

@pytest.mark.skipif(not RAW.exists(),reason='Requiere el archivo fuente descargado')
def test_base_real_completa():
    original,meta=cargar_cned_ip(RAW)
    assert (meta['filas_origen'],meta['columnas_origen'])==(260307,62)
    assert (len(original), original.shape[1])==(4731,62)
    v=validar_fase1(original)
    assert v['matricula_primer_anio']==137481
    assert v['matricula_total']==439607
    assert v['instituciones']==27
    assert v['registro_inicio_posterior']==1
    limpio,a=preparar_fase2(original)
    assert len(a['columnas_vacias'])==13
    assert set(a['columnas_excluidas_por_umbral'])=={'Grado Académico','Mención o Especialidad'}
    assert limpio['categoria_matricula_total'].notna().all()
    assert validar_fase2(original,limpio,a)['filas_sin_perdidas']==4731
