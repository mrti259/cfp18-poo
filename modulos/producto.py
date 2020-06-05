class Producto:
    def __init__(self, producto_id, nombre, descripcion, precio, stock, categoria_id, marca_id, fecha_de_publicacion, fecha_de_ultima_modificacion):
        self.set_producto_id(producto_id)
        self.set_nombre(nombre)
        self.set_descripcion(descripcion)
        self.set_precio(precio)
        self.set_stock(stock)
        self.set_categoria_id(categoria_id)
        self.set_marca_id(marca_id)
        self.set_fecha_de_publicacion(fecha_de_publicacion)
        self.set_fecha_de_ultima_modificacion(fecha_de_ultima_modificacion)

    def set_producto_id(self, producto_id):
        self.producto_id = producto_id
    def get_producto_id(self):
        return self.producto_id

    def set_nombre(self, nombre):
        self.nombre = nombre.title()
    def get_nombre(self):
        return self.nombre

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion.capitalize()
    def get_descripcion(self):
        return self.descripcion

    def set_stock(self, stock):
        self.stock = stock
    def incr_stock(self, incr):
        self.stock += incr
    def decr_stock(self, decr):
        self.stock -= decr
    def get_stock(self):
        return self.stock

    def set_categoria_id(self, categoria_id):
        self.categoria_id = categoria_id
    def get_categoria_id(self):
        return self.categoria_id

    def set_marca_id(self, marca_id):
        self.marca_id = marca_id
    def get_marca_id(self):
        return self.marca_id

    def set_precio(self, precio):
        self.precio = precio
    def get_precio(self):
        return self.precio

    def set_fecha_de_publicacion(self, fecha_de_publicacion):
        self.fecha_de_publicacion = fecha_de_publicacion
    def get_fecha_de_publicacion(self):
        return self.fecha_de_publicacion

    def set_fecha_de_ultima_modificacion(self, fecha_de_ultima_modificacion):
        self.fecha_de_ultima_modificacion = fecha_de_ultima_modificacion
    def get_fecha_de_ultima_modificacion(self):
        return self.fecha_de_ultima_modificacion
