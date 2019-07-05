n=int(input())
ec=0
oc=0
ev=0
ov=0
l=[int(i) for i in input().split()]
for i in l:
    if i%2==0:
        ec=ec+1
        ev=i
    else:
        oc=oc+1
        ov=i
if(ec==1):
    print(ev)
else:
    print(ov)
