from modulos import Ecommerce_app
from dbconf import dbconf

app = Ecommerce_app(dbconf)
app.menu_inicio()
# app.registrar_producto()
# app.registrar_usuario()
