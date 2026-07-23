# Global and local variable
'''
If a variable is inside the function is called local variables
If a variable is declared out the function and accessible in the entire global space is called global variable.

'''

# Global variable 
# it is declared outside the function 
count=0 # global variable 
a=10
def check():
    print(a) # accesing the variable inside the function
check() 
print(a)# accesing the variable outside the function

# So 'a' is a global vaariable

def check2():
    a=5 # this is consider as local variable
    a**=2
    print(a) # It prints 25 
check2()
print(a) # It will print a=10 as the a is here consider as global variable.

# Third case
b=2
def check3():
    b=7
    print("First value is ", b)
    b=10
    print("second value is ", b)
    b=14
    print("third value is ", b)
    c=15
    c+=b
    print("values of c is ", c)
check3()
print("B value is ",b)
# print("c value is ", c)
""" NameError: name 'c' is not defined """
# Error will be raised because C is local scope variable. 

# Fouth case:
'''
In this we use global keyword that access the gobal variable called value and do some operation on the variable
and update the values to the variable.

==> It will update the value in global variable if i access the variable in function by using Global keyword
at first value is 30
called variable inside the def function by using global keyword 
then done some operations on value
as i assign the value to 900 in the function.
as well as the global variable values is also updated to 900. 

'''
value=30
def square():
    global value
    value**=2
    return value

print(square())
print(value)

