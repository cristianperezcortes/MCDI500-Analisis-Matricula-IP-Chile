"""Casos normales, límite y excepciones para F3 (Sumativa 2)."""
import pandas as pd
import pytest

from src.f3_transformaciones import (
    TransformadorCNED, DepuradorEstructura, ImputadorSelectivo, ConstructorVariables
)
from src.f3_pipeline import PipelineCNED
from src.f3_medicion import (
    agrupar_por_bucle, agrupar_vectorizado, comprobar_mismos_resultados,
    comparar_algoritmos,
)
from src.f3_recursion import aplanar_metadatos


def ejemplo():
    return pd.DataFrame({
        'Nombre Institución': ['IP A', 'IP A', 'IP B', 'IP B'],
        'Matrícula Primer Año': [3, 5, 0, 6],
        'Matrícula Total': [12, 20, 1, 8],
    })


def test_herencia_documentada():
    assert issubclass(DepuradorEstructura, TransformadorCNED)
    assert issubclass(ImputadorSelectivo, TransformadorCNED)
    assert issubclass(ConstructorVariables, TransformadorCNED)


def test_polimorfismo_interface_uniforme():
    for cls in (DepuradorEstructura, ImputadorSelectivo, ConstructorVariables):
        obj=cls()
        assert callable(obj.ajustar) and callable(obj.transformar)


def test_encapsulamiento_antes_de_ajuste():
    with pytest.raises(RuntimeError, match='ajustar'):
        PipelineCNED().transformar(ejemplo())
    with pytest.raises(RuntimeError, match='ajustar'):
        DepuradorEstructura().transformar(ejemplo())


def test_entrada_con_tipo_equivocado():
    with pytest.raises(TypeError,match='DataFrame'):
        DepuradorEstructura().ajustar({'x': 1})


def test_entrada_vacia():
    with pytest.raises(ValueError,match='vacía'):
        DepuradorEstructura().ajustar(pd.DataFrame())


def test_pipeline_sin_pasos_validos():
    with pytest.raises(TypeError):
        PipelineCNED([])
    with pytest.raises(TypeError):
        PipelineCNED([object()])


def test_agrupacion_equivalente_normal():
    df=ejemplo()
    assert comprobar_mismos_resultados(df)
    assert int(agrupar_vectorizado(df).sum())==14
    assert int(agrupar_por_bucle(df)['IP A'])==8


def test_agrupacion_con_una_categoria():
    df=ejemplo().iloc[:2]
    assert comprobar_mismos_resultados(df)
    assert len(agrupar_vectorizado(df))==1


def test_agrupacion_sin_columna():
    with pytest.raises(KeyError):
        agrupar_vectorizado(ejemplo().drop(columns=['Nombre Institución']))


def test_agrupacion_sin_filas():
    with pytest.raises(ValueError):
        agrupar_por_bucle(ejemplo().iloc[0:0])


def test_agrupacion_con_nulos():
    df=ejemplo()
    df.loc[0,'Nombre Institución']=None
    with pytest.raises(ValueError,match='nulos'):
        comprobar_mismos_resultados(df)


def test_prueba_de_benchmark_micro():
    df=ejemplo()
    tabla=comparar_algoritmos(df,tamanos=[2,4],repeticiones=2,numero=1)
    assert len(tabla)==4
    assert tabla['equivalencia_validada'].all()
    assert tabla['tiempo_minimo_ms'].ge(0).all()
    assert tabla['memoria_pico_mib'].ge(0).all()


def test_rechazo_benchmark_tamano_imposible():
    with pytest.raises(ValueError):
        comparar_algoritmos(ejemplo(),tamanos=[9999])


def test_recursividad_con_diccionarios_anidados():
    assert aplanar_metadatos({'f1':{'fuente':{'tipo':'CNED'},'año':2025}})=={
        'f1.fuente.tipo':'CNED','f1.año':2025
    }


def test_recursividad_dict_vacio_y_error():
    assert aplanar_metadatos({})=={}
    with pytest.raises(TypeError):
        aplanar_metadatos([])
