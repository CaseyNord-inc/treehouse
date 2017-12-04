# Import everything from the peewee library.

from peewee import *

# Now we need to make a database connection. Make an SqliteDatabase() named "challenges.db". Assign it to the variable db.

db = SqliteDatabase('challenges.db')

# Alright, now for the biggest part. Make a model named Challenge that has two fields, name and language.
# Both fields should be of the type CharField with a max_length of 100.

class Challenge(Model):
    name = CharField(max_length=100)
    language = CharField(max_length=100)

# Now add a Meta class to Challenge and set the database attribute equal to db.

    class Meta:
        database = db