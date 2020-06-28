from datetime import datetime
from .carrito import Carrito
from .compra import Compra
from .categoria import Categoria
from .direccion import Direccion
from .ecommerce_db import Ecommerce_db
from .extras import *
from .formulario import Formulario
from .marca import Marca
from .producto import Producto
from .usuario import Usuario
from .validador import *



class Ecommerce_app:

    def __init__(self, dbconf):
        '''Se inicializa la base de datos. Usuario y Producto se cargan mediante los menus'''
        self.db = Ecommerce_db(dbconf)
        self.usuario = None
        self.producto = None
        self.get_productos = self.db.get_todos_los_productos
        self.get_marcas = self.db.get_todas_las_marcas
        self.get_categorias = self.db.get_todas_las_categorias
        self.formulario = Formulario(self.db)



    def menu_inicio(self):
        '''Menu de inicio de sesion

        Da al usuario la opcion de iniciar sesion con un email y clave previamente
        registrado, la opcion de recuperar la contraseña en caso de olvidarla o la
        de registrar un nuevo usuario.'''

        while True:
            limpiar_pantalla()
            print("""\
Menu de inicio:
===============
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

        limpiar_pantalla()
        print("""\
Iniciar sesión:
===============""")
        email = input("Email: ")
        clave = ingresar_clave("Contraseña: ")
        if valida_administrador(email, clave):
            self.menu_administrador()
        elif valida_email(email) and clave:
            self.comprobar_login(email, clave)
        elif email:
            print("No es un email válido.")
        espera()



    def comprobar_login(self, email, clave):
        '''Comprueba los datos ingreados por el usuario con los registrados en la base de datos.

        Trae datos de db. Si el email no se encuentra en la base de datos se informa
        al usuario y vuelve a menu_inicio(). En caso que el email exista, se comprueba
        si las claves concuerdan y se procede a inicializar el usuario'''

        datos_db = self.db.get_login_usuario(email)
        if datos_db:
            if valida_clave_correcta(clave, datos_db[0]):
                self.usuario = self.db.get_usuario_segun_id(datos_db[1])
                print("Inicio de sesión exitoso")
            else:
                print("Contraseña incorrecta")
        else:
            print("No se encuentra registro de", email)



    def registrar_usuario(self):
        '''Registro de usuario

        Muestra en pantalla los datos que tiene que completar el usuario para registrarse'''

        usuario = self.formulario.nuevo_usuario()
        datos_login = self.db.get_login_usuario(usuario.get_email())
        if datos_login:
            print("Ese email ya se encuentra registrado!")
        else:
            self.db.registrar_direccion(usuario.get_direccion())
            usuario.set_direccion_id(usuario.get_direccion())
            self.db.registrar_usuario(usuario)
            print("Usuario registrado!")
        espera()



    def recuperar_contrasenia(self):
        '''Imprime un mensaje'''

        limpiar_pantalla()
        print("Recuperar contraseña:")
        email = input("Ingrese su email: ")
        datos_usuario = self.db.get_login_usuario(email)
        if datos_usuario:
            print(clave_desencriptada(datos_usuario[0]))
        else:
            print("No se encuentra ese email")
        espera()



    def menu_usuario(self):
        '''Menu usuario

        Permite al usuario modificar acceder a otras funciones relacionadas a su perfil'''

        while self.usuario:
            limpiar_pantalla()
            print(self.usuario.ficha_usuario())
            print("""\
Menu Usuario:
=============
[1] Configuracion perfil
[2] Ver catálogo
[3] Ver carrito/Comprar
[4] Ver compras
[x] Cerrar sesión""")
            rta = input("-> ")
            if rta == "1":
                self.menu_perfil()
            elif rta == "2":
                self.menu_catalogo()
            elif rta == "3":
                producto_en_carrito = self.seleccionar_carrito()
                if producto_en_carrito:
                    self.opciones_carrito(producto_en_carrito)
            elif rta == "4":
                self.ver_compras(self.usuario)
            elif rta == "x":
                self.usuario = None



    def menu_perfil(self):
        '''Menu de configuracion de perfil

        Permite al usuario acceder a distintas funciones para modificar sus datos o eliminar su cuenta'''

        while self.usuario:
            limpiar_pantalla()
            print(self.usuario.ficha_usuario())
            print("""\
Menu:
=====
[1] Modificar nombre
[2] Modificar apellido
[3] Modificar email
[4] Modificar clave
[5] Modificar dni
[6] Modificar telefono
[7] Modificar direccion
[8] Eliminar cuenta
[x] Volver""")
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
                self.modificar_dni()
            elif rta == "6":
                self.modificar_telefono()
            elif rta == "7":
                self.modificar_direccion()
            elif rta == "8":
                self.eliminar_cuenta()
            elif rta == "x":
                return



    def modificar_nombre(self):
        '''Modificar nombre del usuario'''

        nombre = input("Nuevo nombre: ")
        if consiente_cambio() and self.usuario.set_nombre(nombre):
            self.db.actualizar_usuario_nombre(self.usuario)
            print("-cambios realizados-")
        else:
            print("-cambios descartados-")
        espera()



    def modificar_apellido(self):
        '''Modificar apellido del usuario'''

        apellido = input("Nuevo apellido: ")
        if consiente_cambio() and self.usuario.set_apellido(apellido):
            self.db.actualizar_usuario_apellido(self.usuario)
            print("-cambios realizados-")
        else:
            print("-cambios descartados-")
        espera()


    def modificar_email(self):
        '''Modificar email del usuario'''

        email = input("Nuevo email: ")
        if not self.db.get_login_usuario(email):
            if consiente_cambio() and self.usuario.set_email(email):
                self.db.actualizar_usuario_email(self.usuario)
                print("-cambios realizados-")
            else:
                print("-cambios descartados-")
        else:
            print("Ese email se encuentra registrado.")
        espera()



    def modificar_clave(self, recuperar = False):
        '''Modificar clave del usuario'''

        clave0 = ingresar_clave("Nueva clave: ", check=True)
        clave1 = ingresar_clave("Repita la clave:")
        if clave0 == clave1:
            if recuperar:
                self.usuario.set_clave(clave0)
                self.db.actualizar_usuario_clave(self.usuario)
            else:
                clave2 = ingresar_clave("Ingrese su clave actual: ")
                if valida_clave_correcta(clave2, self.usuario.get_clave()):
                    self.usuario.set_clave(clave0)
                    self.db.actualizar_usuario_clave(self.usuario)
                else:
                    print("Contraseña incorrecta")
        else:
            print("Las contraseñas no coinciden.")
        espera()



    def modificar_dni(self):
        '''Modificar dni del usuario'''

        dni = input("Nuevo DNI: ")
        if consiente_cambio() and self.usuario.set_dni(dni):
            self.db.actualizar_usuario_dni(self.usuario)
            print("-cambios realizados-")
        else:
            print("-cambios descartados-")
        espera()



    def modificar_telefono(self):
        '''Modificar telefono del usuario'''

        telefono = input("Nuevo telefono: ")
        if telefono.isdigit():
            if consiente_cambio():
                self.usuario.set_telefono(telefono)
                self.db.actualizar_usuario_telefono(self.usuario)
            print("-cambios realizados-")
        else:
            print("-cambios descartados-")
        espera()



    def modificar_direccion(self):
        '''Modificar direccion predeterminada del usuario'''

        while self.usuario.get_direccion():
            limpiar_pantalla()
            print(self.usuario.ficha_usuario())
            print(self.usuario.get_direccion().ficha_direccion())
            print("""
Modificar direccion:
====================
[1] Registrar otra direccion
[x] Volver""")
            rta = input("->")
            if rta == "x":
                return
            elif rta == "1":
                direccion = self.registrar_direccion()
                self.usuario.set_direccion(direccion)
                self.db.actualizar_usuario_direccion_id(self.usuario)



    def registrar_direccion(self):
        '''Registro de direccion

        Muestra en pantalla los datos que tiene que completar el usuario para una direccion'''

        direccion = self.formulario.nueva_direccion()
        self.db.registrar_direccion(direccion)
        print("Direccion registrada!")
        espera()
        return(direccion)



    def eliminar_cuenta(self):
        '''Elimina usuario de la aplicacion y de la base de datos'''

        print("¿Quiere eliminar su cuenta?")
        if input("Confirmar (s/n): ") == "s":
            if input("Esta acción no se puede deshacer (s/n): ") == 's':
                self.db.eliminar_usuario(self.usuario)
                self.usuario = None



    def menu_catalogo(self):
        '''Permite filtrar y elegir los productos en catalogo'''

        while True:
            limpiar_pantalla()
            print("""\
Catálogo:
=========
[1] Ver todo
[2] Buscar por nombre
[3] Filtrar
[x] Volver""")
            rta = input("-> ")
            if rta == "1":
                producto = self.seleccionar_producto(self.db.get_todos_los_productos())
            elif rta == "2":
                producto = self.buscar_productos_por_nombre()
            elif rta == "3":
                self.filtrar_productos()
            elif rta == "x":
                return

            if producto and self.usuario:
                self.agregar_al_carrito(producto)
            elif producto:
                self.producto = producto



    def listar_productos(self, productos):
        '''Muestra los productos en pantalla'''

        print("""
Lista de productos:
===================""")
        i = 1
        for prod in productos:
            print(f"{i}) {prod}")
            i+=1



    def seleccionar_producto(self, productos):
        '''Selecciona un producto según su id'''

        self.listar_productos(productos)
        num = input("-> ")
        if num.isdigit() and int(num) >= 1 and int(num) <= len(productos):
            print("Se ha seleccionado un producto")
            espera()
            return productos[int(num)-1]
        print("No se pudo seleccionar un producto")
        espera()



    def buscar_productos_por_nombre(self):
        '''Carga un producto de la db buscandolo por su nombre'''

        nombre = ("%" + input("Nombre: ") + "%")
        productos = self.db.get_productos_segun_nombre(nombre)
        if productos:
            print("Se obtuvieron los siguientes resultados:")
            self.seleccionar_producto(productos)



    def filtrar_productos(self):
        '''Filtra los productos por marca o categoria'''



    def agregar_al_carrito(self, producto):
        '''Muestra el producto en pantalla y permite agregar al carrito'''

        carrito = Carrito(0, self.usuario.get_usuario_id(), producto.get_producto_id(), 0)
        carrito.set_producto(producto)
        print(producto.ficha_producto())
        print("¿Quiere agregar al carrito?")
        cant = input("Ingrese una cantidad para agregar: ")
        if carrito.set_cantidad(cant):
            print("Se ha añadido al carrito correctamente.")
            self.db.registrar_carrito(carrito)
        else:
            print("No se ha añadido al carrito.")
        espera()



    def ver_carrito(self):
        '''Ver los productos que se encuentran en carritos'''

        limpiar_pantalla()
        print(self.usuario.ficha_usuario())
        print("""
Productos en carrito:
=====================""")
        i=1
        self.usuario.cargar_carrito(self.db.get_carrito_segun_usuario(self.usuario))
        for carrito in self.usuario.get_carrito():
            print(f"[{i}] {carrito}")
            i+=1



    def seleccionar_carrito(self):
        '''Selecciona alguno de los productos que se encuentre en el carrito del usuario'''

        self.ver_carrito()
        carrito = self.usuario.get_carrito()
        num = input("Ingrese nº para modificar/comprar: ")
        if not num.isdigit():
            num = -1
        elif int(num) >= 1 and int(num) <= len(carrito):
            return carrito[int(num)-1]
        print("No se ha seleccionado ningún producto.")
        espera()



    def opciones_carrito(self, carrito):
        '''Permite comprar o modificar un producto seleccionado en el carrito del usuario'''

        print("""
Opciones:
=========
[1] Comprar
[2] Modificar/Eliminar
[x] Volver""")
        rta = input("->")
        if rta == "x":
            return
        elif rta == "1":
            self.comprar(carrito)
        elif rta == "2":
            self.modificar_carrito(carrito)



    def modificar_carrito(self, carrito):
        '''Permite modificar los productos que se encuentran en carritos'''

        print(carrito)
        print("Ingrese una nueva cantidad para modificar, 0 para eliminar: ")
        rta = input("Cant:")
        if rta.isdigit():
            if rta == "0":
                self.db.eliminar_carrito(carrito)
            elif carrito.set_cantidad(rta):
                self.db.actualizar_carrito_cantidad(carrito)
            else:
                print("No se pudo actualizar")
        self.usuario.cargar_carrito(self.db.get_carrito_segun_usuario(self.usuario))
        espera()



    def comprar(self, carrito):
        '''Registra la compra'''

        precio = carrito.producto.get_precio() * carrito.get_cantidad()
        compra = Compra(0, self.usuario.get_usuario_id(), self.usuario.get_direccion_id(), carrito.get_producto_id(), carrito.get_cantidad(), precio, datetime.now())
        compra.set_producto(carrito.get_producto())
        print("La compra se enviará a", self.usuario.get_direccion())
        print("Actualice su perfil para modificar esto\n")
        print("¿Quiere confirmar la compra de", compra, "?")
        if consiente_cambio():
            self.db.registrar_compra(compra)
            self.db.eliminar_carrito(carrito)
            print("Gracias por su compra!")
        else:
            print("El producto va a permanecer en el carrito")
        espera()



    def ver_compras(self, usuario):
        '''Ve las compras realizadas por el usuario'''

        limpiar_pantalla()
        print(usuario.ficha_usuario())
        print("""
Productos comprados:
====================""")
        usuario.cargar_compras(self.db.get_compras_segun_usuario(usuario))
        i=1
        for compra in usuario.get_compras():
            print(f"{i}) {compra}")
            i+=1
        input()



    def menu_administrador(self):
        '''Menu de administrador

        Permite acceder a menus de ABCM'''

        while not self.usuario:
            limpiar_pantalla()
            print("""\
Menu Administrador:
===================
[1] Producto
[2] Ver compras
[3] Ver usuarios
[x] Salir""")
            rta = input("-> ")
            if rta == "1":
                self.menu_abcm_producto()
            elif rta == "2":
                for usuario in self.db.get_todos_los_usuarios():
                    self.ver_compras(usuario)
            elif rta == "3":
                for usuario in self.db.get_todos_los_usuarios():
                    print(usuario)
                input()
            elif rta == "x":
                return



    def menu_abcm_producto(self):
        '''Menu de Alta Baja Consultas Modificacion de Productos'''

        while True:
            limpiar_pantalla()
            print("""\
Que accion desea realizar:
==========================
[1] Agregar producto
[2] Modificar producto
[3] Eliminar producto
[x] Volver""")
            rta = input("-> ")
            if rta == "x":
                return
            elif rta == "1":
                self.registrar_producto()
            elif rta == "2" or rta == "3":
                self.producto = self.seleccionar_producto(self.db.get_todos_los_productos())
                if self.producto:
                    if rta == "2":
                        self.menu_modificar_producto()
                    else:
                        self.eliminar_producto()



    def registrar_producto(self):
        '''Registro de producto

        Llama al formulario, crea un producto y lo registra en la base de datos.'''

        producto = self.formulario.nuevo_producto()
        self.db.registrar_producto(producto)
        print("Producto registrado")
        espera()



    def eliminar_producto(self):
        '''Elimina un producto de la aplicación y de la base de datos.'''

        print("¿Quiere eliminar el producto?")
        if input("Confirmar (s/n): ") == "s":
            if input("Esta acción no se puede deshacer (s/n): ") == 's':
                self.db.eliminar_producto(self.producto)
                self.producto = None
        espera()



    def menu_modificar_producto(self):
        '''Permite acceder a las funciones para modificar los datos de un producto'''

        while self.producto:
            limpiar_pantalla()
            print(self.producto.ficha_producto())
            print("""
Menu Producto:
==============
[1] Modificar nombre
[2] Modificar descripcion
[3] Modificar precio
[4] Modificar stock
[x] Volver
""")
            rta = input("->")
            if rta == "x":
                self.producto = None
            elif rta == "1":
                self.modificar_nombre_producto()
            elif rta == "2":
                self.modificar_descripcion()
            elif rta == "3":
                self.modificar_precio()
            elif rta == "4":
                self.modificar_stock()



    def modificar_nombre_producto(self):
        '''Modifica el nombre de un producto'''

        nombre = input("Nuevo nombre: ")
        if consiente_cambio() and self.producto.set_nombre(nombre):
            fecha_de_ultima_modificacion = str(datetime.now())
            self.producto.set_fecha_de_ultima_modificacion(fecha_de_ultima_modificacion)
            self.db.actualizar_producto_nombre(self.producto)
        else:
            print("-cambios descartados-")
        espera()



    def modificar_descripcion(self):
        '''Modifica la descripcion de un producto'''

        descripcion = input("Nueva descripcion: ")
        if consiente_cambio() and self.producto.set_descripcion(descripcion):
            fecha_de_ultima_modificacion = str(datetime.now())
            self.producto.set_fecha_de_ultima_modificacion(fecha_de_ultima_modificacion)
            self.db.actualizar_producto_descripcion(self.producto)
        else:
            print("-cambios descartados-")
        espera()



    def modificar_precio(self):
        '''Modifica el precio de un producto'''

        precio = float(input("Nuevo precio: "))
        if consiente_cambio() and self.producto.set_precio(precio):
            fecha_de_ultima_modificacion = str(datetime.now())
            self.producto.set_fecha_de_ultima_modificacion(fecha_de_ultima_modificacion)
            self.db.actualizar_producto_precio(self.producto)
        else:
            print("-cambios descartados-")
        espera()



    def modificar_stock(self):
        '''Modifica el stock de un producto'''

        stock = input("Nuevo stock: ")
        if consiente_cambio() and producto.set_stock(stock):
            fecha_de_ultima_modificacion = str(datetime.now())
            producto.set_fecha_de_ultima_modificacion(fecha_de_ultima_modificacion)
            db.actualizar_producto_stock(self.producto)
        else:
            print("-cambios descartados-")
        espera()
