from modulos import Ecommerce_app, Ecommerce_db, Formulario
from dbconf import dbconf

app = Ecommerce_app(dbconf)
app.menu_inicio()
# ~ app.registrar_producto()
# ~ app.registrar_usuario()
# ~ app.registrar_direccion()
