from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import email_validator

class RegistrationForm(FlaskForm):
    firstname = StringField("Firstname", validators = [DataRequired()])

    lastname = StringField("Lastname", validators = [DataRequired()])

    username = StringField("Username", validators = [DataRequired(), Length(min = 5, max = 15)])

    email = StringField("Email", validators = [DataRequired(), Email()])

    password = PasswordField("Password", validators = [DataRequired(), Length(min = 5)])

    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password")])

    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators = [Email(), DataRequired()])

    password = PasswordField("Password", validators = [DataRequired()])

    submit = SubmitField("Login")
