import base64
from validate_email import validate_email

def encriptar(clave):
    return base64.encodebytes(clave.encode())

def desencriptar(clave):
    return base64.decodebytes(clave.encode())

class Usuario:
    def __init__(self, usuario_id, dni, nombre, apellido, fecha_de_nacimiento, email, clave, telefono, direccion_id, fecha_de_registro):
        self.errores = {}
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
        self.compra = []
        self.carrito = []

    def set_usuario_id(self, usuario_id):
        self.usuario_id = usuario_id
    def get_usuario_id(self):
        return self.usuario_id

    def set_dni(self, dni):
        self.dni = dni
    def get_dni(self):
        return self.dni

    def set_nombre(self, nombre):
        if nombre.isalpha():
            self.nombre = nombre.capitalize()
        else:
            self.errores["nombre"] = "El nombre no es válido"
    def get_nombre(self):
        return self.nombre

    def set_apellido(self, apellido):
        if apellido.isalpha():
            self.apellido = apellido.capitalize()
        else:
            self.errores["apellido"] = "El apellido no es válido"
    def get_apellido(self):
        return self.apellido

    def set_fecha_de_nacimiento(self, fecha_de_nacimiento):
        self.fecha_de_nacimiento = fecha_de_nacimiento
    def get_fecha_de_nacimiento(self):
        return self.fecha_de_nacimiento

    def set_email(self, email):
        if validate_email(email, check_mx=True):
            self.email = email
        else:
            self.errores["email"] = "El email no es válido"
    def get_email(self):
        return self.email

    def set_clave(self, clave):
        clave = desencriptar(clave)
        if any(char.islower() for char in clave) and any(char.isupper() for char in clave) and any(char.isdigit() for char in clave):
            self.clave = clave
        else:
            self.errores["clave"] = "La contraseña no cumple con los criterios: al menos una mayuscula, al menos una minuscula, al menos un numero"
    def get_clave(self):
        return encriptar(self.clave)

    def set_telefono(self, telefono):
        self.telefono = telefono
    def get_telefono(self):
        return self.telefono

    def set_direccion_id(self, direccion_id):
        self.direccion_id = direccion_id
    def get_direccion_id(self):
        return self.direccion_id

    def set_fecha_de_registro(self, fecha_de_registro):
        self.fecha_de_registro = fecha_de_registro
    def get_fecha_de_registro(self):
        return self.fecha_de_registro

    def cargar_compras(self, lista_compras):
        self.carrito.concat(lista_compras)
    def get_carrito(self):
        return self.carrito

    def cargar_carrito(self, lista_carrito):
        self.carrito.concat(lista_carrito)
    def get_carrito(self):
        return self.carrito

    def get_errores(self):
        return [msg for msg in self.errores.values()]
