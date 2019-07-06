import math
n,sri=map(int,input().split())
a=math.factorial(n)
b=math.factorial(n-sri)
print(int(a/b))
