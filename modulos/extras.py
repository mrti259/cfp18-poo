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

def clave_encriptada(clave):
    '''Encriptra una clave'''
    return str(encodebytes(clave.encode()))

def clave_desencriptada(clave):
    '''Desencripta una clave'''
    return str(decodebytes(clave.encode()))

def fecha_a_string(fecha):
    '''Convierte un objeto tipo date a una cadena'''
    return datetime.strftime(fecha, "%d/%m/%Y")

def hora_a_string(hora):
    '''Convierte un objeto tipo time a una cadena'''
    return datetime.strftime(hora, "%H:%M:%S")

def string_a_fecha(fecha):
    '''Convierte una cadena a un objeto tipo date'''
    return datetime.strptime(fecha, "%d/%m/%Y")

def string_a_hora(hora):
    '''Convierte una cadena a un objeto tipo time'''
    return datetime.strptime(hora, "%H:%M:%S")

def consiente_cambio():
    rta = input("¿Quiere confirmar? (s/n)")
    while rta != "s" and rta != "n":
        rta = input("Confirme (s) para continuar o (n) para descartar:")
    return rta == "s"