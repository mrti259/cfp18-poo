from . import db

class Categoria(db.Model):
    categoria_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    productos = db.relationship('Producto', backref="categoria", lazy=True)

    def __repr__(self):
        return f'<Categoria {self.nombre}>'
