n,k=map(int,input().split())
l=[int(i) for i in input().split()]
for i in l:
    if l.count(i)==k:
        print(i)
        break
