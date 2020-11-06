from . import db

class Producto(db.Model):
    producto_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), index=True)
    descripcion = db.Column(db.Text)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.categoria_id'))
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.marca_id'))
    precio = db.Column(db.Float, index=True)
    stock = db.Column(db.Integer, index=True)
    fecha_de_publicacion = db.Column(db.DateTime, index=True)
    fecha_de_actualizacion = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return f'<Producto {self.nombre}>'
