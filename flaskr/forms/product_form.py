from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):

    nombre = StringField("Nombre", validators=[DataRequired()])
    descripcion = StringField("Descripcion", validators=[DataRequired()])
    precio = FloatField("Precio", validators=[DataRequired()])
    # marca
    # categoria
    submit = SubmitField("Registrar")
