"""Regresiones del Paso 7 de la retroalimentación de Sumativa 1."""
import pandas as pd
import pytest
from src.cned_pipeline import auditar_columnas_originales_completas


def _fuente():
    return pd.DataFrame({
        'matricula': [0, 12, 40],
        'institucion': [' A ', 'B', 'C'],
        'vacantes': [5.0, float('nan'), 60.0],
    })


def test_conserva_campos_completos_y_permite_espacios_textuales():
    origen = _fuente()
    result = origen.copy()
    result['institucion'] = result['institucion'].str.strip()
    result['estimacion'] = [False, True, False]
    audit = auditar_columnas_originales_completas(origen, result)
    assert audit == {'numericas_completas': 1, 'textuales_completas': 1,
                     'columnas_completas_auditadas': 2}


def test_detecta_cambio_ilegitimo_en_cero_observado():
    origen = _fuente()
    cambiado = origen.copy()
    cambiado.loc[0, 'matricula'] = 1
    with pytest.raises(AssertionError, match='numérica completa modificada'):
        auditar_columnas_originales_completas(origen, cambiado)


def test_detecta_modificacion_de_etiqueta_completa():
    origen = _fuente()
    cambiado = origen.copy()
    cambiado.loc[1, 'institucion'] = 'Distinta'
    with pytest.raises(AssertionError, match='textual completa modificada'):
        auditar_columnas_originales_completas(origen, cambiado)


def test_rechaza_eliminar_columna_original_completa():
    origen = _fuente()
    with pytest.raises(AssertionError, match='Columna original completa eliminada'):
        auditar_columnas_originales_completas(origen, origen.drop(columns=['matricula']))


def test_rechaza_perdida_de_filas():
    origen = _fuente()
    with pytest.raises(AssertionError, match='distinta cantidad de filas'):
        auditar_columnas_originales_completas(origen, origen.iloc[:-1].copy())


def test_marcadores_null_no_se_tratan_como_datos_completos():
    origen = _fuente()
    origen['ausente_en_texto'] = ['Null']*len(origen)
    salida = origen.drop(columns=['ausente_en_texto']).copy()
    assert auditar_columnas_originales_completas(origen, salida)['columnas_completas_auditadas'] == 2
