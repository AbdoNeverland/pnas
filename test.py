#!/usr/bin/python3
"""doc """
import json
from pymongo import MongoClient
import random
import datetime
import time

import requests
url = "http://127.0.0.1:5000/activate"
data = {"email": "hjh@54.2", "phone": "85465554", "pwd": "jjkjk5"}
res = requests.post(url, json=data)
print(res.json())