###### n terms of fibonaaci
def fibon(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibon(n-1)+fibon(n-2)    #recursive case
def fibonaaci(n):                            #use fibon functon in another function to get desire result
    for i in range(1,n+1):
        print(fibon(i),end=',')
n=int(input("enter a number"))
fibonaaci(n)
