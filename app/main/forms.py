from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange
from app.models import Beer, Review

class BeerSubmit(FlaskForm):
    """ Form for submitting a beer """
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=20)])
    brand = StringField('Brand', validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('Submit')

class BeerReview(FlaskForm):
    """ Form for reviewing a beer """
    # rating = IntegerField('rating')
    rating = IntegerField('Rating (1 - 10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    comment = StringField('Comments', validators=[DataRequired(), Length(min=3, max=60)])
    submit = SubmitField('Submit')