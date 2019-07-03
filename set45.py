a=str(input())
a=a.replace(" ","")
b=[i for i in a if(a.count(i)==1)]
c=' '.join(b)
print(c)
