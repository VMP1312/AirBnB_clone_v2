#!/usr/bin/python3
"""Starts a Flask web application"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Closes sessions"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """Display a HTML page AirBnB"""
    st = storage.all(State).values()
    amen = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=st, amenities=amen)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
