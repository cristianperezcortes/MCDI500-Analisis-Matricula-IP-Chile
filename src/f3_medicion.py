"""Comparación de algoritmos equivalentes de concentración de matrícula IP.

Objetivo: demostrar cómo la estructura algorítmica impacta tiempo y memoria.
No utilizar estos tiempos como referencia universal de rendimiento.
"""
from __future__ import annotations
import timeit
import tracemalloc
import pandas as pd
import numpy as np


def agrupar_por_bucle(df: pd.DataFrame, campo: str = 'Nombre Institución') -> pd.Series:
    """Versión A: filtra el DataFrame para cada grupo (O(n*k) + ordenación)."""
    if campo not in df or 'Matrícula Primer Año' not in df:
        raise KeyError(f'Falta {campo} o Matrícula Primer Año')
    if df.empty: raise ValueError('Conjunto sin filas')
    resultado = {}
    for grupo in df[campo].drop_duplicates().tolist():
        mascara = df[campo].eq(grupo)
        resultado[str(grupo)] = int(df.loc[mascara, 'Matrícula Primer Año'].sum())
    return pd.Series(resultado, dtype='int64').sort_index()


def agrupar_vectorizado(df: pd.DataFrame, campo: str = 'Nombre Institución') -> pd.Series:
    """Versión B: recorre una sola vez para agrupar (O(n) esperado + O(k log k))."""
    if campo not in df or 'Matrícula Primer Año' not in df:
        raise KeyError(f'Falta {campo} o Matrícula Primer Año')
    if df.empty: raise ValueError('Conjunto sin filas')
    if df[campo].isna().any():
        raise ValueError('Comparación limitada a grupos no nulos')
    resultado = (df.groupby(campo, observed=True)['Matrícula Primer Año']
                 .sum().astype('int64').rename_axis(None).sort_index())
    # Pandas puede conservar StringDtype del XLSX; normalizar el tipo de
    # las etiquetas antes de probar igualdad estricta con la versión A.
    resultado.index = resultado.index.astype('object')
    return resultado


def comprobar_mismos_resultados(df: pd.DataFrame, campo: str = 'Nombre Institución') -> bool:
    if df[campo].isna().any(): raise ValueError('No se admiten grupos nulos en esta comparación')
    a=agrupar_por_bucle(df,campo)
    b=agrupar_vectorizado(df,campo)
    pd.testing.assert_series_equal(a,b,check_exact=True,check_names=False)
    return True


def _medir_memoria(funcion, datos, campo):
    tracemalloc.start()
    try:
        funcion(datos, campo)
        _, pico = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    return round(pico/(1024**2),4)


def comparar_algoritmos(datos: pd.DataFrame, tamanos=(250, 1000, 4731),
                         repeticiones: int = 3, numero: int = 3) -> pd.DataFrame:
    """Benchmark con timeit y memoria pico (tracemalloc), comparando salidas.

    Se registra el mínimo de tres rondas, cada una de tres repeticiones.
    Los submuestras se toman desde el inicio para reproducibilidad completa.
    """
    if repeticiones < 2 or numero < 1: raise ValueError('Se necesitan al menos dos rondas y una repetición')
    registros=[]
    for n in tamanos:
        if n<1 or n>len(datos): raise ValueError(f'Tamaño inválido: {n}')
        df=datos.iloc[:n].copy()
        comprobar_mismos_resultados(df)
        for etiqueta,fn in [('bucle_por_grupo',agrupar_por_bucle),('pandas_groupby',agrupar_vectorizado)]:
            timer=timeit.Timer(lambda:fn(df,'Nombre Institución'))
            tiempos=timer.repeat(repeat=repeticiones,number=numero)
            registros.append({'filas':int(n),'algoritmo':etiqueta,'rondas':repeticiones,
                              'repeticiones_por_ronda':numero,
                              'tiempo_minimo_ms':round(min(tiempos)/numero*1000,3),
                              'tiempo_mediana_ms':round(float(np.median(tiempos))/numero*1000,3),
                              'memoria_pico_mib':_medir_memoria(fn,df,'Nombre Institución'),
                              'grupos':int(df['Nombre Institución'].nunique()),
                              'equivalencia_validada':True})
    return pd.DataFrame(registros)
