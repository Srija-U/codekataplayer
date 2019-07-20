n=int(input())
n=str(bin(n))
c=1
for i in range(len(n)-1,0,-1):
    if n[i]=='1':
        print(c)
        break
    c+=1
