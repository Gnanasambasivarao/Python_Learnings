# Dictionary:
#  It is special data type used to store the data in "key : value"
#  If the variable is has {} then it is consider as dictionary not as set
#  IN THE dICTIONARY THE KEY SHOULD BE UNIQUE
#  It is mutable , in this elements can be changes
#  It does not allow duplicates.

a={'name':"Samba", 'year': '2004'} # Declaration of dictionary  
print(type(a))
print(a)  # {'name': 'Samba', 'year': '2004'}

# Dictionary methods:

# 1.Update: Used to add new value to the dictionary 
# In this it over writes the key with new value in place of old value 
print("Before update",a)  # {'name': 'Samba', 'year': '2004'} 
a.update({'last_name':'Thota', 'Gmail': 'samba@gmail.com'})
print(f"After update {a}")  # {'name': 'Samba', 'year': '2004', 'last_name': 'Thota', 'Gmail': 'samba@gmail.com'}

# 2. set default: used to store the value if the key is not used in dict , if mentioned it donot overwrite. 
a.setdefault("age", 20)
print(a)

# Get: used to acces the value from the dictionary by using the key.
print(a["name"])
print(a.get("last_name"))

# keys: used to display the all the keys available in dict
print(a.keys())
# Values: Displaces all the values from dict
print(a.values())
# items: used to display all the key values as a combination in tuple format
print(a.items())

# POP: Used to remove and return the element 
# In this atleast one argument(Key) has to be passed 
b={'city': 'Guntur',"country":"India", 'state':"ap"}
print(b.pop("city"))
print(b)

# POPItem: used to remove the last element of the dictionary.
print(b.popitem())
print(b)

# len, copy,clear
print(len(a))
print(len(b))
print(b.copy())
print(b.clear())

# Mutable(not an method)

c={'Name':"siva","middle": 'Rao',"Name":"Samba"}
print(c)
d={'Name':"siva","middle": 'Rao',"Name1":"Samba"}
print(d)


e={"ids":[10,20,30],"Name":["Siva","samba","rao"],"marks": [80,85,90]}
print(e)
print(e.keys())
print(e.values())
print(e.items())

# count: As in this dictionary no count methods as we use key - value 
# Index : No index method