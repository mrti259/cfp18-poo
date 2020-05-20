conf = {
    "host": "localhost",
    "user": "martina",
    "passwd": "",
    "database": "ecommerce_final"
}

queries = {
    "select_usuarios":"SELECT * FROM usuario",
    "select_productos":"SELECT * FROM producto",
    "select_compras":"SELECT * FROM compra",
    "select_datos_login":"SELECT clave, usuario_id FROM usuario WHERE email = %s",
    "select_datos_usuario":"SELECT * FROM usuario WHERE usuario_id = %s",
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
