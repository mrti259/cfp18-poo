class Carrito:
    def __init__(self, carrito_id, usuario_id, producto_id, cantidad):
        self.set_carrito_id(carrito_id)
        self.set_usuario_id(usuario_id)
        self.set_producto(producto_id)
        self.set_cantidad(cantidad)

    def get_carrito_id(self):
        return self.carrito_id

    def get_usuario_id(self):
        return self.usuario_id

    def get_producto_id(self):
        return self.producto_id

    def get_cantidad(self):
        return self.cantidad

    def set_carrito_id(self, carrito_id):
        self.carrito_id = carrito_id

    def set_usuario_id(self, usuario_id):
        self.usuario_id = usuario_id

    def set_producto_id(self, producto_id):
        self.producto_id = producto_id

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad