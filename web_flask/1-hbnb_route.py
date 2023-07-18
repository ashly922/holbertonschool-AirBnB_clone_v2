#!/usr/bin/python3
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
Route '/hbnb' displays "HBNB"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
