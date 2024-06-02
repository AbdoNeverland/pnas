#!/usr/bin/python3
"""doc """
import json
from pymongo import MongoClient
import random
import datetime
import time

def getRandomDigits(nb):
  rn= ""
  for  i in range(nb):
    rn+= str(random.randint(0,9))
  return rn


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

  def update(self, where,newData, colName="Users"):
    return self.db[colName].update_one(where, newData)

  def activatePhone(self, phone2Activate):
    self.update({"phone":phone2Activate}, { "$set": { 'activated': "yes" } })
   

  def createCollection(self, colName="Users"):
    col = self.db[colName]

  def put(self, data, colName="Users"):
    res = self.db[colName].insert_one(data)

  def addSMS(self, data):
    dt = datetime.datetime.now()
    msg =""
    if self.get({"phone":data["phone"]}, {},colName="Users") == None:
      return "you can't add a new sms without registering"
    else:
      if self.get({"phone":data["phone"]}, {},colName="Users")["activated"] == "no":
        return "you phone is not yet activated to send sms"

    if self.get({"phone":data["phone"]}, {},colName="Sms2Send") == None:
      res = self.put({"email":data["email"],
        "pwd":data["pwd"],
        "phone":data["phone"],
        "msg":data["phone"],
        "sendTo":data["sendTo"],
        "datetime":dt.strftime("%m/%d/%Y,%H:%M:%S"),
        "timestamp":dt.timestamp(),
        "processed":"no",
        "received":"no"
        },colName="Sms2Send")
      msg ="the new smsService has been added"
    else:
      msg = "the smsService already exists"
    return msg

  def addNewUser(self, data):
    dt = datetime.datetime.now()
    msg =""
    if self.get({"phone":data["phone"]}, {}) == None:

      res = self.put({"email":data["email"],
        "pwd":data["pwd"],
        "phone":data["phone"],
        "digits":getRandomDigits(6),
        "activated":"no",
        "datetime":dt.strftime("%m/%d/%Y,%H:%M:%S"),
        "timestamp":dt.timestamp()
        })
      addSMS();
      msg ="the new user has been added"
    else:
      msg = "the user already exists"
    return msg

  def activate(self, data):
    print("activated reached")
    dt = datetime.datetime.now()
    msg =""
    savedUser = self.get({"phone":data["phone"]}, {})
    if savedUser == None:
      msg ="this account doesn't exists"
    else:
      if savedUser["digits"] == data["smsdigits"]:
        self.activatePhone(data["phone"])
        msg = "this phone has been activated"
      else:
        msg = "wrong digits";
    return msg

  def addNewSmsService(self, data):
    dt = datetime.datetime.now()
    msg =""
    if self.get({"phone":data["phone"]}, {},colName="Users") == None:
      return "you can't add a new service"
    else:
      if self.get({"phone":data["phone"]}, {},colName="Users")["activated"] == "no":
        return "you phone is not yet activated to create a service"

    if self.get({"phone":data["phone"]}, {},colName="SmsService") == None:
      res = self.put({"email":data["email"],
        "pwd":data["pwd"],
        "phone":data["phone"],
        "digits":getRandomDigits(6),
        "datetime":dt.strftime("%m/%d/%Y,%H:%M:%S"),
        "timestamp":dt.timestamp()
        },colName="SmsService")
      msg ="the new smsService has been added"
    else:
      msg = "the smsService already exists"
    return msg


