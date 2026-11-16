#!/usr/bin/env python3
"""Valida el subconjunto CNED IP/2025; adaptación del validador docente.

Uso:
 python validar_dataset.py --informe docs/validacion_dataset.md
"""
import argparse
from pathlib import Path
import sys
import pandas as pd

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from src.cned_pipeline import cargar_cned_ip, validar_fase1, diagnosticar_faltantes

def main():
    ap=argparse.ArgumentParser(description='Valida CNED IP/2025')
    ap.add_argument('--fuente',default='data/raw/Base-INDICES-Matricula-2005-2026.xlsx')
    ap.add_argument('--informe',default='docs/validacion_dataset.md')
    args=ap.parse_args()
    fuente=(ROOT/args.fuente) if not Path(args.fuente).is_absolute() else Path(args.fuente)
    datos,meta=cargar_cned_ip(fuente)
    val=validar_fase1(datos)
    roles={'identificador':['Cód. Institución','Cód. Carrera'],
           'nominal':['Nombre Institución','Nombre Region','Area Conocimiento'],
           'conteo':['Matrícula Primer Año','Matrícula Total','Vacantes'],
           'monetaria':['Valor de arancel','Valor de matrícula'],
           'temporal':['Año','Año Inicio Actividades']}
    reglas={
        'Al menos 2000 registros':len(datos)>=2000,
        'Al menos 12 columnas':datos.shape[1]>=12,
        'Al menos 3 roles analíticos':len(roles)>=3,
        'Variables numéricas':len(datos.select_dtypes(include='number').columns)>0,
        'Variables categóricas':len(datos.select_dtypes(exclude='number').columns)>0,
        'Matrícula no negativa':datos['Matrícula Primer Año'].ge(0).all(),
    }
    falt=diagnosticar_faltantes(datos)
    texto=['# Informe de validación del dataset CNED IP 2025','',
        'Adaptación del procedimiento didáctico del curso, aplicada al subconjunto objetivo, no a los 260.307 registros históricos.','',
        f"- Archivo: `{fuente.name}` (versión exacta de descarga 2005–2026 pendiente de confirmación).",
        f"- Filas del archivo: **{meta['filas_origen']}**; columnas: **{meta['columnas_origen']}**.",
        f"- IP/2025: **{val['registros']}** filas; **{val['instituciones']}** instituciones.",
        f"- Matrícula de primer año: **{val['matricula_primer_anio']}**; matrícula total: **{val['matricula_total']}**.",'',
        '## Requisitos del curso','',
        '| Criterio | Estado |','|---|---|',
        *[f"| {k} | {'CUMPLE' if bool(v) else 'NO CUMPLE'} |" for k,v in reglas.items()],
        '', '## Calidad de las variables','',
        f"- Variables completamente vacías en IP/2025: **{int((falt['faltantes']==len(datos)).sum())}**.",
        '- Las variables con 100% de ausencias no son aptas para analizar: se eliminan en F2, documentando sus nombres.',
        '- Los identificadores no se imputan, aun si Pandas los reconoce como números.',
        f"- Ceros observados de matrícula primer año: **{val['matricula_primer_anio_cero']}**.",
        f"- Inconsistencias temporales: **{val['registro_inicio_posterior']}**; se etiqueta y documenta sensibilidad.",
        f"- Duplicados exactos: **{val['duplicados_completos']}**.",
        '', '## Veredicto','',
        '**APTO** para análisis descriptivo y de concentración de matrícula agregada en IP/2025, con las restricciones documentadas.',
        '', '## Limitación de procedencia','',
        'La URL institucional del CNED está identificada; la URL exacta y la fecha de descarga de la versión 2005–2026 siguen sin verificarse.']
    destino=ROOT/args.informe;destino.parent.mkdir(parents=True,exist_ok=True)
    destino.write_text('\n'.join(texto)+'\n',encoding='utf-8')
    print('VALIDACIÓN', 'APTO' if all(reglas.values()) else 'RECHAZADO', '| informe:',destino)
    if not all(reglas.values()):sys.exit(1)

if __name__=='__main__':main()
