from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user

from .models import Producto, Usuario
from .app import db, login

def add(obj):
    """
    Add object to the database.
    """
    db.session.add(obj)
    db.session.commit()

def delete(obj):
    """
    Deletes object from database.
    """
    db.session.delete(obj)
    db.session.commit()

def get_products():
    """
    Get all products from database.
    """
    return Producto.query.all()

def create_product(product_form):
    """
    Returns a Producto object from ProductForm data.
    """
    product = Producto(
        nombre = product_form['nombre'],
        descripcion = product_form['descripcion'],
        precio = product_form['precio']
    )
    return product

def register_product(product_form):
    """
    Register product from ProductForm data and
    adds it into the database.
    """
    product = create_product(product_form)
    add(product)

def check_login(login_form):
    """
    Checks if LoginForm data.
    If it's valid, user logs in.
    """
    user = Usuario.query.filter_by(email=login_form['email']).first()
    if check_password_hash(user.clave, login_form['clave']):
        login_user(user)

def create_user(user_form):
    """
    Returns a Usuario object from UserForm data.
    """
    user = Usuario(
        email = user_form['email'],
        clave = generate_password_hash(user_form['clave']),
        nombre = user_form['nombre'],
        apellido = user_form['apellido'],
        fecha_de_nacimiento = user_form['fecha_de_nacimiento'],
        dni = user_form['dni'],
        telefono = user_form['telefono']
    )
    return user

def register_user(user_form):
    """
    Register user from UserForm data and adds it
    into the database.
    """
    user = create_user(user_form)
    add(user)
