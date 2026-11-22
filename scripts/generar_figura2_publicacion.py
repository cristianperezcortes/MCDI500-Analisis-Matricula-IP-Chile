"""Figura complementaria F4: participaciones por región y área sin confundir Tecnología.

Para reproducir desde un clon limpio:
    python scripts/generar_figura2_publicacion.py --output evidencias/F4_region_area_puntos_publicacion.png
Usa exclusivamente los agregados versionados de F2, no el Excel externo.
"""
from __future__ import annotations
import argparse
import csv
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

RAIZ = Path(__file__).resolve().parents[1]
DATA = RAIZ / "data" / "processed"


def leer_agregado(nombre: str, campo: str):
    with (DATA / f"matricula_por_{nombre}.csv").open(encoding="utf-8-sig", newline="") as archivo:
        filas = list(csv.DictReader(archivo))
    valores = [(fila[campo], int(fila["matricula_primer_anio"])) for fila in filas]
    return sorted(valores, key=lambda x: x[1], reverse=True)


def crear_figura(ruta_salida: str | Path):
    regiones = leer_agregado("region", "Nombre Region")
    areas = leer_agregado("area", "Area Conocimiento")
    assert len(regiones) == 16 and len(areas) == 10
    total = sum(v for _, v in regiones)
    assert total == sum(v for _, v in areas) == 137481
    a = dict(areas)
    assert a["Tecnología"] == 61423 and a["Administración y Comercio"] == 35461
    assert round(100 * a["Tecnología"] / total, 2) == 44.68
    assert round(100 * (a["Tecnología"] + a["Administración y Comercio"]) / total, 2) == 70.47

    reemplazos_region = {
        "Región Metropolitana": "Metropolitana",
        "Región del Bío-Bío": "Biobío",
        "Región de Valparaíso": "Valparaíso",
        "Región del Gral. B. O`Higgins": "O'Higgins",
        "Región de La Araucanía": "Araucanía",
        "Región de Arica y Parinacota": "Arica-Parinacota",
    }
    reemplazos_area = {
        "Agricultura, Silvicultura, Pesca y Veterinaria": "Agricultura y afines",
    }

    fig = plt.figure(figsize=(16.53, 10.28), facecolor="white")
    grupos = [
        (fig.add_axes([.113, .16, .31, .68]), regiones, "A. REGIONES (16)", reemplazos_region),
        (fig.add_axes([.61, .16, .31, .68]), areas, "B. ÁREAS (10)", reemplazos_area),
    ]
    for ax, serie, titulo, renombres in grupos:
        vals = np.array([v for _, v in serie]) / total * 100
        etiquetas = [renombres.get(nombre, nombre.replace("Región de ", "")) for nombre, _ in serie]
        yi = np.arange(len(serie))
        for i, valor in enumerate(vals):
            ax.plot([0, valor], [yi[i], yi[i]], color="#adc2ce", lw=1.8, zorder=1)
            ax.scatter([valor], [yi[i]], s=45 if i == 0 else 20,
                       color="#b91f41" if i == 0 else "#245575", zorder=2)
            if i < 3:
                ax.text(valor + 1.2, yi[i], f"{valor:.2f}%".replace(".", ","),
                        va="center", fontsize=11, color="#263d50",
                        fontweight="bold" if i == 0 else "normal")
        ax.set_yticks(yi, etiquetas)
        ax.set_ylim(-.6, len(serie) - .4)
        ax.invert_yaxis()
        ax.set_xlim(0, 75)
        ax.set_xticks([0, 20, 40, 60], ["0 %", "20 %", "40 %", "60 %"])
        ax.grid(axis="x", lw=.7, color="#dde5eb")
        ax.set_axisbelow(True)
        ax.tick_params(axis="both", length=0, labelsize=11.5)
        ax.set_title(titulo, fontsize=19, fontweight="bold", pad=13)
        for spine in ax.spines.values():
            spine.set_visible(False)
    fig.text(.5, .953, "Concentración territorial y académica: participaciones por categoría",
             ha="center", fontsize=20, fontweight="bold", color="#0e2b40")
    fig.text(.5, .087,
             "Tecnología individual: 44,68 %  |  Tecnología + Administración y Comercio: 70,47 %",
             ha="center", fontsize=15.5, fontweight="bold", color="#a70f32")
    fig.text(.5, .034,
             "Fuente: CNED–INDICES, IP 2025. Universo N=137.481; CR3/HHI se calculan sobre todas las categorías.",
             ha="center", fontsize=10.8, color="#526a7b")
    destino = Path(ruta_salida)
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, dpi=100, facecolor="white")
    plt.close(fig)
    return destino


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(RAIZ / "evidencias" / "F4_region_area_puntos_publicacion.png"))
    args = parser.parse_args()
    print("Figura exportada:", crear_figura(args.output))
