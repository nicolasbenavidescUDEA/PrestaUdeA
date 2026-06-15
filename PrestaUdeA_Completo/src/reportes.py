import csv
from pathlib import Path
from persistencia import cargar_json
from utilidades import texto_a_fecha, dias_transcurridos

BASE_DIR = Path(__file__).resolve().parent.parent
REPORTES_DIR = BASE_DIR / "reportes_csv"


def exportar_csv(nombre_archivo, datos):
    REPORTES_DIR.mkdir(parents=True, exist_ok=True)
    ruta = REPORTES_DIR / nombre_archivo
    if not datos:
        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            archivo.write("Sin datos\n")
        return ruta

    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=datos[0].keys())
        writer.writeheader()
        writer.writerows(datos)
    return ruta


def generar_reporte_prestamos_ordenados():
    prestamos = cargar_json("prestamos")
    activos = [p for p in prestamos if p["estado"] == "activo"]
    for p in activos:
        p["dias_prestado"] = dias_transcurridos(texto_a_fecha(p["fecha_salida"]))
    activos.sort(key=lambda x: x["dias_prestado"], reverse=True)
    return exportar_csv("prestamos_ordenados.csv", activos)
