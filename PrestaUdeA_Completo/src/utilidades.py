from datetime import datetime, timedelta

PREFIJOS = {
    "Videojuegos": "VID",
    "Libros": "LIB",
    "Música y video": "MUS",
    "Herramientas": "HER",
    "Dinero": "DIN",
    "Misceláneo y varios": "MIS",
}


def generar_id_item(categoria, consecutivo):
    return f"{PREFIJOS[categoria]}-{consecutivo:03d}"


def generar_id_prestamo(consecutivo):
    return f"PRE-{consecutivo:04d}"


def fecha_hoy():
    return datetime.now().date()


def sumar_dias(fecha, dias):
    return fecha + timedelta(days=dias)


def dias_transcurridos(fecha_inicio):
    return (fecha_hoy() - fecha_inicio).days


def fecha_a_texto(fecha):
    return fecha.strftime("%Y-%m-%d")


def texto_a_fecha(texto):
    return datetime.strptime(texto, "%Y-%m-%d").date()
