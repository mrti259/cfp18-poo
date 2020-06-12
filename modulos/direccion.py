class Direccion:
    def __init__(self, direccion_id=0, calle="", altura=0, codigo_postal="", ciudad_id=0, provincia_id=0, pais_id=0, ciudad=None):
        '''Se inicializa con datos válidos. Despues se settea un objeto ciudad'''
        self.direccion_id=direccion_id
        self.calle=calle
        self.altura=altura
        self.codigo_postal=codigo_postal
        self.ciudad_id=ciudad_id
        self.provincia_id=provincia_id
        self.pais_id=pais_id
        self.ciudad=ciudad

    def __str__(self):
        '''Da formato a una direccion para ser pasado como cadena'''

        return (f"{self.get_calle()} {self.get_altura()} {self.get_codigo_postal()}, ({self.get_ciudad_id()}) ")


    def ficha_direccion(self):
        '''Da formato a una direccion para pasarlo como una ficha más informativa'''

        return (f"""\
Direccion:
==========
Calle y altura: {self.get_calle()} {self.get_altura()}
Codigo Postal: {self.get_codigo_postal()}
Ciudad: {("aca tendria que figurar la ciudad")}
""")



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



    def set_provincia_id(self, provincia_id):
        self.provincia_id = provincia_id
        return 1

    def get_provincia_id(self):
        return self.provincia_id


    def set_pais_id(self, pais_id):
        self.pais_id = pais_id
        return 1

    def get_pais_id(self):
        return self.pais_id
