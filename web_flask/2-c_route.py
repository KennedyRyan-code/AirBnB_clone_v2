#!/usr/bin/python3
""" Write a script that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return ("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
