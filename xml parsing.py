import urllib.request,urllib.parse,urllib.parse
import xml.etree.ElementTree as ET

fhand=urllib.request.urlopen(' http://py4e-data.dr-chuck.net/comments_937753.xml').read()
stuff=ET.fromstring(fhand)
a=stuff.findall('comments/comment')

list=[]
for items in a:
    list.append(items.find('count').text)
#print(list)
sum=0
for i in list:
    sum=sum+float(i)
print(sum)