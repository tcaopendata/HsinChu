import json
import codecs

f = codecs.open("fire.json", 'r', 'utf-8-sig')
data = json.loads(f.read())
dlist =[]
for i in data:
    dlist.append([i["年度"],i["月份"],i["火災次數總計"],i["死亡人數"],i["受傷人數"],i["房屋損失"],i["財物損失"],i["合計"]])

for i in dlist:
    print(i)