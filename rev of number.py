def rev(n):
    sum=0
    while n>0:
        d=n%10
        sum=sum*10+d
        n=n//10
    print(sum)
n=int(input("enter a number"))
rev(n)
if(rev(n)==sum):
    print("PAllindrome")
else:
    ("not pallindrome")
