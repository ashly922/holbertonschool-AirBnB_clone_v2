#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

app.route('/', strict_slashes=False)
def hello_route():
    '''
    Route handler for the root URL '/'. Returns a greeting message.

    Returns:
        str: A string containing the greeting message.
    '''
    return 'Hello HBNB!'

if __name__ == '__main__':
    '''
    Main entry point of the application.
    Starts the Flask web server.

    Note:
        This section will only execute when the script is directly run, not when it is imported as a module.
    '''
    app.run(host='0.0.0.0', port=5000)
