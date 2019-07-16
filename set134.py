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
    gcd=den
    lcm=int(int(x*y)/int(gcd))
    return lcm
n=int(input())
l=[int(i) for i in input().split()]
x=l[0]
y=l[1]
lcm=fun(x,y)
for i in range(2,len(l)):
    lcm=fun(lcm,l[i])
print(lcm)
