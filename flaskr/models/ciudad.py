from . import db

class Ciudad(db.Model):
    ciudad_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    provincia_id = db.Column(db.Integer, db.ForeignKey('provincia.provincia_id'))
    direcciones = db.relationship('Direccion', backref='ciudad', lazy=True)

    def __repr__(self):
        return f'<Ciudad {self.nombre}>'
