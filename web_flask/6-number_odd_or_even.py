#!/usr/bin/python3
"""Importing the needed framework"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Function that returns a simple string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Function that returns HBNB string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_print(text):
    """Function that returns a C string"""
    result = text.replace('_', ' ')
    return "C {}".format(result)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_print(text="is cool"):
    """Function that returns a Python string"""
    result = text.replace('_', ' ')
    return "Python {}".format(result)


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    """Function that returns a string only if n is a number"""
    if type(n) == int:
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    """Function that displays a HTML page only if n is an int"""
    if type(n) == int:
        return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_odd_or_even(n):
    """Function that displays a HTML page only if n is an int"""
    if type(n) == int:
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
