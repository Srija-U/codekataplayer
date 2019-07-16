l=[str(i) for i in input().split()]
s=input()
for i in l:
    if(i==s):
        l.remove(i)
print(*l)
