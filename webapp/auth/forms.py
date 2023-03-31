from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, URL, ValidationError

# from . import authenticate


class LoginForm(Form):
    email = StringField('Email', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired()])
    remember = BooleanField("Remember Me")


class RegisterForm(Form):
    email = StringField('Email', [DataRequired(), Length(max=255)])
    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired(), Length(min=8)])
    confirm = PasswordField('Confirm Password', [
        DataRequired(),
        EqualTo('password')
    ])

    
    #validators
    def validate_email(self, field):
        from ..models.user import User
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        from ..models.user import User
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
