n=str(input())
r=0
for i in range(len(n)):
    t=int(n[i])
    t=t*(2**i)
    r=r+t
print(r)
