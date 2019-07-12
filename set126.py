n=int(input())
l=[int(i) for i in input().split()]
d={}
res=[]
for i in range(n):
    t=l.count(l[i])
    d[l[i]]=t
l1=list(d.values())
l1.sort()
l1=l1[::-1]
for i in l1:
    for j in d:
        te=d.get(j)
        if te==i:
            res.append(j)
            d.pop(j)
            break
print(sep=" ",*res)
