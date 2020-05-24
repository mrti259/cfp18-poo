from todos_los_modulos import Carrito, Compra, Ecommerce_db, dbconf, datetime

db = Ecommerce_db(dbconf)

def agregar_al_carrito(usuario, producto, cantidad):
    carrito = Carrito(0, usuario.get_usuario_id(), producto.get_producto_id(), cantidad)
    db.agregar_a_carrito(carrito)

def comprar(carrito, direccion):
    precio_total = db.precio_de_producto_id() * carrito.get_cantidad()
    fecha_de_compra = str(datetime.today())
    compra = Compra(0, carrito.get_usuario_id(), direccion.get_direccion_id(); carrito.get_producto_id(), carrito.get_cantidad(), precio_total, fecha_de_compra)
    db.registrar_compra(compra)

def menu_carrito():
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
