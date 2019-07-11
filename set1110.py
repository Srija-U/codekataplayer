n=int(input())
l=[int(i) for i in input().split()]
s=0
r=[]
res=[]
for i in l:
    s=s+i
    r.append(s)
re=r[::-1]
for i in range(n):
    res.append(r[i]+re[i])
print(sep=" ",*res)
