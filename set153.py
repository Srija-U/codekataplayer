n=int(input())
l1=[int(i)for i in input().split()]
l2=[int(i) for i in input().split()]
for i in range(n):
    t=min(l2)
    p=l2.index(t)
    print(l1[p],end=' ')
    l2[p]=10000000000
