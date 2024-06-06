#!/usr/bin/python3
"""testing api module"""
import json
from pymongo import MongoClient
import random
import datetime
import time

import requests
url = "http://127.0.0.1:5000/add-sms"
data = {"email": "",
        "pwd": "",
        "phone": "",
        "msg": "testing",
        "sendTo": ""
        }
res = requests.post(url, json=data)
print(res.json())
