l=[int(i) for i in input().split()]
n=l[0]
k=l[1]
b=n//2
for i in range(0,b):
    a=pow(k,i)
    if(a==n):
        print("yes")
        exit()
print("no")
