from modulos.db import *
import mysql.connector
from modulos.dbconf import conf, queries
from modulos.usuarios import Usuario, encriptar
from modulos.productos import Producto
from modulos.compras import Compra
import base64
from getpass import getpass
