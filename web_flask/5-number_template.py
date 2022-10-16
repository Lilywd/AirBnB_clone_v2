#!/usr/bin/python3
"""
script that starts a Flask web application

"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/",strict_slashes=False)
def index():
    return "Hello HBNB!"

@app.route("/hbnb",strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>",strict_slashes=False)
def cisfun(text):
    return "C"  + text.replace('_', ' ')

@app.route("/python",strict_slashes=False)
@app.route("/python/<text>",strict_slashes=False)
def python(text='is cool'):
    return "Python" + text.replace('_', ' ')

@app.route("/number/<int:n>",strict_slashes=False)
def number(n):
    return '{:d} is a number'.format(n)

@app.route("/number_template/<int:n>",strict_slashes=False)
def numbertemplate(n):
    return render_template('5-number.html', n=n)


if  __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

