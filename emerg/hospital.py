# -*- coding:utf8 -*-
import os, json, codecs
import googlemaps
import time
import random


gmaps = googlemaps.Client(key='AIzaSyADIUvx0j9HZqiSDEVpzR7DiN4zynB3zZw')
#geocode_result = gmaps.geocode(address=words, language='zh-TW')

file = codecs.open('hospital.json', 'r', 'utf-8-sig')
data = json.loads(file.read())
rec = {}


for i in data:
    if "lat" in i.keys():
        continue
    print(i["地址"])


    if i["地址"] in rec.keys():
        lat, lng=rec[i["地址"]]
        i["lat"] = str(lat)
        i["lng"] = str(lng)
        with open('hospital.json.json', 'w') as file1:
            json.dump(data, file1)
        file1.close()
        print("直接套用",i["地址"])
        continue


    geocode_result = gmaps.geocode(address="新竹"+i["地址"], language='zh-TW')
    if len(geocode_result) != 0:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        print("找到了",i["地址"], " -> ",i["地址"],lat, lng)
        rec[i["地址"]]=(lat, lng)
        i["lat"]=str(lat)
        i["lng"]=str(lng)
    else:
        print("\n失敗",i["地址"], " -> ",i["地址"],"---------------------------------")
        result = (24.8049301 + random.uniform(-0.05, 0.05), 120.9723226 + random.uniform(-0.05, 0.05))
        print("亂數分配",result)
        i["lat"] = str(result[0])
        i["lng"] = str(result[1])
    with open('hospital.json', 'w') as file1:
        json.dump(data, file1)
    file1.close()

with open('hospital.json', 'w') as file1:
    json.dump(data, file1)
file1.close()