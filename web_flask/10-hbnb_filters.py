#!/usr/bin/python3
from flask import Flask, render_template, g
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
'''start up app import files'''

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    '''filters function'''
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    cities = sorted(storage.all(City).values(), key=lambda c: c.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)
    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)


@app.teardown_appcontext
def teardown_appcontext(exception):
    '''tear down function'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
