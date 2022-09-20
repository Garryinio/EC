from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, InputRequired, Length
from app.models import User


class RegistrationForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=25), InputRequired()])
    username = StringField('Username', [Length(min=4, max=25), DataRequired()])
    email = StringField('Email Address', [Length(min=6, max=35), Email(), DataRequired()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password', [DataRequired()])
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class LoginForm(FlaskForm):
    email = StringField('Email Address', [Length(min=6, max=35), Email(), DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    remember_me = BooleanField('Remember Me')