s1,s2=map(str,input().split())
s2=int(s2)
f=s1[-s2:]
g=s1[:len(s1)-len(f)]
print(f+g)
