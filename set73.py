n=int(input())
l1=[int(i) for i in input().split()]
l2=[int(i) for i in input().split()]
res=[]
for i in l1:
    if(i in l2)and(i not in res):
        res.append(i)
print(sep=" ",*res)
