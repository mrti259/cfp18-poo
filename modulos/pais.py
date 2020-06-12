class Pais:
    def __init__(self, pais_id=0, nombre=""):
        self.pais_id = pais_id
        self.nombre = nombre



    def __str__(self):
        return (f"[{self.get_pais_id()}] {self.get_nombre()}")



    def set_pais_id(self, pais_id):
        self.pais_id = pais_id
        return 1

    def get_pais_id(self):
        return self.pais_id



    def set_nombre(self, nombre):
        self.nombre = nombre
        return 1

    def get_nombre(self):
        return self.nombre
