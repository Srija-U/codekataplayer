n=int(input())
r=[]
if(n%2==0):
    t=n+1
else:
    t=n
for i in range(2,t,2):
    if(n%i==0):
        r.append(i)
print(sep=" ",*r)
