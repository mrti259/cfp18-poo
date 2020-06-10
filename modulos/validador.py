from validate_email import validate_email
import .extras

'''Funciones que constrolan la validez de los datos'''
def valida_nombre(self, nombre):
    return nombre != ""

def valida_precio(self, precio):
    return str(precio).isdigit()

def valida_stock_es_valido(self, stock):
    return str(stock).isdigit()

def valida_id(self, ID):
    return str(ID).isdigit()

def valida_clave_segura(self, clave):
    return len(clave) >= 8 and any(char.islower() for char in clave) and any(char.isupper() for char in clave) and any(char.isdigit() for char in clave)

def valida_email(self, email):
    return validate_email(email, check_mx=True)

def valida_telefono(self, telefono):
    return str(telefono).isdigit()

def valida_dni(self, dni):
    return str(dni).isdigit()

def valida_fecha(self, fecha):
    try:
        return extras.string_a_fecha(fecha)
    except:
        return str(type(fecha)) == "<class 'datetime.date'>":

def valida_clave_correcta(self, clave1, clave2):
    return clave1 == clave2
