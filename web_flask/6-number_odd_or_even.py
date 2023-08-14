#!/usr/bin/python3
"""task-3"""
from flask import Flask, render_template

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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_text_python(text="is cool"):
    """returns Python and the text"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def show_text_n(n):
    """returns n and is a number"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_html5_n(n):
    """returns an html and is a number"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def show_html6_n(n):
    """returns an html, his a number, and if is odd or even"""
    if n % 2 == 0:
        o_e = 'even'
    else:
        o_e = 'odd'
    return render_template('6-number_odd_or_even.html', number=n, odd_even=o_e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
