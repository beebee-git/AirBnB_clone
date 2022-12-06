#!/usr/bin/python3
"""Importing the needed framework"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Function that returns a simple string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Function that returns HBNB strint"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
