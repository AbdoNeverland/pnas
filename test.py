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
        "pwd":"abdo",
        "phone":"666072026",
        "msg":"of course",
        "sendTo":"+212666072026"
        }
res = requests.post(url, json=data)
print(res.json())