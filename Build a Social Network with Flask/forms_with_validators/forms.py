# Import Form from Flask-WTF. Import StringField and PasswordField from wtforms.
# Lastly, import DataRequired, Email, and Length from wtforms.validators.

from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length

# Create a new Form class named SignUpForm. Give it two fields, email and password.
# Email should be a StringField and password should be a PasswordField.

# Add DataRequired and Email to the validators for the email field.

# Finally, add DataRequired and Length to the validators for password. Set the min for Length to 8.

class SignUpForm(Form):
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired(), Length(min=8)])