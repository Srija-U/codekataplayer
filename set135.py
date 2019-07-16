def fun(x,y):
    if(x>y):
        num=x
        den=y
    else:
        num=y
        den=x
    rem=num%den
    while(rem!=0):
        num=den
        den=rem
        rem=num%den
    return den
n=int(input())
l=[int(i) for i in input().split()]
x=l[0]
y=l[1]
gcd=fun(x,y)
for i in range(2,len(l)):
    gcd=fun(gcd,l[i])
print(gcd)
