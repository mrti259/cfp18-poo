from datetime import date, datetime
from .direccion import Direccion
from .extras import *
from .producto import Producto
from .usuario import Usuario

class Formulario:
    '''Contiene distintos formularios para la creación de objetos'''

    def __init__(self, db):
        self.ahora = datetime.now
        self.hoy = date.today
        self.get_paises = db.get_todos_los_paises
        self.get_provincias_segun_pais = db.get_provincias_segun_pais
        self.get_ciudades_segun_provincia = db.get_ciudades_segun_provincia
        self.get_marcas = db.get_todas_las_marcas
        self.get_categorias = db.get_todas_las_categorias



    def listar(self, lista):
        '''Despliega la lista de opciones disponibles para un campo'''

        i = 1
        for opcion in lista:
            print(f"{i}) {opcion}")
            i+=1



    def seleccionar(self, lista):
        """Devuelve uno de los objetos de la lista"""

        self.listar(lista)
        opc = input("-> ")
        if opc.isdigit() and int(opc) >= 0 and int(opc) <= len(lista):
            return lista[int(opc)-1]
        return self.seleccionar



    def nuevo_producto(self):
        '''Formulario que se mostrara cuando se desee crear un nuevo producto'''

        producto = Producto()
        modificadores = {
            "Nombre": producto.set_nombre,
            "Descripcion": producto.set_descripcion,
            "Precio": producto.set_precio,
            "Stock": producto.set_stock,
        }
        for campo, setter in modificadores.items():
            limpiar_pantalla()
            print(producto.ficha_producto())
            dato = input("->" + campo + ": ")
            while not setter(dato):
                dato = input("->" + campo + ": ")
        producto.set_categoria(self.seleccionar(self.get_categorias()))
        producto.set_marca(self.seleccionar(self.get_marcas()))
        producto.set_fecha_de_publicacion(self.ahora())
        producto.set_fecha_de_ultima_modificacion(self.ahora())
        limpiar_pantalla()
        print(producto.ficha_producto())
        input("-> Enviar")
        return producto



    def nuevo_usuario(self):
        '''Formulario que se mostrara cuando se desee crear un nuevo usuario'''

        usuario = Usuario(fecha_de_nacimiento=self.hoy())
        modificadores = {
            "Email": usuario.set_email,
            "Clave": usuario.set_clave,
            "Nombre": usuario.set_nombre,
            "Apellido": usuario.set_apellido,
            "Fecha de nacimiento": usuario.set_fecha_de_nacimiento,
            "DNI": usuario.set_dni,
            "Telefono": usuario.set_telefono,
        }
        for campo, setter in modificadores.items():
            limpiar_pantalla()
            print(usuario.ficha_usuario())
            if campo == "Clave":
                setter(ingresar_clave("-> " + campo +": ", True))
            elif campo == "Fecha de nacimiento":
                print("-> " + campo + ":")
                fecha = ingresar_fecha()
                setter(fecha)
            else:
                dato = input("->" + campo + ": ")
                while not setter(dato):
                    dato = input("->" + campo + ": ")
        usuario.set_direccion(self.nueva_direccion())
        usuario.set_fecha_de_registro(self.ahora())
        limpiar_pantalla()
        print(usuario.ficha_usuario())
        input("-> Enviar")
        return usuario



    def nueva_direccion(self):
        '''Formulario que se mostrara cuando se desee registrar una nueva direccion'''

        direccion = Direccion()
        modificadores = {
            "Calle": direccion.set_calle,
            "Altura": direccion.set_altura,
            "Codigo postal": direccion.set_codigo_postal,
        }
        for campo, setter in modificadores.items():
            limpiar_pantalla()
            print(direccion.ficha_direccion())
            dato = input("-> " + campo + ": ")
            while not setter(dato):
                dato = input("-> " + campo + ": ")
        pais = self.seleccionar(self.get_paises())
        provincia = self.seleccionar(self.get_provincias_segun_pais(pais))
        ciudad = self.seleccionar(self.get_ciudades_segun_provincia(provincia))
        direccion.set_ciudad(ciudad)
        limpiar_pantalla()
        print(direccion.ficha_direccion())
        input("-> Enviar")
        return direccion
