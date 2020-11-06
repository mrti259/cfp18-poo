from . import db

class Pais(db.Model):
    pais_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    provincias = db.relationship('Provincia', backref='pais', lazy=True)

    def __repr__(self):
        return f'<Pais {self.nombre}>'
