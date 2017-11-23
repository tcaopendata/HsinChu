# -*- coding: utf8 -*-
from flask import Flask, jsonify
from flask import make_response
from flask import request
from flask import abort
import os, csv, json
import codecs

def sortdict(monstat):
    mon = []
    dlist = list(monstat.keys())
    dlist.sort()
    for j in dlist:
        mon.append([j, len(monstat[j])])
    return mon

app = Flask(__name__)

@app.route('/')
def index():
    return open("index.html").read()

@app.route('/stolen')
def stolen():
    os.chdir("/home/yung-sung/HsinChu/ill")
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
        if data[1][:5] in monstat.keys():
            monstat[data[1][:5]].append(data)
        else:
            monstat[data[1][:5]]=[data]

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

    #for i in monstat.keys():#    print(i,":",len(monstat[i]))
    # for i in mon:
    #     print(i)
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
    return jsonify(result)

@app.route('/fireDep')
def fireDep():
    os.chdir("/home/yung-sung/HsinChu/emerg")
    f = codecs.open("fireDep.json", 'r', 'utf-8-sig')
    j = json.load(f)
    return jsonify(j)

@app.route('/emerg')
def emerg():
    os.chdir("/home/yung-sung/HsinChu/emerg")
    file = codecs.open('AED.json', 'r', 'utf-8-sig')
    a = json.loads(file.read())

    file = codecs.open('emergPlace.json', 'r', 'utf-8-sig')
    e = json.loads(file.read())

    file = codecs.open('fireDep.json', 'r', 'utf-8-sig')
    f = json.loads(file.read())

    file = codecs.open('hydrant.json', 'r', 'utf-8-sig')
    h = json.loads(file.read())

    file = codecs.open('monitor.json', 'r', 'utf-8-sig')
    m = json.loads(file.read())

    file = codecs.open('police.json', 'r', 'utf-8-sig')
    p = json.loads(file.read())

    result = {"AED":a,
            "emergPlace":e,
            "fireDep":f,
            "hydrant":h,
            "monitor":m,
            "police":p}
    return jsonify(result)


if __name__ == '__main__':
    app.run()
