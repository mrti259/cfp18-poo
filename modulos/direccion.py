from Ecommerce_db import get_ciudad_segun_id
class Direccion:
    def __init__(self, direccion_id, calle, altura, codigo_postal, ciudad_id):
        self.set_direccion_id(direcion_id)
        self.set_calle(calle)
        self.set_altura(altura)
        self.set_codigo_postal(codigo_postal)
        self.set_ciudad_id(ciudad_id)

    def __str__(self):
        '''Da formato a una direccion para ser pasado como cadena'''

        return (f"{self.get_calle()}. {self.get_altura()}")


    def ficha_direccion(self):
        '''Da formato a una direccion para pasarlo como una ficha más informativa'''

        return (f"""\
direccion:
========
Calle y altura: {self.get_calle()} {self.get_altura()}
Codigo Postal: {self.get_codigo_postal()}
Ciudad: {get_ciudad_segun_id(self.get_ciudad_id())}
""")
#fijarse si el get_ciudad_segun_id anda bien porque el select devuelve mas de un valor



    def set_direccion_id(self, direccion_id):
        self.direccion_id = direccion_id
        return 1
    def get_direccion_id(self):
        return self.direccion_id

    def set_calle(self, calle):
        self.calle = calle.title()
        return 1
    def get_calle(self):
        return self.calle

    def set_altura(self, altura):
        self.altura = altura
        return 1
    def get_altura(self):
        return self.altura

    def set_codigo_postal(self, codigo_postal):
        self.codigo_postal = codigo_postal
        return 1
    def get_codigo_postal(self):
        return self.codigo_postal

    def set_ciudad_id(self, ciudad_id):
        self.ciudad_id = ciudad_id
        return 1
    def get_ciudad_id(self):
        return self.ciudad_id
