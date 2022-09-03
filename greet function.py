#making of a function
name=str(input("enter your name"))
def greet(name):
    """This function greets to the person
        whose name is entered"""
    print("Hello "+name+ " GOOD Morning")
    return()
greet(name)
print(greet.__doc__)#it is used to print your doc string(iwhich is in triple quote)

		
