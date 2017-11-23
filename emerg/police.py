# -*- coding: utf8 -*-
import os, csv, json, codecs, re

file = codecs.open('police.json', 'r', 'utf-8-sig')
data = json.loads(file.read())

for i in data:
    i["lat"] = i.pop("X軸座標")
    i["lng"] = i.pop("Y軸座標")

with open('police.json', 'w') as file1:
    json.dump(data, file1)
file1.close()