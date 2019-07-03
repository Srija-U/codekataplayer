n,s=map(int,input().split())
peri=(n//2)-1
area=s
for i in range(1,peri+1):
    if(i*peri==area):
        print("yes")
        exit()
    else:
        peri=peri-1
print("no")
