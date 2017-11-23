import json
import codecs
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