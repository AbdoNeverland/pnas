#!/usr/bin/python3
"""doc """
from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def route_home():
    """display home"""
    print("route home reached")
    return render_template('index.html')



@app.route("/post", methods=['POST'])
def route_hadle_post():
    print("post endpoint reached")
    if request.method == 'POST':
        print(f"------json data------{request.get_data()}")
        data= request.get_json()
        print(data)
        print(data["input"])
        print("------end------")
    di ={"age":(2024- int(data["input"]))}
    m= json.dumps(di)
    print(f"sending m =## {m} ##")
    return jsonify(di)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=False)