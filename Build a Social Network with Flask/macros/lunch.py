# Create a macro named hide_email. It should take a User as an argument.
# Print out the email attribute of the User in the following format:
# t***@example.com for the email test@example.com.
# This will require splitting the email string and using a for loop.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    class User:
        email = None
    user = User()
    user.email = 'kenneth@teamtreehouse.com'
    return render_template('user.html', user=user)