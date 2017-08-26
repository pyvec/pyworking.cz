#!/usr/bin/env python3

import flask
from flask import render_template


app = flask.Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
