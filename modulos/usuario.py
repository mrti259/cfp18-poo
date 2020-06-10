import .validador

class Usuario:

    def __init__(self, usuario_id=0, dni=0, nombre="", apellido="", fecha_de_nacimiento="", email=" ", clave=" ", telefono=0, direccion_id=0, fecha_de_registro=""):
        '''Inicializa un usuario con sus datos'''

        self.set_usuario_id(usuario_id)
        self.set_email(email)
        self.set_clave(clave)
        self.set_nombre(nombre)
        self.set_apellido(apellido)
        self.set_fecha_de_nacimiento(fecha_de_nacimiento)
        self.set_dni(dni)
        self.set_telefono(telefono)
        self.set_direccion_id(direccion_id)
        self.set_fecha_de_registro(fecha_de_registro)
        self.compras = []
        self.carrito = []



    def __str__(self):
        '''Da formato a un usuario para ser pasado como cadena'''

        return (f"{self.get_usuario_id()}. {self.get_email()}")



    def ficha_usuario(self):
        '''Da formato a un usuario para pasarlo como una ficha más informativa'''

        return (f"""\
Usuario:
========
Nombre y apellido: {self.get_nombre()} {self.get_apellido()}
Email: {self.get_email()}
DNI: {self.get_dni()}
Telefono: {self.get_telefono()}
Fecha de nacimiento: {self.get_fecha_de_nacimiento()}
Fecha de registro: {self.get_fecha_de_registro()}
""")



    def set_usuario_id(self, usuario_id):
        self.usuario_id = usuario_id

    def get_usuario_id(self):
        return self.usuario_id


    def set_dni(self, dni):
        self.dni = dni
        return 1

    def get_dni(self):
        return self.dni


    def set_nombre(self, nombre):
        self.nombre = nombre
        return 1

    def get_nombre(self):
        return self.nombre


    def set_apellido(self, apellido):
        self.apellido = apellido
        return 1

    def get_apellido(self):
        return self.apellido


    def set_fecha_de_nacimiento(self, fecha_de_nacimiento):
        if validador.valida_fecha(fecha_de_nacimiento):
            self.fecha_de_nacimiento = fecha_de_nacimiento
            return 1
        print("La fecha no es válida")

    def get_fecha_de_nacimiento(self):
        return self.fecha_de_nacimiento


    def set_email(self, email):
        self.email = email
        return 1

    def get_email(self):
        return self.email


    def set_clave(self, clave):
        self.clave = clave
        return 1

    def get_clave(self):
        return self.clave


    def set_telefono(self, telefono):
        self.telefono = telefono
        return 1

    def get_telefono(self):
        return self.telefono


    def set_direccion_id(self, direccion_id):
        self.direccion_id = direccion_id
        return 1

    def get_direccion_id(self):
        return self.direccion_id


    def set_fecha_de_registro(self, fecha_de_registro):
        self.fecha_de_registro = fecha_de_registro
        return 1

    def get_fecha_de_registro(self):
        return self.fecha_de_registro


    def cargar_compras(self, lista_compras):
        self.compras.concat(lista_compras)

    def get_compras(self):
        return self.compras


    def cargar_carrito(self, lista_carrito):
        self.carrito.concat(lista_carrito)

    def get_carrito(self):
        return self.carrito
