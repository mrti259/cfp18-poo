import mysql.connector
from modulos.dbconf import *

queries = {
    "select_usuarios":"SELECT * FROM usuario",
    "select_productos":"SELECT * FROM producto",
    "select_compras":"SELECT * FROM compra",
    "select_datos_login":"SELECT clave, usuario_id FROM usuario WHERE email = %s",
    "select_datos_usuario":"SELECT * FROM usuario WHERE usuario_id = %s",
    "select_categoria_id":"SELECT categoria_id FROM categoria WHERE nombre = %s",
    "select_marca_id":"SELECT marca_id FROM marca WHERE nombre = %s",
    "update_producto_nombre":"UPDATE producto SET nombre = %s, fecha_de_ultima_modificacion = %s WHERE producto_id = %s",
    "update_producto_descripcion":"UPDATE producto SET descripcion = %s, fecha_de_ultima_modificacion = %s WHERE producto_id = %s",
    "update_producto_precio":"UPDATE producto SET precio = %s, fecha_de_ultima_modificacion = %s WHERE producto_id = %s",
    "update_usuario_email":"UPDATE usuario SET email = %s WHERE usuario_id = %s",
    "update_usuario_clave":"UPDATE usuario SET clave = %s WHERE usuario_id = %s",
    "update_usuario_telefono":"UPDATE usuario SET telefono = %s WHERE usuario_id = %s",
    "update_usuario_direccion_id":"UPDATE usuario SET direccion_id = %s WHERE usuario_id = %s",
    "insert_producto":"INSERT INTO producto(nombre, descripcion, precio, categoria_id, marca_id, fecha_de_publicacion, fecha_de_ultima_modificacion) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    "insert_usuario":"INSERT INTO usuario(dni, nombre, apellido, fecha_de_nacimiento, email, clave, telefono, fecha_de_registro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    "insert_compra":"INSERT INTO compra(usuario_id, direccion_id, producto_id, cantidad, precio_total, fecha_de_compra) VALUES (%s, %s, %s, %s, %s, %s)",
    "delete_producto":"DELETE FROM producto WHERE producto_id = %s",
    "delete_usuario":"DELETE FROM usuario WHERE usuario_id = %s",
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

    def datos_de_usuario_id(self, usuario_id):
        val = (usuario_id,)
        self.cursor.execute(queries["select_datos_usuario"], val)
        return self.cursor.fetchone()

    def datos_login(self, email):
        val = (email,)
        self.cursor.execute(queries["select_datos_login"], val)
        return self.cursor.fetchone()

    def id_de_categoria(self, categoria_nombre):
        val = (categoria_nombre,)
        self.cursor.execute(queries["select_categoria_id"], val)
        categoria_id = self.cursor.fetchone()
        if not categoria_id:
            categoria_id = 0
        return categoria_id

    def id_de_marca(self, marca_nombre):
        val = (marca_nombre,)
        self.cursor.execute(queries["select_marca_id"], val)
        marca_id = self.cursor.fetchone()
        if not marca_id:
            marca_id = 0
        return marca_id

    def registrar_usuario(self, usuario):
        val = (usuario.get_dni(), usuario.get_nombre(), usuario.get_apellido(), usuario.get_fecha_de_nacimiento(), usuario.get_email(), usuario.get_clave(), usuario.get_telefono(), usuario.get_fecha_de_registro())
        self.cursor.execute(queries["insert_usuario"], val)
        self.conexion.commit()
        usuario.set_usuario_id(self.cursor.lastrowid)

    def registrar_producto(self, producto):
        val = (producto.get_nombre(), producto.get_descripcion(), producto.get_precio(), producto.get_categoria_id(), producto.get_marca_id(), producto.get_fecha_de_publicacion(), producto.get_fecha_de_ultima_modificacion())
        self.cursor.execute(queries["insert_producto"], val)
        self.conexion.commit()
        producto.set_producto_id(self.cursor.lastrowid)

    def registrar_compra(self, compra):
        val = (compra.get_usuario_id(), compra.get_direccion_id(), compra.get_producto_id(), compra.get_cantidad(), compra.get_precio_total(), compra.get_fecha_de_compra())
        self.cursor.execute(queries["insert_compra"], val)
        self.conexion.commit()
        compra.set_compra_id(self.cursor.lastrowid)

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
