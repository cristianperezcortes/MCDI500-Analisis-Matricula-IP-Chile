#!/usr/bin/env python3
"""Auditoría local reproducible de F1, F2, el CSV y sus invariantes."""
from pathlib import Path
import sys,json
import pandas as pd
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.cned_pipeline import validar_fase1, validar_fase2, preparar_fase2, cargar_cned_ip

def verificar():
    src=ROOT/'data/raw/Base-INDICES-Matricula-2005-2026.xlsx'
    if not src.is_file():
        src=ROOT/'data/fixtures/ip_2025_origen_filtrado.csv'
    extra=ROOT/'data/interim/ip_2025_origen_filtrado.csv'
    output=ROOT/'data/processed/matricula_ip_2025_procesada_v3.csv'
    for p in (src,extra,output,ROOT/'requirements.txt'):
        if not p.is_file():raise FileNotFoundError(p)
    fuente, procedencia = cargar_cned_ip(src)
    x=pd.read_csv(extra,encoding='utf-8-sig',low_memory=False)
    assert x.shape == fuente.shape == (4731,62)
    assert (x['Matrícula Primer Año'].sum(),x['Matrícula Total'].sum()) == (137481,439607)
    y=pd.read_csv(output,encoding='utf-8-sig',low_memory=False)
    fase1=validar_fase1(x)
    generado,auditoria=preparar_fase2(x)
    fase2=validar_fase2(x,generado,auditoria)
    assert y.shape==generado.shape
    assert int(y['Matrícula Primer Año'].sum())==137481
    assert int(y['Matrícula Total'].sum())==439607
    assert (y[['nivel_pregrado_onehot','nivel_posgrado_onehot']].sum(axis=1)==1).all()
    assert y['categoria_matricula_total_codigo'].between(1,4).all()
    assert y['matricula_primer_anio_escala_0_1'].between(0,1).all()
    assert np.allclose(y['matricula_primer_anio_log1p'],np.log1p(y['Matrícula Primer Año']))
    assert fase2['filas_sin_perdidas']==4731
    assert fase1['duplicados_completos']==0
    import nbformat
    nbinfo={}
    for fase,nombre in [('F1','F1_Definicion_Cned.ipynb'),('F2','F2_Preprocesamiento_Cned.ipynb')]:
        nb=nbformat.read(ROOT/fase/nombre,as_version=4)
        cc=[c for c in nb.cells if c.cell_type=='code']
        nbinfo[fase]={"celdas":len(nb.cells),"codigo":len(cc),"ejecutadas":sum(c.execution_count is not None for c in cc),
                       "errores":sum(o.output_type=='error' for c in cc for o in c.outputs),
                       "secuencia": [c.execution_count for c in cc],
                       "vacias":sum(not ''.join(c.source).strip() for c in nb.cells)}
        assert nbinfo[fase]['ejecutadas']==len(cc)
        assert nbinfo[fase]['secuencia']==list(range(1,len(cc)+1))
        assert nbinfo[fase]['errores']==0 and nbinfo[fase]['vacias']==0
    reporte={"estado":"APROBADO", "F1":fase1,"F2":fase2, "notebooks":nbinfo,
             "fuente_utilizada":str(src.relative_to(ROOT)),"sha256_ejecutada":procedencia["sha256"],
             "salida":output.relative_to(ROOT).as_posix(),
             "pendientes_externos":["evidencia formal de aprobación administrativa del grupo de 2 integrantes",
              "plantilla institucional original","fecha y URL directa de descarga del XLSX 2005-2026","entrega Canvas"]}
    dest=ROOT/'evidencias/auditoria_guia_sumativa1.json'
    dest.write_text(json.dumps(reporte,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps(reporte,indent=2,ensure_ascii=False))
    return reporte
if __name__=='__main__': verificar()
