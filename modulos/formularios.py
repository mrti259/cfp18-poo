import os
import platform
import datetime
from validate_email import validate_email
from base64 import encodebytes

def validate_clave(clave):
    return any(char.islower() for char in clave) and any(char.isupper() for char in clave) and any(char.isdigit() for char in clave)

def limpiar_pantalla():
    if platform.system() == "Windows":
        clear = "cls"
    else:
        clear = "clear"
    os.system(clear)



def formulario_registro():
    def mostrar_datos(datos):
        for k,v in datos.items():
            print(k+":", v)

    datos = {
        "Nombres":"",
        "Apellidos":"",
        "Email":"",
        "Clave":"",
        "Dni":"",
        "Telefono":"",
        "Fecha de nacimiento (dd/mm/aaaa)":"",
        }

    errores = {}

    for k in datos:
        limpiar_pantalla()
        mostrar_datos(datos)
        datos[k] = input("-> " + k + ": ")
        if not datos[k]:
            errores[k] = "No puede dejar un casillero vacío"

    nombre, apellido, email, clave, dni, telefono, fecha_de_nacimiento = tuple([val for val in datos.values()])

    if not dni.isdigit():
        errores["Dni"] = "El DNI no es válido"
    if not telefono.isdigit():
        errores["Telefono"] = "El telefono no es válido"
    if not validate_email(email, check_mx=True):
        errores["Email"] = "No es un email válido"
    if not validate_clave(clave):
        errores["Clave"] = "La contraseña no es segura"
    try:
        fecha_de_nacimiento = datetime.datetime.strptime(fecha_de_nacimiento, "%d/%m/%Y")
    except:
        errores["Fecha de nacimiento"] = "La fecha no es válida"

    if errores:
        for err in errores.values():
            print(err)
        input()
        return formulario_registro()
    else:
        return int(dni), nombre.capitalize(), apellido.capitalize(), fecha_de_nacimiento, email, encodebytes(clave.encode()), int(telefono)

