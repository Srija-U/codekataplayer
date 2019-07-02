li=[int(i) for i in input().split()]
n=li[0]
a=li[1]
l=[int(i) for i in input().split()]
l1=[int(i) for i in input().split()]
for i in range(0,a):
    l.append(l1[i])
    print(max(l),end=' ')
