from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    """
    The form for entering values for the house. Feel free to add additional 
    fields for the remaining features in the data set (features missing in the form 
    are set to default values in `predict.py`).
    """

    YearBuilt = IntegerField('In what yeat was your house biult?', validators=[DataRequired()])
    YearRemodAdd = IntegerField('Has your house been remodeled? What year was this?', validators=[DataRequired()])
    OverallQual = IntegerField('How would you rate the quality of your house?', validators=[NumberRange(min=0,max=10)])
    ExterQual = IntegerField('How would you rate the overall External quality of your house?', validators=[NumberRange(min=0,max=10)])
    KitchenQual = IntegerField('How would you rate the overall kitchen quality of your house?', validators=[NumberRange(min=0,max=10)])
    GarageCars = IntegerField('How many cars fits in your garage?', validators=[DataRequired()])
    GrLivArea = IntegerField('How many square feet is your above ground living area?', validators=[DataRequired()])
    FullBath = IntegerField('How many full bathrooms are there in your house?', validators=[DataRequired()])
    Fireplace = IntegerField('How many fireplaces are there in your house?', validators=[DataRequired()])
    FirstFlrSF = IntegerField('How many square feet is your is your first floor?', validators=[DataRequired()])

    submit = SubmitField('Submit')

