# Import Flask from the flask library.

from flask import Flask

# Create a new Flask instance as a variable named app.
# The name you pass to the Flask app should be __name__.

app = Flask(__main__)

# Add a view function named index. Give this view a route of "/".
# Make the view return your name. You do not need to use app.run().

@app.route('/')
def index():
    return "Hello World!"

# Import request from Flask.
# Then update the index view to return "Hello {name}", replacing {name} with
# a name argument in the query string.

from flask import request

@app.route('/')
def index(name='Treehouse'):
    name = request.args.get('name', name)
    return 'Hello {}'.format(name)

# Add a new route to hello() that expects a name argument.
# The view will need to accept a name argument, too.
# Update the response from hello() to say "Hello {name}", replacing {name} with the passed-in name.
# Now give hello() a default name argument of "Treehouse".

@app.route('/')
@app.route('/<name>')
def hello(name='Treehouse'):
     return 'Hello {}'.format(name)

# Add an import for render_template. It comes directly from the flask library.

from flask import render_template

# Use render_template() to render the "hello.html" template in hello().
# Pass the name argument to the template. Print the name variable in the <h1> in the template.

@app.route('/hello/<name>')
def hello(name="Treehouse"):
    return render_template('hello.html', name=name)

