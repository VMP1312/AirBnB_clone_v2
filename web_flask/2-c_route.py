#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Hello Holberton"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_variable_text(text):
    """C Variable printing"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)