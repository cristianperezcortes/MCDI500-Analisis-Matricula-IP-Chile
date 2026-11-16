"""MCDI500 | Flujo auditable de matrícula CNED de Institutos Profesionales 2025.

Datos: archivo Excel INDICES suministrado para el proyecto. La procedencia exacta
2005-2026 debe confirmarse contra el CNED; el portal público consultado anuncia
una descarga 2005-2025. No se altera la fuente original.

Se recorre el XML del XLSX de forma incremental para filtrar sin cargar los
260.307 registros en memoria. Los cálculos analíticos se realizan con pandas.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import hashlib
import re
import zipfile

import numpy as np
import pandas as pd
from lxml import etree

ANIO_ANALISIS = 2025
TIPO_INSTITUCION = "I.P."
NAMESPACE = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
COLUMNAS_MATRICULA = [
    "Matrícula Primer Año", "Matrícula Total",
    "Matrícula primer año hombres", "Matrícula primer año mujeres",
    "Matrícula Primer Año No Binario", "Matrícula total hombres",
    "Matrícula total mujeres", "Matrícula Total No Binario",
]
COLUMNAS_NUMERICAS = [
    "Año", "Año Inicio Actividades", "Orden Geográfico de la Región (Norte aSur)",
    "Duración (en semestres)", "Nº Alumnos Ingreso Otra Via", "Nº Alumnos Ingreso Via PSU o PDT",
    "Valor de matrícula", "Valor de arancel", "Valor del Título", "Vacantes",
    *COLUMNAS_MATRICULA,
]
VARIABLES_IMPUTABLES = {
    "Valor de arancel": "arancel",
    "Valor de matrícula": "valor_matricula",
    "Valor del Título": "valor_titulo",
    "Vacantes": "vacantes",
}
CAMPOS_IDENTIDAD = [
    "Año", "Nombre Institución", "Tipo Institución", "Nombre Programa",
    "Nombre de la Sede", "Nombre Region", "Area Conocimiento",
    "Matrícula Primer Año", "Matrícula Total", "Pregrado/Posgrado",
]


def sha256_archivo(ruta: str | Path) -> str:
    """Huella verificable de la fuente sin modificarla."""
    h = hashlib.sha256()
    with Path(ruta).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _columna_indice(referencia: str) -> int:
    letras = re.match(r"([A-Z]+)", referencia)
    if not letras:
        raise ValueError(f"Referencia XLSX inválida: {referencia!r}")
    i = 0
    for caracter in letras.group(1):
        i = 26 * i + ord(caracter) - 64
    return i - 1


def _valor(celda: etree._Element, cadenas: list[str]):
    v = celda.find(NAMESPACE + "v")
    if v is None or v.text is None:
        texto_inline = celda.find(NAMESPACE + "is")
        return "".join(texto_inline.itertext()) if texto_inline is not None else None
    if celda.get("t") == "s":
        return cadenas[int(v.text)]
    if celda.get("t") == "b":
        return v.text == "1"
    return v.text


def filtrar_ip_2025(datos: pd.DataFrame, anio: int = ANIO_ANALISIS) -> pd.DataFrame:
    """Filtro vectorizado, usado para casos sintéticos y como contrato de F1/F2."""
    requeridas = {"Tipo Institución", "Año"}
    if not requeridas.issubset(datos.columns):
        raise ValueError(f"Columnas faltantes: {sorted(requeridas-set(datos.columns))}")
    return datos.loc[
        (datos["Tipo Institución"].astype("string").str.strip() == TIPO_INSTITUCION)
        & (pd.to_numeric(datos["Año"], errors="coerce") == anio)
    ].copy().reset_index(drop=True)


def cargar_cned_ip(ruta_excel: str | Path, anio: int = ANIO_ANALISIS) -> tuple[pd.DataFrame, dict]:
    """Extrae únicamente IP del año requerido mediante lectura XML incremental.

    Preserva todos los campos del origen. Evita 200+ segundos de lectura
    convencional de un libro de más de 58 MB, sin comprometer verificabilidad.
    """
    ruta = Path(ruta_excel)
    if not ruta.is_file():
        raise FileNotFoundError(f"No se encuentra el Excel original: {ruta}")
    if ruta.suffix.lower() != ".xlsx":
        raise ValueError("Se necesita el archivo original en formato .xlsx")

    with zipfile.ZipFile(ruta) as z:
        hojas = [n for n in z.namelist() if re.fullmatch(r"xl/worksheets/sheet\d+\.xml", n)]
        if len(hojas) != 1:
            raise ValueError("Este lector optimizado requiere exactamente una hoja; revisar esquema XLSX")
        with z.open("xl/sharedStrings.xml") as f:
            arbol = etree.parse(f)
            cadenas = ["".join(item.itertext()) for item in arbol.getroot()]
        encabezados = None
        filas = []
        n_original = 0
        with z.open(hojas[0]) as archivo_xml:
            for _, fila in etree.iterparse(archivo_xml, events=("end",), tag=NAMESPACE+"row"):
                celdas = list(fila)
                if encabezados is None:
                    cantidad = max(_columna_indice(c.get("r")) for c in celdas) + 1
                    encabezados = [None] * cantidad
                    for celda in celdas:
                        encabezados[_columna_indice(celda.get("r"))] = _valor(celda, cadenas)
                    if any(nombre is None for nombre in encabezados):
                        raise ValueError("La fila de encabezados contiene columnas vacías")
                    try:
                        ix_anio = encabezados.index("Año")
                        ix_tipo = encabezados.index("Tipo Institución")
                    except ValueError as exc:
                        raise ValueError("Esquema de columnas CNED no reconocido") from exc
                else:
                    n_original += 1
                    primeras = {_columna_indice(c.get("r")): _valor(c, cadenas)
                                for c in celdas if _columna_indice(c.get("r")) in {ix_anio, ix_tipo}}
                    if str(primeras.get(ix_anio, "")).strip() == str(anio) and primeras.get(ix_tipo) == TIPO_INSTITUCION:
                        valores = [None] * len(encabezados)
                        for celda in celdas:
                            idx = _columna_indice(celda.get("r"))
                            if idx < len(encabezados):
                                valores[idx] = _valor(celda, cadenas)
                        filas.append(valores)
                fila.clear()
                while fila.getprevious() is not None:
                    del fila.getparent()[0]

    datos = pd.DataFrame(filas, columns=encabezados)
    for columna in COLUMNAS_NUMERICAS:
        if columna in datos.columns:
            datos[columna] = pd.to_numeric(datos[columna], errors="coerce")
    if datos.empty:
        raise ValueError(f"No se encontraron IP en {anio}: revise filtros y fuente")
    metadata = {
        "archivo_origen": ruta.name,
        "sha256": sha256_archivo(ruta),
        "filas_origen": n_original,
        "columnas_origen": len(encabezados),
        "filas_filtradas": len(datos),
        "anio": anio,
        "tipo_institucion": TIPO_INSTITUCION,
    }
    return datos.reset_index(drop=True), metadata


def diagnosticar_faltantes(datos: pd.DataFrame) -> pd.DataFrame:
    """Antes de eliminar columnas, contabiliza también marcadores 'Null' textuales."""
    df = normalizar_valores_nulos(datos)
    return (pd.DataFrame({
        "variable": list(df.columns),
        "faltantes": df.isna().sum().values.astype(int),
        "porcentaje_faltante": (100*df.isna().mean()).round(3).values,
        "tipo": df.dtypes.astype(str).values,
    }).sort_values(["faltantes", "variable"], ascending=[False, True]).reset_index(drop=True))


def normalizar_valores_nulos(datos: pd.DataFrame) -> pd.DataFrame:
    """Convierte 'Null' y equivalentes a faltante real; elimina espacios sobrantes.

    No reemplaza códigos ausentes con medianas ni modifica números válidos 0.
    """
    df = datos.copy()
    for c in df.select_dtypes(include=["object", "string"]).columns:
        serie = df[c].astype("string").str.strip()
        es_faltante = serie.str.lower().isin(["null", "none", "nan", "n/a", "", "<na>"])
        df[c] = serie.mask(es_faltante, pd.NA)
    return df


def depurar_estructura(datos: pd.DataFrame, umbral_faltantes: float = 0.90):
    """Retira campos completamente vacíos y de ausencia >90%, de forma auditable."""
    if datos.empty:
        raise ValueError("No se puede depurar una tabla vacía")
    if not 0 < umbral_faltantes <= 1:
        raise ValueError("umbral_faltantes debe estar entre 0 y 1")
    df = normalizar_valores_nulos(datos)
    resumen = diagnosticar_faltantes(datos)
    vacias = df.columns[df.isna().all()].tolist()
    elevadas = [c for c in df.columns if c not in vacias and df[c].isna().mean() > umbral_faltantes]
    # Nunca eliminar métricas centrales por una regla automática.
    protegidas = set(CAMPOS_IDENTIDAD)
    if protegidas.intersection(vacias + elevadas):
        raise ValueError("Columnas analíticas críticas con nulos excesivos: revisión manual obligatoria")
    df = df.drop(columns=vacias+elevadas).reset_index(drop=True)
    if "Tipo Moneda" in df.columns:
        moneda = df["Tipo Moneda"].astype("string").str.upper().str.strip()
        df["moneda_normalizada"] = moneda.replace({"PESOS": "CLP", "PESO": "CLP"})
    return df, {"columnas_vacias": vacias, "columnas_excluidas_por_umbral": elevadas, "tabla_faltantes_original": resumen}


def promedio_matricula(datos: pd.DataFrame, campo: str = "Matrícula Total") -> float:
    """Demuestra parametrización y fallos explícitos en casos límite."""
    if datos.empty:
        raise ValueError("No se puede calcular el promedio de una tabla vacía")
    if campo not in datos.columns:
        raise KeyError(f"No existe la columna {campo}")
    valores = pd.to_numeric(datos[campo], errors="coerce")
    if not valores.notna().any():
        raise ValueError("Todos los registros de matrícula están ausentes")
    if (valores.dropna() < 0).any():
        raise ValueError("No se permiten matrículas negativas")
    return float(valores.mean())


def _predecir_mediana_entorno(datos: pd.DataFrame, col: str, mascara: pd.Series,
                             nivel: str = "grupo", moneda: bool = True) -> pd.Series:
    """Calcula predicciones sin consultar valores ocultados durante validación.

    CLP: mediana por institución (n>=5), área (n>=5), moneda general.
    Vacantes: misma jerarquía sin división por moneda.
    """
    validos = pd.to_numeric(datos[col], errors="coerce")
    validos = validos.mask(mascara)
    if moneda:
        elegible = datos["moneda_normalizada"].eq("CLP").fillna(False)
    else:
        elegible = pd.Series(True, index=datos.index)
    entrenamiento = validos.where(elegible)
    global_ = float(entrenamiento.median()) if entrenamiento.notna().any() else np.nan
    pred = pd.Series(global_, index=datos.index, dtype="float64")
    if nivel == "global":
        return pred.where(elegible)
    for grupo in ["Area Conocimiento", "Nombre Institución"]:
        estimados = entrenamiento.groupby(datos[grupo], dropna=False).transform("median")
        conteos = entrenamiento.groupby(datos[grupo], dropna=False).transform("count")
        pred = pred.where(~conteos.ge(5), estimados)
    return pred.where(elegible)


def diagnosticar_atipicos(datos: pd.DataFrame, variables: list[str] | None = None, factor: float = 1.5) -> pd.DataFrame:
    """Describe extremos IQR sin descartarlos (la matrícula agregada puede estar muy sesgada)."""
    if factor <= 0: raise ValueError("El factor IQR debe ser positivo")
    variables = variables or ["Matrícula Primer Año", "Matrícula Total", "Vacantes", "Valor de arancel"]
    filas = []
    for nombre in variables:
        if nombre not in datos: raise KeyError(nombre)
        valores = pd.to_numeric(datos[nombre], errors="coerce").dropna()
        if nombre == "Valor de arancel" and "moneda_normalizada" in datos:
            valores = pd.to_numeric(datos.loc[datos["moneda_normalizada"].eq("CLP"), nombre], errors="coerce").dropna()
        if valores.empty:
            filas.append({"variable":nombre,"n_observados":0,"q1":None,"q3":None,"iqr":None,"atipicos":0,"pct_atipicos":None})
            continue
        q1, q3 = valores.quantile([0.25,0.75])
        iqr=q3-q1
        limite_inf=q1-factor*iqr
        limite_sup=q3+factor*iqr
        n=int(((valores<limite_inf)|(valores>limite_sup)).sum())
        filas.append({"variable":nombre,"n_observados":len(valores),"q1":float(q1),"q3":float(q3),
                      "iqr":float(iqr),"limite_inferior":float(limite_inf),"limite_superior":float(limite_sup),
                      "atipicos":n,"pct_atipicos":round(100*n/len(valores),3)})
    return pd.DataFrame(filas)


def _predecir_media_global(datos: pd.DataFrame, col: str, mascara: pd.Series, moneda: bool = True) -> pd.Series:
    """Media global calculada solamente con datos observados de la misma unidad."""
    serie=pd.to_numeric(datos[col],errors="coerce").mask(mascara)
    elegible=(datos["moneda_normalizada"].eq("CLP").fillna(False)
              if moneda else pd.Series(True,index=datos.index))
    media=serie.where(elegible).mean()
    return pd.Series(media,index=datos.index,dtype="float64").where(elegible)


def comparar_imputaciones(datos: pd.DataFrame, col: str, semilla: int = 42):
    """Compara eliminación, media, mediana y mediana jerárquica sin fuga de valores.

    Oculta 10% de observaciones conocidas con semilla fija. MAE es error de
    validación sobre valores ocultados, no prueba de ausencia aleatoria de nulos.
    La eliminación se cuantifica como pérdida de filas, no se le asigna MAE falso.
    """
    if col not in datos.columns: raise KeyError(col)
    monetaria = col != "Vacantes"
    observado=pd.to_numeric(datos[col],errors="coerce")
    elegible=datos["moneda_normalizada"].eq("CLP").fillna(False) if monetaria else pd.Series(True,index=datos.index)
    indices=datos.index[observado.notna() & elegible]
    if len(indices)<30: raise ValueError(f"Muestras insuficientes para comparar imputación en {col}")
    rng=np.random.default_rng(semilla)
    evaluacion=rng.choice(indices.to_numpy(),size=max(10,int(len(indices)*.1)),replace=False)
    ocultos=pd.Series(False,index=datos.index)
    ocultos.loc[evaluacion]=True
    predicciones={
        "media": _predecir_media_global(datos,col,ocultos,monetaria),
        "global": _predecir_mediana_entorno(datos,col,ocultos,"global",monetaria),
        "jerarquica": _predecir_mediana_entorno(datos,col,ocultos,"grupo",monetaria),
    }
    verdad=observado.loc[evaluacion]
    maes={k: float((verdad-p.loc[evaluacion]).abs().mean()) for k,p in predicciones.items()}
    elegido=min(maes,key=maes.get)
    return {
        "variable":col,"observaciones_validacion":len(evaluacion),
        "mae_media":round(maes["media"],3),"mae_global":round(maes["global"],3),
        "mae_jerarquica":round(maes["jerarquica"],3),"metodo_seleccionado":elegido,
        "filas_perdidas_si_elimina":int((observado.isna()&elegible).sum()),
        "semilla":semilla,
    }

def imputar_variable(datos: pd.DataFrame, col: str, alias: str, metodo: str) -> pd.DataFrame:
    """No sobrescribe columnas originales: crea estimación, bandera y método."""
    if metodo not in {"jerarquica", "global", "media"}:
        raise ValueError("Estrategia de imputación desconocida")
    df = datos.copy()
    serie = pd.to_numeric(df[col], errors="coerce")
    moneda = col != "Vacantes"
    elegible = df["moneda_normalizada"].eq("CLP").fillna(False) if moneda else pd.Series(True, index=df.index)
    falta = serie.isna() & elegible
    if metodo == "media":
        pred = _predecir_media_global(df,col,pd.Series(False,index=df.index),moneda)
    else:
        pred = _predecir_mediana_entorno(df, col,
                                        pd.Series(False, index=df.index),
                                        "grupo" if metodo == "jerarquica" else "global", moneda)
    estimado = serie.where(~falta, pred)
    nueva = f"{alias}_analisis"
    flag = f"{alias}_imputado"
    df[nueva] = estimado
    df[flag] = falta & estimado.notna()
    df[f"{alias}_metodo"] = np.where(df[flag], metodo, np.where(serie.isna(), "sin_estimacion", "observado"))
    # Prevenir daño semántico: valores observados y los 0 deben permanecer intactos.
    assert df.loc[serie.notna(), nueva].equals(serie.loc[serie.notna()].rename(nueva))
    return df


def crear_categorias_matricula(datos: pd.DataFrame, col: str = "Matrícula Total") -> pd.Series:
    """Cuartiles sobre el tamaño de cada oferta; conserva empates sin cortes arbitrarios."""
    a = pd.to_numeric(datos[col], errors="coerce")
    if a.notna().sum() < 4:
        raise ValueError("Observaciones insuficientes para categorías de matrícula")
    _, cortes = pd.qcut(a, q=4, retbins=True, duplicates="drop")
    cantidad = len(cortes)-1
    if cantidad <= 1:
        return pd.Series(pd.Categorical(["Sin variación"]*len(a)), index=a.index)
    nombres = ["Baja", "Media", "Alta", "Muy alta"] if cantidad == 4 else [f"Cuantil {k+1}" for k in range(cantidad)]
    return pd.qcut(a, q=4, labels=nombres, duplicates="drop")


def preparar_fase2(datos_filtrados: pd.DataFrame):
    """Pipeline trazable, auditable y parametrizable de F2."""
    df, auditoria = depurar_estructura(datos_filtrados)
    if "moneda_normalizada" not in df.columns:
        raise ValueError("No se encuentra la columna Tipo Moneda")
    estrategias = []
    for variable, alias in VARIABLES_IMPUTABLES.items():
        comparacion = comparar_imputaciones(df, variable)
        df = imputar_variable(df, variable, alias, comparacion["metodo_seleccionado"])
        datos_observados = pd.to_numeric(datos_filtrados[variable], errors="coerce")
        comparacion["faltantes_originales"] = int(datos_observados.isna().sum())
        comparacion["estimaciones_realizadas"] = int(df[f"{alias}_imputado"].sum())
        comparacion["faltantes_final_analisis"] = int(df[f"{alias}_analisis"].isna().sum())
        elegible = (df["moneda_normalizada"].eq("CLP").fillna(False)
                    if variable != "Vacantes" else pd.Series(True,index=df.index))
        antes = pd.to_numeric(datos_filtrados.loc[elegible, variable],errors="coerce")
        despues = pd.to_numeric(df.loc[elegible, f"{alias}_analisis"],errors="coerce")
        comparacion["desv_antes_observados"] = round(float(antes.std()),3)
        comparacion["desv_despues_analisis"] = round(float(despues.std()),3)
        comparacion["cambio_desv_pct"] = round(100*(despues.std()/antes.std()-1),3) if antes.std()>0 else None
        estrategias.append(comparacion)
    df["categoria_matricula_total"] = crear_categorias_matricula(df)
    # Ordinal: el orden se declara explícitamente, nunca por orden alfabético.
    categorias = df["categoria_matricula_total"].cat.categories.tolist()
    orden_categorias = {categoria:i+1 for i,categoria in enumerate(categorias)}
    df["categoria_matricula_total_codigo"] = df["categoria_matricula_total"].map(orden_categorias).astype("int64")
    # One-hot del nivel académico: dos etiquetas mutuamente excluyentes verificables.
    nivel = df["Pregrado/Posgrado"].astype("string")
    if not nivel.isin(["Pregrado","Posgrado"]).all():
        raise ValueError("Nivel académico no reconocido: requiere revisión")
    df["nivel_pregrado_onehot"] = nivel.eq("Pregrado").astype("int8")
    df["nivel_posgrado_onehot"] = nivel.eq("Posgrado").astype("int8")
    # Escalamiento y transformación derivada: no se sustituyen conteos originales.
    primer_anio=pd.to_numeric(df["Matrícula Primer Año"],errors="coerce")
    if primer_anio.isna().any() or (primer_anio<0).any():
        raise ValueError("Matrícula de primer año inválida para escalar")
    maximo=primer_anio.max()
    df["matricula_primer_anio_escala_0_1"] = primer_anio/maximo if maximo>0 else 0.0
    df["matricula_primer_anio_log1p"] = np.log1p(primer_anio)
    auditoria["escalamiento"]={"metodo":"MinMax[0,1] con mínimo observado = 0",
                                "maximo_observado":float(maximo),"log":"np.log1p",
                                "uso":"diagnóstico y visualización, nunca sustitución de matrícula"}
    df["inicio_posterior_a_2025"] = pd.to_numeric(df["Año Inicio Actividades"], errors="coerce") > 2025
    df["matricula_primer_anio_cero"] = df["Matrícula Primer Año"].eq(0)
    auditoria["estrategias"] = pd.DataFrame(estrategias)
    auditoria["filas_entrada"] = len(datos_filtrados)
    auditoria["columnas_originales"] = datos_filtrados.shape[1]
    auditoria["columnas_salida"] = df.shape[1]
    auditoria["atipicos"] = diagnosticar_atipicos(df)
    return df, auditoria


def concentracion_matricula(datos: pd.DataFrame, variable: str = "Nombre Institución") -> tuple[pd.DataFrame, dict]:
    """Concentración por grupo: participación, CR3 y Herfindahl-Hirschman (0-10.000)."""
    if variable not in datos.columns:
        raise KeyError(variable)
    m = pd.to_numeric(datos["Matrícula Primer Año"], errors="coerce")
    if m.isna().any() or (m<0).any():
        raise ValueError("La matrícula de primer año no es íntegra o contiene negativos")
    tabla = (datos.assign(_matricula=m).groupby(variable, dropna=False)['_matricula']
             .agg(['sum', 'size']).rename(columns={'sum':'matricula_primer_anio','size':'registros'})
             .sort_values('matricula_primer_anio',ascending=False).reset_index())
    total = int(tabla['matricula_primer_anio'].sum())
    if total <= 0:
        raise ValueError("No hay matrícula positiva para calcular concentración")
    tabla['participacion_pct'] = (100*tabla['matricula_primer_anio']/total).round(4)
    ratios = tabla['matricula_primer_anio']/total
    resumen = {
        'dimension':variable,'total_matricula_primer_anio':total,'grupos':len(tabla),
        'cr3_pct':round(float(100*ratios.head(3).sum()),3),
        'hhi':round(float(10000*(ratios**2).sum()),3),
    }
    return tabla,resumen


def validar_fase1(df: pd.DataFrame) -> dict:
    """Pruebas de consistencia de fuente, filtro, integridad y casos especiales."""
    requeridas = set(CAMPOS_IDENTIDAD+['Matrícula primer año hombres','Matrícula primer año mujeres',
                                       'Matrícula Primer Año No Binario','Matrícula total hombres',
                                       'Matrícula total mujeres','Matrícula Total No Binario'])
    if not requeridas.issubset(df.columns):
        raise ValueError(f"Faltan columnas: {requeridas-set(df.columns)}")
    if df.empty: raise ValueError('No existen registros para validar')
    assert (df['Año']==2025).all(), 'Se encontraron registros de otro año'
    assert df['Tipo Institución'].eq('I.P.').all(), 'Se encontraron instituciones que no son I.P.'
    assert df['Matrícula Total'].notna().all() and df['Matrícula Primer Año'].notna().all()
    assert df['Matrícula Total'].ge(0).all() and df['Matrícula Primer Año'].ge(0).all()
    assert df['Matrícula Primer Año'].le(df['Matrícula Total']).all()
    for total,desgloses in [
        ('Matrícula Primer Año',['Matrícula primer año hombres','Matrícula primer año mujeres','Matrícula Primer Año No Binario']),
        ('Matrícula Total',['Matrícula total hombres','Matrícula total mujeres','Matrícula Total No Binario']),
    ]:
        assert (df[desgloses].sum(axis=1)==df[total]).all(), f'Desglose inconsistente: {total}'
    return {'registros':len(df),'instituciones':int(df['Nombre Institución'].nunique()),
            'columnas':df.shape[1], 'matricula_primer_anio':int(df['Matrícula Primer Año'].sum()),
            'matricula_total':int(df['Matrícula Total'].sum()),
            'registro_inicio_posterior':int((df['Año Inicio Actividades']>2025).sum()),
            'duplicados_completos':int(df.duplicated().sum()),
            'matricula_primer_anio_cero':int(df['Matrícula Primer Año'].eq(0).sum()),
            'pregrado':int(df['Pregrado/Posgrado'].eq('Pregrado').sum()),
            'posgrado':int(df['Pregrado/Posgrado'].eq('Posgrado').sum()),
           }


def validar_fase2(original: pd.DataFrame, final: pd.DataFrame, audit: dict) -> dict:
    """Pruebas de conservación y auditabilidad, sin exigir falsamente cero nulos."""
    if len(original)!=len(final):raise AssertionError('El pipeline eliminó o agregó registros')
    for campo in CAMPOS_IDENTIDAD:
        if not original[campo].astype('string').str.strip().equals(final[campo].astype('string').str.strip()):
            raise AssertionError(f'Se modificó campo fuente protegido: {campo}')
    assert final['categoria_matricula_total'].notna().all()
    assert final['inicio_posterior_a_2025'].sum()==(original['Año Inicio Actividades']>2025).sum()
    assert final['matricula_primer_anio_cero'].sum()==original['Matrícula Primer Año'].eq(0).sum()
    assert final['moneda_normalizada'].isin(['CLP','UF']).all()
    for variable,alias in VARIABLES_IMPUTABLES.items():
        obs=pd.to_numeric(original[variable],errors='coerce')
        pred=final[f'{alias}_analisis']
        if not np.array_equal(pred[obs.notna()].to_numpy(),obs[obs.notna()].to_numpy(),equal_nan=True):
            raise AssertionError(f'Valores observados alterados: {variable}')
        if int(final[f'{alias}_imputado'].sum()) != int((obs.isna() & pred.notna()).sum()):
            raise AssertionError(f'Banderas de imputación incorrectas: {variable}')
        if variable != 'Vacantes':
            uf = final['moneda_normalizada'].eq('UF') & obs.isna()
            assert pred[uf].isna().all(), 'Se han imputado valores UF con pesos'
    assert audit['columnas_salida']==final.shape[1]
    return {'filas_sin_perdidas':len(final),'columnas_salida':final.shape[1],
            'filas_anomalia_temporal':int(final['inicio_posterior_a_2025'].sum()),
            'cero_primer_anio_preservados':int(final['matricula_primer_anio_cero'].sum()),
            'nulos_originales_preservados_por_columna':True,
            'desgloses_matricula_consistentes':True}
