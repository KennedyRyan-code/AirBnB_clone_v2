#!/usr/bin/python3
""" Write a script that starts a Flask web application """

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Replace underscore symbols with a space in the text"""
    text = text.replace("_", " ")
    return f"C {escape(text)}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    text = text.replace("_", " ")
    return f"Python {escape(text)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
