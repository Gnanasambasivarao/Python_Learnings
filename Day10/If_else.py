# If else conditions by using comparision operators.

'''
Syntax:

if Condition:
    Block of Code(It executes if condition is true)
else:
    Block of code(it executes if condition is false)

'''
a=3
b=6
if a<b:
    print("true")
else:
    print("false")

c=9
d=10
if c!=d:
    print("Both values are different")
else:
    print("Values are same")
    
# If else using logical operators.
e=10
f=20
if e>f and e>0:
    print(f"greater than")
else:
    print(f" less than ")
    
if e<f or f>0:
    print(f"true")
else:
    print("False")
    
if not e>f:
    print("True")
else:
    print("False")


# If else using membership operator.

lis=[10,20,30,40,50,60,70,80,90,100]
required=int(input("Value:"))
if required in lis:
    print("Available in list")
else:
    print("Not Available")

lis1=["samba", "siva","Rao"]
required1=input("Value")
if required1 not in lis1:
    print("Not Available in list")
else:
    print("Available in list")

# If else using identity operator.

username=input("Enter username")
Name=input("Enter name:")

if username is Name:
    print("Both are same")
else:
    print("Both are different")

if username is not Name:
    print("Both are different values")
else:
    print("Both are same")
