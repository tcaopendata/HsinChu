# -*- coding:utf8 -*-
import os, json, codecs
import googlemaps
import time
import random

def is_chinese(uchar):
    if u'\u4e00' <= uchar<=u'\u9fff':
        return True
    else:
        return False

gmaps = googlemaps.Client(key='AIzaSyADIUvx0j9HZqiSDEVpzR7DiN4zynB3zZw')
#geocode_result = gmaps.geocode(address=words, language='zh-TW')

file = codecs.open('ruleshot.json', 'r', 'utf-8-sig')
data = json.loads(file.read())
rec = {}


for i in data:
    if "lat" in i.keys():
        continue
    print(i["違規地點"])

    sta = -1
    while (sta < len(i["違規地點"])):
        sta += 1
        if is_chinese(i["違規地點"][sta]):
            break

    pos = 0
    while (pos < len(i["違規地點"])):
        pos += 1
        if i["違規地點"][pos] in ["、", "與", "上", "(", "口", "匝", "往", "制", "前"]:
            break
        if i["違規地點"][pos] in ["巷", "段", "號", "街", "弄", "場"]:
            pos += 1
            break

    if i["違規地點"][sta:pos] in rec.keys():
        lat, lng=rec[i["違規地點"][sta:pos]]
        i["lat"] = str(lat)
        i["lng"] = str(lng)
        with open('ruleshot.json', 'w') as file1:
            json.dump(data, file1)
        file1.close()
        print("直接套用",i["違規地點"][sta:pos])
        continue


    geocode_result = gmaps.geocode(address="新竹"+i["違規地點"][sta:pos], language='zh-TW')
    if len(geocode_result) != 0:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        print("找到了",i["違規地點"], " -> ",i["違規地點"][sta:pos],lat, lng)
        rec[i["違規地點"][sta:pos]]=(lat, lng)
        i["lat"]=str(lat)
        i["lng"]=str(lng)
    else:
        print("\n失敗",i["違規地點"], " -> ",i["違規地點"][sta:pos],"---------------------------------")
        result = (24.8049301 + random.uniform(-0.05, 0.05), 120.9723226 + random.uniform(-0.05, 0.05))
        print("亂數分配",result)
        i["lat"] = str(result[0])
        i["lng"] = str(result[1])
    with open('ruleshot.json', 'w') as file1:
        json.dump(data, file1)
    file1.close()

with open('ruleshot.json', 'w') as file1:
    json.dump(data, file1)
file1.close()