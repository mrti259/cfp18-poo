# import datetime
from getpass import getpass
from .ecommerce_db import Ecommerce_db
from .producto import Producto
from .marca import Marca
from .categoria import Categoria
from .carrito import Carrito
from .usuario import Usuario
from .formulario import Formulario
import .extras
import .validador



class Ecommerce_app:

    def __init__(self, dbconf):
        '''Se inicializa la base de datos. Usuario y Producto se cargan mediante los menus'''
        self.db = Ecommerce_db(dbconf)
        self.usuario = None
        self.producto = None
        self.productos = []
        self.marcas = []
        self.categorias = []
        self.formulario = Formulario()



    def actualizar_catalogo(self):
        '''Vuelve a cargar los datos de productos, marcas y categorias'''
         datos_productos = self.db.get_todos_los_productos()
         self.productos = [Producto(*datos) for datos in datos_productos]
         datos_marcas = self.db.get_todas_las_marcas()
         self.marcas = [Marca(*datos) for datos in datos_marcas]
         datos_categorias = self.db.get_todas_las_categorias()
         self.categorias = [Categoria(*datos) for datos in datos_categorias]



    def ingresar_clave(self, texto):
        '''Pide al usuario que ingrese una cadena y la devuelve encriptada'''

        clave = getpass(texto)
        return extras.clave_encriptada(clave)



    def menu_inicio(self):
        '''Menu de inicio de sesion

        Da al usuario la opcion de iniciar sesion con un email y clave previamente
        registrado, la opcion de recuperar la contraseña en caso de olvidarla o la
        de registrar un nuevo usuario.'''

        while True:
            extras.limpiar_pantalla()
            print("""Menu de inicio
[1] Iniciar sesión
[2] Registrarse
[3] Recuperar contraseña
[x] Volver""")
            rta = input("-> ")
            if rta == "1":
                self.iniciar_sesion()
                if self.usuario:
                    self.menu_usuario()
            elif rta == "2":
                self.registrar_usuario()
            elif rta == "3":
                self.recuperar_contrasenia()
            elif rta == "x":
                return



    def iniciar_sesion(self):
        '''Pide email y clave. El administrador puede acceder al ABM de producto. Un usuario inicia sesion.'''

        extras.limpiar_pantalla()
        print("Iniciar sesión: ")
        email = input("Email: ")
        clave = self.ingresar_clave("Contraseña: ")
        if email == "@admin" and clave == clave_encriptada("123")):
            self.menu_abm_producto()
        elif validador.valida_email(email) and clave:
            self.comprobar_login(email, clave)
        elif email:
            print("No es un email válido.")
        input()



    def comprobar_login(self, email, clave):
        '''Comprueba los datos ingreados por el usuario con los registrados en la base de datos.

        Trae datos de db. Si el email no se encuentra en la base de datos se informa
        al usuario y vuelve a menu_inicio(). En caso que el email exista, se comprueba
        si las claves concuerdan y se procede a inicializar el usuario'''

        datos_db = self.db.get_datos_login(email)
        if datos_db:
            if validador.valida_clave_correcta(clave, datos_db[0]):
                datos_usuario = self.db.get_usuario_segun_id(datos_db[1])
                self.usuario = Usuario(*datos_usuario)
                print("Inicio de sesión exitoso")
            else:
                print("Contraseña incorrecta")
        else:
            print("No se encuentra registro de", email)



    def registrar_usuario(self):
        '''Registro de usuario

        Muestra en pantalla los datos que tiene que completar el usuario para registrarse'''

        usuario = self.formulario.nuevo_usuario()
        datos_login = self.db.get_datos_login(usuario.get_email())
        if datos_login:
            print("Ese email ya se encuentra registrado!")
        else:
            self.db.registrar_usuario(usuario)
            print("Usuario registrado!")
        input()



    def recuperar_contrasenia(self):
        '''Imprime un mensaje'''

        extras.limpiar_pantalla()
        print("Recuperar contraseña:")
        email = input("Ingrese su email: ")
        datos_usuario = self.db.get_datos_login(email)
        if datos_usuario:
            print(clave_desencriptada(datos_usuario[0]))
        else:
            print("No se encuentra ese email")
        input()



    def menu_usuario(self):
        '''Menu usuario

        Permite al usuario modificar acceder a otras funciones relacionadas a su perfil'''

        while self.usuario:
            extras.limpiar_pantalla()
            print(self.usuario.ficha_usuario())
            print("""Menu Usuario
[1] Configuracion perfil
[2] Ver catálogo
[3] Ver carrito
[x] Cerrar sesión""")
            rta = input("-> ")
            if rta == "1":
                self.menu_perfil()
            elif rta == "2":
                self.menu_catalogo()
            elif rta == "3":
                self.menu_carrito()
            elif rta == "x":
                self.usuario = None
                return



    def menu_perfil(self):
        '''Menu de configuracion de perfil

        Permite al usuario acceder a distintas funciones para modificar sus datos o eliminar su cuenta'''

        while self.usuario:
            extras.limpiar_pantalla()
            print(self.usuario.ficha_usuario())
            print("""Menu:
[1]Modificar nombre
[2]Modificar apellido
[3]Modificar email
[4]Modificar clave
[5]Modificar telefono
[6]Modificar direccion
[7]Eliminar cuenta
[x]Volver""")
            rta = input("-> ")
            if rta == "1":
                self.modificar_nombre()
            elif rta == "2":
                self.modificar_apellido()
            elif rta == "3":
                self.modificar_email()
            elif rta == "4":
                self.modificar_clave()
            elif rta == "5":
                self.modificar_telefono()
            elif rta == "6":
                self.modificar_direccion()
            elif rta == "7":
                self.eliminar_cuenta()
            elif rta == "x":
                return



    def modificar_nombre(self):
        '''Modificar nombre del usuario'''

        extras.limpiar_pantalla()
        nombre = input("Nuevo nombre: ")
        if self.consiente_cambio():
            self.usuario.set_nombre(nombre)
            self.db.actualizar_usuario_nombre(self.usuario)
            print("-cambios realizados-")
        else:
            print("-cambios descartados-")
        input()



    def modificar_apellido(self):
        '''Modificar apellido del usuario'''

        extras.limpiar_pantalla()
        apellido = input("Nuevo apellido: ")
        if self.consiente_cambio():
            self.usuario.set_apellido(apellido)
            self.db.actualizar_usuario_apellido(self.usuario)
            print("-cambios realizados-")
        else:
            print("-cambios descartados-")
        input()


    def modificar_email(self):
        '''Modificar email del usuario'''

        extras.limpiar_pantalla()
        email = input("Nuevo email: ")
        while not validador.valida_email(email):
            print("Ese mail no es correcto...")
            email = input("Nuevo email:")
        if not self.db.get_datos_login(email):
            if self.consiente_cambio():
                self.usuario.set_email(email)
                self.db.actualizar_usuario_email(self.usuario)
                print("-cambios realizados-")
            else:
                print("-cambios descartados-")
        else:
            print("Ese email se encuentra registrado.")
        input()



    def modificar_clave(self, recuperar = False):
        '''Modificar clave del usuario'''

        etras.limpiar_pantalla()
        clave0 = self.ingresar_clave("Nueva clave: ")
        clave1 = self.ingresar_clave("Repita la clave:")
        if clave0 == clave1:
            if recuperar:
                self.usuario.set_clave(clave0)
                self.db.actualizar_usuario_clave(self.usuario)
            else:
                clave2 = getpass("Ingrese su clave actual: ")
                if clave2 == usuario.get_clave():
                    self.usuario.set_clave(clave0)
                    self.db.actualizar_usuario_clave(self.usuario)
                else:
                    print("Contraseña incorrecta")
        else:
            print("Las contraseñas no coinciden.")
        input()





    def modificar_telefono(self):
        '''Modificar telefono del usuario'''

        extras.limpiar_pantalla()
        telefono = input("Nuevo telefono: ")
        if telefono.isdigit():
            if self.consiente_cambio():
                self.usuario.set_telefono(telefono)
                self.db.actualizar_usuario_telefono(self.usuario)
            print("-cambios realizados-")
        else:
            print("-cambios descartados-")
        input()



    def modificar_direccion(self):
        '''Modificar direccion predeterminada del usuario'''





    def eliminar_cuenta(self):
        '''Elimina usuario de la aplicacion y de la base de datos'''

        limpiar_pantalla()
        print("¿Quiere eliminar su cuenta?")
        if input("Confirmar (s/n): ") == "s":
            if input("Esta acción no se puede deshacer (s/n): ") == 's':
                self.db.eliminar_usuario(self.usuario)
                self.usuario = None



    def menu_catalogo(self):
        '''Permite filtrar y elegir los productos en catalogo'''

        while True:
            limpiar_pantalla()
            print("""Catálogo:
[1] Ver todo
[2] Buscar por nombre
[3] Filtrar
[x] Volver
""")
            rta = input("-> ")
            if rta == "1":
                self.listar_productos()
                self.seleccionar_producto()
            if rta == "2":
                self.buscar_productos_por_nombre()
            if rta == "3":
                self.filtrar_productos()
            elif rta == "x":
                return



    def listar_productos(self):
        '''Muestra los productos en pantalla'''

        extras.limpiar_pantalla()
        print("Lista de productos:")
        for producto in self.productos:
            print(producto)



    def seleccionar_producto(self):
        '''Selecciona un producto según su id'''

        print("Ingrese nº de producto:")
        producto_id = input("-> ")
        datos_producto = self.db.get_producto_segun_id(producto_id)
        if datos_producto:
            self.producto = Producto(*datos_producto)
            print(self.producto.ficha_producto())
        else:
            self.producto = None
            print("No se pudo seleccionar un producto")
        input()




    def buscar_productos_por_nombre(self):
        '''Carga un producto de la db buscandolo por su nombre'''





    def filtrar_productos(self):
        '''Trae la listra de produtos filtrada'''





    def ver_carrito(self):
        '''Ver los productos que se encuentran en carritos'''

        while self.usuario:
            extras.limpiar_pantalla()
            input()
            return



    def ver_compras(self):
        '''Ve las compras realizadas por el usuario'''

        while self.usuario:
            extras.limpiar_pantalla()
            input()
            return



    def menu_abm_producto(self):
        '''Menu de Alta Baja Modificacion de Productos'''

        while True:
            extras.limpiar_pantalla()
            print(""""Que accion desea realizar:
[1] Agregar producto
[2] Modificar producto
[3] Eliminar producto
[4] Lista de productos
[x] Volver""")
            rta = input("-> ")
            if rta == "x":
                return
            elif rta == "1":
                self.registrar_producto()
            elif rta == "4":
                self.listar_productos()
            else:
                producto = self.buscar_producto_por_nombre()
                if producto:
                    if rta == "3":
                        self.eliminar_producto(producto)
                    if opc=="2":
                        self.menu_modificar_producto(producto)

    def registrar_producto(self):
        '''Registro de producto

        Llama al formulario, crea un producto y lo registra en la base de datos.'''

        producto = self.formulario.nuevo_producto(self.marcas, self.categorias)
        self.db.registrar_producto(producto)
        print("Producto registrado")
        input()




    def eliminar_producto(self):
        '''Elimina un producto de la aplicación y de la base de datos.'''






    def menu_modificar_producto(self):
        '''Permite acceder a las funciones para modificar los datos de un producto'''