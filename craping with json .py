#https://www.coursera.org/learn/python-network-data/lecture/G1up7/worked-example-json-chapter-13
import urllib.request,urllib.parse,urllib.error
import json
data=urllib.request.urlopen(' http://py4e-data.dr-chuck.net/comments_937754.json').read()
info = json.loads(data)
total=0

for tags in info['comments']:
    total=total+tags['count']
print(total)