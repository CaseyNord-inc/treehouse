# Your template has been given a list named options.
# Loop through each item in options and create an <li> inside the <ul>. Print out the name key of each item.

from flask import Flask, render_template

from options import OPTIONS

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('options.html', options=OPTIONS)