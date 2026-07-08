# IF elif else conditional statement is used check mutiple condition.

'''
Syntax:

if Condition1:
    Block of code
elif Condition2:
    Blok of code
elif condition3:
    Block of code
else:
    Block of code

'''
# If elif else by using comparison operator.

first=int(input("First value: "))
second=int(input("Second value: "))

if first> second:
    print(f"{first} is greatest")
elif second>first:
    print(f"{second} is greatest")
else:
    print("All are equal.")
        
if first==second:
    print("All are equal")
elif first != second:
    print("Both are different")
else:
    print("Default")

# If elif else using identity operator.
loginapproved=None
if loginapproved is None:
    print("Login is restricted")
elif loginapproved is not None:
    print("Login approved")
else:
    print("Unauthorised access get your permission.")
    
# If elif else by using logical operator.

a=int(input("First value"))
b=int(input("Second value"))

if a>b and a>0:
    print(f"{a} is positive value and it is greater than {b}")
elif b>a and b>0:
    print(f"{b} is positive value and it is greater than {a}")
elif a==b and a!=0:
    print("Both values are equal and first is not equal to zero ")
else:
    print("")
    
# If elif else using Member ship operator
password=["SAmbasivarao","Thota","2026"]
entered_password=input("Password:")
if entered_password in password:
    print("available")
elif entered_password not in password:
    print("True and Not available")
else:
    print("Access denied try again")
    