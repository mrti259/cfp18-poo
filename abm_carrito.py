from todos_los_modulos import Carrito, Compra, Ecommerce_db, dbconf, datetime

db = Ecommerce_db(dbconf)

def agregar_al_carrito(usuario, producto, cantidad):
    carrito = Carrito(0, usuario.get_usuario_id(), producto.get_producto_id(), cantidad)
    db.agregar_a_carrito(carrito)

def comprar(carrito, direccion):
    precio_total = db.precio_de_producto_id() * carrito.get_cantidad()
    producto = db.producto_por_id(carrito.get_producto_id())
    producto.decr_stock(carrito.get_cantidad())
    # habria q agregar lago q verifique q el stock no es negativo para permitir la compra
    db.actualizar_producto_stock(producto)
    fecha_de_compra = str(datetime.today())
    compra = Compra(0, carrito.get_usuario_id(), direccion.get_direccion_id(); carrito.get_producto_id(), carrito.get_cantidad(), precio_total, fecha_de_compra)
    db.registrar_compra(compra)

def menu_carrito(usuario):
    datos_de_carrito = db.carritos_segun_usuario_id(usuario_id)
    lista_carrito = [Carrito(*datos) for datos in datos_de_carrito]
    usuario.cargar_carrito(lista_carrito)
    print("Qué quiere hacer?")
    print("1. Modificar carrito")
    print("2. Comprar")
    opc = input("n: ")
    if opc == "1":
        pass
    elif opc == "2":
        direccion = input()
        comprar(carrito, direccion)
        pass
    else:
        pass
