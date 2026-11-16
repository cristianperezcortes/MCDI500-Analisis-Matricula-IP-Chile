"""Pruebas sintéticas de funciones, límites y semántica del dato."""
import numpy as np
import pandas as pd
import pytest

from src.cned_pipeline import (
    CAMPOS_IDENTIDAD,
    _columna_indice,
    comparar_imputaciones,
    concentracion_matricula,
    crear_categorias_matricula,
    depurar_estructura,
    filtrar_ip_2025,
    imputar_variable,
    normalizar_valores_nulos,
    promedio_matricula,
    validar_fase1,
)


def test_columnas_excel():
    assert [_columna_indice(x) for x in ["A1", "D4", "Z20", "AA100", "BJ5"]] == [0,3,25,26,61]


def test_filtrar_ip_fecha():
    df = pd.DataFrame({"Tipo Institución": ["I.P.", "C.F.T.", "I.P."], "Año": [2025,2025,2024]})
    out = filtrar_ip_2025(df)
    assert len(out) == 1 and out.iloc[0]["Año"] == 2025


def test_filtro_rechaza_esquema_erroneo():
    with pytest.raises(ValueError, match="faltantes"):
        filtrar_ip_2025(pd.DataFrame({"Año": [2025]}))


def test_normalizacion_placeholders_sin_modificar_ceros():
    x = pd.DataFrame({'texto':['Null','NULL',' No informado ', '',None], 'valor':[0,1,2,3,4]})
    y = normalizar_valores_nulos(x)
    assert y['texto'].isna().sum()==4
    assert y['valor'].tolist()==[0,1,2,3,4]
    assert y.loc[2,'texto']=='No informado'


def test_columnas_excluidas_por_regla_y_preserva_identificadores():
    x=pd.DataFrame({'A':['Null']*95 + ['valido']*5,'B':[None]*100,'C':[1]*100})
    y,a=depurar_estructura(x)
    assert y.shape==(100,1)
    assert a['columnas_vacias']==['B']
    assert a['columnas_excluidas_por_umbral']==['A']


def test_promedio_normal_y_missing():
    assert promedio_matricula(pd.DataFrame({'Matrícula Total':[10,20,30]}))==20
    assert promedio_matricula(pd.DataFrame({'Matrícula Total':[0,10]}))==5


@pytest.mark.parametrize('x,mensaje',[
    (pd.DataFrame({'Matrícula Total':[]}), 'vacía'),
    (pd.DataFrame({'Matrícula Total':[None,None]}), 'ausentes'),
    (pd.DataFrame({'Matrícula Total':[-1,2]}), 'negativas'),
])
def test_promedio_excepciones(x,mensaje):
    with pytest.raises(ValueError,match=mensaje):promedio_matricula(x)


def test_crear_categorias_cuartiles():
    x=pd.DataFrame({'Matrícula Total':list(range(1,101))})
    c=crear_categorias_matricula(x)
    assert c.notna().all() and len(c.cat.categories)==4
    assert list(c.cat.categories)==['Baja','Media','Alta','Muy alta']


def test_crear_categorias_empatadas():
    x=pd.DataFrame({'Matrícula Total':[0]*25+[1]*25+[2]*25+[3]*25})
    c=crear_categorias_matricula(x)
    assert c.notna().all()


def test_categorias_todos_iguales():
    x=pd.DataFrame({'Matrícula Total':[5]*10})
    c=crear_categorias_matricula(x)
    assert (c.astype(str)=='Sin variación').all()


def test_categorias_insuficientes():
    with pytest.raises(ValueError):crear_categorias_matricula(pd.DataFrame({'Matrícula Total':[1,2,3]}))


def test_arancel_uf_no_se_imputa_con_pesos():
    n=40
    df=pd.DataFrame({
       'Valor de arancel':[100000.0]*15+[200000.0]*15+[np.nan]*5+[np.nan]*5,
       'moneda_normalizada':['CLP']*35+['UF']*5,
       'Area Conocimiento':['Salud']*n,
       'Nombre Institución':['IP A']*n,
    })
    fin=imputar_variable(df,'Valor de arancel','arancel','jerarquica')
    assert fin.loc[30:34,'arancel_imputado'].all()
    assert fin.loc[35:39,'arancel_analisis'].isna().all()
    assert fin.loc[35:39,'arancel_imputado'].eq(False).all()
    assert fin.loc[0,'arancel_analisis']==100000


def test_imputacion_global_frente_a_grupo_escogible():
    df=pd.DataFrame({
       'Vacantes':[10.]*40+[100.]*40,
       'moneda_normalizada':['CLP']*80,
       'Area Conocimiento':['Salud']*40+['Tecnología']*40,
       'Nombre Institución':['IP A']*40+['IP B']*40,
    })
    c=comparar_imputaciones(df,'Vacantes')
    assert c['mae_jerarquica'] <= c['mae_global']
    assert c['metodo_seleccionado']=='jerarquica'


def test_concentracion_normal():
    x=pd.DataFrame({'Nombre Institución':['A','A','B','C'],'Matrícula Primer Año':[20,10,5,5]})
    tabla,s=concentracion_matricula(x)
    assert s['total_matricula_primer_anio']==40
    assert s['cr3_pct']==100.0
    assert 0 < s['hhi'] < 10000


def test_concentracion_vacia_y_negativos():
    x=pd.DataFrame({'Nombre Institución':['A','B'],'Matrícula Primer Año':[0,0]})
    with pytest.raises(ValueError,match='positiva'):concentracion_matricula(x)
    x.loc[0,'Matrícula Primer Año']=-1
    with pytest.raises(ValueError,match='negativos'):concentracion_matricula(x)
