#!/usr/bin/python3
"""task-3"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def h_hbnb():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_text_c(text):
    """returns C and the text"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False)
def show_text_python(text="is cool"):
    """returns Python and the text"""
    text = text.replace("_", " ")
    return f"Python {text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
