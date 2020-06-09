from validate_email import validate_email

class Validador:
    '''Funciones que constrolan la validez de los datos'''
    def nombre_es_valido(self, nombre):
        return nombre != ""

    def precio_es_valido(self, precio):
        return str(precio).isdigit()

    def stock_es_valido(self, stock):
        return str(stock).isdigit()

    def id_es_valido(self, ID):
        return str(ID).isdigit()

    def clave_es_segura(self, clave):
        return any(char.islower() for char in clave) and any(char.isupper() for char in clave) and any(char.isdigit() for char in clave)

    def email_es_valido(self, email):
        return validate_email(email, check_mx=True)

    def telefono_es_valido(self, telefono):
        return str(telefono).isdigit()

    def dni_es_valido(self, dni):
        return str(dni).isdigit()

    def fecha_es_valida(self, fecha):
        return 

    def clave_es_correcta(self, clave1, clave2):
        return clave1 == clave2
