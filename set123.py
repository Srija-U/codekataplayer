d,m,y=map(str,input().split('/'))
v=0
if(len(d)==2):
    if(int(d)>1)and(int(d)<32):
        v=1
    else:
        v=0
        print("no")
        exit()
else:
    v=0
    print("no")
    exit()
if(len(m)==2):
    if(int(m)>1)and(int(m)<13):
        v=1
    else:
        v=0
        print("no")
        exit()
else:
    v=0
    print("no")
    exit()
if(len(y)!=4):
    v=0
    print("no")
    exit()
if(v==1):
    print("yes")
