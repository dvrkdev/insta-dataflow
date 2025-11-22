from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import Account


class UsernameForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=64)]
    )
    submit = SubmitField("Fetch User")

    def validate_username(self, username):
        account = Account.query.filter_by(username=username.data).first()
        if account:
            raise ValidationError('This user already exists.')
