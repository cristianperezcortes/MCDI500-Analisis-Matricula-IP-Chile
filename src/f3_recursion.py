"""Recorrido recursivo de metadatos con profundidad variable (uso auxiliar)."""
from __future__ import annotations

def aplanar_metadatos(arbol: dict, prefijo: str = '') -> dict:
    """Convierte dicts anidados a claves delimitadas por punto.

    Caso base: valor escalar; caso recursivo: diccionario hijo.
    No se fuerza recursividad al cálculo tabular, donde groupby es apropiado.
    """
    if not isinstance(arbol, dict): raise TypeError('Se esperaba un diccionario')
    plano = {}
    for clave,valor in arbol.items():
        ruta = f'{prefijo}.{clave}' if prefijo else str(clave)
        if isinstance(valor, dict):
            plano.update(aplanar_metadatos(valor,ruta))
        else:
            plano[ruta] = valor
    return plano
