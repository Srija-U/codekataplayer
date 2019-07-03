n=int(input())
l=[int(i) for i in input().split()]
l1=l
l1=sorted(l)
if(l1==l):
    print("yes")
else:
    print("no")
