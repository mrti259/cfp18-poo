from .validador import Validador

class Producto:
    def __init__(self, producto_id=0, nombre=" ", descripcion=" ", precio=0, stock=0, categoria_id=0, marca_id=0, fecha_de_publicacion="", fecha_de_ultima_modificacion=""):
        '''Inicializa un producto con sus datos'''
        self.validador = Validador()
        self.set_producto_id(producto_id)
        self.set_nombre(nombre)
        self.set_descripcion(descripcion)
        self.set_precio(precio)
        self.set_stock(stock)
        self.set_categoria_id(categoria_id)
        self.set_marca_id(marca_id)
        self.set_fecha_de_publicacion(fecha_de_publicacion)
        self.set_fecha_de_ultima_modificacion(fecha_de_ultima_modificacion)


    def __str__(self):
        '''Da formato al objeto para ser pasado como cadena'''
        return (f"{self.get_producto_id()}. {self.get_nombre()} ({self.get_precio()})")


    def ficha_producto(self):
        '''Da formato al objeto para pasarlo como una ficha más informativa'''
        return (f"""\
Producto:
=========
Nombre: {self.get_nombre()}
Descripcion: {self.get_descripcion()}
Precio: {self.get_precio()}
Stock: {self.get_stock()}
Categoria: {self.get_categoria_id()}
Marca: {self.get_marca_id()}
Fecha de publicacion: {self.get_fecha_de_publicacion()}
Fecha de ultima modificacion: {self.get_fecha_de_ultima_modificacion()}
""")


    def set_producto_id(self, producto_id):
        self.producto_id = producto_id
        return 1

    def get_producto_id(self):
        return self.producto_id


    def set_nombre(self, nombre):
        if self.validador.nombre_es_valido(nombre):
            self.nombre = nombre.title()
            return 1

    def get_nombre(self):
        return self.nombre


    def set_descripcion(self, descripcion):
        self.descripcion = descripcion.capitalize()
        return 1

    def get_descripcion(self):
        return self.descripcion


    def set_stock(self, stock):
        if self.validador.stock_es_valido(stock):
            self.stock = stock
            return 1

    def incr_stock(self, incr):
        self.stock += incr
        return 1

    def decr_stock(self, decr):
        self.stock -= decr
        return 1

    def get_stock(self):
        return self.stock


    def set_categoria_id(self, categoria_id):
        self.categoria_id = categoria_id
        return 1

    def get_categoria_id(self):
        return self.categoria_id


    def set_marca_id(self, marca_id):
        self.marca_id = marca_id
        return 1

    def get_marca_id(self):
        return self.marca_id


    def set_precio(self, precio):
        if self.validador.precio_es_valido(precio):
            self.precio = precio
            return 1

    def get_precio(self):
        return self.precio


    def set_fecha_de_publicacion(self, fecha_de_publicacion):
        self.fecha_de_publicacion = fecha_de_publicacion
        return 1

    def get_fecha_de_publicacion(self):
        return self.fecha_de_publicacion


    def set_fecha_de_ultima_modificacion(self, fecha_de_ultima_modificacion):
        self.fecha_de_ultima_modificacion = fecha_de_ultima_modificacion
        return 1

    def get_fecha_de_ultima_modificacion(self):
        return self.fecha_de_ultima_modificacion
