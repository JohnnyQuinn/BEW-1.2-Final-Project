from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField, PasswordField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL, ValidationError
from app.models import User, Beer, Review

class BeerSubmit(FlaskForm):
    """ Form for submitting a beer """
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=20)])
    brand = StringField('Brand', validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('Submit')

class BeerReview(FlaskForm):
    """ Form for reviewing a beer """
    rating = IntegerField('rating')
    comment = StringField('Comments')
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    """ Form for user login """
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class SignUpForm(FlaskForm):
    """ Form for user account sign up """
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')