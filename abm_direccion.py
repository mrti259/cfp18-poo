from todos_los_modulos import Direccion

db = Ecommerce_db(dbconf)

def agregar_direccion():
    calle = input("Calle: ")
    altura = input("Altura: ")
    codigo_postal = input("Codigo postal: ")
    ciudad = input("Ciudad: ")
    provincia = input("Provincia: ")
    pais = input("Pais: ")
    pais_id = db.id_de_pais(pais)
    provincia_id = db.id_de_provincia(provincia, pais_id)
    ciudad_id = db.id_de_ciudad(ciudad, provincia_id)
    direccion = direccion(0, calle, altura, codigo_postal, ciudad_id)
    db.registrar_direccion(direccion)


def eliminar_direccion(direccion):
    print(f"¿Quiere esta direccion {direccion.get_calle()} {direccion.get_altura()}, {direccion.get_codigo_postal()}?")
    if (input("Confirmar (s/n): ") == "s"):
        if (input("Esta acción no se puede deshacer (s/n): ") == 's'):
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
