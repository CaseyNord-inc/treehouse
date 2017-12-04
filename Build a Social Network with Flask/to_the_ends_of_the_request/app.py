# Import the g object from the flask library.

# Now add a function named before_request that sets g.db to the DATABASE variable in models and calls the .connect() method.
# The function should be decorated with the before_request decorator.

from flask import Flask, g

import models

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()


# Finally, create a function named after_request that takes a response object. The function should close the g.db connection and return the response.
# You should decorate the function with after_request.

@app.after_request
def after_request(response):
    g.db.close()
    return response