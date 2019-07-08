n=int(input())
l=[int(i) for i in input().split()]
r=[]
for i in range(len(l)-1):
    if(l[i]>l[i+1]):
        r.append(l[i])
    else:
        r.append(l[i+1])
s=0
for i in range(len(r)):
    s=s+r[i]
print(s)
