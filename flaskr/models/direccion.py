from . import db

class Direccion(db.Model):
    direccion_id = db.Column(db.Integer, primary_key=True)
    calle = db.Column(db.String(100))
    altura = db.Column(db.Integer)
    codigo_postal = db.Column(db.String(30))
    ciudad_id = db.Column(db.Integer, db.ForeignKey('ciudad.ciudad_id'))

    def __repr__(self):
        return f'<Direccion {self.calle} {self.altura}>'
