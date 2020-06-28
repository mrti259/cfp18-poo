class Marca:
    def __init__(self,marca_id,nombre):
        self.set_marca_id(marca_id)
        self.set_nombre(nombre)


    def __str__(self):
        return (f"({self.get_marca_id}) {self.get_nombre()}")



    def set_marca_id(self, marca_id):
        self.marca_id = marca_id
        return 1

    def get_marca_id(self):
        return self.marca_id



    def set_nombre(self, nombre):
        self.nombre = nombre.title()
        return 1

    def get_nombre(self):
        return self.nombre
