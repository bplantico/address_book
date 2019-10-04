from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class NewAddressForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip = IntegerField('Zip', validators=[DataRequired()])
    submit = SubmitField('Create Address')

class DeleteAddressForm(FlaskForm):
    submit = SubmitField('Delete Address')
