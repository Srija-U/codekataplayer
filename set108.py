s,a1=map(str,input().split())
f=0
a=int(a1)
s=list(s)
for i in range(a+1):
    if(str(i) in s):
        f=1
        continue
    else:
        f=0
        break
if(f==1):
    print("yes")
else:
    print("no")
