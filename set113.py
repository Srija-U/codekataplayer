no=int(input())
l=[int(i) for i in input().split()]
l.sort()
print(2*(l[-1]+l[-2]))
