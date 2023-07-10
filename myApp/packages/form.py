from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import email_validator
from packages.models import user

class RegistrationForm(FlaskForm):
    firstname = StringField("Firstname", validators = [DataRequired()])

    lastname = StringField("Lastname", validators = [DataRequired()])

    username = StringField("Username", validators = [DataRequired(), Length(min = 5, max = 15)])

    email = StringField("Email", validators = [DataRequired(), Email()])

    password = PasswordField("Password", validators = [DataRequired(), Length(min = 5)])

    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password")])

    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        User = user.query.filter_by(username = username.data).first()
        if User:
            raise ValidationError('username taken')
    
    
    def validate_email(self, email):
        User = user.query.filter_by(email = email.data).first()
        if User:
            raise ValidationError('email taken')


class LoginForm(FlaskForm):
    email = StringField("Email", validators = [Email(), DataRequired()])

    password = PasswordField("Password", validators = [DataRequired()])

    submit = SubmitField("Login")

    remember_me = BooleanField("remember me")
