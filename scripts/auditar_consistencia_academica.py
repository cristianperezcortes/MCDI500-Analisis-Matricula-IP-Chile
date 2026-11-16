#!/usr/bin/env python3
"""Controla objetivos y notebooks; no reemplaza la plantilla institucional."""
import json
import re
import zipfile
from pathlib import Path
import nbformat
from lxml import etree
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
W="{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
def auditar():
    paths={x:ROOT/f"{x}/{name}" for x,name in (("F1","F1_Definicion_Cned.ipynb"),("F2","F2_Preprocesamiento_Cned.ipynb"),("F3","S2_F3_NucleoAlgoritmico_Cned.ipynb"))}
    nb={k:nbformat.read(p,as_version=4) for k,p in paths.items()}
    for n in nb.values():nbformat.validate(n)
    textos={k:"\n".join(c.source for c in n.cells if c.cell_type=="markdown") for k,n in nb.items()}
    with zipfile.ZipFile(ROOT/"docs/Informe_Sumativa1_F1_F2_Guia_Integrada.docx") as z:
        node=etree.fromstring(z.read("word/document.xml"))
    doc="\n".join("".join(t.text or "" for t in p.iter(W+"t")) for p in node.iter(W+"p"))
    objetivos=(ROOT/"docs/objetivos_analiticos_f1f3.txt").read_text(encoding="utf-8").strip().splitlines()
    checks={"tres_objetivos_analiticos":len(objetivos)==3}
    for i,o in enumerate(objetivos,1):
        for f in ("F1","F2"):checks[f"objetivo_{i}_{f}"]=o in textos[f]
        checks[f"objetivo_{i}_informe"]=o in doc
    for f,n in nb.items():
        code=[c for c in n.cells if c.cell_type=="code"]
        checks[f"{f}_secuencia"]=[c.execution_count for c in code]==list(range(1,len(code)+1))
        checks[f"{f}_sin_errores"]=all(o.output_type!="error" for c in code for o in c.outputs)
        checks[f"{f}_sin_instalaciones"]=not re.search(r"(?m)^\s*(?:%pip|!pip|pip install)", "\n".join(c.source for c in code))
    pdf=PdfReader(str(ROOT/"docs/Informe_Sumativa1_F1_F2_Guia_Integrada.pdf"))
    texto_pdf=" ".join(" ".join((p.extract_text() or "").split()) for p in pdf.pages)
    checks["pdf_carta"]=len(pdf.pages)>=7 and all(abs(float(p.mediabox.width)-612)<1 and abs(float(p.mediabox.height)-792)<1 for p in pdf.pages)
    checks["pdf_tres_objetivos"]=all(" ".join(o.split())[:85] in texto_pdf for o in objetivos)
    checks["pdf_dos_figuras"]="Figura 1" in texto_pdf and "Figura 2" in texto_pdf
    checks["notebook_fijado"]="notebook==7.5.3" in (ROOT/"requirements.txt").read_text(encoding="utf-8")
    salida={"aprobados":sum(checks.values()),"total":len(checks),"fallidos":[x for x,y in checks.items() if not y],"controles":checks}
    print(json.dumps(salida,indent=2,ensure_ascii=False))
    if salida["fallidos"]:raise SystemExit(1)
    return salida
if __name__=="__main__":auditar()
