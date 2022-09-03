#fibonacci Series
A=int(input("enter a number"))
a=-1
b=1
sum=0
I=1
while(I<=A):
    print(sum)
    I+=1
    a=b
    b=sum
    sum=a+b
