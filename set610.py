l=[str(i) for i in input().split()]
s1=l[0]
s2=l[1]
for i in s1:
    if(i in s2):
        print("yes")
        exit()
print("no")
