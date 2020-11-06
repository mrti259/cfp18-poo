from . import db

class Provincia(db.Model):
    provincia_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.pais_id'))
    ciudades = db.relationship('Ciudad', backref='provincia', lazy=True)

    def __repr__(self):
        return f'<Provincia {self.nombre}>'
