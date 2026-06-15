import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

ARCHIVOS = {
    "usuarios": DATA_DIR / "usuarios.json",
    "items": DATA_DIR / "items.json",
    "prestamos": DATA_DIR / "prestamos.json",
    "devoluciones": DATA_DIR / "devoluciones.json",
    "ventas": DATA_DIR / "ventas.json",
    "auditoria": DATA_DIR / "auditoria.json",
    "admins": DATA_DIR / "admins.json",
}


def inicializar_archivos():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for clave, ruta in ARCHIVOS.items():
        if not ruta.exists():
            if clave == "admins":
                guardar_json(clave, [{"usuario": "admin", "contrasena": "1234"}])
            else:
                guardar_json(clave, [])


def cargar_json(clave):
    ruta = ARCHIVOS[clave]
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_json(clave, datos):
    ruta = ARCHIVOS[clave]
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)
