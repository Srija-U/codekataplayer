a1,b1=map(int,input().split())
s=0
for i in range(a1,b1+1):
    if i%2==1:
        s=s+i
print(s)
