class Item:
    def __init__(self, item_id, nombre, categoria, precio_compra, estado, disponible=True):
        self.item_id = item_id
        self.nombre = nombre
        self.categoria = categoria
        self.precio_compra = precio_compra
        self.estado = estado
        self.disponible = disponible

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio_compra": self.precio_compra,
            "estado": self.estado,
            "disponible": self.disponible,
        }
