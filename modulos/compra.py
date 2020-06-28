class Compra:
    def __init__(self, compra_id, usuario_id, direccion_id, producto_id, cantidad, precio_total, fecha_de_compra):
        self.compra_id = compra_id
        self.usuario_id = usuario_id
        self.direccion_id = direccion_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.precio_total = precio_total
        self.fecha_de_compra = fecha_de_compra
        self.usuario = None
        self.producto = None
        

    def __str__(self):
        return (f"{self.producto.get_nombre()}  Cant: {self.get_cantidad()}  Precio: {self.get_precio_total()}")



    def set_compra_id(self, compra_id):
        self.compra_id = compra_id
        return 1

    def get_compra_id(compra_id):
        return self.compra_id



    def set_usuario_id(self, usuario_id):
        self.usuario_id = usuario_id
        return 1

    def get_usuario_id(self):
        return self.usuario_id



    def set_direccion_id(self, direccion_id):
        self.direccion_id = direccion_id
        return 1

    def get_direccion_id(self):
        return self.direccion_id



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



    def set_precio_total(self, precio_total):
        self.precio_total = precio_total
        return 1

    def get_precio_total(self):
        return self.precio_total



    def set_fecha_de_compra(self, fecha_de_compra):
        self.fecha_de_compra = fecha_de_compra
        return 1

    def get_fecha_de_compra(self):
        return self.fecha_de_compra



    def set_producto(self, producto):
        self.producto = producto
        return 1

    def get_producto(self):
        return self.producto
