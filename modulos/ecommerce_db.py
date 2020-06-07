import mysql.connector

queries = {
    "select_usuarios":"SELECT * FROM usuario",
    "select_compras":"SELECT * FROM compra",
    "select_productos":"SELECT * FROM producto",
    "select_categorias":"SELECT * FROM categoria",
    "select_marcas":"SELECT * FROM marca",
    "select_login_segun_email":"SELECT clave, usuario_id FROM usuario WHERE email = %s",
    "select_usuario_segun_id":"SELECT * FROM usuario WHERE usuario_id = %s",
    "select_carrito_segun_usuario":"SELECT * FROM carrito WHERE usuario_id = %s",
    "select_pais_id_segun_nombre":"SELECT pais_id FROM pais WHERE nombre = %s",
    "select_provincia_id_segun_nombre_y_pais_id":"SELECT provincia_id FROM provincia WHERE nombre = %s AND pais_id %s",
    "select_ciudad_id_segun_nombre_y_provincia_id":"SELECT ciudad_id FROM ciudad WHERE nombre = %s AND provincia_id = %s",
    "select_direccion_segun_id":"SELECT * FROM direccion WHERE direccion_id = %s",
    "select_ciudad_segun_id":"SELECT nombre, provincia_id FROM ciudad WHERE ciudad_id  = %s",
    "select_provincia_segun_id":"SELECT nombre, pais_id FROM provincia WHERE provincia_id = %s",
    "select_pais_segun_id":"SELECT nombre FROM pais WHERE pais_id = %s",
    "select_productos_segun_nombre":"SELECT * FROM producto WHERE nombre = %s",
    "select_producto_segun_id":"SELECT * FROM producto WHERE producto_id = %s",
    "select_precio_segun_producto":"SELECT precio FROM producto WHERE producto_id = %s",
    "select_categoria_id_segun_nombre":"SELECT categoria_id FROM categoria WHERE nombre = %s",
    "select_marca_id_segun_nombre":"SELECT marca_id FROM marca WHERE nombre = %s",

    "update_producto_nombre":"UPDATE producto SET nombre = %s, fecha_de_ultima_modificacion = %s WHERE producto_id = %s",
    "update_producto_descripcion":"UPDATE producto SET descripcion = %s, fecha_de_ultima_modificacion = %s WHERE producto_id = %s",
    "update_producto_precio":"UPDATE producto SET precio = %s, fecha_de_ultima_modificacion = %s WHERE producto_id = %s",
    "update_usuario_nombre":"UPDATE usuario SET nombre = %s WHERE usuario_id = %s",
    "update_usuario_apellido":"UPDATE usuario SET apellido = %s WHERE usuario_id = %s",
    "update_usuario_email":"UPDATE usuario SET email = %s WHERE usuario_id = %s",
    "update_usuario_clave":"UPDATE usuario SET clave = %s WHERE usuario_id = %s",
    "update_usuario_telefono":"UPDATE usuario SET telefono = %s WHERE usuario_id = %s",
    "update_usuario_direccion_id":"UPDATE usuario SET direccion_id = %s WHERE usuario_id = %s",
    "update_direccion_calle_y_altura":"UPDATE direccion SET calle = %s, altura = %s WHERE direccion_id = %s",
    "update_direccion_codigo_postal":"UPDATE direccion SET codigo_posta = %s WHERE direccion_id = %s",
    "update_producto_stock":"UPDATE producto SET stock = %s WHERE producto_id = %s",

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

    def get_todos_los_usuarios(self):
        self.cursor.execute(queries["select_usuarios"])
        resultados = self.cursor.fetchall()
        return resultados

    def get_todos_los_productos(self):
        self.cursor.execute(queries["select_productos"])
        resultados = self.cursor.fetchall()
        return resultados

    def get_todas_las_compras(self):
        self.cursor.execute(queries["select_compras"])
        resultados = self.cursor.fetchall()
        return resultados

    def get_todas_las_categorias(self):
        self.cursor.execute(queries["select_categorias"])
        resultados = self.cursor.fetchall()
        return resultados

    def get_todas_las_marcas(self):
        self.cursor.execute(queries["select_marcas"])
        resultados=self.cursor.fetchall()
        return resultados

    def get_carrito_de_usuario_segun_id(self, usuario_id):
        val = (usuario_id,)
        self.cursor.execute(queries["select_carrito_segun_usuario"], val)
        resultados = self.cursor.fetchall()
        return resultados

    def get_usuario_segun_id(self, usuario_id):
        val = (usuario_id,)
        self.cursor.execute(queries["select_usuario_segun_id"], val)
        resultado = self.cursor.fetchone()
        return resultado

    def get_datos_login(self, email):
        val = (email,)
        self.cursor.execute(queries["select_login_segun_email"], val)
        resultado = self.cursor.fetchone()
        return resultado

    def get_id_de_categoria(self, categoria_nombre):
        val = (categoria_nombre,)
        self.cursor.execute(queries["select_categoria_id_segun_nombre"], val)
        categoria_id = self.cursor.fetchone()
        if not categoria_id:
            categoria_id = (0,)
        return categoria_id[0]

    def get_id_de_marca(self, marca_nombre):
        val = (marca_nombre,)
        self.cursor.execute(queries["select_marca_id_segun_nombre"], val)
        marca_id = self.cursor.fetchone()
        if not marca_id:
            marca_id = (0,)
        return marca_id[0]

    def get_id_de_pais(self, pais_nombre):
        val = (pais_nombre,)
        self.cursor.execute(queries["select_pais_id_segun_nombre"], val)
        pais_id = self.cursor.fetchone()
        if not pais_id:
            pais_id = (0,)
        return pais_id[0]

    def get_id_de_provincia(self, provincia_nombre, pais_id):
        val = (provincia_nombre, pais_id)
        self.cursor.execute(queries["select_provincia_id_segun_nombre"], val)
        provincia_id = self.cursor.fetchone()
        if not provincia_id:
            provincia_id = (0,)
        return provincia_id[0]

    def get_id_de_ciudad(self, ciudad_nombre, provincia_id):
        val = (ciudad_nombre, provincia_id)
        self.cursor.execute(queries["select_ciudad_id_segun_nombre"], val)
        ciudad_id = self.cursor.fetchone()
        if not ciudad_id:
            ciudad_id = (0,)
        return ciudad_id[0]

    def get_direccion_segun_id(self, direccion_id):
        val = (direccion_id,)
        self.cursor.execute(queries["select_direccion_segun_id"])
        resultado = self.cursor.fetchone()
        return resultado

    def get_ciudad_segun_id(self, ciudad_id):
        val = (ciudad_id,)
        self.cursor.execute(queries["select_ciudad_segun_id"], val)
        resultados = self.cursor.fetchone()
        return resultados

    def get_provincia_segun_id(self, provincia_id):
        val = (prinvicia_id,)
        self.cursor.execute(queries["select_provincia_segun_id"], val)
        resultados = self.cursor.fetchone()
        return resultados

    def get_pais_segun_id(self, pais_id):
        val = (pais_id,)
        self.cursor.execute(queries["select_pais_segun_id"], val)
        resultados = self.cursor.fetchone()
        return resultados

    def get_precio_de_producto(self, producto):
        val = (producto.get_producto_id(),)
        self.cursor.execute(queries["select_precio_segun_producto"], val)
        precio = self.cursor.fetchone()
        if not precio:
            precio = (-1,)
        return precio[0]

    def get_productos_segun_nombre(self, producto_nombre):
        val = (producto_nombre,)
        self.cursor.execute(queries["select_productos_segun_nombre"], val)
        resultados = self.cursor.fetchall()
        return resultados

    def get_producto_segun_id(self, producto_id):
        val = (producto_id,)
        self.cursor.execute(queries["select_producto_segun_id"], val)
        resultado = self.cursor.fetchone()
        return resultado

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
        if usuario.get_carrito():
            for carrito in usuario.get_carrito():
                self.eliminar_carrito(carrito)
        if usuario.get_compras():
            for compra in usuario.get_compras():
                compra.set_usuario_id(-1)
                self.actualizar_compra_usuario_id(compra)
        val = (usuario.get_usuario_id(),)
        self.cursor.execute(queries["delete_usuario"], val)
        self.conexion.commit()

    def eliminar_producto(self, producto):
        val = (producto.get_producto_id(),)
        self.cursor.execute(queries["delete_producto"], val)
        self.conexion.commit()

    def eliminar_carrito(self, carrito):
        val = (carrito.get_carrito)
        self.cursor.execute(queries["delete_carrito"], val)
        self.conexion.commit()

    def eliminar_compra(self, compra):
        val = (compra.get_compra_id(),)
        self.cursor.execute(queries["delete_compra"], val)
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
        val = (direccion.get_calle(), direccion.get_altura(), direccion.get_direccion_id())
        self.cursor.execute(queries["update_direccion_calle_y_altura"], val)
        self.conexion.commit()

    def actualizar_direccion_codigo_postal(self, direccion):
        val = (direccion.get_codigo_postal(), direccion.get_direccion_id())
        self.cursor.execute(queries["update_direccin_codigo_postal"], val)
        self.conexion.commit()

    def actualizar_producto_stock(self, producto):
        val = (producto.get_stock(), producto.get_producto_id())
        self.cursor.execute(queries["update_producto_stock"], val)
        self.conexcion.commit()

if __name__=="__main__":
    from dbconf import dbconf
    db = Ecommerce_db(dbconf)
    lista_usuarios=db.get_todos_los_usuarios()
    lista_productos=db.get_todos_los_productos()
    print(lista_usuarios)
    print(lista_productos)
