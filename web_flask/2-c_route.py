#!/usr/bin/python3
"""Importing the needed framework
A script that starts a Flask web application
"""
from flask import Flask


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
