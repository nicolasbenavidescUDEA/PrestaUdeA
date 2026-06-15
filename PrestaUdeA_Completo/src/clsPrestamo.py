class clsPrestamo:
    def __init__(self, prestamo_id, documento_usuario, item_id, fecha_salida, fecha_devolucion_pactada, estado="activo"):
        self.prestamo_id = prestamo_id
        self.documento_usuario = documento_usuario
        self.item_id = item_id
        self.fecha_salida = fecha_salida
        self.fecha_devolucion_pactada = fecha_devolucion_pactada
        self.estado = estado

    def to_dict(self):
        return {
            "prestamo_id": self.prestamo_id,
            "documento_usuario": self.documento_usuario,
            "item_id": self.item_id,
            "fecha_salida": self.fecha_salida,
            "fecha_devolucion_pactada": self.fecha_devolucion_pactada,
            "estado": self.estado,
        }
