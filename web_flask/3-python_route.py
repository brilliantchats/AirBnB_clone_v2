#!/usr/bin/python3
""" Starts a Flask web app """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def print_c(text):
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def print_python(text='is cool'):
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
