queries = {
# TOTALES
    "total_usuarios":"SELECT COUNT(usuario_id) FROM usuario WHERE usuario_id != 1",
    "total_ventas":"SELECT COUNT(compra_id) FROM compra WHERE compra_id != 1",
    "total_ingresos":"SELECT SUM(precio_total) FROM compra WHERE compra_id != 1",
# CONSULTAS
    "select_paises":"SELECT * FROM pais",
    "select_pais_segun_id":"SELECT * FROM pais WHERE pais_id = %s",
    "select_provincias_segun_pais":"SELECT * FROM provincia WHERE pais_id = %s",
    "select_ciudades_segun_provincia":"SELECT * FROM ciudad WHERE provincia_id = %s",
    "select_provincia_segun_id":"SELECT * FROM provincia WHERE provincia_id = %s",
    "select_ciudad_segun_id":"SELECT * FROM ciudad WHERE ciudad_id  = %s",
    "select_direccion_segun_id":"SELECT * FROM direccion WHERE direccion_id = %s",

    "select_categorias":"SELECT * FROM categoria",
    "select_categoria_segun_id":"SELECT * FROM categoria WHERE categoria_id = %s",
    "select_marcas":"SELECT * FROM marca",
    "select_marca_segun_id":"SELECT * FROM marca WHERE marca_id = %s",

    "select_productos":"SELECT * FROM producto WHERE producto_id != 1",
    "select_productos_segun_nombre":"SELECT * FROM producto WHERE nombre LIKE %s",
    "select_producto_segun_id":"SELECT * FROM producto WHERE producto_id = %s",

    "select_usuarios":"SELECT * FROM usuario WHERE usuario_id != 1",
    "select_login_segun_email":"SELECT clave, usuario_id FROM usuario WHERE email = %s",
    "select_usuario_segun_id":"SELECT * FROM usuario WHERE usuario_id = %s",

    "select_compras":"SELECT * FROM compra WHERE compra_id != 1",
    "select_compras_segun_usuario_id":"SELECT * FROM compra WHERE usuario_id = %s",

    "select_carrito_segun_usuario":"SELECT * FROM carrito WHERE usuario_id = %s",

# ACTUALIZACIONES
    "update_producto_nombre":"UPDATE producto SET nombre = %s, fecha_de_ultima_modificacion = %s WHERE producto_id = %s",
    "update_producto_descripcion":"UPDATE producto SET descripcion = %s, fecha_de_ultima_modificacion = %s WHERE producto_id = %s",
    "update_producto_precio":"UPDATE producto SET precio = %s, fecha_de_ultima_modificacion = %s WHERE producto_id = %s",
    "update_producto_stock":"UPDATE producto SET stock = %s WHERE producto_id = %s",

    "update_usuario_email":"UPDATE usuario SET email = %s WHERE usuario_id = %s",
    "update_usuario_clave":"UPDATE usuario SET clave = %s WHERE usuario_id = %s",
    "update_usuario_nombre":"UPDATE usuario SET nombre = %s WHERE usuario_id = %s",
    "update_usuario_apellido":"UPDATE usuario SET apellido = %s WHERE usuario_id = %s",
    "update_usuario_dni":"UPDATE usuario SET dni = %s WHERE usuario_id = %s",
    "update_usuario_telefono":"UPDATE usuario SET telefono = %s WHERE usuario_id = %s",
    "update_usuario_direccion_id":"UPDATE usuario SET direccion_id = %s WHERE usuario_id = %s",

    "update_carrito_cantidad":"UPDATE carrito SET cantidad = %s WHERE carrito_id = %s",

# INSERCIONES
    "insert_pais":"INSERT INTO pais(nombre) VALUES (%s)",
    "insert_provincia":"INSERT INTO provincia(nombre, pais_id) VALUES (%s, %s)",
    "insert_ciudad":"INSERT INTO ciudad(nombre, provincia_id) VALUES (%s, %s)",
    "insert_direccion":"INSERT INTO direccion(calle, altura, codigo_postal, ciudad_id) VALUES (%s, %s, %s, %s)",
    "insert_producto":"INSERT INTO producto(nombre, descripcion, precio, stock, categoria_id, marca_id, fecha_de_publicacion, fecha_de_ultima_modificacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    "insert_usuario":"INSERT INTO usuario(email, clave, nombre, apellido, fecha_de_nacimiento, dni, telefono, direccion_id, fecha_de_registro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
    "insert_compra":"INSERT INTO compra(usuario_id, direccion_id, producto_id, cantidad, precio_total, fecha_de_compra) VALUES (%s, %s, %s, %s, %s, %s)",
    "insert_carrito":"INSERT INTO carrito(usuario_id, producto_id, cantidad) VALUES (%s, %s, %s)",

# ELIMINACIONES
    "delete_producto":"DELETE FROM producto WHERE producto_id = %s",
    "delete_usuario":"DELETE FROM usuario WHERE usuario_id = %s",
    "delete_compras_de_producto":"UPDATE compra SET producto_id = 1 WHERE producto_id = %s",
    "delete_compras_de_usuario":"UPDATE compra SET usuario_id = 1 WHERE usuario_id = %s",
    "delete_carrito_de_usuario":"DELETE FROM carrito WHERE usuario_id = %s",
    "delete_carrito":"DELETE FROM carrito WHERE carrito_id = %s",

}
