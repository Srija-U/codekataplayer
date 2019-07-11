n=int(input())
l=[int(i) for i in input().split()]
l1=sorted(l)
for i in l1:
    print(l.index(i)+1,end=" ")
