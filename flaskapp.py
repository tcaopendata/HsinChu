# -*- coding: utf8 -*-
from flask import Flask
import os, csv, json
app = Flask(__name__)

@app.route('/index.html')
def index():
    text = '''
        <!DOCTYPE HTML>
        <title>User Manual</title>
        <h1 align="center">-&emsp;-&emsp;-&emsp;&emsp;使用說明&emsp;&emsp;-&emsp;-&emsp;- </h1>
        <pre>(1) http://114.34.123.174:8080/index.html       ---> 查看使用說明</pre>
        <pre>(2) http://114.34.123.174:8080/                 ---> 生成path<->stop資料(不會用到，由其他API使用)</pre>
        <pre>(3) http://114.34.123.174:8080/                 ---> 生成Map Net資料(不會用到，由其他API使用)</pre>
        <pre>(4) http://114.34.123.174:8080/{緯度}/{經度}     ---> 查詢附近站牌</pre>
        '''
    return text

@app.route('/stolen')
def stolen():
    final = []
    for root, dirs, files in os.walk("."):
        for f in files:
            filename = str(f)
            print(filename,"\n------------\n")
            if filename.startswith('1'):
                csvf = open(filename,encoding = 'utf8')
                csvr = csv.reader(csvf)
                for row in csvr:
                    if row[2].startswith(u"新竹"):
                        row[0] = row[0].rstrip()
                        row = row[0:3]
                        final.append(row)
                        print(row)
    result = {"data":final}
    return jsonify(result)



if __name__ == '__main__':
    app.run()
