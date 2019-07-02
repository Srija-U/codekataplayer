n=int(input())
l=[int(i) for i in input().split()]
for i in l:
    c=0
    for j in range(0,len(l)):
        if i==l[j]:
            c=c+1
    if c<2:
        print(i)
