import math
n=int(input())
r=[]
while n%2==0:
    if (2 not in r):
        r.append(2)
    n=n/2
for i in range(3,int(math.sqrt(n))+1,2):
    while(n%i==0):
        if(i not in r):
            r.append(i)
        n=n/i
if n>2:
    r.append(n)
r.sort()
print(sep=" ",*r)
