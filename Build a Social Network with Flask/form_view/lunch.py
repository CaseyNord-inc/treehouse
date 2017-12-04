# Add a new view to lunch.py. The function name should be register and the route should be "/register". 
# It should accept both GET and POST methods. For now, have it return the string "register".

# Your register() view needs to create an instance of the SignUpForm from forms.
#  It should also render and return the register.html template. You'll need to import render_template.
#  In the template's context, name the SignUpForm instance as form.

#Finally, update the register() view so that the form is validated on submission.
#  If it's valid, use the models.User.new() method to create a new User from the form data and flash
#  the message "Thanks for registering!". You'll need to import flash().

from flask import Flask, g, render_template, flash
from flask.ext.login import LoginManager

import forms
import models

app = Flask(__name__)
app.secret_key = 'this is our super secret key. do not share it with anyone!'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.select().where(
            models.User.id == int(userid)
        ).get()
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()
    

@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.SignUpForm()
    if form.validate_on_submit():
        flash("Thanks for registering!")
        models.User.new(email=form.email.data, password=form.password.data)
    return render_template('register.html', form=form)