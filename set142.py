s=input()
s=list(s)
l=[]
c=0
for i in range(len(s)-1):
    k=int(s[i])+int(s[i+1])
    if k%2!=0:
        c+=1
    else:
        l.append(c)
        c=0
    l.append(c)
m=max(l)
if m==0:
    print(0)
else:
    print(m+1)
