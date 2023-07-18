#!/usr/bin/python3
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
Route '/hbnb' displays "HBNB"
Route '/c/<text>' displays c then the text variable
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    '''displays "HBNB"'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    '''replace underscore w space'''
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")