def dectobin(n):
    if n>1:
        dectobin(n//2)
    print(n%2,end="")
n=int(input())
dectobin(n)
