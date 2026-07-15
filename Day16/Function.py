# Function: A function is a specific block of code designed to perform a particular task, which can involve single or multiple operations
# => Python give inbuilt function like print, u can make your own function. these are called user defined function
# => function blocks begin with thekeyword called def, followed by function name with paranthesis()
'''
Syntax:
def Function _name():
    Block of code
'''
# Normal way of aithematic operation without using functions
a=1000
b=2000
print("add",a+b)
print("subtract",a-b) 
print("Multiple",a*b)
a=20000
b=30000
print("add",a+b)
print("subtract",a-b) 
print("Multiple",a*b)
a=50000000
b=2560515493
print("add",a+b)
print("subtract",a-b) 
print("Multiple",a*b)

# By using Function for this operation.
# It reduces the line in the code by reusability concept.
def calculate(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
calculate(20,30)
calculate(20045,3000)
calculate(202544,3096568)

def power(a,b):
    print(a**b)
def modulus(a,b):
    print(a%b)
def floordivsion(a,b):
    print(a//b)

power(20,30)
modulus(50,60)
floordivsion(200,10)

# Using inbuilt function
print(pow(10,20))
quo,rem=divmod(200,100)
print(quo) #Floor division
print(rem) # Modulus

#Recursive Function : A function inside another function
'''while True:
    def add():
        a=int(input("Enter value"))
        b=int(input("Enter value"))
        print(a+b)
    add()
It is one way of printing values in infinity loop
'''   
# It is another ways of printing values in infinity loop by usinf recursive function.
'''
def add():
    a=int(input("Enter a value"))
    b=int(input("Enter a value"))
    print(a+b)
    add()
add()
'''
#WAP to print my name using function and make sure the first alphabet in the name should be capital
def fullname():
    first=input()
    second=input()
    print((first+' '+second).title())
fullname()

'''
Print: it displays information to the human user on the screen.Inbuilt function
Return(keyword): The function hands the data back to the code. Nothing shows up on the screen unless you explicitly(extenally) ask it to display.
'''
# Using return:
def multiplication():
    a=int(input("Enter a value:"))
    b=int(input("Enter b value:"))
    return a*b

print(multiplication())

'''
If you want to just display the data and leave the dat use "PRINT",
If your function is doing work that another piece of code will need to use later.If you want to use the data in entire process just use the return 
'''


