from flask_login import UserMixin

from . import db
from ..app import login

class Usuario(UserMixin, db.Model):
    usuario_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    clave = db.Column(db.String(120), nullable=False)
    nombre = db.Column(db.String(60))
    apellido = db.Column(db.String(60))
    fecha_de_nacimiento = db.Column(db.Date)
    dni = db.Column(db.Integer, index=True, unique=True)
    telefono = db.Column(db.Integer, index=True)
    #direcciones
    #compras

    def get_id(self):
        """
        Overwrites UserMixin.get_id()
        """
        return self.usuario_id

    def __repr__(self):
        return f'<User {self.email}>'


@login.user_loader
def load_user(id):
    return Usuario.query.get(int(id))
