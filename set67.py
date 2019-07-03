l=[str(i) for i in input().split()]
s=l[0]
k=l[1]
c=0
for i in s:
    if(i==k):
        c=c+1
print(c)
