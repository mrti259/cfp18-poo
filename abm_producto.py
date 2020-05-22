from todos_los_modulos import Producto, Ecommerce_db, dbconf

db = Ecommerce_db(dbconf)

def crear_producto():
    nombre = input("Nombre: ")
    descripcion = input("Descripcion: ")
    precio = float(input("Precio: "))
    categoria = input("Categoria: ")
    marca = input("Marca")
    categoria_id = db.id_de_categoria(categoria)
    marca_id = db.id_de_marca(marca)
    producto = Producto(0, nombre, descripcion, precio, categoria_id, marca_id)
    db.registrar_producto(producto)
    return producto

def eliminar_producto(producto):
    print(f"¿Quiere eliminar el producto {producto.get_nombre_id()} id{producto.get_producto_id()}?")
    if (input("Confirmar (s/n): ") == "s"):
        if (input("Esta acción no se puede deshacer (s/n): ") == 's'):
            db.eliminar_producto(producto)

def modificar_nombre(producto):
    nombre = input("Nuevo nombre: ")
    if (input('Confirmar? (s/n) ') == 's'):
        producto.set_nombre(nombre)
        db.actualizar_producto_nombre(producto)
    else:
        pass

def modificar_descripcion(producto):
    descripcion = input("Nueva descripcion: ")
    if (input('Confirmar? (s/n) ') == 's'):
        producto.set_descripcion(descripcion)
        db.actualizar_producto_descripcion(producto)
    else:
        pass

def modificar_precio(producto):
    precio = float(input("Nuevo precio: "))
    if (input('Confirmar? (s/n) ') == 's'):
        producto.set_precio(precio)
        db.actualizar_producto_precio(producto)
    else:
        pass

def menu_producto():
    pass
