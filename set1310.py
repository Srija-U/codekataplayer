n=int(input())
l=[int(i) for i in input().split()]
s=0
for i in range(n):
    t=l[:i+1]
    if sum(t)%2==0:
        print(sum(t),end=" ")
    else:
        print(l[i],end=" ")
