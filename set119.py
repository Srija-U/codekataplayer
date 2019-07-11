n=int(input())
l=[int(i) for i in input().split()]
s=0
r=[]
for i in l:
    s=s+i
    r.append(s)
r=r[::-1]
print(sep=" ",*r)
