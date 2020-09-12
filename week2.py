import re
fhand=open(r"C:\Users\IITKGP\Desktop\python\regex_sum_937749.txt").read()
lst=[]
y=re.findall('[0-9]+',fhand)
z=0
count=0
for num in y:
    x=float(num)
    z=z+x
    count=count+1
print(count)
print(z)


    
