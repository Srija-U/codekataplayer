n=int(input())
l=[int(i) for i in input().split()]
r=[]
for i in range(n):
    for j in range(n):
        t=l[i]|l[j]
        r.append(t)
print(max(r))
