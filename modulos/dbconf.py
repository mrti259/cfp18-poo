conf = {
    "host": "localhost",
    "user": "martina",
    "passwd": "",
    "database": "ecommerce_final"
}

queries = {
    "select_usuarios":"SELECT * FROM usuarios",
    "select_productos":"SELECT * FROM productos",
    "select_compras":"SELECT * FROM compras",
    "select_datos_login":"SELECT clave, usuario_id FROM usuarios WHERE email = %s",
    "select_datos_usuario":"SELECT * FROM usuarios WHERE usuario_id = %s",
    "update_producto_nombre":"UPDATE productos SET nombre = %s WHERE producto_id = %s",
    "update_producto_descripcion":"UPDATE productos SET descripcion = %s WHERE producto_id = %s",
    "update_producto_precio":"UPDATE productos SET precio = %s WHERE producto_id = %s",
    "update_usuario_email":"UPDATE usuarios SET email = %s WHERE usuario_id = %s",
    "update_usuario_clave":"UPDATE usuarios SET clave = %s WHERE usuario_id = %s",
    "update_usuario_telefono":"UPDATE usuarios SET telefono = %s WHERE usuario_id = %s",
    "update_usuario_direccion":"UPDATE usuarios SET direccion_id = %s WHERE usuario_id = %s",
    "insert_producto":"INSERT INTO productos(nombre, descripcion, precio, categoria_id, marca_id) VALUES (%s, %s, %s, %s, %s)",
    "insert_usuario":"INSERT INTO usuarios(dni, nombre, apellido, clave, email, telefono) VALUES (%s, %s, %s, %s)",
    "insert_compra":"INSERT INTO compras(usuario_id, direccion_id, producto_id, cantidad, precio_total) VALUES (%s, %s, %s, %s, %s)",
    "delete_producto":"DELETE FROM productos WHERE producto_id = %s",
    "delete_usuario":"DELETE FROM usuarios WHERE usuario_id = %s",
}
