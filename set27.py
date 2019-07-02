import math
l=[int(i) for i in input().split()]
print((int((l[0]*l[1])/(math.gcd(l[0],l[1])))))
