class Categoria:
    def __init__(self,categoria_id,nombre):
        self.set_nombre(nombre)
        self.set_categoria_id(categoria_id)

    def set_categoria_id(self, categoria_id):
        self.categoria_id = categoria_id
        return 1
    def get_categoria_id(self):
        return self.categoria_id

    def set_nombre(self, nombre):
        self.nombre = nombre.title()
        return 1
    def get_nombre(self):
        return self.nombre
