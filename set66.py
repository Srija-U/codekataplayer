l=[str(i) for i in input().split()]
s=l[0]
k=l[1]
for i in s:
    if(i==k):
        p=s.index(k)
print(p+1)
