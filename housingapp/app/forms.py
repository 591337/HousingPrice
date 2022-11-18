from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    """
    The form for entering values for the house. Feel free to add additional 
    fields for the remaining features in the data set (features missing in the form 
    are set to default values in `predict.py`).
    """

    YearBuilt = IntegerField('In what year was your house biult?', validators=[NumberRange(min=1900,max=2020)])
    OverallQual = IntegerField('How would you rate the quality of your house? (0 worst, 10 best)', validators=[NumberRange(min=0,max=10)])
    ExterQual = IntegerField('How would you rate the overall External quality of your house? (0 best, 4 worst)', validators=[NumberRange(min=0,max=4)])
    KitchenQual = IntegerField('How would you rate the overall kitchen quality of your house? (0 best, 4 worst)', validators=[NumberRange(min=0,max=4)])
    TotalBsmtSF = IntegerField('How many square feet is your is your basement?', validators=[NumberRange(min=0,max=20000)])
    GarageCars = IntegerField('How many cars fits in your garage?', validators=[NumberRange(min=0,max=6)])
    FullBath = IntegerField('How many full bathrooms are there in your house?', validators=[NumberRange(min=0,max=20)])
    Fireplace = IntegerField('How many fireplaces are there in your house?', validators=[NumberRange(min=0,max=10)])
    FirstFlrSF = IntegerField('How many square feet is your is your first floor?', validators=[NumberRange(min=0,max=20000)])
    SecondFlrSF = IntegerField('How many square feet is your is your second floor?', validators=[NumberRange(min=0,max=20000)])

    submit = SubmitField('Submit')

