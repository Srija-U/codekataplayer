s=[str(i) for i in input().split()]
for i in range(1,len(s)-1):
    t=s[i]
    t=t[::-1]
    s[i]=t
print(*s)
