s=input()
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if(s[i]==s[j]):
            print("yes")
            exit()
print("no")
