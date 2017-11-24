# -*- coding:utf8 -*-
import os, json, codecs
import googlemaps
import time
import random

gmaps = googlemaps.Client(key='AIzaSyADIUvx0j9HZqiSDEVpzR7DiN4zynB3zZw')
#geocode_result = gmaps.geocode(address=words, language='zh-TW')

file = codecs.open('ruleshot.json', 'r', 'utf-8-sig')
data = json.loads(file.read())
rec = {}
for i in data:
    if "lat" in i.keys():
        continue
    if i["違規地點"] in rec.keys():
        lat, lng=rec[i["違規地點"]]
        i["lat"] = str(lat)
        i["lng"] = str(lng)
        with open('ruleshot.json', 'w') as file1:
            json.dump(data, file1)
        file1.close()
        print("直接套用",i["違規地點"])
        continue

    pos = 0
    while(pos<len(i["違規地點"])):
        pos+=1
        if i["違規地點"][pos] in ["、","與","上","(","口","匝"]:
            break
        if i["違規地點"][pos] in ["巷","段","號","街","弄"]:
            pos+=1
            break

    geocode_result = gmaps.geocode(address=i["違規地點"][:pos], language='zh-TW')
    if len(geocode_result) != 0:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        print("找到了",i["違規地點"],lat, lng)
        rec[i["違規地點"]]=(lat, lng)
        i["lat"]=str(lat)
        i["lng"]=str(lng)
    else:
        print("fail!---------start digging",i["違規地點"][:pos],"---------------------------------")
    with open('ruleshot.json', 'w') as file1:
        json.dump(data, file1)
    file1.close()

with open('ruleshot.json', 'w') as file1:
    json.dump(data, file1)
file1.close()