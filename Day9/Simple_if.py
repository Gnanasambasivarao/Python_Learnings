# Conditional statement: It is used to make decisions and execute different blocks of code based on whether a condition is true or false.
# As we use only logical , relational(Comparision), membership.

# Simple IF: In this used to execute one true case block of code.
"""
Syntax:
        If:
            Block of Code
"""

a=2
b=3
# Greaterthan(>):
if a>b:
    print(f"{a} is greatest")

# lessthan(<):
if a<b:
    print("True")

# Greaterthan or equal
if(a>=b):
    print("true")

# Less than or equal to:
if(a<=b):
    print("true")
 
# Not operation:
if(a!=b):
    print("true")

# User Input
first=int(input("First value: "))
second=int(input("second value: "))
if a==b:
    print("Both are same values.")

# first=int(input("First value: ")) =>20
# second=input("second value: ") =>20

# if a==b:
#     print("Both are same values.") 
# The above one will not execute because it check both the vallues are from same data type and values must be same 

#If condtion using Logical operator:

# ANd: Both the conditions are to be true then the block of code is executed
if first>second and second==first:
    print("true")
if first<second and second!=first:
    print("true")
if first>=second and second<=first:
    print("true")

# OR: Checks weather any one condition is true then it will execute

if first>second or second!=first:
    print(f"first value{first} is greatest")
    
# Not: 
value=False
if not first>second and second == first:
    print("true")
    
# If Condition by using membership operator

name="Samba"
# Integer:
if type(name) is int:
    print("It is integer")

if type(name) is not int:
    print(f"It is {type(name)} not integer")
    
# Float:
if type(name) is float:
    print("It is Float")

if type(name) is not float:
    print(f"It is {type(name)} not float")
    
# String:
if type(name) is str:
    print("It is String")

if type(name) is not str:
    print(f"It is {type(name)}")

lis=[10,20,30,4,5,60,44,15]    
if 10 in lis:
    print(f"10 is available in list")
    
# lists=int(input("Value:")) # single value
# if 30 in a:
#     print("true") Error

required=int(input("enter a value:"))
if required in lis:
    print("available")
if required not in lis:
    print("True value is not available")