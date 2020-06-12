from datetime import date, datetime
from .categoria import Categoria
from .ciudad import Ciudad
from .direccion import Direccion
from .extras import *
from .marca import Marca
from .pais import Pais
from .producto import Producto
from .provincia import Provincia
from .usuario import Usuario

class Formulario:
    '''Contiene distintos formularios para la creación de objetos'''

    def __init__(self, db):
        self.ahora = datetime.now
        self.hoy = date.today
        self.get_paises = db.get_todos_los_paises
        self.get_provincias_segun_pais_id = db.get_provincias_segun_pais_id
        self.get_ciudades_segun_provincia_id = db.get_ciudades_segun_provincia_id
        self.get_marcas = db.get_todas_las_marcas
        self.get_categorias = db.get_todas_las_categorias



    def listar_opciones(self, opciones):
        '''Despliega las opciones disponibles para un campo'''

        for o in opciones:
            print(o)



    def nuevo_producto(self):
        '''Formulario que se mostrara cuando se desee crear un nuevo producto'''

        producto = Producto()
        marcas = [Marca(*datos) for datos in self.get_marcas()]
        categorias = [Categoria(*datos) for datos in self.get_categorias()]
        modificadores = {
            "Nombre": producto.set_nombre,
            "Descripcion": producto.set_descripcion,
            "Precio": producto.set_precio,
            "Stock": producto.set_stock,
            "Marca": producto.set_marca_id,
            "Categoria": producto.set_categoria_id,
        }
        for campo, setter in modificadores.items():
            limpiar_pantalla()
            print(producto.ficha_producto())
            if campo == "Marca":
                print("Marcas registradas:")
                self.listar_opciones(marcas)
            elif campo == "Categoria":
                print("Categorias disponibles:")
                self.listar_opciones(categorias)
            dato = input("->" + campo + ": ")
            while not setter(dato):
                dato = input("->" + campo + ": ")
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
            "Direccion": usuario.set_direccion_id,
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
            elif campo == "Direccion":
                direccion = self.nueva_direccion()
                setter(direccion.get_direccion_id())
                usuario.set_direccion(direccion)
            else:
                dato = input("->" + campo + ": ")
                while not setter(dato):
                    dato = input("->" + campo + ": ")
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
            "Pais": direccion.set_pais_id,
            "Provincia": direccion.set_provincia_id,
            "Ciudad": direccion.set_ciudad_id,
        }
        for campo, setter in modificadores.items():
            limpiar_pantalla()
            print(direccion.ficha_direccion())
            if campo == "Pais":
                paises = [Pais(*datos) for datos in self.get_paises()]
                print("Paises disponibles:")
                self.listar_opciones(paises)
            elif campo == "Provincia":
                provincias = [Provincia(*datos) for datos in self.get_provincias_segun_pais_id(direccion.get_pais_id())]
                print("Provincias disponibles:")
                self.listar_opciones(provincias)
            elif campo == "Ciudad":
                ciudades = [Ciudad(*datos) for datos in self.get_ciudades_segun_provincia_id(direccion.get_provincia_id())]
                print("Ciudades disponibles:")
                self.listar_opciones(ciudades)    
            dato = input("-> " + campo + ": ")
            while not setter(dato):
                dato = input("-> " + campo + ": ")
        limpiar_pantalla()
        print(direccion.ficha_direccion())
        input("-> Enviar")
        return direccion
