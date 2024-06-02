#!/usr/bin/python3
"""doc """
import json
from pymongo import MongoClient

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
 
    if self.get({"email":data["email"]}, {}) == None:
      res = self.put({"email":data["email"], "pwd":data["pwd"],"phone":data["phone"]})
    else:
      print("the user already exist")
