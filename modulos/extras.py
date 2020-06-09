import os
import platform
from base64 import encodebytes, decodebytes

'''Otras funciones utiles'''

def limpiar_pantalla():
    '''Sólo limpia la pantalla'''
    if platform.system() == "Windows":
        clear = "cls"
    else:
        clear = "clear"
    os.system(clear)

def encriptar(clave):
    '''Encriptra una clave'''
    return str(encodebytes(clave.encode()))

def desencriptar(clave):
    '''Desencripta una clave, la devuelve en bytes'''
    return str(decodebytes(clave.encode()))

def arreglar_fecha(fecha):
    '''Convierte un objeto tipo date a una cadena'''
    return datetime.strftime(fecha, "%d/%m/%Y")

def convertir_a_fecha(fecha):
    '''Convierte una cadena a un objeto tipo date'''
    return datetime.strptime(fecha, "%d/%m/%Y")

def consentir():
    rta = input("¿Quiere confirmar? (s/n)")
    while rta != "s" and rta != "n":
        rta = input("Confirme (s) para continuar o (n) para descartar:")
    return rta == "s"
