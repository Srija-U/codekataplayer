n,k=map(int,input().split())
l=[]
c=0
for i in range(n):
    s=input()
    l.append(s)
for i in range(n-1):
    if l[i]==l[i+1]:
        c+=1
if c==k-1:
    print("yes")
else:
    print("no")
