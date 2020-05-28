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
        self.errores = {}

    def set_producto_id(self, producto_id):
        self.producto_id = producto_id
    def get_producto_id(self):
        return self.producto_id

    def set_nombre(self, nombre):
        if nombre.isalnum():
            self.nombre = nombre.title()
        else:
            self.errores["nombre"] = "El nombre no es válido"
    def get_nombre(self):
        return self.nombre

    def set_descripcion(self, descripcion):
        if descripcion.isalnum():
            self.descripcion = descripcion.capitalize()
        else:
            self.errores["descripcion"] = "La descripcion no es válida"
    def get_descripcion(self):
        return self.descripcion

    def set_stock(self, stock):
        if stock.isdigit() and int(stock) > 0:
            self.stock = int(stock)
        else:
            self.errores["stock"] = "El stock no es válido"
    def incr_stock(self, incr):
        if incr.isdigit() and int(incr) >= stock:
            self.stock += int(incr)
        else:
            self.errores["stock"] = "No es una cantidad válida"
    def decr_stock(self, decr):
        if incr.isdigit():
            self.stock -= int(decr)
        else:
            self.errores["stock"] = "No es una cantidad válida"
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
        try:
            if precio > 0:
                self.precio = float(precio)
            else:
                self.errores["precio"] = "El precio no es válido"
        except:
            self.errores["precio"] = "El precio no es válido"
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

    def get_errores(self):
        return [msg for msg in self.errores.values()]
