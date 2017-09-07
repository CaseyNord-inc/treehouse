# Import everything from the Peewee library. Create a new model named User.
# Give User an email attribute that is a CharField(). email should be unique.

import datetime

from flask.ext.login import UserMixin
from peewee import *


class User(UserMixin, Model):
    email = CharField(unique=True)

# Now add two more attributes/fields to User.
# The password field should be a CharField with a max_length of 100.
# And the join_date field should be a DateTimeField with a default value of datetime.datetime.now.

    user = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)

# Finally, add a last field named bio that is a TextField.
# It should have an empty string for its default value. This makes it optional.

    bio = TextField(default='')

# Import the UserMixin from Flask-Login. 
# Remember that Flask extensions usually have import paths that start with flask.ext.

# Now add UserMixin to the inheritance chain of the User model.