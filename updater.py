from todos_los_modulos import *

#encriptar claves
db = Ecommerce(conf)

lista_usuarios = db.todos_los_usuarios()

for datos in lista_usuarios:
    usuario = Usuario(*datos)
    print(datos)
    # ~ db.actualizar_usuario_direccion_id(usuario)
