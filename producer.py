import requests
from requests.auth import HTTPBasicAuth
import json
import lorem
import time
import random
import multiprocess

headers = {"Content-Type": "application/vnd.kafka.json.v2+json"}


url = "http://localhost:8082/topics/geoff13"
headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}

def f():
    cpt = 0
    while(cpt < 100000):
        data = {"records":[{"value":{"id": cpt, "random": lorem.sentence()}}]}
        r = requests.post(url, data=json.dumps(data), headers=headers, auth=HTTPBasicAuth('thisismyusername', 'thisismypass'))
        cpt = cpt + 1
        #time.sleep(random.random()/10)
        if(cpt%100 == 0):
            print(cpt)

f()
