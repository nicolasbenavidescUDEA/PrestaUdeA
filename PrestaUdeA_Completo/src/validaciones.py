import re

CATEGORIAS_VALIDAS = [
    "Videojuegos",
    "Libros",
    "Música y video",
    "Herramientas",
    "Dinero",
    "Misceláneo y varios",
]

ESTADOS_DIFUSOS = ["Malo", "Regular", "Bueno", "Excelente"]


def validar_nombre_persona(texto):
    return len(texto.strip()) >= 3 and texto.replace(" ", "").isalpha()


def validar_nombre_item(texto):
    return len(texto.strip()) >= 3


def validar_documento(texto):
    return texto.isdigit() and 3 <= len(texto) <= 15


def validar_correo(texto):
    patron = r"^[^@\s]+@[^@\s]+\.com$"
    return re.match(patron, texto.strip().lower()) is not None


def validar_tiempo_prestamo(valor):
    return valor in [5, 10, 15, 30]


def validar_categoria(categoria):
    return categoria in CATEGORIAS_VALIDAS


def validar_precio(precio):
    return precio >= 0


def validar_estado_item(estado):
    return estado in ESTADOS_DIFUSOS
