#!/usr/bin/python3
"""task-0"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def h_hbnb():
    """returns Hello HBNB!"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
