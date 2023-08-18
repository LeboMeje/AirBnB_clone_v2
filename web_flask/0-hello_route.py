#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /airbnb-onepage/: display "Hello HBNB!"
"""

from flask import Flask, render_template

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display text"""
    return render_template("100-hbnb.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
