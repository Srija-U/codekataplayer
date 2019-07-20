n=int(input())
c=0
if(n==1):
    c=1
for i in range(0,n):
    t=2**i
    if t==n:
        c=1
        break
if c==0:
    print("no")
else:
    print("yes")
