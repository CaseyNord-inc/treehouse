from flask import Flask, render_template

DEBUG = True
HOST = '0.0.0.0'
PORT = 8000

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/starfield')
def starfield():
    return render_template('starfield.html')


app.run(debug=DEBUG, host=HOST, port=PORT)