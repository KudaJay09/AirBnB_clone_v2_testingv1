#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'
<<<<<<< HEAD


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
=======

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB!"""
>>>>>>> 85aa91b0c3ce8bedb7bc84ae738c6562315f48f1
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
