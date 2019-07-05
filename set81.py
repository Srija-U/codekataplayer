n=int(input())
l=[int(i) for i in input().split()]
for i in range(len(l)-1):
    if(l[i]>l[i+1]):
        print(l[i],end=' ')
    else:
        print(l[i+1],end=' ')
