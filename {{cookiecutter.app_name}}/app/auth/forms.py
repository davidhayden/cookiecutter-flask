from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username required.')])
    password = PasswordField('Password', validators=[DataRequired(message='Password required.')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username required.')])
    email = StringField('Email', validators=[DataRequired(message='Email required.'), Email(message='Valid Email Required.')])
    password = PasswordField('Password', validators=[DataRequired(message='Password required.')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired('Confirm Password required.'), EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please choose a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError('Please choose a different email.')
