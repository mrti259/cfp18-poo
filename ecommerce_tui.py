from modulos import Ecommerce_app, Ecommerce_db, Formulario
from dbconf import dbconf

app = Ecommerce_app(dbconf)
#app.registrar_direccion()
#app.registrar_producto()
#app.registrar_usuario()
app.menu_inicio()
