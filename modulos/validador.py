from validate_email import validate_email
from validate_email import validate_email

'''Funciones que controlan la validez de los datos'''
def valida_nombre(nombre):
    return nombre != ""

def valida_precio(precio):
    return str(precio).isdigit()

def valida_stock(stock):
    return str(stock).isdigit()

def valida_id(ID):
    return str(ID).isdigit()

def valida_clave_segura(clave):
    return len(clave) >= 8 and any(char.islower() for char in clave) and any(char.isupper() for char in clave) and any(char.isdigit() for char in clave)

def valida_email(email):
    return validate_email(email, check_mx=True)

def valida_telefono(telefono):
    return str(telefono).isdigit()

def valida_dni(dni):
    return str(dni).isdigit()

def valida_fecha(fecha):
    return str(type(fecha)) == "<class 'datetime.date'>"

def valida_clave_correcta(clave1, clave2):
    return clave1 == clave2.encode()

def valida_administrador(usuario, clave):
    return usuario == "@admin" and clave == "".encode()
