"""Orquestación del pipeline F3 y contrato de equivalencia con F2."""
from __future__ import annotations
import pandas as pd
from src.f3_transformaciones import (
    TransformadorCNED, DepuradorEstructura, ImputadorSelectivo, ConstructorVariables,
)
from src.cned_pipeline import preparar_fase2, validar_fase2


class PipelineCNED:
    """Composición polimórfica de transformaciones (no hereda de DataFrame)."""
    def __init__(self, pasos: list[TransformadorCNED] | None = None):
        self._pasos = list(pasos) if pasos is not None else [
            DepuradorEstructura(), ImputadorSelectivo(42), ConstructorVariables()
        ]
        if not self._pasos or any(not isinstance(p, TransformadorCNED) for p in self._pasos):
            raise TypeError('El pipeline necesita una lista de TransformadorCNED')
        self._ajustado = False

    def ajustar(self, datos: pd.DataFrame) -> 'PipelineCNED':
        intermedio = datos.copy()
        for paso in self._pasos:
            intermedio = paso.ajustar(intermedio).transformar(intermedio)
        self._ajustado = True
        return self

    def transformar(self, datos: pd.DataFrame) -> pd.DataFrame:
        if not self._ajustado:
            raise RuntimeError('PipelineCNED: primero debe llamar ajustar()')
        resultado = datos.copy()
        for paso in self._pasos:
            resultado = paso.transformar(resultado)
        return resultado

    def resumen(self) -> pd.DataFrame:
        return pd.DataFrame([{'paso': i+1, 'transformador':p.nombre,
                              'ajustado': p._ajustado,
                              'parametros':', '.join(p.parametros.keys())}
                             for i,p in enumerate(self._pasos)])

    def __len__(self):
        return len(self._pasos)


def comprobar_equivalencia(datos_ip: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Prueba fuerte: mismo DataFrame, columnas, tipos, orden y valores que F2."""
    referencia, auditoria = preparar_fase2(datos_ip)
    propuesto = PipelineCNED().ajustar(datos_ip).transformar(datos_ip)
    pd.testing.assert_frame_equal(referencia, propuesto, check_exact=True)
    validar_fase2(datos_ip, propuesto, auditoria)
    return referencia, propuesto
