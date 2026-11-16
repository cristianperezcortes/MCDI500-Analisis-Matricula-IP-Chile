#!/usr/bin/env python3
"""Repite F1-F2-F3 en una copia temporal sin modificar informes ni benchmarks."""
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
import nbformat
ROOT=Path(__file__).resolve().parents[1]
EXCEL=ROOT/"data/raw/Base-INDICES-Matricula-2005-2026.xlsx"
NOTEBOOKS=("F1/F1_Definicion_Cned.ipynb","F2/F2_Preprocesamiento_Cned.ipynb","F3/S2_F3_NucleoAlgoritmico_Cned.ipynb")
def reproducir(ejecutar=False,timeout=1500):
    from verificar_entorno import verificar
    verificar(exigir_excel=True)
    result={"modo":"preflight","fases":[],"original_sha_comprobado":True}
    if not ejecutar:
        print("PRECHECK APROBADO. Use --ejecutar para repetir F1-F3.")
        return result
    with tempfile.TemporaryDirectory(prefix="mcdi500_reproduccion_") as temporal:
        destino=Path(temporal)
        for name in ("F1","F2","F3","src","scripts","docs","evidencias","tests"):
            shutil.copytree(ROOT/name,destino/name,ignore=shutil.ignore_patterns("__pycache__","*.pyc",".ipynb_checkpoints"))
        for name in ("requirements.txt","pytest.ini","validar_dataset.py"):
            shutil.copy2(ROOT/name,destino/name)
        raw=destino/"data/raw";raw.mkdir(parents=True)
        shutil.copy2(EXCEL,raw/EXCEL.name)
        if (ROOT/"data/raw/README.md").is_file():
            shutil.copy2(ROOT/"data/raw/README.md",raw/"README.md")
        for d in ("data/interim","data/processed","evidencias/reproduccion_limpia"):
            (destino/d).mkdir(parents=True,exist_ok=True)
        outputs=destino/"evidencias/reproduccion_limpia"
        for i,name in enumerate(NOTEBOOKS,1):
            cmd=[sys.executable,"-m","jupyter","nbconvert","--to","notebook","--execute",str(destino/name),"--ExecutePreprocessor.timeout="+str(timeout),"--output",f"fase_{i}_ejecutada.ipynb","--output-dir",str(outputs)]
            p=subprocess.run(cmd,cwd=destino,capture_output=True,text=True)
            if p.returncode:raise RuntimeError(f"Fase {i} falló: {(p.stderr or p.stdout)[-4000:]}")
            nb=nbformat.read(outputs/f"fase_{i}_ejecutada.ipynb",as_version=4)
            code=[c for c in nb.cells if c.cell_type=="code"]
            errors=[x for c in code for x in c.outputs if x.output_type=="error"]
            if errors:raise RuntimeError(f"Fase {i}: {errors[0].get('evalue')}")
            result["fases"].append({"fase":i,"codigo":len(code),"errores":0})
        import pandas as pd
        f2=pd.read_csv(destino/"data/processed/matricula_ip_2025_procesada_v3.csv",encoding="utf-8-sig",low_memory=False)
        f3=pd.read_csv(destino/"data/processed/matricula_ip_2025_procesada_f3.csv",encoding="utf-8-sig",low_memory=False)
        if f2.shape!=f3.shape or f2.shape!=(4731,68):raise AssertionError("Dimensiones F2/F3 incorrectas")
        if int(f2["Matrícula Primer Año"].sum())!=137481 or int(f2["Matrícula Total"].sum())!=439607:
            raise AssertionError("Totales alterados")
        result.update({"modo":"ejecucion_completa_en_copia_temporal","dimensiones":list(f2.shape),"primer_anio":137481,"total":439607})
    (ROOT/"evidencias/reproduccion_limpia_resultado.json").write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return result
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--ejecutar",action="store_true");p.add_argument("--timeout",type=int,default=1500)
    args=p.parse_args();reproducir(args.ejecutar,args.timeout)
