n=int(input())
l=[int(i) for i in input().split()]
r=[]
for i in l:
    if l.count(i)==1:
        r.append(i)
    else:
        if i not in r:
            r.append(i)
print(sep=" ",*r)
