class Compra:
    def __init__(self, compra_id, usuario_id, direccion_id, producto_id, cantidad, precio_total, fecha_de_compra):
        self.errores = {}
        self.set_compra_id(compra_id)
        self.set_usuario_id(usuario_id)
        self.set_direccion_id(direccion_id)
        self.set_producto_id(producto_id)
        self.set_cantidad(cantidad)
        self.set_precio_total(precio_total)
        self.set_fecha_de_compra(fecha_de_compra)

    def set_compra_id(self, compra_id):
        self.compra_id = compra_id
    def get_compra_id(compra_id):
        return self.compra_id

    def set_usuario_id(self, usuario_id):
        self.usuario_id = usuario_id
    def get_usuario_id(self):
        return self.usuario_id

    def set_direccion_id(self, direccion_id):
        self.direccion_id = direccion_id
    def get_direccion_id(self):
        return self.direcicon_id

    def set_producto_id(self, producto_id):
        self.producto_id(producto_id)
    def get_producto_id(self):
        return self.producto_id

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    def get_cantidad(self):
        return self.cantidad

    def set_precio_total(self, precio_total):
        self.precio_total = precio_total
    def get_precio_total(self):
        return self.precio_total

    def set_fecha_de_compra(self, fecha_de_compra):
        self.fecha_de_compra = fecha_de_compra
    def get_fecha_de_compra(self):
        return self.fecha_de_compra

    def get_errores(self):
        return [msg for msg in self.errores.values()]
