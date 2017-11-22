# -*- coding: utf8 -*-
from flask import Flask, jsonify
from flask import make_response
from flask import request
from flask import abort
import os, csv, json
import codecs
app = Flask(__name__)

@app.route('/')
def index():
    text = '''
        <!DOCTYPE HTML>
        <title>User Manual</title>
        <h1 align="center">-&emsp;-&emsp;-&emsp;&emsp;使用說明&emsp;&emsp;-&emsp;-&emsp;- </h1>
    <pre>(1) <a href="http://114.34.123.174:8080/">http://114.34.123.174:8080/</a>       ---> 查看使用說明</pre>
        <pre>(2) <a href="http://114.34.123.174:8080/stolen">http://114.34.123.174:8080/stolen</a>           ---> 新竹犯罪資料</pre>
        <pre>(3) <a href="http://114.34.123.174:8080/fireDep">http://114.34.123.174:8080/fireDep</a>           --->消防局資料 </pre>
        <pre>(4) http://114.34.123.174:8080/{緯度}/{經度}    ---> </pre>
        '''
    return text

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
    result = {"data":final}
    return jsonify(result)

@app.route('/fireDep')
def fireDep():
    os.chdir("/home/yung-sung/HsinChu/emerg")
    f = codecs.open("fireDep.json", 'r', 'utf-8-sig')
    j = json.load(f)
    return jsonify(j)


if __name__ == '__main__':
    app.run()
