z=int(input())
a=[]
for i in range(0,z):
    a.append(list(map(int,input().split())))
m=0
res=0
for i in range(0,z):
    for j in range(0,z):
        if(a[i][j]==1):
            if(i!=z-1)and(a[i+1][j]==0):
                m=m+1
            if(j!=z-1)and(a[i][j+1]==0):
                m=m+1
            if(i!=0)and(a[i-1][j]==0):
                m=m+1
            if(j!=0)and(a[i][j-1]==0):
                m=m+1
            if((i==0)and(j==0))or((i==z-1)and(j==0))or((i==z-1)and(j==z-1))or((j==z-1)and(i==0)):
                res=res+1
            elif i==1 and j>0 and j<z-1 and m==3:
                res=res+1
            elif m==4:
                res=res+1
        m=0
print(res)
