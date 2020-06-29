import mysql.connector
from .queries import queries
from .pais import Pais
from .provincia import Provincia
from .ciudad import Ciudad
from .direccion import Direccion
from .categoria import Categoria
from .marca import Marca
from .producto import Producto
from .usuario import Usuario
from .compra import Compra
from .carrito import Carrito



class Ecommerce_db:
    def __init__(self, dbconf):
        self.conexion = mysql.connector.connect(**dbconf)
        self.cursor = self.conexion.cursor()


    def total_usuarios(self):
        self.cursor.execute(queries["total_usuarios"])
        return self.cursor.fetchone()[0]


    def total_ventas(self):
        self.cursor.execute(queries["total_ventas"])
        return self.cursor.fetchone()[0]


    def total_ingresos(self):
        self.cursor.execute(queries["total_ingresos"])
        return self.cursor.fetchone()[0]



    def get_todos_los_paises(self):
        self.cursor.execute(queries["select_paises"])
        paises = [Pais(*datos) for datos in self.cursor.fetchall()]
        return paises



    def get_todas_las_categorias(self):
        self.cursor.execute(queries["select_categorias"])
        categorias = [Categoria(*datos) for datos in self.cursor.fetchall()]
        return categorias



    def get_todas_las_marcas(self):
        self.cursor.execute(queries["select_marcas"])
        marcas = [Marca(*datos) for datos in self.cursor.fetchall()]
        return marcas



    def get_todos_los_productos(self):
        self.cursor.execute(queries["select_productos"])
        productos = [Producto(*datos) for datos in self.cursor.fetchall()]
        return productos



    def get_todos_los_usuarios(self):
        self.cursor.execute(queries["select_usuarios"])
        usuarios = [Usuario(*datos) for datos in self.cursor.fetchall()]
        return usuarios



    def get_provincias_segun_pais(self, pais):
        val = (pais.get_pais_id(),)
        self.cursor.execute(queries["select_provincias_segun_pais"], val)
        provincias = [Provincia(*datos) for datos in self.cursor.fetchall()]
        for res in provincias:
            res.set_pais(pais)
        return provincias



    def get_ciudades_segun_provincia(self, provincia):
        val = (provincia.get_provincia_id(),)
        self.cursor.execute(queries["select_ciudades_segun_provincia"], val)
        ciudades = [Ciudad(*datos) for datos in self.cursor.fetchall()]
        for res in ciudades:
            res.set_provincia(provincia)
        return ciudades



    def get_ciudad_segun_id(self, ciudad_id):
        val = (ciudad_id,)
        self.cursor.execute(queries["select_ciudad_segun_id"], val)
        ciudad = Ciudad(*self.cursor.fetchone())
        ciudad.set_provincia(self.get_provincia_segun_id(ciudad.get_provincia_id()))
        return ciudad



    def get_provincia_segun_id(self, provincia_id):
        val = (provincia_id,)
        self.cursor.execute(queries["select_provincia_segun_id"], val)
        provincia = Provincia(*self.cursor.fetchone())
        provincia.set_pais(self.get_pais_segun_id(provincia.get_pais_id()))
        return provincia



    def get_pais_segun_id(self, pais_id):
        val = (pais_id,)
        self.cursor.execute(queries["select_pais_segun_id"], val)
        pais = Pais(*self.cursor.fetchone())
        return pais



    def get_direccion_segun_id(self, direccion_id):
        val = (direccion_id,)
        self.cursor.execute(queries["select_direccion_segun_id"], val)
        direccion = Direccion(*self.cursor.fetchone())
        direccion.set_ciudad(self.get_ciudad_segun_id(direccion.get_ciudad_id()))
        return direccion



    def get_categoria_segun_id(self, categoria_id):
        val = (categoria_id,)
        self.cursor.execute(queries["select_categoria_segun_id"], val)
        categoria = Categoria(*self.cursor.fetchone())
        return categoria



    def get_marca_segun_id(self, marca_id):
        val = (marca_id,)
        self.cursor.execute(queries["select_marca_segun_id"], val)
        marca = Marca(*self.cursor.fetchone())
        return marca



    def get_productos_segun_nombre(self, producto_nombre):
        val = (producto_nombre,)
        self.cursor.execute(queries["select_productos_segun_nombre"], val)
        productos = [Producto(*datos) for datos in self.cursor.fetchall()]
        return productos



    def get_producto_segun_id(self, producto_id):
        val = (producto_id,)
        self.cursor.execute(queries["select_producto_segun_id"], val)
        producto = Producto(*self.cursor.fetchone())
        producto.set_categoria(self.get_categoria_segun_id(producto.get_categoria_id()))
        producto.set_marca(self.get_marca_segun_id(producto.get_marca_id()))
        return producto



    def get_usuario_segun_id(self, usuario_id):
        val = (usuario_id,)
        self.cursor.execute(queries["select_usuario_segun_id"], val)
        usuario = Usuario(*self.cursor.fetchone())
        usuario.set_direccion(self.get_direccion_segun_id(usuario.get_direccion_id()))
        return usuario



    def get_login_usuario(self, email):
        val = (email,)
        self.cursor.execute(queries["select_login_segun_email"], val)
        resultado = self.cursor.fetchone()
        return resultado



    def get_compras_segun_usuario(self, usuario):
        val = (usuario.get_usuario_id(),)
        self.cursor.execute(queries["select_compras_segun_usuario_id"], val)
        compras = [Compra(*datos) for datos in self.cursor.fetchall()]
        for res in compras:
            res.set_producto(self.get_producto_segun_id(res.get_producto_id()))
        return compras



    def get_carrito_segun_usuario(self, usuario):
        val = (usuario.get_usuario_id(),)
        self.cursor.execute(queries["select_carrito_segun_usuario"], val)
        carrito = [Carrito(*datos) for datos in self.cursor.fetchall()]
        for res in carrito:
            res.set_producto(self.get_producto_segun_id(res.get_producto_id()))
        return carrito



    def registrar_producto(self, producto):
        val = (producto.get_nombre(), producto.get_descripcion(), producto.get_precio(), producto.get_stock(), producto.get_categoria_id(), producto.get_marca_id(), producto.get_fecha_de_publicacion(), producto.get_fecha_de_ultima_modificacion())
        self.cursor.execute(queries["insert_producto"], val)
        self.conexion.commit()
        producto.set_producto_id(self.cursor.lastrowid)



    def registrar_usuario(self, usuario):
        val = (usuario.get_email(), usuario.get_clave(), usuario.get_nombre(), usuario.get_apellido(), usuario.get_fecha_de_nacimiento(), usuario.get_dni(), usuario.get_telefono(), usuario.get_direccion_id(), usuario.get_fecha_de_registro())
        self.cursor.execute(queries["insert_usuario"], val)
        self.conexion.commit()
        usuario.set_usuario_id(self.cursor.lastrowid)



    def registrar_compra(self, compra):
        val = (compra.get_usuario_id(), compra.get_direccion_id(), compra.get_producto_id(), compra.get_cantidad(), compra.get_precio_total(), compra.get_fecha_de_compra())
        self.cursor.execute(queries["insert_compra"], val)
        self.conexion.commit()
        compra.set_compra_id(self.cursor.lastrowid)



    def registrar_carrito(self, carrito):
        val = (carrito.get_usuario_id(), carrito.get_producto_id(), carrito.get_cantidad())
        self.cursor.execute(queries["insert_carrito"], val)
        self.conexion.commit()
        carrito.set_carrito_id(self.cursor.lastrowid)



    def registrar_direccion(self, direccion):
        val = (direccion.get_calle(), direccion.get_altura(), direccion.get_codigo_postal(), direccion.get_ciudad_id())
        self.cursor.execute(queries["insert_direccion"], val)
        self.conexion.commit()
        direccion.set_direccion_id(self.cursor.lastrowid)



    def eliminar_producto(self, producto):
        val = (producto.get_producto_id(),)
        self.cursor.execute(queries["delete_compras_de_producto"], val)
        self.cursor.execute(queries["delete_producto"], val)
        self.conexion.commit()



    def eliminar_usuario(self, usuario):
        val = (usuario.get_usuario_id(),)
        self.cursor.execute(queries["delete_carrito_de_usuario"], val)
        self.cursor.execute(queries["delete_compras_de_usuario"], val)
        self.cursor.execute(queries["delete_usuario"], val)
        self.conexion.commit()



    def eliminar_carrito(self, carrito):
        val = (carrito.get_carrito_id(),)
        self.cursor.execute(queries["delete_carrito"], val)
        self.conexion.commit()



    def actualizar_producto_nombre(self, producto):
        val = (producto.get_nombre(), producto.get_fecha_de_ultima_modificacion(), producto.get_producto_id())
        self.cursor.execute(queries["update_producto_nombre"], val)
        self.conexion.commit()



    def actualizar_producto_descripcion(self, producto):
        val = (producto.get_descripcion(), producto.get_fecha_de_ultima_modificacion(), producto.get_producto_id())
        self.cursor.execute(queries["update_producto_descripcion"], val)
        self.conexion.commit()



    def actualizar_producto_precio(self, precio):
        val = (producto.get_precio(), producto.get_fecha_de_ultima_modificacion(), producto.get_producto_id())
        self.cursor.execute(queries["update_producto_precio"], val)
        self.conexion.commit()



    def actualizar_producto_stock(self, producto):
        val = (producto.get_stock(), producto.get_producto_id())
        self.cursor.execute(queries["update_producto_stock"], val)
        self.conexion.commit()



    def actualizar_usuario_nombre(self, usuario):
        val = (usuario.get_nombre(), usuario.get_usuario_id())
        self.cursor.execute(queries["update_usuario_nombre"], val)
        self.conexion.commit()



    def actualizar_usuario_apellido(self, usuario):
        val = (usuario.get_apellido(), usuario.get_usuario_id())
        self.cursor.execute(queries["update_usuario_apellido"], val)
        self.conexion.commit()



    def actualizar_usuario_direccion_id(self, usuario):
        val = (usuario.get_direccion_id(), usuario.get_usuario_id())
        self.cursor.execute(queries["update_usuario_direccion_id"], val)
        self.conexion.commit()



    def actualizar_usuario_email(self, usuario):
        val = (usuario.get_email(), usuario.get_usuario_id())
        self.cursor.execute(queries["update_usuario_email"], val)
        self.conexion.commit()



    def actualizar_usuario_clave(self, usuario):
        val = (usuario.get_clave(), usuario.get_usuario_id())
        self.cursor.execute(queries["update_usuario_clave"], val)
        self.conexion.commit()



    def actualizar_usuario_dni(self, usuario):
        val = (usuario.get_dni(), usuario.get_usuario_id())
        self.cursor.execute(queries["update_usuario_dni"], val)
        self.conexion.commit()



    def actualizar_usuario_telefono(self, usuario):
        val = (usuario.get_telefono(), usuario.get_usuario_id())
        self.cursor.execute(queries["update_usuario_telefono"], val)
        self.conexion.commit()



    def actualizar_carrito_cantidad(self, carrito):
        val = (carrito.get_cantidad(), carrito.get_cantidad())
        self.cursor.execute(queries["update_carrito_cantidad"], val)
        self.conexion.commit()


