import base64
import mysql.connector
from datetime import date, datetime
from getpass import getpass
from validate_email import validate_email
from modulos.db import Ecommerce_db
from modulos.dbconf import conf, queries
from modulos.usuarios import Usuario, encriptar
from modulos.productos import Producto
from modulos.compras import Compra
