from todos_los_modulos import Direccion, Ecommerce_db, dbconf, Usuario

db = Ecommerce_db(dbconf)

def mostrar_direccion(direccion):
    ciudad_nombre, provincia_id = db.ciudad_por_id(direccion.get_ciudad_id())
    provincia_nombre, pais_id = db.provincia_por_id(provincia_id)
    pais_nombre = db.pais_por_id(pais_id)
    print(f"(id.{direccion.get_direccion_id()})", direccion.get_calle(), direccion.get_altura(), direccion.get_codigo_postal(), ciudad_nombre, provincia_nombre, pais_nombre)

def crear_direccion():
    calle = input("Calle: ")
    altura = input("Altura: ")
    codigo_postal = input("Codigo postal: ")
    ciudad = input("Ciudad: ")
    provincia = input("Provincia: ")
    pais = input("Pais: ")
    pais_id = db.id_de_pais(pais)
    provincia_id = db.id_de_provincia(provincia, pais_id)
    ciudad_id = db.id_de_ciudad(ciudad, provincia_id)
    direccion = Direccion(0, calle, altura, codigo_postal, ciudad_id)
    mostrar_direccion(direccion)
    opc = input("Confirmar? (s/N) ").lower()
    if opc == "s":
        db.registrar_direccion(direccion)
    else:
        print("Por favor, ingrese una dirección")
        direccion = crear_direccion()
    return direccion

def eliminar_direccion(direccion):
    print(f"¿Quiere esta direccion {direccion.get_calle()} {direccion.get_altura()}, {direccion.get_codigo_postal()}?")
    if (input("Confirmar (s/N): ").lower() == "s"):
        if (input("Esta acción no se puede deshacer (s/N): ") == 's'):
            db.eliminar_direccion(direccion)


def actualizar_calle_y_altura(direccion):
    calle = input("Nueva calle: ")
    altura = input("Nueva altura: ")
    direccion.set_calle(calle)
    direccion.set_altura(altura)
    db.actualizar_direccion_calle_y_altura(direccion)

def actualizar_codigo_postal(direccion):
    codigo_postal = input("Codigo postal: ")
    direccion.set_codigo_postal(codigo_postal)
    db.set_codigo_postal(direccion)
    db.actualizar_direccion_codigo_postal(direccion)

def menu_direcciones_de_compra(usuario):
    # Al realizar la compra se muestra este menú dando la opcion
    # al usuario a poner su direccion predefinida, o una nueva
    direccion = None
    if usuario.get_direccion_id():
        direccion = Direccion(*db.direccion_por_id(usuario.get_direccion_id()))
        mostrar_direccion(direccion)
        print("Quiere usar esta direccion? ")
        opc = input("(S/n)").lower()
        if opc == "n":
            print("Ingrese una nueva direccion:")
            direccion = crear_direccion()
    else:
        print("Ingrese una dirección:")
        direccion = crear_direccion()
    return direccion

def menu_direcciones_de_perfil(usuario):
    direccion_usuario = None
    if usuario.get_direccion_id():
        direccion_usuario = db.direccion_por_id(usuario.get_direccion_id())
        mostrar_direccion(direccion_usuario)
        print("Qué quiere hacer?")
        print("[1]Modificar direccion actual")
        print("[2]Eliminar")
        opc = input()
        if opc
    else:
        print("Ingrese una direccion: ")
        direccion = crear_direccion()
        usuario.set_direccion_id(direccion.get_direccion_id())
        db.actualizar_usuario_direccion_id(usuario)
