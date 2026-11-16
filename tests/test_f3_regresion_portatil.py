"""Pruebas de integración autónomas de F2/F3, sin dependencia del Excel CNED.

Este conjunto es SINTÉTICO. No reemplaza los controles con datos reales ni
sustituye el archivo original, que nunca se publica en el repositorio.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from src.cned_pipeline import preparar_fase2, validar_fase2
from src.f3_pipeline import PipelineCNED
from src.f3_transformaciones import ConstructorVariables, DepuradorEstructura


def _datos_sinteticos(n: int = 120) -> pd.DataFrame:
    """Crea un ejemplo CNED ficticio con faltantes CLP, UF y ceros válidos."""
    indices = np.arange(n)
    def _numerico(base: float, paso: float, divisor_faltante: int) -> list[float]:
        valores = [base + paso * (int(i) % 9) for i in indices]
        return [np.nan if i % divisor_faltante == 0 else v for i, v in enumerate(valores)]

    return pd.DataFrame({
        'Año': [2025] * n,
        'Nombre Institución': [f'IP Ficticio {i % 3}' for i in indices],
        'Tipo Institución': ['I.P.'] * n,
        'Nombre Programa': [f'Programa Ficticio {i % 7}' for i in indices],
        'Nombre de la Sede': [f'Sede {i % 3}' for i in indices],
        'Nombre Region': ['Metropolitana' if i % 2 else 'Valparaíso' for i in indices],
        'Area Conocimiento': ['Tecnología' if i % 2 else 'Salud' for i in indices],
        'Pregrado/Posgrado': ['Pregrado' if i % 10 else 'Posgrado' for i in indices],
        'Año Inicio Actividades': [2026 if i == n-1 else 2015 for i in indices],
        'Tipo Moneda': ['UF' if i % 13 == 0 else 'PESOS' for i in indices],
        'Matrícula Primer Año': [0 if i % 11 == 0 else (i % 51) + 1 for i in indices],
        'Matrícula Total': [(i % 41) + 3 for i in indices],
        'Valor de arancel': _numerico(700000, 12000, 17),
        'Valor de matrícula': _numerico(40000, 3000, 19),
        'Valor del Título': _numerico(95000, 5000, 23),
        'Vacantes': _numerico(45, 3, 29),
        'Columna Sin Información': ['Null'] * n,
    })


def test_pipeline_poo_igualdad_exacta_con_datos_sinteticos():
    """Ejecuta el ciclo F2->F3 en CI; verifica tipos, columnas y valores."""
    origen = _datos_sinteticos()
    copia = origen.copy(deep=True)
    anterior, auditoria = preparar_fase2(origen)
    resultado = PipelineCNED().ajustar(origen).transformar(origen)
    pd.testing.assert_frame_equal(anterior, resultado, check_exact=True)
    pd.testing.assert_frame_equal(origen, copia, check_exact=True)
    assert validar_fase2(origen, resultado, auditoria)['filas_sin_perdidas'] == len(origen)
    assert int(resultado['matricula_primer_anio_cero'].sum()) == int(origen['Matrícula Primer Año'].eq(0).sum())
    assert resultado['nivel_pregrado_onehot'].add(resultado['nivel_posgrado_onehot']).eq(1).all()
    # No se imputan los montos de filas UF donde el original está ausente.
    uf_sin_arancel = (resultado['moneda_normalizada'].eq('UF') & origen['Valor de arancel'].isna())
    assert resultado.loc[uf_sin_arancel, 'arancel_analisis'].isna().all()


def test_parametros_encapsulados_no_cambian_desde_fuera():
    x = _datos_sinteticos()
    transformador = DepuradorEstructura().ajustar(x)
    estado = transformador.parametros
    estado['columnas_vacias'].append('Nombre Institución')
    assert 'Nombre Institución' not in transformador.parametros['columnas_vacias']


def test_rechazo_de_nivel_academico_fuera_del_catalogo():
    x = _datos_sinteticos()
    x.loc[0, 'Pregrado/Posgrado'] = 'Nivel inventado'
    con_estructura = DepuradorEstructura().ajustar(x).transformar(x)
    constructor = ConstructorVariables().ajustar(con_estructura)
    with pytest.raises(ValueError, match='Nivel académico desconocido'):
        constructor.transformar(con_estructura)


def test_rechazo_de_matricula_negativa_en_constructor():
    x = _datos_sinteticos()
    x.loc[4, 'Matrícula Primer Año'] = -3
    con_estructura = DepuradorEstructura().ajustar(x).transformar(x)
    constructor = ConstructorVariables().ajustar(con_estructura)
    with pytest.raises(ValueError, match='Matrícula de primer año inválida'):
        constructor.transformar(con_estructura)
