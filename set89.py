n=int(input())
l=[int(i) for i in input().split()]
r=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        t=abs(l[i]-l[j])
        r.append(t)
print(max(r))
