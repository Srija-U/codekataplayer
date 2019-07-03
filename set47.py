n=int(input())
c=0
for i in range(n):
    l=[int(i) for i in input().split()]
    if(l[0]<l[1]):
        c=c+1
print(c)
