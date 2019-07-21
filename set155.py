n=int(input())
l=[int(i)for i in input().split()]
for i in range(n-1):
    if(l[i+1]-l[i]==1):
        c=1
    else:
        c=0
        break
if c==1:
    print("yes")
else:
    print("no")
