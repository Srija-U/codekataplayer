n=int(input())
l=[int(i)for i in input().split()]
for i in range(n-1):
    if(l[i+1]%l[i]==0):
        print(l[i+1],end=' ')
