from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError

from ..models import Usuario

class UserForm(FlaskForm):

    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=60)])
    clave = PasswordField("Clave", validators=[DataRequired(), Length(min=8, max=20)])
    nombre = StringField("Nombre")
    apellido = StringField("Apellido")
    fecha_de_nacimiento = DateField("Fecha de nacimiento")
    dni = IntegerField("DNI")
    telefono = IntegerField("Teléfono")
    submit = SubmitField("Registarse!")

    def valitate_email(self, email):
        """
        Checks if email exists on database.
        """
        if Usuario.query.filter_by(email=email.data):
            raise ValidationError('Este mail ya se encuentra registrado.')

    def validate_clave(self, clave):
        """
        Clave must have one Upper, one Lower, one number and one special caracter
        """
        if not (
            any(char.isupper() for char in clave.data)
            and any(char.islower() for char in clave.data)
            and any(char.isnumeric() for char in clave.data)
            and any(char in "!@#*^" for char in clave.data)
        ):
            raise ValidationError(
                'La clave no es segura. Ponele mayus, minusculas, numeros y cosas raras'
            )
