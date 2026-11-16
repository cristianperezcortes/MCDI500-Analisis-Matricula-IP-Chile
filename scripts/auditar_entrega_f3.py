#!/usr/bin/env python3
"""Puerta de calidad documental y de datos de la Sumativa 2 (F3).

El modo predeterminado puede ejecutarse en CI sin publicar el Excel CNED.
El modo --integracion coteja la fuente original con los extractos y ejecuta
la comparación exacta F2/F3. No simula ni suplanta la revisión del equipo.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys
import zipfile

import nbformat
import pandas as pd
from lxml import etree
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

RUTAS_CRITICAS = (
    'F1/F1_Definicion_Cned.ipynb',
    'F2/F2_Preprocesamiento_Cned.ipynb',
    'F3/S2_F3_NucleoAlgoritmico_Cned.ipynb',
    'src/cned_pipeline.py', 'src/f3_transformaciones.py',
    'src/f3_pipeline.py', 'src/f3_medicion.py', 'src/f3_recursion.py',
    'docs/f3_s02_entregable_g8.docx', 'docs/f3_s02_entregable_g8.pdf',
    'evidencias/f3_benchmarks.csv', 'evidencias/f3_equivalencia_f2.json',
    'tests/test_f3_regresion_portatil.py', 'requirements.txt',
)


def _registrar(checks: list[dict], codigo: str, condicion: bool, detalle: str) -> None:
    checks.append({'control': codigo, 'aprobado': bool(condicion), 'evidencia': detalle})


def _texto_docx(ruta: Path):
    with zipfile.ZipFile(ruta) as z:
        xml = etree.fromstring(z.read('word/document.xml'))
    w = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    texto = '\n'.join(xml.xpath('//w:t/text()', namespaces=w))
    tablas = []
    for tr in xml.xpath('//w:tr', namespaces=w):
        celdas = []
        for tc in tr.xpath('./w:tc', namespaces=w):
            celdas.append(''.join(tc.xpath('.//w:t/text()', namespaces=w)))
        if celdas:
            tablas.append(celdas)
    return texto, tablas


def auditar(integracion: bool = False) -> dict:
    checks = []
    for rel in RUTAS_CRITICAS:
        _registrar(checks, 'archivo:' + rel, (ROOT / rel).is_file(), rel)

    notebooks = {}
    for fase, ruta in {
        'F1': 'F1/F1_Definicion_Cned.ipynb',
        'F2': 'F2/F2_Preprocesamiento_Cned.ipynb',
        'F3': 'F3/S2_F3_NucleoAlgoritmico_Cned.ipynb',
    }.items():
        nb = nbformat.read(ROOT / ruta, as_version=4)
        nbformat.validate(nb)
        celdas = [c for c in nb.cells if c.cell_type == 'code']
        cuentas = [c.execution_count for c in celdas]
        errores = sum(o.output_type == 'error' for c in celdas for o in c.get('outputs', []))
        valido = cuentas == list(range(1, len(celdas) + 1)) and errores == 0
        notebooks[fase] = {'total': len(nb.cells), 'codigo': len(celdas), 'secuencia': cuentas, 'errores': errores}
        _registrar(checks, 'notebook:' + fase, valido, f'{len(celdas)} celdas ejecutadas y {errores} errores')

    datos_bench = pd.read_csv(ROOT / 'evidencias/f3_benchmarks.csv', encoding='utf-8-sig')
    conjuntos = set(datos_bench['algoritmo'])
    grupos = datos_bench.groupby('filas')['algoritmo'].nunique()
    bien = (conjuntos == {'bucle_por_grupo', 'pandas_groupby'}
            and len(grupos) >= 3 and grupos.eq(2).all()
            and datos_bench['equivalencia_validada'].eq(True).all()
            and datos_bench['tiempo_minimo_ms'].gt(0).all()
            and datos_bench['memoria_pico_mib'].ge(0).all())
    _registrar(checks, 'benchmark:replicable', bien,
               f'{len(datos_bench)} filas, {len(grupos)} tamaños, 2 algoritmos, tiempos y memoria')

    texto, filas_tablas = _texto_docx(ROOT / 'docs/f3_s02_entregable_g8.docx')
    tabla_bench = [f for f in filas_tablas if len(f) == 4 and f[0].strip().isdigit() and f[1] in conjuntos]
    valores_coherentes = True
    for _, r in datos_bench.iterrows():
        matching = [f for f in tabla_bench if int(f[0]) == int(r['filas']) and f[1] == r['algoritmo']]
        esperado = f"{float(r['tiempo_minimo_ms']):.3f}"
        if len(matching) != 1 or matching[0][2] != esperado:
            valores_coherentes = False
    _registrar(checks, 'informe:benchmark_concordante', valores_coherentes,
               'tabla DOCX coincide con CSV de evidencia en los seis registros')

    _registrar(checks, 'informe:sin_marcadores_md', '**' not in texto,
               'no aparecen marcas Markdown literales en el DOCX')
    _registrar(checks, 'informe:seis_apartados', all(re.search(rf'\b{rom}\.', texto)
                for rom in ('I', 'II', 'III', 'IV', 'V', 'VI')),
               'portada/índice, soluciones algorítmicas, POO, GitHub, notebook y bibliografía')
    referencias = ('Salinas Silva, O. I. (2026a)', 'Salinas Silva, O. I. (2026b)',
                   'Python Software Foundation.', 'pandas development team.', 'McKinney, W. (2022)')
    _registrar(checks, 'informe:referencias', all(r in texto for r in referencias),
               '2 fuentes docentes + documentación oficial + libro técnico de 2022')
    pdf = ROOT / 'docs/f3_s02_entregable_g8.pdf'
    _registrar(checks, 'informe:pdf', pdf.read_bytes()[:4] == b'%PDF' and pdf.stat().st_size > 20_000,
               'PDF generado y verificable; cotejo de la plantilla Canvas permanece pendiente')
    lector = PdfReader(str(pdf))
    texto_pdf = '\n'.join(pagina.extract_text() or '' for pagina in lector.pages)
    carta = len(lector.pages) >= 6 and all(
        abs(float(p.mediabox.width) - 612.0) < 1 and abs(float(p.mediabox.height) - 792.0) < 1
        for p in lector.pages
    )
    _registrar(checks, 'informe:formato_carta', carta,
               f'{len(lector.pages)} páginas, cada una de 612×792 puntos (carta)')
    importes_bench = all(f"{float(r['tiempo_minimo_ms']):.3f}" in texto_pdf
                         for _, r in datos_bench.iterrows())
    _registrar(checks, 'informe:pdf_cifras', importes_bench and '**' not in texto_pdf,
               'PDF coincide con seis tiempos del CSV y no contiene marcas Markdown')

    fuente = ROOT / 'data/raw/Base-INDICES-Matricula-2005-2026.xlsx'
    externo = ['plantilla institucional de Canvas', 'confirmación docente de grupo de dos',
               'fecha y URL oficiales de origen del XLSX',
               'revisión y contribución independiente de Cristian', 'entrega en Canvas']
    if integracion:
        from src.cned_pipeline import preparar_fase2, validar_fase2, sha256_archivo
        from src.f3_pipeline import PipelineCNED
        origen_csv = ROOT / 'data/interim/ip_2025_origen_filtrado.csv'
        procesado_csv = ROOT / 'data/processed/matricula_ip_2025_procesada_v3.csv'
        for ruta in (fuente, origen_csv, procesado_csv):
            if not ruta.is_file():
                raise FileNotFoundError(f'Falta {ruta}; ejecute F2 con el Excel suministrado')
        esperado = json.loads((ROOT / 'docs/metadatos_fase1.json').read_text(encoding='utf-8'))['sha256_origen']
        observado = sha256_archivo(fuente)
        _registrar(checks, 'origen:sha256', esperado == observado,
                   f'Hash observado {observado}; no modificar el Excel original')
        datos = pd.read_csv(origen_csv, encoding='utf-8-sig', low_memory=False)
        ref, aud = preparar_fase2(datos)
        propuesto = PipelineCNED().ajustar(datos).transformar(datos)
        pd.testing.assert_frame_equal(ref, propuesto, check_exact=True)
        validar_fase2(datos, propuesto, aud)
        _registrar(checks, 'datos:f2_f3',
                   propuesto.shape == (4731, 68)
                   and int(propuesto['Matrícula Primer Año'].sum()) == 137481
                   and int(propuesto['Matrícula Total'].sum()) == 439607,
                   'comparación exhaustiva F2=F3; 4.731×68; matrículas 137.481 y 439.607')
    else:
        _registrar(checks, 'integracion:sin_excel', True,
                   'No requerida en CI; ejecutar con --integracion en equipo con Excel original')

    reporte = {'fecha_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
               'tipo': 'revisión interna, no nota docente', 'integracion_excel': integracion,
               'notebooks': notebooks,
               'controles': checks,
               'aprobados': sum(x['aprobado'] for x in checks),
               'fallidos': [x['control'] for x in checks if not x['aprobado']],
               'pendientes_externos': externo}
    destino = ROOT / 'evidencias/auditoria_adicional_f3.json'
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(reporte, indent=2, ensure_ascii=False), encoding='utf-8')
    print(json.dumps({'aprobados': reporte['aprobados'],
                      'total': len(checks), 'fallidos': reporte['fallidos'],
                      'integracion_excel': integracion}, ensure_ascii=False))
    if reporte['fallidos']:
        raise SystemExit(1)
    return reporte


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--integracion', action='store_true',
                        help='Verificar XLSX original, SHA-256 y equivalencia F2/F3 completa')
    args = parser.parse_args()
    auditar(args.integracion)
