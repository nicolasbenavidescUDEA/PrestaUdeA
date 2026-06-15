class clsUsuarios:
    def __init__(self, nombre, apellido, documento, correo, tiempo_prestamo, activo=True):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.correo = correo
        self.tiempo_prestamo = tiempo_prestamo
        self.activo = activo

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "documento": self.documento,
            "correo": self.correo,
            "tiempo_prestamo": self.tiempo_prestamo,
            "activo": self.activo,
        }
