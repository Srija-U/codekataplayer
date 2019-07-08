a1,b1=map(int,input().split())
su=0
for i in range(a1,b1+1):
    if i%2==1:
        su=su+i
print(su)
