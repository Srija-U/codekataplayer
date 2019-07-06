n=int(input())
l=[int(i) for i in input().split()]
r=0
for i in range(0,n):
    for j in range(i+1,n):
        r=l[i]^l[j]
print(r)
