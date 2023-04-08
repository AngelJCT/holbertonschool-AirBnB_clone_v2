#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list(id=None):
    """Displays a HTML page with a list of states"""
    states = storage.all(State).values()
    return render_template('9-states.html', state=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """Displays a HTML page with info about <id>"""
    states = storage.all(State)
    for k, v in states.items:
        if v.id == id:
            return render_template('9-states.html', state=v)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
