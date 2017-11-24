# -*- coding:utf8 -*-
import os, json, codecs
import googlemaps
import time
import random

file = codecs.open('monitor.json', 'r', 'utf-8-sig')
data = json.loads(file.read())

for i in data:
    result = (24.8049301 + random.uniform(-0.05, 0.05), 120.9723226 + random.uniform(-0.05, 0.05))
    i["lat"]=str(result[0])
    i["lng"]=str(result[1])

with open('monitor.json', 'w') as file1:
    json.dump(data, file1)
file1.close()