import os
import platform
import datetime
from getpass import getpass
from base64 import encodebytes, decodebytes
from validate_email import validate_email
from dbconf import dbconf
from ecommerce_db import Ecommerce_db
from producto import Producto
from usuario import Usuario

def limpiar_pantalla():
    if platform.system() == "Windows":
        clear = "cls"
    else:
        clear = "clear"
    os.system(clear)

class Ecommerce_app:

    def __init__(self, dbconf):
        '''Se inicializa la base de datos. Usuario y Producto se cargan mediante los menus'''
        self.db = Ecommerce_db(dbconf)
        self.usuario = None
        self.producto = None



    def ingresar_clave(self, texto):
        '''Pide al usuario que ingrese una cadena y la devuelve encriptada'''

        clave = getpass(texto)
        return encodebytes(clave.encode())



    def menu_inicio(self):
        '''Menu de inicio de sesion

        Da al usuario la opcion de iniciar sesion con un email y clave previamente
        registrado, la opcion de recuperar la contraseña en caso de olvidarla o la
        de registrar un nuevo usuario.'''

        while True:
            limpiar_pantalla()
            print("""Menu de inicio
[1] Iniciar sesión
[2] Registrarse
[3] Recuperar contraseña
[4] Salir""")
            rta = input("-> ")
            if rta == "1":
                self.iniciar_sesion()
            elif rta == "2":
                self.registrar_usuario()
            elif rta == "3":
                self.recuperar_contrasenia()
            elif rta == "4":
                return



    def iniciar_sesion(self):
        '''Pide email y clave. El administrador puede acceder al ABM de producto. Un usuario inicia sesion.'''

        limpiar_pantalla()
        print("Iniciar sesión: ")
        email = input("Email: ")
        clave = self.ingresar_clave("Contraseña: ")
        if email == "@admin" and clave == encodebytes("123".encode()):
            self.menu_abm_producto()
        elif validate_email(email, check_mx=True) and clave:
            self.comprobar_login(email, clave)
        elif email:
            print("No es un email válido.")
        input()



    def comprobar_login(self, email, clave):
        '''Comprueba los datos ingreados por el usuario con los registrados en la base de datos.

        Trae datos de db. Si el email no se encuentra en la base de datos se informa
        al usuario y vuelve a menu_inicio(). En caso que el email exista, se comprueba
        si las claves concuerdan y se procede a inicializar el usuario'''

        datos_db = self.db.datos_login(email)
        if datos_db:
            if clave == datos_db[0].encode():
                datos_usuario = self.db.datos_de_usuario_id(datos_db[1])
                self.usuario = Usuario(*datos_usuario)
                print("Inicio de sesión exitoso")
            else:
                print("Contraseña incorrecta")
        else:
            print("No se encuentra registro de", email)



    def registrar_usuario(self):
        '''Registro de usuario

        Muestra en pantalla los datos que tiene que completar el usuario para registrarse'''

        def mostrar_datos(datos):
            '''Muestra el formulario'''
            limpiar_pantalla()
            for k,v in datos.items():
                print(k+":", v)

        while True:
            datos = {"Nombre":"", "Apellido":"", "Fecha de nacimiento (dd/mm/aaaa)":"", "Email":"", "Clave":"", "DNI":"", "Telefono":""}
            for k in datos:
                mostrar_datos(datos)
                datos[k] = input("-> " + k + ": ")

            try:
                dni, nombre, apellido, telefono = datos["DNI"], datos["Nombre"], datos["Apellido"], datos["Telefono"]
                fecha_de_nacimiento = datetime.datetime.strptime(datos["Fecha de nacimiento (dd/mm/aaaa)"], "%d/%m/%Y")
                email = datos["Email"]
                clave = datos["Clave"]
                usuario = Usuario(0, dni, nombre, apellido, fecha_de_nacimiento, email, clave, telefono, 0, datetime.datetime.now())
                print("Usuario creado")
            except:
                print("Hubo un error")
            input()



    def recuperar_contrasenia(self):
        '''Imprime un mensaje'''

        print("Recuperar contraseña:")
        email = input("Ingrese su email: ")
        datos_usuario = self.db.datos_login(email)
        if datos_usuario:
            print(decodebytes(datos_usuario[0].encode()))
        else:
            print("No se encuentra ese email")
        input()



    def menu_perfil(self):
        '''ABM usuario'''



    def ver_productos(self):
        '''Muestra en pantalla los productos en catalogo'''



    def ver_carrito(self):
        '''Ver los productos que se encuentran en carritos'''



    def ver_compras(self):
        '''Ve las compras realizadas por el usuario'''



    def menu_abm_producto(self):
        '''Menu de Alta Baja Modificacion de Productos'''

app = Ecommerce_app(dbconf)
app.menu_inicio()
