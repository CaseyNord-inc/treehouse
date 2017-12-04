# In forms.py, add a new form class named LunchOrderForm. It should have two fields, order and date.
# The order field should be a TextAreaField and date should be a DateField.
# Both should have DataRequired as a validator.

# Finally, you need to instantiate, process, and send LunchOrderForm to the template.
# If the form is valid after submission, create a new LunchOrder object with the data and set the user to the current user.

from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email, Length


class SignUpInForm(Form):
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired(), Length(min=8)])
    
    
class LunchOrderForm(Form):
    order = TextAreaField(validators=[DataRequired()])
    date = DateField(validators=[DataRequired()])