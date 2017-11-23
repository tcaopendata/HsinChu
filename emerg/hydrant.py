import os, json, codecs
import googlemaps

def dig_address(words,lg):
    if lg == 0:
        print("totally fails!------------------\n\n")
        return (24.8049301,120.9723226)
    geocode_result = gmaps.geocode(address=words[lg], language='zh-TW')
    if len(geocode_result) != 0:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        if pow(lat - 24,2) > 4 or pow(lng - 120,2) >4:
            print("geo fails!")
            print(lat, lng)
            print(words[:lg])
            print("dig in len =", lg - 1)
            return dig_address(words, lg - 1)
        else:
            print("dig_succeed! in len =",lg,"---------------------")
            print(words[:lg])
            print(lat, lng)
            print('\n\n')
            return (lat, lng)
    else:
        print("still fails!")
        print(words[:lg])
        print("dig in len =",lg-1)
        return dig_address(words,lg-1)


gmaps = googlemaps.Client(key='AIzaSyDr3z6Nu2lBSE1bZqg-u-oeENCaF53Xhcs')
#geocode_result = gmaps.geocode(address=words, language='zh-TW')

file = codecs.open('hydrant.json', 'r', 'utf-8-sig')
data = json.loads(file.read())

for i in data:
    geocode_result = gmaps.geocode(address=i["設置地點"], language='zh-TW')
    if len(geocode_result) != 0:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        print(lat, lng)
        i["lat"]=str(lat)
        i["lng"]=str(lng)
    else:
        print("fail!---------start digging")
        print(i["設置地點"])
        result = dig_address(i["設置地點"],len(i["設置地點"])-2)
        i["lat"]=str(result[0])
        i["lng"]=str(result[1])

with open('hydrant.json', 'w') as file1:
    json.dump(data, file1)
file1.close()