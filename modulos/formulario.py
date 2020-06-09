from datetime import date, datetime
from .producto import Producto
from .usuario import Usuario
from .direccion import Direccion
from .extras import limpiar_pantalla

class Formulario:
    '''Contiene distintos formularios para la creación de objetos'''

    def __init__(self):
        self.ahora = datetime.now
        self.hoy = date.today



    def listar_opciones(self, opciones):
        '''Despliega las opciones disponibles para un campo'''

        for o in opciones:
            print(o)



    def nuevo_producto(self, marcas, categorias):
        '''Formulario que se mostrara cuando se desee crear un nuevo producto'''

        producto = Producto(fecha_de_publicacion=self.ahora(), fecha_de_ultima_modificacion=self.ahora())
        modificadores = {
            "Nombre": producto.set_nombre,
            "Descripcion": producto.set_descripcion,
            "Precio": producto.set_precio,
            "Stock": producto.set_stock,
            "Marca_id": producto.set_marca_id,
            "Categoria_id": producto.set_categoria_id,
        }
        i = len(modificadores)
        for campo, setter in modificadores.items():
            limpiar_pantalla()
            print(producto.ficha_producto())
            if campo == "Marca_id":
                self.listar_opciones(marcas)
            elif campo == "Categoria_id":
                self.listar_opciones(categorias)
            dato = input(campo + ": ")
            while not setter(dato):
                print("No es un dato válido!")
                dato = input(campo)
        return producto



    def nuevo_usuario(self):
        '''Formulario que se mostrara cuando se desee crear un nuevo usuario'''

        usuario = Usuario()
        modificadores = {
            "Email": usuario.set_email,
            "Clave": usuario.set_clave,
            "Nombre": usuario.set_nombre,
            "Apellido": usuario.set_apellido,
            "(dd/mm/aaaa)": usuario.set_fecha_de_nacimiento,
            "DNI": usuario.set_dni,
            "Telefono": usuario.set_telefono,
            "Direccion": usuario.set_direccion_id,
        }
        i = len(modificadores)
        for campo, setter in modificadores.items():
            limpiar_pantalla()
            print(usuario.ficha_usuario())
            if campo == "(dd/mm/aaaa)":
                print("Fecha de nacimiento", end=" ")
            elif campo == "Direccion":
                self.registrar_direccion()
            dato = input(campo + ": ")
            while not setter(dato):
                print("No es un dato válido!")
                dato = input(campo)
        return usuario



    def nueva_direccion(self):
        '''Formulario que se mostrara cuando se desee registrar una nueva direccion'''
        direccion = Direccion()
