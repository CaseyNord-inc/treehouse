# Update templates/today.html to show today's order's date and the order attribute from the order variable.
# Use strftime on the date with the format %Y-%m-%d.

# Now add a <a> with an href attribute that points to the url for the cancel_order view. The view takes one argument,
# order_id, which should be the id attribute of the order.

import datetime

from flask import Flask, g, render_template, flash, redirect, url_for
from flask.ext.bcrypt import check_password_hash
from flask.ext.login import LoginManager, login_user, current_user, login_required, logout_user

import forms
import models

app = Flask(__name__)
app.secret_key = 'this is our super secret key. do not share it with anyone!'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


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
    g.user = current_user
    

@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.SignUpInForm()
    if form.validate_on_submit():
        models.User.new(
            email=form.email.data,
            password=form.password.data
        )
        flash("Thanks for registering!") 
    return render_template('register.html', form=form)
  

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.SignUpInForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(
                models.User.email == form.email.data
            )
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("You're now logged in!")
            else:
                flash("No user with that email/password combo")
        except models.DoesNotExist:
              flash("No user with that email/password combo")
    return render_template('register.html', form=form)

@app.route('/secret')
@login_required
def secret():
    return "I should only be visible to logged-in users"

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
  

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order', methods=('GET', 'POST'))
def order_lunch():
    form = forms.LunchOrderForm()
    if form.validate_on_submit():
        models.LunchOrder.create(
            user=g.user._get_current_object(),
            date=form.date.data,
            order=form.order.data.strip()
        )
    return render_template('lunch.html', form=form)


@app.route('/today')
@login_required
def today():
    order = models.LunchOrder.select().where(
        models.LunchOrder.date == datetime.date.today() &
        models.LunchOrder.user == g.user._get_current_object()
    ).get()
    return render_template('today.html', order=order)
  

@app.route('/cancel_order/<int:order_id>')
@login_required
def cancel_order(order_id):
    try:
        order = models.LunchOrder.select().where(
            id=order_id,
            user=g.user._get_current_object()
        ).get()
    except models.DoesNotExist:
        pass
    else:
        order.delete_instance()
    return redirect(url_for('index'))