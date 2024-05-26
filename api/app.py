#!/usr/bin/python3
"""doc """
from flask import Flask, jsonify, request, render_template
import json
from pymongo import MongoClient

app = Flask(__name__)


class mongoHelper:
  def __init__(self):
    self.mongoClient = MongoClient("mongodb://127.0.0.1:27017/")
    self.db = None
    self.createDatabase()
    self.createCollection()

  def createDatabase(self, dbNmae="maindb"):
    alldb = self.mongoClient.list_database_names()
    if dbNmae not in alldb:
      self.db = self.mongoClient[dbNmae]
    else:
      self.db = self.mongoClient[dbNmae]

  def get(self, what, _filter, colName="Users"):
    return self.db[colName].find_one(what, _filter)

  def createCollection(self, colName="Users"):
    col = self.db[colName]

  def put(self, data, colName="Users"):
    res = self.db[colName].insert_one(data)

  def addNewUser(self, data):
    p_user = data["user"]
    p_pwd = data["pwd"]
    if self.get({"user":p_user}, {}) == None:
      res = self.put({"user":p_user, "pwd":p_pwd})
    else:
      print("the user already exist")


storeHelper = mongoHelper()
storeHelper.addNewUser({"user":"hicham", "pwd":"hichampass"})
print(storeHelper.get({"user":"hichami"}, {}))


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
        data = request.get_json()
        print(data)
        print(data["input"])
        print("------end------")
    di = {"age": (2024 - int(data["input"]))}
    m = json.dumps(di)
    print(f"sending m =## {m} ##")
    return jsonify(di)


if __name__ == "__main__":
  pass
  #app.run(host="0.0.0.0",port=5000,debug=False)
