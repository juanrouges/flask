from flask_wtf import FlaskForm 
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import InputRequired, Email, Optional

class RegisterForm(FlaskForm):
    """for to register a new user"""
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    email = EmailField("Email", validators=[InputRequired(), Email()])
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name", validators=[InputRequired()])
