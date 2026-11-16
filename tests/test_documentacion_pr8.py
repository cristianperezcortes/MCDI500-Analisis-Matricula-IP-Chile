"""Controles portátiles para fechas, procedencia e integridad documental del PR #8."""
from pathlib import Path
from zipfile import ZipFile
import re

from lxml import etree
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PDFS = ["Informe_Sumativa1_F1_F2_Guia_Integrada.pdf", "f3_s02_entregable_g8.pdf"]
DOCXS = ["Informe_Sumativa1_F1_F2_Guia_Integrada.docx", "f3_s02_entregable_g8.docx"]


def _texto_docx(ruta):
    with ZipFile(ruta) as z:
        assert z.testzip() is None
        xml = etree.fromstring(z.read("word/document.xml"))
        texts = xml.xpath("//w:t/text()", namespaces={"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"})
        return " ".join(texts)


def test_informes_distinguen_periodo_2025_y_elaboracion_2026():
    for name in PDFS:
        reader = PdfReader(DOCS / name)
        contenido = " ".join(page.extract_text() or "" for page in reader.pages)
        assert "2025" in contenido and "2026" in contenido, name
        creado = str(reader.metadata.get("/CreationDate", ""))
        assert creado.startswith("D:2026"), (name, creado)


def test_documentos_word_indican_cned_y_limite_edicion():
    for name in DOCXS:
        t = _texto_docx(DOCS / name)
        assert "Consejo Nacional de Educación" in t, name
        assert "2005" in t and "2025" in t and "2026" in t, name
        assert "descarga" in t.lower(), name


def test_origen_institucional_no_simula_url_de_la_copia_local():
    texto = (DOCS / "Proveniencia_CNED_INDICES.md").read_text(encoding="utf-8")
    assert "cned.cl/institucional/bases-de-datos/" in texto
    assert "SHA-256" in texto
    assert "2005–2025" in texto and "2005-2026" in texto
    assert "no se afirma" in texto.lower()
    assert "fecha" in texto.lower() and "sin acreditar" in texto.lower()


def test_concentracion_declara_limites_por_dimension():
    texto = (DOCS / "Nota_metodologica_concentracion.md").read_text(encoding="utf-8")
    for valor in ("CR3", "HHI", "institución", "región", "área"):
        assert valor in texto
    assert "no son particiones intercambiables" in texto.lower()


def test_pr7_no_figura_como_pendiente_tras_su_merge():
    rutas = [
        ROOT / "README.md",
        DOCS / "Estado_integracion_GitHub.md",
        DOCS / "README_VERSIONES.md",
        DOCS / "Checklist_entrega_F3_grupo8.md",
        DOCS / "Auditoria_cierre_reproducibilidad_20261116.md",
        DOCS / "Protocolo_reproducibilidad_20261116.md",
    ]
    for path in rutas:
        txt = path.read_text(encoding="utf-8")
        assert not re.search(r"PR\s*#?\s*7[^\n]{0,100}(?:pendiente|abierto|por fusionar)", txt, re.I), path
        assert not re.search(r"PR\s*#?\s*7\s+propone", txt, re.I), path
    assert "PR #1–7" in (ROOT / "README.md").read_text(encoding="utf-8")
