#!/usr/bin/python3
"""Starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def state_id():
    """States and Citites"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close(self):
    """Close sessions"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
