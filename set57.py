l=[int(i) for i in input().split()]
s=0
for i in range(0,len(l)):
    if(l[i]<=0):
        print("no")
        exit()
    s=s+l[i]
if(s==180):
    print("yes")
else:
    print("no")
