import os, json, codecs
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyDr3z6Nu2lBSE1bZqg-u-oeENCaF53Xhcs')
#geocode_result = gmaps.geocode(address=words, language='zh-TW')

while(1):
    geocode_result = gmaps.geocode(address=input("Search:"), language='zh-TW')
    if len(geocode_result) != 0:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        print(lat, lng)
