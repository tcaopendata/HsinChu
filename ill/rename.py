# -*- coding: utf-8 -*-
import os, csv, json
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
with open('stolen_event.json', 'w') as file1:
    json.dump(result, file1)
file1.close()
