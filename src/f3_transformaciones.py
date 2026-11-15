"""Fase 3 del proyecto CNED: transformaciones por etapas orientadas a objetos.

Se reutilizan las funciones verificadas de F2, sin inventar un procesamiento nuevo.
Esta versión reproduce el MISMO conjunto descriptivo. No es un estimador
predictivo para datos futuros; en tal caso los parámetros deberán entrenarse
exclusivamente sobre el conjunto de entrenamiento.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np
import pandas as pd

from src.cned_pipeline import (
    VARIABLES_IMPUTABLES, depurar_estructura, comparar_imputaciones,
    imputar_variable, crear_categorias_matricula,
)


class TransformadorCNED(ABC):
    """Contrato y ciclo de vida comunes (patrón Template Method).

    Las subclases implementan el aprendizaje y la aplicación de su tarea.
    El estado ``_ajustado`` evita operaciones fuera de orden y las copias
    protegen la entrada de cambios accidentales.
    """
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._ajustado = False
        self._parametros: dict = {}

    def ajustar(self, datos: pd.DataFrame) -> 'TransformadorCNED':
        self._validar_entrada(datos)
        self._parametros = self._aprender(datos.copy())
        self._ajustado = True
        return self

    def transformar(self, datos: pd.DataFrame) -> pd.DataFrame:
        if not self._ajustado:
            raise RuntimeError(f'{self.nombre}: debe ejecutar ajustar() primero')
        self._validar_entrada(datos)
        resultado = self._aplicar(datos.copy())
        if not isinstance(resultado, pd.DataFrame):
            raise TypeError(f'{self.nombre}: se esperaba DataFrame de salida')
        if len(resultado) != len(datos):
            raise AssertionError(f'{self.nombre}: se modificó el número de filas')
        return resultado

    @property
    def parametros(self) -> dict:
        """Copia de la información aprendida: protege el estado interno."""
        import copy
        return copy.deepcopy(self._parametros)

    @staticmethod
    def _validar_entrada(datos):
        if not isinstance(datos, pd.DataFrame):
            raise TypeError('Se requiere un DataFrame de pandas')
        if datos.empty:
            raise ValueError('La tabla de entrada está vacía')

    @abstractmethod
    def _aprender(self, datos: pd.DataFrame) -> dict:
        raise NotImplementedError

    @abstractmethod
    def _aplicar(self, datos: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError


class DepuradorEstructura(TransformadorCNED):
    """Normaliza marcadores NA y aplica las reglas documentadas de F2."""
    def __init__(self, umbral: float = 0.90):
        super().__init__('DepuradorEstructura')
        self.umbral = umbral

    def _aprender(self, datos):
        _, audit = depurar_estructura(datos, umbral_faltantes=self.umbral)
        return {'columnas_vacias': list(audit['columnas_vacias']),
                'columnas_excluidas_por_umbral': list(audit['columnas_excluidas_por_umbral'])}

    def _aplicar(self, datos):
        depurado, audit = depurar_estructura(datos, umbral_faltantes=self.umbral)
        if sorted(audit['columnas_vacias']) != sorted(self._parametros['columnas_vacias']):
            raise ValueError('El conjunto posee otra estructura de columnas vacías; revise el origen')
        if sorted(audit['columnas_excluidas_por_umbral']) != sorted(self._parametros['columnas_excluidas_por_umbral']):
            raise ValueError('La proporción de faltantes cambió respecto de la base de referencia')
        return depurado


class ImputadorSelectivo(TransformadorCNED):
    """Estima únicamente COPIAS analíticas de valores monetarios CLP y vacantes.

    El conjunto descriptivo F2 utiliza toda la población IP 2025. Las estrategias
    se eligen con el procedimiento de enmascaramiento de F2 (semilla 42).
    No se presenta este algoritmo como inferencia fuera de muestra.
    """
    def __init__(self, semilla: int = 42):
        super().__init__('ImputadorSelectivo')
        self.semilla = semilla

    def _aprender(self, datos):
        return {campo: comparar_imputaciones(datos, campo, self.semilla)
                for campo in VARIABLES_IMPUTABLES}

    def _aplicar(self, datos):
        resultado = datos.copy()
        for variable, alias in VARIABLES_IMPUTABLES.items():
            estrategia = self._parametros[variable]['metodo_seleccionado']
            resultado = imputar_variable(resultado, variable, alias, estrategia)
        return resultado


class ConstructorVariables(TransformadorCNED):
    """Construye categorías, one-hot, escalamiento y banderas sin alterar CNED."""
    def __init__(self):
        super().__init__('ConstructorVariables')

    def _aprender(self, datos):
        requeridas = ['Matrícula Total', 'Matrícula Primer Año', 'Pregrado/Posgrado', 'Año Inicio Actividades']
        faltantes = [x for x in requeridas if x not in datos.columns]
        if faltantes:
            raise KeyError(f'Columnas requeridas no disponibles: {faltantes}')
        return {'variables_requeridas': requeridas,
                'maximo_matricula_primer_anio': float(pd.to_numeric(datos['Matrícula Primer Año'], errors='coerce').max())}

    def _aplicar(self, datos):
        df = datos.copy()
        df['categoria_matricula_total'] = crear_categorias_matricula(df)
        categorias = df['categoria_matricula_total'].cat.categories.tolist()
        orden = {c: i + 1 for i, c in enumerate(categorias)}
        df['categoria_matricula_total_codigo'] = df['categoria_matricula_total'].map(orden).astype('int64')
        nivel = df['Pregrado/Posgrado'].astype('string')
        if not nivel.isin(['Pregrado', 'Posgrado']).all():
            raise ValueError('Nivel académico desconocido')
        df['nivel_pregrado_onehot'] = nivel.eq('Pregrado').astype('int8')
        df['nivel_posgrado_onehot'] = nivel.eq('Posgrado').astype('int8')
        matricula = pd.to_numeric(df['Matrícula Primer Año'], errors='coerce')
        if matricula.isna().any() or matricula.lt(0).any():
            raise ValueError('Matrícula de primer año inválida')
        # El máximo se aprendió al ajustar; no se recalcula al transformar.
        maximo = self._parametros['maximo_matricula_primer_anio']
        df['matricula_primer_anio_escala_0_1'] = matricula / maximo if maximo > 0 else 0.0
        df['matricula_primer_anio_log1p'] = np.log1p(matricula)
        df['inicio_posterior_a_2025'] = pd.to_numeric(df['Año Inicio Actividades'], errors='coerce') > 2025
        df['matricula_primer_anio_cero'] = df['Matrícula Primer Año'].eq(0)
        return df
