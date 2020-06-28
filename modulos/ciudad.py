class Ciudad:
    def __init__(self, ciudad_id=0, nombre="", provincia_id=0):
        self.ciudad_id = ciudad_id
        self.nombre = nombre
        self.provincia_id = provincia_id
        self.provincia = None



    def __str__(self):
        return (self.get_nombre())



    def set_ciudad_id(self,ciudad_id):
        self.ciudad_id = ciudad_id
        return 1

    def get_ciudad_id(self):
        return self.ciudad_id



    def set_nombre(self, nombre):
        self.nombre = nombre
        return 1

    def get_nombre(self):
        return self.nombre



    def set_provincia_id(self, provincia_id):
        self.provincia_id = provincia_id
        return 1

    def get_provincia_id(self):
        return self.provincia_id



    def set_provincia(self, provincia):
        self.provincia = provincia
        self.set_provincia_id(provincia.get_provincia_id())
        return 1

    def get_provincia(self):
        return self.provincia
