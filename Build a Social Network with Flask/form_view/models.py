import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase(':memory:')


class User(Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = CharField(default='')
    
    class Meta:
        database = DATABASE
    
    @classmethod
    def new(cls, email, password):
        cls.create(
            email=email,
            password=generate_password_hash(password)
        )


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()