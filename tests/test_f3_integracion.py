"""Prueba de regresión real: los objetos reproducen el resultado de F2 sin diferencias."""
from pathlib import Path
import pandas as pd
import pytest

from src.f3_pipeline import PipelineCNED, comprobar_equivalencia
from src.cned_pipeline import validar_fase2, preparar_fase2

ROOT=Path(__file__).resolve().parents[1]
FILE=ROOT/'data/interim/ip_2025_origen_filtrado.csv'


@pytest.mark.skipif(not FILE.exists(),reason='Primero ejecutar F2 para generar el extracto')
def test_equivalencia_exhaustiva_f2_f3():
    origen=pd.read_csv(FILE,encoding='utf-8-sig',low_memory=False)
    antes=origen.copy(deep=True)
    legacy, po= comprobar_equivalencia(origen)
    assert legacy.shape==po.shape==(4731,68)
    assert int(po['Matrícula Primer Año'].sum())==137481
    assert int(po['Matrícula Total'].sum())==439607
    pd.testing.assert_frame_equal(origen,antes)


@pytest.mark.skipif(not FILE.exists(),reason='Primero ejecutar F2 para generar el extracto')
def test_proteccion_de_columnas_y_ceros():
    origen=pd.read_csv(FILE,encoding='utf-8-sig',low_memory=False)
    final=PipelineCNED().ajustar(origen).transformar(origen)
    assert final['matricula_primer_anio_cero'].sum()==1576
    assert final['nivel_pregrado_onehot'].sum()==4714
    assert final['nivel_posgrado_onehot'].sum()==17
    assert (final['Matrícula Primer Año']==origen['Matrícula Primer Año']).all()
    assert (final['Matrícula Total']==origen['Matrícula Total']).all()
    assert (final['nivel_pregrado_onehot']+final['nivel_posgrado_onehot']==1).all()
