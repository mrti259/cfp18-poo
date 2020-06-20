from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from dbconf import dbconf

app = Flask(__name__)

app.config["MYSQL_HOST"] = dbconf["host"]
app.config["MYSQL_USER"] = dbconf["user"]
app.config["MYSQL_PASSWORD"] = dbconf["passwd"]
app.config["MYSQL_DB"] = dbconf["database"]
mysql = MySQL(app)
app.config["USE_SESSION_FOR_NEXT"] = True
app.secret_key="miclave"

# cur = mysql.connection.cursor()
# cur.excute()
# mysql.connection.commit()
# flash("")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    if request.method=="POST":
        datos={}
        datos["email"] = request.form["email"]
        datos["clave"] = request.form["clave"]
        return redirect(url_for("index"))

@app.route("/registrar_usuario", methods=["POST"])
def registrar_usuario():
    if request.method=="POST":
        datos={}
        datos["email"] = request.form["email"]
        datos["clave"] = request.form["clave"]
        datos["nombre"] = request.form["nombre"]
        datos["apellido"] = request.form["apellido"]
        datos["fecha_de_nacimiento"] = request.form["fecha_de_nacimiento"]
        datos["dni"] = request.form["dni"]
        datos["telefono"] = request.form["telefono"]
        return redirect(url_for("index"))

@app.route("/registrar_producto", methods=["POST"])
def registrar_producto():
    if request.method=="POST":
        datos={}
        datos["nombre"] = request.form["nombre"]
        datos["descripcion"] = request.form["descripcion"]
        datos["precio"] = request.form["precio"]
        datos["stock"] = request.form["stock"]
        datos["categoria"] = request.form["categoria"]
        datos["marca"] = request.form["marca"]
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(port=3000)
