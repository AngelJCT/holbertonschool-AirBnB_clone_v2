#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Function that returns a string """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function that returns a string """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Function that returns a string """
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ Function that returns a string """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Function that returns a string """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Function that returns a number in template """
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Function that returns a number even|odd """
    html_str = '6-number_odd_or_even.html'
    if n % 2 == 0:
        return render_template(html_str, num=n, odd_or_even='even')
    else:
        return render_template(html_str, num=n, odd_or_even='odd')


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a HTML page with a list of states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
