from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

from ..models import Usuario

class LoginForm(FlaskForm):

    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=60)])
    clave = PasswordField("Clave", validators=[DataRequired(), Length(max=30)])
    submit = SubmitField("Entrar!")

    def validate_email(self, email):
        """
        Checks if email is in database.
        """
        return Usuario.query.filter_by(email=email)
