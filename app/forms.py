from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")


class UsernameForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=64)]
    )
    submit = SubmitField("Fetch User")
