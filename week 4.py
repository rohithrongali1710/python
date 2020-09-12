import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

fhand=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_937751.html').read()
soup=BeautifulSoup(fhand,'html.parser')

tags=soup('span')
list=[]
for tag in tags:
    list.append(tag.contents[0])
##print(list)
sum=0
count=0
for i in list:
    sum=float(i)+sum
    count=count+1
print(sum)
print(count)


#imp part
 # Look at the parts of a tag
 #  print 'TAG:',tag                     to print tag
 #  print 'URL:',tag.get('href', None)   to print link
 #  print 'Contents:',tag.contents[0]    to print tag contents
 #  print 'Attrs:',tag.attrs             to print tag attributes
