l=[int(i) for i in input().split()]
n=l[0]
l.pop(0)
l1=[int(i) for i in input().split()]
l1.sort()
for i in l1:
    if i>=l[0] and i<=l[1]:
        print(i)
        break
