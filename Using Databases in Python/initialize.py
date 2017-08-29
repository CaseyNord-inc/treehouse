# Create a variable named db that is an SqliteDatabase with a filename of challenges.db.

from peewee import *

db = SqliteDatabase('challenges.db')

class Challenge(Model):
    name = CharField(max_length=100)
    language = CharField(max_length=100)
    steps = IntegerField(default=1)

    # Now add db as the database attribute in the Meta class for Challenge.

    class Meta:
        database = db

# Finally, create a function named initialize. Your initialize() function should connect to the database
# and then create the Challenge table. Make sure it creates the table safely.

def initialize():
    db.connect()
    db.create_tables([Challenge], safe=True)