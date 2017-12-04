# Loop through each of the teachers in teachers and create an <li> for them in the provided <ul>.
# Inside the <li>, create an <h2> that holds the teacher's 'name' key.

# Now add a new <ul> inside of the <li> with a class of "courses".
# Inside this <ul> loop through the teacher's 'courses' key, creating an <li> for each course and printing the course.

from flask import Flask, render_template

from teachers import TEACHERS

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("teachers.html", teachers=TEACHERS)