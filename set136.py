n,k=map(int,input().split())
l=[int(i)for i in input().split()]
res=[]
for i in l:
    t=l.count(i)
    if(t<k):
        if(i not in res):
            res.append(i)
print(*res)
