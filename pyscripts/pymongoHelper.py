#!/usr/bin/python3
"""Mongo helper module"""
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
import random
import datetime
import time


def getRandomDigits(nb):
  """get a random digits"""
  rn = ""
  for i in range(nb):
    rn += str(random.randint(0, 9))
  return rn


class mongoHelper:
  """mongo class heper"""
  def __init__(self):
    """class constructor"""
    self.mongoClient = MongoClient("mongodb://127.0.0.1:27017/")
    self.db = None
    self.CodeExpiredTime = 600 # second
    self.createDatabase()
    self.createCollection()

  def createDatabase(self, dbNmae="maindb"):
    """create database"""
    alldb = self.mongoClient.list_database_names()
    if dbNmae not in alldb:
      self.db = self.mongoClient[dbNmae]
    else:
      self.db = self.mongoClient[dbNmae]

  def get(self, what, _filter, colName="Users"):
    """get from mongo"""
    return self.db[colName].find_one(what, _filter)

  def update(self, where, newData, colName="Users"):
    """update entry"""
    return self.db[colName].update_one(where, newData)

  def activatePhone(self, phone2Activate):
    """activate phone"""
    self.update({"phone": phone2Activate}, {"$set": {'activated': "yes"}})

  def createCollection(self, colName="Users"):
    """create mongo collection"""
    col = self.db[colName]

  def put(self, data, colName="Users"):
    """put a value"""
    res = self.db[colName].insert_one(data)

  def isValidUser(self, data):
    """check if user is valid"""
    user = self.get({"phone": data["phone"]}, {})
    if user["phone"] == data["phone"] and user["pwd"] == data["pwd"]:
      return True
    return False

  def addSMS(self, data, noPwd=False):
    """add sms"""
    dt = datetime.datetime.now()
    msg = ""
    user = self.get({"phone": data["phone"]}, {})
    d2Add = {"email": data["email"],
             "pwd": data["pwd"],
             "phone": data["phone"],
             "msg": data["msg"],
             "sendTo": data["sendTo"],
             "datetime": dt.strftime("%m/%d/%Y,%H:%M:%S"),
             "timestamp": dt.timestamp(),
             "processed": "no",
             "received": "no"
             }
    if noPwd:
      self.put(d2Add, colName="Sms2Send")
      return "sms was added to stack"
    else:
      if self.isValidUser(data):
        if user["activated"] == "no":
          return "your phone is not activated"
        res = self.put(d2Add, colName="Sms2Send")
        return "the new sms was added to stack"
      else:
        return "wrong user phone or password"

  def sentVerificationCode(self, data, sdigit):
    """sent verification code"""
    dt = datetime.datetime.now()
    self.addSMS({"email": data["email"],
                 "pwd": data["pwd"],
                 "phone": data["phone"],
                 "msg": f"your pnas verification code is {sdigit}",
                 "sendTo": data["phone"],
                 "datetime": dt.strftime("%m/%d/%Y,%H:%M:%S"),
                 "timestamp": dt.timestamp(),
                 "processed": "no",
                 "received": "no"
                 }, noPwd=True)

  def addNewUser(self, data):
    """add a new user"""
    dt = datetime.datetime.now()
    msg = ""
    if self.get({"phone": data["phone"]}, {}) == None:

      sdigit = getRandomDigits(6)
      res = self.put({"email": data["email"],
                      "pwd": data["pwd"],
                      "phone": data["phone"],
                      "digits": sdigit,
                      "activated": "no",
                      "datetime": dt.strftime("%m/%d/%Y,%H:%M:%S"),
                      "timestamp": dt.timestamp()
                      })
      self.sentVerificationCode(data, sdigit)
      msg = "the new user has been added"
    else:
      sdigit = getRandomDigits(6)
      user = self.get({"phone": data["phone"]}, {})
      if user["activated"] == "yes":
        msg = "this phone number already exists"
        msg = ""
      else:
        self.update({"phone": data["phone"]}, {"$set": {'digits': sdigit, "timestamp": dt.timestamp()}})
        self.sentVerificationCode(data, sdigit)
        msg = "a verification code was sent again to this number"
    return msg

  def activate(self, data):
    """activate a user"""
    print("activated reached")
    dt = datetime.datetime.now()
    msg = ""
    savedUser = self.get({"phone": data["phone"]}, {})
    if savedUser == None:
      msg = "this account doesn't exists"
    else:
      t1 = datetime.datetime.fromtimestamp(savedUser["timestamp"])
      t2 = datetime.datetime.now()
      expireTime = t2 - t1
      if savedUser["digits"] == data["smsdigits"]:
        if (expireTime.total_seconds() > self.CodeExpiredTime):
          msg = "This verification code has expired"
        else:
          self.activatePhone(data["phone"])
          msg = "this phone has been activated"
      else:
        msg = "wrong digits"
    return msg

  def addNewSmsService(self, data):
    """add a new sms service"""
    dt = datetime.datetime.now()
    msg = ""
    if self.get({"phone": data["phone"]}, {}, colName="Users") == None:
      return "you can't add a new service"
    else:
      if self.get({"phone": data["phone"]}, {}, colName="Users")["activated"] == "no":
        return "you phone is not yet activated to create a service"

    if self.get({"phone": data["phone"]}, {}, colName="SmsService") == None:
      res = self.put({"email": data["email"],
                      "pwd": data["pwd"],
                      "phone": data["phone"],
                      "digits": getRandomDigits(6),
                      "datetime": dt.strftime("%m/%d/%Y,%H:%M:%S"),
                      "timestamp": dt.timestamp()
                      }, colName="SmsService")
      msg = "the new smsService has been added"
    else:
      msg = "the smsService already exists"
    return msg

  def getStack(self, data):
    """get the stack"""
    if data["phone"] == "" and data["pwd"] == "":
        allsms = self.db["Sms2Send"].find({"processed": "no"}, {"_id": 1, "sendTo": 1, "msg": 1})
        ar = {"all": []}
        for os in allsms:
          ms = {"sendTo": os["sendTo"], "msg": os["msg"], "id": str(os['_id'])}
          ar["all"].append(ms)
          #remove sms from stack
          self.db["Sms2Send"].update_one({'_id': ObjectId(str(os['_id']))}, {'$set': {"processed": "yes"}})
        return ar
    else:
      return "wrong phone number or password "
