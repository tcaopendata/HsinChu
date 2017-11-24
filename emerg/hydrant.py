# -*- coding:utf8 -*-
import os, json, codecs
import googlemaps
import time
import random

def dig_address(words,lg):
    if lg == 0:
        print("totally fails!------------------\n\n")
        return (24.8049301+random.uniform(-0.05,0.05),120.9723226+random.uniform(-0.05,0.05))
    geocode_result = gmaps.geocode(address=words[:lg], language='zh-TW')
    if len(geocode_result) != 0:
        idx = 0
        while(idx<len(geocode_result)):
            lat = geocode_result[idx]['geometry']['location']['lat']
            lng = geocode_result[idx]['geometry']['location']['lng']
            if(pow(lat - 24, 2) < 4 and pow(lng - 120, 2) < 4):
                print("dig_succeed! in len =", lg, "---------------------",words[:lg],lat, lng)
                if(lg<=3):
                    return (24.8049301+random.uniform(-0.05,0.05),120.9723226+random.uniform(-0.05,0.05))
                else:
                    return (lat, lng)
            idx+=1
        print("geo fails!")
        print(lat, lng)
        print(words[:lg])
        print("dig in len =", lg - 1)
        return dig_address(words, lg - 1)
    else:
        print("still fails!")
        print(words[:lg])
        print("dig in len =",lg-1)
        return dig_address(words,lg-1)


gmaps = googlemaps.Client(key='AIzaSyADIUvx0j9HZqiSDEVpzR7DiN4zynB3zZw')
#geocode_result = gmaps.geocode(address=words, language='zh-TW')

file = codecs.open('hydrant.json', 'r', 'utf-8-sig')
data = json.loads(file.read())

for i in data:
    if "lat" in i.keys():
        continue
    geocode_result = gmaps.geocode(address=i["設置地點"], language='zh-TW')
    if len(geocode_result) != 0:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        print(lat, lng)
        i["lat"]=str(lat)
        i["lng"]=str(lng)
    else:
        print("fail!---------start digging",i["設置地點"],"---------------------------------")
        result = dig_address(i["設置地點"],len(i["設置地點"])-2)
        i["lat"]=str(result[0])
        i["lng"]=str(result[1])
    with open('hydrant.json', 'w') as file1:
        json.dump(data, file1)
    file1.close()

with open('hydrant.json', 'w') as file1:
    json.dump(data, file1)
file1.close()