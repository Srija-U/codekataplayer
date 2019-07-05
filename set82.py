n=int(input())
l=[int(i) for i in input().split()]
for i in range(len(l)-1):
    if(l[i]<=l[i+1]):
        continue
    else:
        print(l[i])
        exit()
