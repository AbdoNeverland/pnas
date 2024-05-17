#!/usr/bin/python3
"""doc """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """display home"""
    return "f starting"


if __name__ == "__main__":
    app.run(host="0.0.0.0")