import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
x=int(input('Enter position:'))-1
y=int(input('Enter count:'))
count=0
url='http://py4e-data.dr-chuck.net/known_by_Riyadh.htmly'
while (y>count):
    fhand=urllib.request.urlopen(  url).read()
    soup=BeautifulSoup(fhand,'html.parser')

    tags=soup('a')
    list=[]
    for tag in tags:
        list.append(tag.get('href', None))
    print(list[x])
    url=list[x]
    count=count+1
    

 
    


    





