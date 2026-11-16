"""Contratos adicionales solicitados por la guía docente de la Sumativa 1."""
import numpy as np
import pandas as pd
import pytest
from src.cned_pipeline import (diagnosticar_atipicos, comparar_imputaciones, imputar_variable,
                                preparar_fase2, validar_fase2, validar_fase1)


def _datos_apoyo():
    n=80
    return pd.DataFrame({
      'Vacantes':[10.]*35+[np.nan]*5+[100.]*35+[np.nan]*5,
      'moneda_normalizada':['CLP']*80,
      'Area Conocimiento':['Salud']*40+['Tecnología']*40,
      'Nombre Institución':['IP A']*40+['IP B']*40})

def test_compara_cuatro_alternativas_y_cuenta_perdida():
    d=_datos_apoyo()
    c=comparar_imputaciones(d,'Vacantes',semilla=42)
    assert c['filas_perdidas_si_elimina']==10
    assert all(np.isfinite(c[k]) for k in ('mae_media','mae_global','mae_jerarquica'))
    assert c['metodo_seleccionado'] in ('media','global','jerarquica')

def test_permite_imputacion_media_sin_modificar_observados():
    d=_datos_apoyo()
    salida=imputar_variable(d,'Vacantes','vacantes','media')
    assert int(salida['vacantes_imputado'].sum())==10
    assert salida.loc[d['Vacantes'].notna(),'vacantes_analisis'].equals(d.loc[d['Vacantes'].notna(),'Vacantes'].rename('vacantes_analisis'))

def test_rechaza_parametros_iqr_invalidos():
    with pytest.raises(ValueError,match='positivo'):
        diagnosticar_atipicos(pd.DataFrame({'A':[1,2,3]}),['A'],factor=-1)

def test_atipicos_en_columna_constante():
    tab=diagnosticar_atipicos(pd.DataFrame({'mat':[5,5,5,5]}),['mat'])
    assert int(tab.iloc[0]['atipicos'])==0

def test_rechaza_categoria_monetaria_desconocida_en_comparacion():
    d=_datos_apoyo()
    d['Vacantes']=[np.nan]*80
    with pytest.raises(ValueError,match='insuficientes'):
        comparar_imputaciones(d,'Vacantes')
