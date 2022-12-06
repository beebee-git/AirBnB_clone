#!/usr/bin/python3
"""Importing the needed framework"""
from flask import Flask


app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello():
    """Function that returns a simple string"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
