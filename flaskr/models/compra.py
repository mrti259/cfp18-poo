from . import db

class Compra(db.Model):
    compra_id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.usuario_id'))
    direccion_id = db.Column(db.Integer, db.ForeignKey('direccion.direccion_id'))
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.producto_id'))
    cantidad = db.Column(db.Integer, index=True)
    precio_total = db.Column(db.Float, index=True)
    fecha_de_compra = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Compra {self.compra_id}>'
