import base64

def encriptar(clave):
    return base64.encodebytes(clave.encode())

class Usuario:
    def __init__(self, usuario_id, dni, nombre, apellido, fecha_de_nacimiento, email, clave, telefono, direccion_id, fecha_de_registro):
        self.set_usuario_id(usuario_id)
        self.set_dni(dni)
        self.set_nombre(nombre)
        self.set_apellido(apellido)
        self.set_fecha_de_nacimiento(fecha_de_nacimiento)
        self.set_email(email)
        self.set_clave(clave)
        self.set_telefono(telefono)
        self.set_direccion_id(direccion_id)
        self.set_fecha_de_registro(fecha_de_registro)
        self.carrito = []

    def get_usuario_id(self):
        return self.usuario_id

    def get_dni(self):
        return self.dni

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_fecha_de_nacimiento(self):
        return self.fecha_de_nacimiento

    def get_email(self):
        return self.email

    def get_clave(self):
        return encriptar(self.clave)

    def get_telefono(self):
        return self.telefono

    def get_direccion_id(self):
        return self.direccion_id

    def get_fecha_de_registro(self):
        return self.fecha_de_registro

    def get_carrito(self):
        return self.carrito

    def set_usuario_id(self, usuario_id):
        self.usuario_id = usuario_id

    def set_dni(self, dni):
        self.dni = dni

    def set_nombre(self, nombre):
        self.nombre = nombre.capitalize()

    def set_apellido(self, apellido):
        self.apellido = apellido.capitalize()

    def set_fecha_de_nacimiento(self, fecha_de_nacimiento):
        self.fecha_de_nacimiento = fecha_de_nacimiento

    def set_email(self, email):
        self.email = email

    def set_clave(self, clave):
        self.clave = clave

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_direccion_id(self, direccion_id):
        self.direccion_id = direccion_id

    def set_fecha_de_registro(self, fecha_de_registro):
        self.fecha_de_registro = fecha_de_registro

    def cargar_carrito(self, carrito):
        self.carrito.concat(carrito)
