class Carrito:
    def __init__(self, carrito_id, usuario_id, producto_id, cantidad):
        self.set_carrito_id(carrito_id)
        self.set_usuario_id(usuario_id)
        self.set_producto_id(producto_id)
        self.set_cantidad(cantidad)

    def set_carrito_id(self, carrito_id):
        self.carrito_id = carrito_id
        return 1
    def get_carrito_id(self):
        return self.carrito_id

    def set_usuario_id(self, usuario_id):
        self.usuario_id = usuario_id
        return 1
    def get_usuario_id(self):
        return self.usuario_id

    def set_producto_id(self, producto_id):
        self.producto_id = producto_id
        return 1
    def get_producto_id(self):
        return self.producto_id

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
        return 1        
    def get_cantidad(self):
        return self.cantidad
