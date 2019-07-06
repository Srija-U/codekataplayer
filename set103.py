n=int(input())
t=0
if(n%2==1):
    n=n-1
    t=1
l=[int(i) for i in input().split()]
r=[]
for i in range(n):
    if(i%2==0):
        r.append(l[i+1])
    else:
        r.append(l[i-1])
if(t==1):
    r.append(l[n])
print(sep=" ",*r)
