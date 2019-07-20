n=int(input())
n=str(bin(n))
c=0
for i in n:
    if i=='1':
        c+=1
print(c)
