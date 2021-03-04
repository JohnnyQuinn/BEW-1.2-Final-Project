from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length
from app.models import Beer, Review

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