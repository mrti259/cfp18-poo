from todos_los_modulos import Producto, Ecommerce_db, dbconf, datetime

db = Ecommerce_db(dbconf)

def buscar_producto_por_nombre():
    nombre = input("Nombre: ")
    resultado_de_productos = db.productos_por_nombre(nombre)
    producto = []
    if resultado_de_productos:
        print("Se obtuvieron los siguientes resultados:")
        for datos_producto in resultado_de_productos:
            print(datos_producto)
        print("Si busca uno de los siguientes productos, ingrese su id: ")
        producto_id = int(input("Id: "))
        for datos_producto in resultado_de_productos:
            if producto_id == datos_producto[0]:
                producto = datos_producto
    else:
        print("No se obtuvieron resultados.")
    if producto:
        producto = Producto(*producto)
    return producto

def registrar_producto():
    nombre = input("Nombre: ")
    descripcion = input("Descripcion: ")
    precio = float(input("Precio: "))
    print("--para lista pulse L--")
    categoria = input("Categoria: ")
    while categoria == "l" or categoria == "L":
        listar_categorias()
        categoria = input("Categoria: ")
    print("--para lista pulse L--")
    marca = input("Marca: ")
    while marca == "l" or marca == "L":
        listar_marcas()
        marca = input("Marca: ")
    stock = int(input("Cantidad disponible: "))

    fecha_de_publicacion = str(datetime.now())
    fecha_de_ultima_modificacion = str(datetime.now())
    producto = Producto(0, nombre, descripcion, precio, stock, categoria, marca, fecha_de_publicacion, fecha_de_ultima_modificacion)
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
        fecha_de_ultima_modificacion = str(datetime.now())
        producto.set_fecha_de_ultima_modificacion(fecha_de_ultima_modificacion)
        producto.set_nombre(nombre)
        db.actualizar_producto_nombre(producto)
    else:
        pass

def modificar_descripcion(producto):
    descripcion = input("Nueva descripcion: ")
    if (input('Confirmar? (s/n) ') == 's'):
        fecha_de_ultima_modificacion = str(datetime.now())
        producto.set_fecha_de_ultima_modificacion(fecha_de_ultima_modificacion)
        producto.set_descripcion(descripcion)
        db.actualizar_producto_descripcion(producto)
    else:
        pass

def modificar_precio(producto):
    precio = float(input("Nuevo precio: "))
    if (input('Confirmar? (s/n) ') == 's'):
        fecha_de_ultima_modificacion = str(datetime.now())
        producto.set_fecha_de_ultima_modificacion(fecha_de_ultima_modificacion)
        producto.set_precio(precio)
        db.actualizar_producto_precio(producto)
    else:
        pass

def listar_productos():
    for datos in db.todos_los_productos():
        print(datos)
def listar_categorias():
    for datos in db.todas_las_categorias():
        print(datos)
def listar_marcas():
    for datos in db.todas_las_marcas():
        print(datos)

def menu_modificar_producto(producto):
    print("Que desea modificar: ")
    print("1. Nombre")
    print("2. Descripcion")
    print("3. Precio")
    print("4. Salir")
    opc = input()
    if opc == "1":
        modificar_nombre(producto)
    if opc == "2":
        modificar_descripcion(producto)
    if opc == "3":
        modificar_precio(producto)

def menu_producto():
    print("Que accion desea realizar:")
    print("1. Agregar producto")
    print("2. Modificar producto")
    print("3. Eliminar producto")
    print("4. Lista de productos")
    print("0. SALIR")
    opc=input("n: ")
    if opc== "1":
        registrar_producto()
    elif opc == "4":
        listar_productos()
    elif opc == "0":
        print("Salir")
    else:
        producto = buscar_producto_por_nombre()
        if producto:

            if opc == "3":
                eliminar_producto(producto)
            if opc=="2":
                menu_modificar_producto(producto)

menu_producto()
