import requests
from requests.auth import HTTPBasicAuth
import json
import time
import numpy as np
import random

# create consumer
headers = {"Content-Type": "application/vnd.kafka.json.v2+json","Accept":"application/vnd.kafka.v2+json"}
data = {"name": "geoff13", "format": "json", "auto.offset.reset": "earliest"}
url = "http://localhost:8082/consumers/geoff13"
r = requests.post(url, data=json.dumps(data), headers=headers, auth=HTTPBasicAuth('thisismyusername', 'thisismypass'))

print(r.text)
print("create consumer ok")

## Subscribe
headers = {"Content-Type": "application/vnd.kafka.json.v2+json"}
data = {"topics":["geoff13"]}
url = 'http://localhost:8082/consumers/geoff13/instances/geoff13/subscription'
r = requests.post(url, data=json.dumps(data), headers=headers, auth=HTTPBasicAuth('thisismyusername', 'thisismypass'))

print(r.text)
print("subscribe ok")

arr = []
while(len(arr) < 100000):
   # Get records
   headers = {"Accept": "application/vnd.kafka.json.v2+json"}
   data = {"topics":["geoff13"]}
   url = 'http://localhost:8082/consumers/geoff13/instances/geoff13/records'
   r = requests.get(url, headers=headers, auth=HTTPBasicAuth('thisismyusername', 'thisismypass'))
   dic = json.loads(r.text)
   for d in dic: 
      arr.append(d['value']['id'])
   time.sleep(random.random()*10)

np.savetxt("array.txt", np.array(arr), fmt="%s")


