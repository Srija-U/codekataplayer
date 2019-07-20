n,m=map(int,input().split())
c=0
for i in range(n):
    l=[int(i) for i in input().split()]
    if l[1]==m:
        c+=1
if c==0:
    print("no")
else:
    print("yes")
