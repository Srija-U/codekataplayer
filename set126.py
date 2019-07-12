n=int(input())
l=[int(i) for i in input().split()]
l=list(set(l))
b=[]
res=[]
c=0
for i in l:
    b.append(l.count(i))
while c<len(b):
    t=b.index(max(b))
    res.append(l[t])
    b[t]=0
    c+=1
print(*res)
