import math
n=int(input())
l=[int(i) for i in input().split()]
if n%2==1:
    o=math.floor((n-2)/2)
else:
    o=math.floor(n/2)
l1=l[:o+1]
l2=l[o+1:]
l1.sort()
l2.sort(reverse=True)
l=l1+l2
print(*l)
