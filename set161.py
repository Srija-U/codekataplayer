s=input()
c=0
for i in range(len(s)):
    if s[i]=='a' or s[i]=='b':
        continue
    else:
        c+=1
if c==0 or c==1:
    print("yes")
else:
    print("no")
