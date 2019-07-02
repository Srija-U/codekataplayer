import math
l=[int(i) for i in input().split()]
c=0
n=l[1]+1
s=l[0]
for i in range(s,n):
    s=math.sqrt(i)
    if(s-math.floor(s)==0):
        c=c+1
print(c)
