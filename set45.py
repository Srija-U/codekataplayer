import string
a=str(input())
a=a.lower()
a=a.replace(" ","")
b=[i for i in a if(a.count(i)==1)]
c=' '.join(b)
print(c.lower())
