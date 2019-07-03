import math
n=int(input())
n=math.radians(n)
n=math.sin(n)
if(n>0):
    print(round(n,1))
else:
    print(round(n))
