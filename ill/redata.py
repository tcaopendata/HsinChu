# -*- coding: utf-8 -*-
import os, csv, json

def sortdict(monstat):
    mon = []
    dlist = list(monstat.keys())
    dlist.sort()
    for j in dlist:
        mon.append([j, len(monstat[j])])
    return mon


final = []
for root, dirs, files in os.walk("."):
    for f in files:
        filename = str(f)
        #print(filename,"\n------------\n")
        if filename.startswith('1'):
            csvf = open(filename,encoding = 'utf8')
            csvr = csv.reader(csvf)
            for row in csvr:
                if row[2].startswith(u"新竹"):
                    row[0] = row[0].rstrip()
                    row = row[0:3]
                    final.append(row)
                    #print(row)
monstat = {}
placestat = {}
eventstat = {}
for data in final:
    if data[1][:5]+data[0] in monstat.keys():
        monstat[data[1][:5]+data[0]].append(data)
    else:
        monstat[data[1][:5]+data[0]]=[data]

    if data[2] in placestat.keys():
        placestat[data[2]].append(data)
    else:
        placestat[data[2]]=[data]

    if data[0] in eventstat.keys():
        eventstat[data[0]].append(data)
    else:
        eventstat[data[0]]=[data]

mon = sortdict(monstat)
place = sortdict(placestat)
event = sortdict(eventstat)


for i in monstat.keys():
   print(i,":",len(monstat[i]))
for i in mon:
    print(i)
# for i in place:
#     print(i)
# for i in event:
#     print(i)

# for i in placestat.keys():
#     print(i,":",len(placestat[i]))
#
# for i in eventstat.keys():
#     print(i,":",len(eventstat[i]))
result = {"mon":mon,"place":place,"event":event}
with open('stolen2.json', 'w') as file1:
    json.dump(result, file1)
file1.close()



