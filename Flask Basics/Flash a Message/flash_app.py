# Import flash from Flask.
# Add a secret_key attribute to the app object.
# flash() a message in the fishy() view before the return. The message can have any content you want.

from flask import Flask, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = 'fkahlg3&&*Y#*QR.g.13at$^&13wnu;ll;ds..gwm(*(*GJIJGE'


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/fishy')
def fishy():
    flash("This is easier than I thought!")
    return redirect(url_for('index'))

