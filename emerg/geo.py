import os, csv, json, codecs, re
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyDr3z6Nu2lBSE1bZqg-u-oeENCaF53Xhcs')
#geocode_result = gmaps.geocode(address=words, language='zh-TW')

file = codecs.open('AED.json', 'r', 'utf-8-sig')
data = json.loads(file.read())

for i in data:
    geocode_result = gmaps.geocode(address=i["場所地址"], language='zh-TW')
    if len(geocode_result)!=0:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        print(lat, lng)
        i["lat"]=lat
        i["lng"]=lng
    else:
        print("fail!")
        i["lat"]="24.8049301"
        i["lng"]="120.9723226"

with open('AED.json', 'w') as file1:
    json.dump(data, file1)
file1.close()