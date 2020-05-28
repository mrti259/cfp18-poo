class Categoria:
    def __init__(self,categoria_id,nombre):
        self.set_nombre(nombre)
        self.set_categoria_id(categoria_id)
        self.errores = {}

    def set_categoria_id(self, categoria_id):
        self.categoria_id = categoria_id
    def get_categoria_id(self):
        return self.categoria_id

    def set_nombre(self, nombre):
        if nombre.isalnum():
            self.nombre = nombre.title()
        else:
            self.errores["nombre"] = "No es un nombre válido"
    def get_nombre(self):
        return self.nombre
