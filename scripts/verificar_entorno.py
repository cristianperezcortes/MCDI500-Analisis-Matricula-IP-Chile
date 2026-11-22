#!/usr/bin/env python3
"""Verifica versiones fijadas y, opcionalmente, SHA-256 del Excel CNED."""
import argparse
import hashlib
import json
import sys
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def verificar(exigir_excel=False, exigir_fuente=False):
    req={}
    for line in (ROOT/"requirements.txt").read_text(encoding="utf-8").splitlines():
        line=line.strip()
        if not line or line.startswith("#"):continue
        if line.count("==") != 1:raise ValueError("Dependencia sin versión exacta: "+line)
        n,v=line.split("==",1);req[n]=v
    errores=[]
    if sys.version_info[:2]!=(3,13):errores.append("Requiere Python 3.13")
    if "notebook" not in req:errores.append("Falta Jupyter Notebook fijado")
    for n,esperado in req.items():
        try:actual=version(n)
        except PackageNotFoundError:actual="NO INSTALADO"
        if actual!=esperado:errores.append(f"{n}: esperado {esperado}; instalado {actual}")
    excel=ROOT/"data/raw/Base-INDICES-Matricula-2005-2026.xlsx"
    sha=None
    sha_csv=None
    if excel.is_file():
        h=hashlib.sha256()
        with excel.open("rb") as f:
            for bloque in iter(lambda:f.read(1<<20),b""):h.update(bloque)
        sha=h.hexdigest()
        meta=ROOT/"docs/metadatos_fase1.json"
        if meta.is_file():
            if sha!=json.loads(meta.read_text(encoding="utf-8"))["sha256_origen"]:
                errores.append("SHA-256 Excel no coincide con la fuente original")
        else:errores.append("Falta docs/metadatos_fase1.json")
    elif exigir_excel:errores.append("No existe "+str(excel))
    elif exigir_fuente:
        csv = ROOT/"data/fixtures/ip_2025_origen_filtrado.csv"
        if not csv.is_file():
            errores.append("No existe Excel CNED ni CSV IP 2025 versionado")
        else:
            h = hashlib.sha256()
            with csv.open("rb") as f:
                for bloque in iter(lambda: f.read(1<<20), b""): h.update(bloque)
            sha_csv = h.hexdigest()
            esperado = "dd5f92fd31edc9d5cea40a443646ed899a3857a8e018e78f003bc6de0705080d"
            if sha_csv != esperado:
                errores.append("SHA-256 del CSV publicado no coincide con el validado")
    resultado={"correcto":not errores,"python":sys.version.split()[0],"interprete":sys.executable,"dependencias":req,"sha256_excel":sha,"sha256_csv_ip2025":sha_csv,"errores":errores}
    print(json.dumps(resultado,indent=2,ensure_ascii=False))
    if errores:raise SystemExit(1)
    return resultado
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--exigir-excel",action="store_true");p.add_argument("--exigir-fuente",action="store_true")
    args=p.parse_args(); verificar(args.exigir_excel, args.exigir_fuente)
