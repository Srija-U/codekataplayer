n=int(input())
l=[]
c=0
for i in range(n):
    s=input()
    l.append(s)
for i in range(n-1):
    if l[i]==l[i+1]:
        c=1
        break
if c==0:
    print("no")
else:
    print("yes")
