n=int(input())
l=[str(i) for i in input().split()]
l.sort()
l.sort(key=len)
print(sep=" ",*l)
