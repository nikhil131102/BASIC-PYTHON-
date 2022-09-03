#64
X=input(("Enter your figure for which area to be calculated:-"))
X=X.lower()
if(X=="circle"):
    R=int(input("enter radius:- "))
    A_C=3.14*R*R
    print(A_C)
elif(X=="square"):
    S=int(input("enter side"))
    A_S=S*S
    print(A_S)
elif(X=="rectangle"):
    L=int(input("enter length:-"))
    B=int(input("enter breadth:-"))
    A_R=L*B
    print(A_R)
elif(X=="triangle"):
    BH=int(input("enter base:-"))
    H=int(input("enter height:-"))
    A_T=0.5*BH*H
    print(A_T)
else:
    print("enter a right fig.")

    

