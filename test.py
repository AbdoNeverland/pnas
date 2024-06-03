#!/usr/bin/python3
"""doc """
import json
from pymongo import MongoClient
import random
import datetime
import time

import requests
url = "http://127.0.0.1:5000/add-sms"
data = {"email":"",
        "pwd":"bismiallah",
        "phone":"666072026",
        "msg":"again your verific",
        "sendTo":"85455"
        }
res = requests.post(url, json=data)
print(res.json())