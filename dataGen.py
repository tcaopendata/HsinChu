import urllib.request
txt = "http://opendata.hccg.gov.tw/dataset/cb7a7eed-cbd3-493a-98b1-f3def68f41dc/resource/45172179-8878-467d-a180-c816ca80c110/download/20171102170538990.json"
urls = txt.split('\n')
for url in urls:
    urllib.request.urlretrieve(url,"fire.json")
