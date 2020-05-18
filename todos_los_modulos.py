import base64
import mysql.connector
from getpass import getpass
from modulos.db import Ecommerce_db
from modulos.dbconf import conf, queries
from modulos.usuarios import Usuario, encriptar
from modulos.productos import Producto
from modulos.compras import Compra
