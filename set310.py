l=[str(i) for i in input().split()]
s1=l[0]
s2=l[1]
k=l[2]
c=0
for i in range(0,len(s1)):
    if(s1[i]!=s2[i]):
        c=c+1
if(c==int(k)):
    print("yes")
else:
    print("no")
