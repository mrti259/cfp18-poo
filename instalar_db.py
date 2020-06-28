import mysql.connector

sql_script = input("Ingrese archivo: ")
database = "ecommerce_final"
user = input("Ingrese administrador: ")
passwd = input("Ingrese contraseña: ")

dbconf = {
    "host":"localhost",
    "user": user,
    "passwd": passwd,
}

queries = []

with open(sql_script, "r") as file:
    texto = file.read()
    query = ""
    for char in texto:
        query += char
        if char == ';':
            queries.append(query)
            query = ""


db = mysql.connector.connect(**dbconf)
cursor = db.cursor()
for query in queries:
    cursor.execute(query)
    db.commit()
print("db configurada")


dbconf["database"] = database
with open("dbconf.py", "w") as file:
    file.write(f"dbconf={dbconf}")
