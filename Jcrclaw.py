import requests
from urllib import parse,request
import json

url = 'http://webapi.fenqubiao.com/api/journal'
textmod={'year':'2019','abbr':'0957-0233'}
textmod = parse.urlencode(textmod)
req = requests.get(url='%s%s%s' % (url,'?',textmod))
result = json.loads(req.text)
print(result)
print(req.text)
print("期刊名称:",result['Title'])
for index,jcr in enumerate(result['JCR']):
    print (index,"类别：%s,分区：%s"%(jcr["NameCN"],jcr["Section"]))