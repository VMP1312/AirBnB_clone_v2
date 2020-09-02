#!/usr/bin/python3
"""Starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_id(id=None):
    """States and ID"""
    states = storage.all(State)
    if id:
        _id = "State." + id
        if _id in states.keys():
            state = states[_id]
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def close(self):
    """Closes sessions"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
