s=input()
su=0
for i in range(len(s)):
    if(int(s[i])%2==1):
        su+=int(s[i])
if su%2==0:
    print("E")
else:
    print("O")
