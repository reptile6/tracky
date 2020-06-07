from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Email(message='Invalid email format.')])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match.')])
    confirm = PasswordField('Confirm Password.')


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired()])
