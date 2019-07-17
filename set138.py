n=int(input())
l=[int(i) for i in input().split()]
prod=1
for i in range(n):
    prod*=l[i]
if prod%2==0:
    print("even")
else:
    print("odd")
