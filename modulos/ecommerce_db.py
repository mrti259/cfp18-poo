import mysql.connector
from modulos.dbconf import *

queries = {
    "select_usuarios":"SELECT * FROM usuario",
    "select_productos":"SELECT * FROM producto",
    "select_compras":"SELECT * FROM compra",
    "select_categorias":"SELECT * FROM categoria",
    "select_marcas":"SELECT * FROM marca",
    "select_datos_login":"SELECT clave, usuario_id FROM usuario WHERE email = %s",
    "select_datos_usuario":"SELECT * FROM usuario WHERE usuario_id = %s",
    "select_categoria_id":"SELECT categoria_id FROM categoria WHERE nombre = %s",
    "select_marca_id":"SELECT marca_id FROM marca WHERE nombre = %s",
    "select_productos_nombre":"SELECT * FROM producto WHERE nombre = %s",
    "select_pais_id":"SELECT pais_id FROM pais WHERE nombre = %s",
    "select_provincia_id":"SELECT provincia_id FROM provincia WHERE nombre = %s AND pais_id %s",
    "select_ciudad_id":"SELECT ciudad_id FROM ciudad WHERE nombre = %s AND provincia_id = %s",
    "select_producto_precio":"SELECT precio FROM producto WHERE producto_id = %s",
    "update_producto_nombre":"UPDATE producto SET nombre = %s, fecha_de_ultima_modificacion = %s WHERE producto_id = %s",
    "update_producto_descripcion":"UPDATE producto SET descripcion = %s, fecha_de_ultima_modificacion = %s WHERE producto_id = %s",
    "update_producto_precio":"UPDATE producto SET precio = %s, fecha_de_ultima_modificacion = %s WHERE producto_id = %s",
    "update_usuario_email":"UPDATE usuario SET email = %s WHERE usuario_id = %s",
    "update_usuario_clave":"UPDATE usuario SET clave = %s WHERE usuario_id = %s",
    "update_usuario_telefono":"UPDATE usuario SET telefono = %s WHERE usuario_id = %s",
    "update_usuario_direccion_id":"UPDATE usuario SET direccion_id = %s WHERE usuario_id = %s",
    "update_direccion_calle_y_altura":"UPDATE direccion SET calle = %s, altura = %s WHERE direccion_id = %s",
    "update_direccion_codigo_postal":"UPDATE direccion SET codigo_posta = %s WHERE direccion_id = %s",
    "insert_producto":"INSERT INTO producto(nombre, descripcion, precio, stock, categoria_id, marca_id, fecha_de_publicacion, fecha_de_ultima_modificacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    "insert_usuario":"INSERT INTO usuario(dni, nombre, apellido, fecha_de_nacimiento, email, clave, telefono, fecha_de_registro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    "insert_compra":"INSERT INTO compra(usuario_id, direccion_id, producto_id, cantidad, precio_total, fecha_de_compra) VALUES (%s, %s, %s, %s, %s, %s)",
    "insert_direccion":"INSERT INTO direccion(calle, altura, codigo_postal, ciudad_id) VALUES (%s, %s, %s, %s)",
    "delete_producto":"DELETE FROM producto WHERE producto_id = %s",
    "delete_usuario":"DELETE FROM usuario WHERE usuario_id = %s",
    "delete_carrito":"DELETE FROM carrito WHERE carrito_id = %s",
    "delete_direccion":"DELETE FROM direccion WHERE direccion_id = %s",
}

class Ecommerce_db:
    def __init__(self, dbconf):
        self.conexion = mysql.connector.connect(**dbconf)
        self.cursor = self.conexion.cursor()

    def todos_los_usuarios(self):
        self.cursor.execute(queries["select_usuarios"])
        resultados = self.cursor.fetchall()
        return resultados

    def todos_los_productos(self):
        self.cursor.execute(queries["select_productos"])
        resultados = self.cursor.fetchall()
        return resultados

    def todas_las_compras(self):
        self.cursor.execute(queries["select_compras"])
        resultados = self.cursor.fetchall()
        return resultados

    def todas_las_categorias(self):
        self.cursor.execute(queries["select_categorias"])
        resultados = self.cursor.fetchall()
        return resultados

    def todas_las_marcas(self):
        self.cursor.execute(queries["select_marcas"])
        resultados=self.cursor.fetchall()
        return resultados

    def productos_por_nombre(self, producto_nombre):
        val = (producto_nombre,)
        self.cursor.execute(queries["select_productos_nombre"], val)
        resultados = self.cursor.fetchall()
        return resultados

    def datos_de_usuario_id(self, usuario_id):
        val = (usuario_id,)
        self.cursor.execute(queries["select_datos_usuario"], val)
        resultado = self.cursor.fetchone()
        return resultado

    def datos_login(self, email):
        val = (email,)
        self.cursor.execute(queries["select_datos_login"], val)
        resultado = self.cursor.fetchone()
        return resultado

    def id_de_categoria(self, categoria_nombre):
        val = (categoria_nombre,)
        self.cursor.execute(queries["select_categoria_id"], val)
        categoria_id = self.cursor.fetchone()
        if not categoria_id:
            categoria_id = (0,)
        return categoria_id[0]

    def id_de_marca(self, marca_nombre):
        val = (marca_nombre,)
        self.cursor.execute(queries["select_marca_id"], val)
        marca_id = self.cursor.fetchone()
        if not marca_id:
            marca_id = (0,)
        return marca_id[0]

    def id_de_pais(self, pais_nombre):
        val = (pais_nombre,)
        self.cursor.execute(queries["select_pais_id"], val)
        pais_id = self.cursor.fetchone()
        if not pais_id:
            pais_id = (0,)
        return pais_id[0]

    def id_de_provincia(self, provincia_nombre, pais_id):
        val = (provincia_nombre, pais_id)
        self.cursor.execute(queries["select_provincia_id"], val)
        provincia_id = self.cursor.fetchone()
        if not provincia_id:
            provincia_id = (0,)
        return provincia_id[0]

    def id_de_ciudad(self, ciudad_nombre, provincia_id):
        val = (ciudad_nombre, provincia_id)
        self.cursor.execute(queries["select_ciudad_id"], val)
        ciudad_id = self.cursor.fetchone()
        if not ciudad_id:
            ciudad_id = (0,)
        return ciudad_id[0]

    def precio_producto_id(self, producto):
        val = (producto.get_producto_id(),)
        self.cursor.execute(queries["select_producto_precio"], val)
        precio = self.cursor.fetchone()
        if not precio:
            precio = (-1,)
        return precio[0]

    def registrar_usuario(self, usuario):
        val = (usuario.get_dni(), usuario.get_nombre(), usuario.get_apellido(), usuario.get_fecha_de_nacimiento(), usuario.get_email(), usuario.get_clave(), usuario.get_telefono(), usuario.get_fecha_de_registro())
        self.cursor.execute(queries["insert_usuario"], val)
        self.conexion.commit()
        usuario.set_usuario_id(self.cursor.lastrowid)

    def registrar_producto(self, producto):
        val = (producto.get_nombre(), producto.get_descripcion(), producto.get_precio(), producto.get_stock(), producto.get_categoria_id(), producto.get_marca_id(), producto.get_fecha_de_publicacion(), producto.get_fecha_de_ultima_modificacion())
        self.cursor.execute(queries["insert_producto"], val)
        self.conexion.commit()
        producto.set_producto_id(self.cursor.lastrowid)

    def registrar_compra(self, compra):
        val = (compra.get_usuario_id(), compra.get_direccion_id(), compra.get_producto_id(), compra.get_cantidad(), compra.get_precio_total(), compra.get_fecha_de_compra())
        self.cursor.execute(queries["insert_compra"], val)
        self.conexion.commit()
        compra.set_compra_id(self.cursor.lastrowid)

    def registrar_direccion(self, direccion):
        val = (direccion.get_calle(), direccion.get_altura(), direccion.get_codigo_postal(), direccion.get_ciudad_id())
        self.cursor.execute(queries["insert_direccion"], val)
        self.conexion.commit()
        direccion.set_direccion_id(self.cursor.lastrowid)

    def eliminar_usuario(self, usuario):
        val = (usuario.get_id(),)
        self.cursor.execute(queries["delete_usuario"], val)
        self.conexion.commit()

    def eliminar_producto(self, usuario):
        val = (producto.get_id(),)
        self.cursor.execute(queries["delete_producto"], val)
        self.conexion.commit()

    def eliminar_compra(self, usuario):
        val = (compra.get_id(),)
        self.cursor.execute(queries["delete_compra"], val)
        self.conexion.commit()

    def actualizar_usuario_direccion_id(self, usuario):
        val = (usuario.get_direccion_id(), usuario.get_usuario_id())
        self.cursor.execute(queries["update_usuario_direccion"], val)
        self.conexion.commit()

    def actualizar_usuario_email(self, usuario):
        val = (usuario.get_email(), usuario.get_usuario_id())
        self.cursor.execute(queries["update_usuario_email"], val)
        self.conexion.commit()

    def actualizar_usuario_clave(self, usuario):
        val = (usuario.get_clave(), usuario.get_usuario_id())
        self.cursor.execute(queries["update_usuario_clave"], val)
        self.conexion.commit()

    def actualizar_usuario_telefono(self, usuario):
        val = (usuario.get_telefono(), usuario.get_usuario_id)
        self.cursor.execute(queries["update_usuario_telefono"], val)
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

    def actualizar_direccion_calle_y_altura(self, direccion):
        val = (direccion.get_calle(), direccion.get_altura(), direccion.get_id())
        self.cursor.execute(queries["update_direccion_calle_y_altura"], val)
        self.conexion.commit()

    def actualizar_direccion_codigo_postal(self, direccion):
        val = (direccion.get_codigo_postal(), direccion.get_direccion_id())
        self.cursor.execute(queries["update_direccin_codigo_postal"], val)
        self.conexion.commit()
