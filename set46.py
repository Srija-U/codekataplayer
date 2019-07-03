l=[str(i) for i in input().split()]
s=l[0]
c=0
for i in range(0,len(s)):
    if(s[i]==l[1]):
        c=c+1
print(c)
