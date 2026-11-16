#!/usr/bin/env python3
"""Sincroniza el informe F1/F2 de la rama correctiva (idempotente)."""
from pathlib import Path
from docx import Document
from docx.shared import Inches
from docx.text.paragraph import Paragraph
from docx.oxml import OxmlElement

ROOT=Path(__file__).resolve().parents[1]
DOC=ROOT/"docs/Informe_Sumativa1_F1_F2_Guia_Integrada.docx"
OBJECTIVES=(ROOT/"docs/objetivos_analiticos_f1f3.txt").read_text(encoding="utf-8").strip().splitlines()
assert len(OBJECTIVES)==3
d=Document(DOC)
p=list(d.paragraphs)
head=next(x for x in p if x.text.startswith("4.3.2 ") and "objetivos específicos" in x.text)
head.text="4.3.2 Objetivos específicos analíticos"
p=list(d.paragraphs)
idx=next(i for i,v in enumerate(p) if v._element is head._element)
bullets=[]
for a in p[idx+1:]:
    if a.style.name.startswith("Heading"):break
    if a.style.name=="List Bullet":bullets.append(a)
if len(bullets)==5:
    for i,t in enumerate(OBJECTIVES):bullets[i].text=t
    for old in bullets[3:]:
        el=old._element
        el.getparent().remove(el)
elif len(bullets)==3:
    for i,t in enumerate(OBJECTIVES):bullets[i].text=t
else:raise RuntimeError(f"Objetivos inesperados: {len(bullets)}")
p=list(d.paragraphs)
idx=next(i for i,v in enumerate(p) if v._element is head._element)
last_bullet=next(a for a in reversed(p[:next(i for i,v in enumerate(p) if i>idx and v.style.name.startswith("Heading"))]) if a.style.name=="List Bullet")
if not any("Actividades metodológicas, no objetivos:" in x.text for x in d.paragraphs):
    elem=OxmlElement("w:p");last_bullet._p.addnext(elem)
    par=Paragraph(elem,last_bullet._parent);par.style=d.styles["Normal"]
    par.add_run("Actividades metodológicas, no objetivos: ").bold=True
    par.add_run("selección y diagnóstico en F1; comparación de imputaciones y validación en F2; arquitectura POO y eficiencia en F3. Son actividades de método, no sustituyen los objetivos de análisis.")
for x in d.paragraphs:
    for run in x.runs:
        run.text=run.text.replace("aprobó 44 pruebas locales de F1–F3","verificó 44/44 pruebas en Windows; la batería ampliada con la fuente original alcanzó 53/53")
        run.text=run.text.replace("comprobó 44 pruebas","comprobó 44/44 en Windows; una auditoría ampliada posterior alcanzó 53/53")
        run.text=run.text.replace("los PR #2, #3 y #4","los PR #2, #3 y #4; los PR #5 y #6 cerraron correcciones académicas y trazabilidad")
        run.text=run.text.replace("lo pendiente para F3/F4","lo ejecutado en F3 y lo pendiente para F4")
    if x.text.startswith("El entorno de auditoría se ejecutó con") and "Notebook 7.5.3" not in x.text:
        x.add_run(" El entorno de trabajo fija también Jupyter Notebook 7.5.3 y JupyterLab 4.5.3. Se configuró una matriz de instalación limpia en GitHub Actions para Windows y Ubuntu, independiente de las pruebas con el Excel original.")
for table in d.tables:
    for row in table.rows:
        if len(row.cells)<2:continue
        key=row.cells[0].text.strip()
        c=row.cells[1]
        if key=="Pytest (unitarias e integración)":c.text="53/53 aprobadas con Excel original (auditoría local); 50/50 pruebas portátiles"
        if key=="Pruebas":c.text="44/44 en Windows por Cristian; 53/53 en auditoría local ampliada; CI omite las pruebas que requieren Excel"
        if key=="Segundo equipo":c.text="Cristian: Windows, Python 3.13.17, ejecución F1–F3 y 44/44 pruebas; 53/53 con fuente original en auditoría posterior"
        if key=="Autoría Git":c.text="Commits reales de ambos integrantes y PR #1–6 integrados a main, con revisiones registradas donde corresponden"
for x in list(d.paragraphs):
    for prefix,rel,width in (("Figura 1.","evidencias/top10_matricula_instituciones.png",5.65),("Figura 2.","docs/mapa_fases_evidencia.png",6.25)):
        if not x.text.startswith(prefix):continue
        if not (ROOT/rel).is_file():raise FileNotFoundError(rel)
        el=OxmlElement("w:p");x._p.addprevious(el)
        par=Paragraph(el,x._parent);par.alignment=1
        par.add_run().add_picture(str(ROOT/rel),width=Inches(width))
        par.paragraph_format.keep_with_next=True
        x.paragraph_format.keep_together=True
d.save(DOC)
print("Informe F1/F2 actualizado con objetivos, 2 imágenes y datos de validación.")
