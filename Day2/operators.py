# Arithematic operation
a=2
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# Assignment Operator 
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a//=b
print(a)
a**=b
print(a)
a%=b
print(a)

# Comparision Operators
print(a==b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)

# Logical operator
x= True
y= False
print(x and y)#Logical AND returns True if both the operands are true
print(x or y) #Logical OR returns True if either of the operands is true
print(not x) #Logical NOT returns the opposite of the operand
print(not y) #Logical NOT returns the opposite of the operand

# Bitwise operator : 
a=10 #In binary 1010
b=5 #In binary 0101
print(a & b) #Bitwise AND returns 1 if both the bits are 1
print(a | b) #Bitwise OR returns 1 if either of the bits is 1
print(a ^ b) #Bitwise XOR returns 1 if the bits are different
print(~a) #Bitwise NOT returns the complement of the bits
print(a << 2) #Bitwise left shift shifts the bits to the left, multiple by 2
print(a >> 3) #Bitwise right shift shifts the bits to the right by the specified number of positions, dived by 2

# Membership operator
li=[10,20,30,40,50]
print(30 in li) #It return True because value is available in list.
print(66 in li) #It return False because the value is not found in list.
print(40 not in li) # It returns False, because the value is found in list.
print(60 not in li) # It returns True becuase the given value is not in list

# Note: In Dictionary It checks only keys not values, as the data in dict stored as Keys:"Value".
names={"First":" Gnana Sambasivarao", "Last":"Thota"}
print("First" in names, names)
print("Thota" in names, names)

# Identity Operation
password="Sambasivarao"
repassword="Sambasivarao"

print("\n",password is repassword) # It return True ,if the both objects are same. 
print(type(password) is int) # It returns False, if the values are not the same.
print(password is not repassword) # It returns False, if the bothe objects are same. 
print(type(password) is not float) # It return True if the both objects(values) are not same.
