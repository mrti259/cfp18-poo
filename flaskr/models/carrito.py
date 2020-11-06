from . import db

# class Carrito(db.Model):
#     carrito_id = db.Column(db.Integer, primary_key=True)
#     producto_id = db.Column(db.Integer, db.ForeignKey('producto.producto_id'))
#     usuario = db.Column(db.Integer, db.ForeignKey('usuario.usuario_id'))
#     cantidad = db.Column(db.Integer, index=True)

#     def __repr__(self):
#         return f'<Carrito {self.carrito_id}>'
