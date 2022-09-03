def fibo(n):
    if n==1:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
def fbo(n):
    for i in range(1,n+1):
        print(fbo(i),end=" ")
n=int(input("enter a number:-"))
fbo(n)
