import urllib.request
txt = '''http://opendata.hccg.gov.tw/dataset/c2ca1a41-541a-43d6-b36d-925987f9e413/resource/ff4dfae5-3d65-4e74-a08d-bdf780612552/download/20171005143110939.json'''

urls = txt.split('\n')
i=0
for url in urls:
    urllib.request.urlretrieve(url,".\emerg\data"+str(i)+".json")
    i+=1
