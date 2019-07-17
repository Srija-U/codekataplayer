n=int(input())
l=[int(i) for i in input().split()]
s=0
for i in l:
    if(i<0):
        s+=i
print(s)
