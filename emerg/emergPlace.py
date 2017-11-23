import os, csv, json, codecs, re

file = codecs.open('emergPlace.json', 'r', 'utf-8-sig')
data = json.loads(file.read())

for i in data:
    i["lat"] = i.pop(u"緯度")
    i["lng"] = i.pop(u"經度")

with open('emergPlace.json', 'w') as file1:
    json.dump(data, file1)
file1.close()