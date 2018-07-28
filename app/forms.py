from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, InputRequired
from app.models import User

class RegistrationForm(FlaskForm):
    community_organizer = BooleanField('Community organizer or group looking to find available spaces to host an event.')
    community_space = BooleanField('Community space looking to host or offer up space for an event.')
    submit = SubmitField('Register')

class CommunityOrganizerForm(FlaskForm):
    organization_name = StringField('Organization Name', validators=[InputRequired()])
    address = StringField('Street Address', validators=[InputRequired()])
    city = StringField('City', validators=[InputRequired()])
    state = StringField('State', validators=[InputRequired()])
    zipcode = StringField('Zipcode', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Register')

class CommunitySpaceForm(FlaskForm):
    space_name = StringField('Organization Name', validators=[InputRequired()])
    address = StringField('Street Address', validators=[InputRequired()])
    city = StringField('City', validators=[InputRequired()])
    state = StringField('State', validators=[InputRequired()])
    zipcode = StringField('Zipcode', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class AdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Add User')

  

