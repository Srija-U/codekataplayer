n=int(input())
l=[int(i) for i in input().split()]
r=l[0]
for i in range(1,n):
    r=r|l[i]
print(r)
