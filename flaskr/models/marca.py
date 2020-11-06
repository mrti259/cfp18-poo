from . import db

class Marca(db.Model):
    marca_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    productos = db.relationship('Producto', backref='marca', lazy=True)

    def __repr__(self):
        return f'<Marca {self.nombre}>'
