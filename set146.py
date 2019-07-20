n,k=map(int,input().split())
l=[int(i) for i in input().split()]
c=0
for i in l:
    if i==k:
        c+=1
if c==0:
    print("no")
else:
    print("yes",c)
