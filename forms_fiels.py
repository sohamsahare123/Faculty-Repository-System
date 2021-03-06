  
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FileField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import *
from passlib.hash import pbkdf2_sha256

def invalid(form, field):

    username = form.username.data
    password = field.data
    
    user_data = User.query.filter_by(username = username).first()
        
    if user_data is None:
        raise ValidationError("Username or password is incorrect")

    elif not pbkdf2_sha256.verify(password, user_data.password):
        raise ValidationError("Username or password is incorrect")

def validate_email(form, field):

        user_object = User.query.filter_by(username = form.email.data).first()
        
        if user_object:
            raise ValidationError("Email already exists")

class Registration(FlaskForm):

    email = EmailField('email_label', validators = [InputRequired("Email Required"), validate_email])
    username = StringField('username_label', validators = [InputRequired("Username Required"), Length(min = 5, max = 20, message = "Username must be between 5 to 20 characters")])
    password = PasswordField('password_label', validators = [InputRequired("Password Required"), Length(min = 5, max = 20, message = "Password must be between 5 to 20 characters")])
    confirm_password = PasswordField('confirm_password_label', validators = [InputRequired("Password Required"), EqualTo('password', message = "Password must match")])
    submit = SubmitField('Submit')

    def validate_username(self, username):

        user_object = User.query.filter_by(username = username.data).first()
        if user_object:
            raise ValidationError("Username already exists")

class LoginForm(FlaskForm):
    
    username = StringField('username_label', validators = [InputRequired("Username Required")])
    password = PasswordField('password_label', validators = [InputRequired("Password Required"), invalid])
    submit = SubmitField('Submit')

class Download(FlaskForm):

    name = StringField('Name', validators = [InputRequired("Name Required")])
    title = StringField('Title', validators = [InputRequired("Title Required")])
    source =  StringField('Source', validators = [InputRequired("Source Required")])
    submit = SubmitField('Submit')

class Uploaddata(FlaskForm):

    name = StringField('Name', validators = [InputRequired("Name Required")])
    title = StringField('Title', validators = [InputRequired("Title Required")])
    source =  StringField('Source', validators = [InputRequired("Source Required")])
    duration =  StringField('Duration', validators = [InputRequired("Duration Required")])
    year = IntegerField('Year', validators = [InputRequired("year Required")])
    data = FileField('File', validators = [InputRequired("File Required")])
    submit = SubmitField('Submit')

class forgot_password(FlaskForm):

    email = EmailField('Email', validators = [InputRequired("Email Required")])
    submit = SubmitField('Submit')

class change_pass(FlaskForm):

    password = PasswordField('password_label', validators = [InputRequired("Password Required"), Length(min = 5, max = 20, message = "Password must be between 5 to 20 characters")])
    confirm_password = PasswordField('confirm_password_label', validators = [InputRequired("Password Required"), EqualTo('password', message = "Password must match")])
    submit = SubmitField('Submit')