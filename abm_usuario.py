from todos_los_modulos import Ecommerce_db, dbconf, Usuario, encriptar, validate_email, getpass

db = Ecommerce_db

def eliminar_usuario(usuario):
    print("¿Quiere eliminar su cuenta?")
    if (input("Confirmar (s/n): ") == "s"):
        if (input("Esta acción no se puede deshacer (s/n): ") == 's'):
            db.eliminar_usuario(usuario)

def modificar_nombre(usuario):
    dato = input("Nuevo nombre: ")
    usuario.set_nombre(dato)
    if not usuario.get_errores():
        db.actualizar_usuario_nombre(usuario)
        print("-cambios realizados-")
    else:
        print(usuario.get_errores())
        print("-cambios descartados-")

def modificar_apellido(usuario):
    dato = input("Nuevo apellido: ")
    opc=input("cambiar apellido por: ",dato)
    if(opc):
        usuario.set_apellido(dato)
        db.actualizar_usuario_apellido(usuario)
        print("-cambios realizados-")
    else:
        print("-cambios descartados-")

def modificar_telefono(usuario):
    try:
        dato = int(input("Nuevo telefono: "))
    except:
        print("NUMERO NO VALIDO")
    opc=input("cambiar telefono por: ",dato)
    if(opc):
        usuario.set_telefono(dato)
        db.actualizar_usuario_telefono(usuario)
        print("-cambios realizados-")
    else:
        print("-cambios descartados-")


def modificar_email(usuario):
    email = input("Nuevo email: ")
    while not validate_email(email, check_mx=True):
        print("Ese mail no es correcto...")
        email = input("Nuevo email:")
    if not db.datos_login(email):
        usuario.set_email(email)
        db.actualizar_usuario_email(usuario)
    else:
        print("Ese email se encuentra ocupado.")

def modificar_clave(usuario, recuperar = False):
    clave0 = getpass("Nueva clave: ")
    clave1 = getpass("Repita la clave:")
    if clave0 == clave1:
        if recuperar:
            usuario.set_clave(clave0)
            db.actualizar_usuario_clave(usuario)
        else:
            clave2 = getpass("Ingrese su clave actual: ")
            if encriptar(clave2) == usuario.get_clave():
                usuario.set_clave(clave0)
                db.actualizar_usuario_clave(usuario)
            else:
                print("Contraseña incorrecta")
    else:
        print("Las contraseñas no coinciden.")

def menu_modificar_usuario(usuario):
    print("Que desea modificar: ")
    print("1. Nombre")
    print("2. Apellido")
    print("3. telefono")
    print("4. email")
    print("5. clave")

    opc = input()
    if opc == "1":
        modificar_nombre(usuario)
    if opc == "2":
        modificar_apellido(usuario)
    if opc == "3":
        modificar_telefono(usuario)
    if opc == "4":
        modificar_email(usuario)
    if opc == "5":
        modificar_clave(usuario)

def menu_perfil(usuario):
    print("Que accion desea realizar:")
    print("1. Modificar mi perfil")
    print("2. Eliminar mi usuario")
    print("0. ATRAS")
    opc=input("> ")
    if opc== "1":
        menu_modificar_usuario(usuario)
    elif opc == "2":
        eliminar_usuario(usuario)
    elif opc == "0":
        print("Salir")
