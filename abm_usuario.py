from todos_los_modulos import Usuario, encriptar, validate_email, getpass

def eliminar_usuario(usuario):
    print(f"¿Quiere eliminar su cuenta?")
    if (input("Confirmar (s/n): ") == "s"):
        if (input("Esta acción no se puede deshacer (s/n): ") == 's'):
            db.eliminar_producto(producto)

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

def menu_perfil():
    pass
