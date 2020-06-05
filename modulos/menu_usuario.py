class Menu_Usuario:
    def __init__(self):
        self.db = Ecommerce_db(dbconf)

    def registro_usuario(email):
        if db.datos_login(email):
            print("Ya tiene un usuario. ¿Olvidó su contraseña?")
            pass
        else:
            usuario = None
            print("Se va a crear un usuario con el email:", email)
            while not usuario:
                try:
                    nombre = input("Nombre: ")
                    apellido = input("Apellido: ")
                    print("Fecha de nacimiento:")
                    dd = int(input("Día (dd): "))
                    mm = int(input("Mes (mm): "))
                    aa = int(input("Año (aaaa): "))
                    dni = int(input("Dni: "))
                    clave = getpass("Clave: ")
                    telefono = int(input("Telefono: "))
                    fecha_de_nacimiento = date(aa,mm,dd)
                    fecha_de_registro = datetime.now()
                    usuario = Usuario(0, dni, nombre, apellido, fecha_de_nacimiento, email, clave, telefono, 0, fecha_de_registro)
                except:
                    print("Ocurrio un error. Pruebe nuevamente")
            if not usuario.get_errores():
                print("Usuario creado")
                db.registrar_usuario(usuario)
            else:
                errores = usuario.get_errores()
                for err in errores:
                    print(err)

    def inicio_sesion():
        email = input("Email: ")
        while not validate_email(email, check_mx=True):
            print("No es un mail válido. Pruebe nuevamente:")
            email = input("Email: ")
        clave = encriptar(getpass("Clave: ")).decode()
        login_usuario = db.datos_login(email)
        if login_usuario:
            if clave == login_usuario[0]:
                datos_usuario = db.datos_de_usuario_id(login_usuario[1])
                usuario_actual = Usuario(*datos_usuario)
                print("Usuario cargado.")
            else:
                print("Contraseña incorrecta")
        else:
            print("Ese mail no se encuentra en nuestra base de datos.")
            rta = input("Quiere crear un usuario? (s/n) ")
            if rta == 's':
                registro_usuario(email)

    def menu_sesion():
        rta = ''
        while not (rta == '1' or rta == '2'):
            print("[1] Iniciar sesion [2] Registrarse")
            rta = input("(1/2): ")
            if rta == '1':
                inicio_sesion()
            elif rta == '2':
                email = input('Ingrese su email: ')
                if validate_email(email, check_mx=True):
                    registro_usuario(email)
                else:
                    print("No es un email válido.")
                    rta = ''
