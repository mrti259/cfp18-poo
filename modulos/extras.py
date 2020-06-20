import os
import platform
from base64 import encodebytes, decodebytes
from getpass import getpass
from datetime import datetime, date
from time import sleep
from .validador import valida_clave_segura

# ~ class Extras:
'''Otras funciones utiles'''

def limpiar_pantalla():
    '''Sólo limpia la pantalla'''
    if platform.system() == "Windows":
        clear = "cls"
    else:
        clear = "clear"
    os.system(clear)

def espera(tiempo=1):
    sleep(tiempo)

def clave_encriptada(clave):
    '''Encriptra una clave'''
    return encodebytes(clave.encode())

def clave_desencriptada(clave):
    '''Desencripta una clave'''
    return decodebytes(clave.encode())

def ingresar_clave(texto, check=False):
        '''Pide al usuario que ingrese una cadena y la devuelve encriptada'''
        clave = getpass(texto)
        while check and not valida_clave_segura(clave):
            print("No es segura. La clave tiene que tener al menos 8 caracteres, entre ellos una mayuscula, una minuscula y un número")
            clave = getpass(texto)
        return clave_encriptada(clave)

def fecha_a_string(fecha):
    '''Convierte un objeto tipo date a una cadena'''
    return datetime.strftime(fecha, "%d/%m/%Y")

def hora_a_string(hora):
    '''Convierte un objeto tipo time a una cadena'''
    return datetime.strftime(hora, "%H:%M:%S")

def string_a_fecha(fecha):
    '''Convierte una cadena a un objeto tipo date'''
    return datetime.strptime(fecha, "%d/%m/%Y")

def ingresar_fecha():
    '''Se pide una fecha hasta obtener un objeto date válido'''
    dd = input("Día: ")
    mm = input("Mes: ")
    aa = input("Año: ")
    try:
        return string_a_fecha(f"{dd}/{mm}/{aa}")
    except:
        return ingresar_fecha()

def string_a_hora(hora):
    '''Convierte una cadena a un objeto tipo time'''
    return datetime.strptime(hora, "%H:%M:%S")

def consiente_cambio():
    rta = input("¿Quiere confirmar? (s/n)")
    while rta != "s" and rta != "n":
        rta = input("Confirme (s) para continuar o (n) para descartar:")
    return rta == "s"
