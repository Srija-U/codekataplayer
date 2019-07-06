n,k=map(int,input().split())
l1=[int(i) for i in input().split()]
l2=[int(i) for i in input().split()]
for i in l2:
    l1.append(i)
l1.sort()
print(sep=" ",*l1)
