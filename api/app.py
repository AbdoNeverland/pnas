#!/usr/bin/python3
"""doc """
from flask import Flask, jsonify, request, render_template, url_for
import json
from pymongo import MongoClient
import os
import pyscripts
print(os.getcwd())
from pyscripts.pymongoHelper import mongoHelper

app = Flask(__name__, template_folder='export')
app.static_folder = 'static'
jinja_options = app.jinja_options.copy()
jinja_options.update(dict(
    comment_start_string='<#',
    comment_end_string='#>',
))
app.jinja_options = jinja_options



storeHelper = mongoHelper()
#storeHelper.addNewUser({"user":"hicham", "pwd":"hichampass"})
#print(storeHelper.get({"user":"hichami"}, {}))


@app.route("/", strict_slashes=False)
def route_home():
    """display home"""
    print("route home reached")
    return render_template('index.html')


@app.route("/register", methods=['POST'])
def route_hadle_post():
    print("post endpoint reached")
    if request.method == 'POST':
        print(f"------json data------{request.get_data()}")
        data = request.get_json()
        print(data)
        #print(data["input"])
        print("------end------")
        storeHelper.addNewUser(data)
    di = {"age": 35}
    m = json.dumps(di)
    print(f"sending m =## {m} ##")
    return jsonify(di)

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=5000,debug=False)
