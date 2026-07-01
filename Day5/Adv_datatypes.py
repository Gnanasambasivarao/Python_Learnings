# list: It collection of group of different datatypes 
# The elements in the list are mutable
# Any data type value can be stored in list
# It can contain duplicates
# It stores the elements in sequential order 

a=[1,2,3.5,"samba","siva"] #Declaration of list by using Square braces []

# List Methods 

# Append(): USed to add the elements into the list

print(a) # Before adding elemnts to list
a.append("Rao")
print(a) # After adding elements to list 

# Extend: used to add one or more elemets to the list
print(a) # Before using extend 
a.extend(["Thota","gnana"])
print(a) #After adding elements to the list 

# Insert: USed to add the elements to list in a paticular position.
print(a) # Before adding elements
a.insert(2,"5.6")
print(a) #After inserting elements at a 2nd positon 

# Sort: used to arrge the elements in the list 
b=["samba","Gnana","thota","Rao","siva"]
b.sort()
print(b)
# ['Gnana', 'Rao', 'samba', 'siva', 'thota']

c=[1,5,6,7,9,2,4,1,5]
c.sort()
print(c) 
# [1, 1, 2, 4, 5, 5, 6, 7, 9]

# Reverse: used to reverse the elements from list
b.reverse()
print(b)
c.reverse()
print(c)

# POP: it used to remove last elemnt in the list and removes that element
c.pop()
print(c)
c.pop(1)
print(c)

# Remove() : Used to remove the value from the list by given specific value
b.remove("thota")
print(b)
c.remove(5)
print(c)

# clear: used to remove all elements in the list and keep it as empty
d=["samba","sam","rao"]
print(d)
d.clear()
print(d) #remove all elements from the list leave it as empty list

# Copy: Used to make shallow copy 
d=c.copy()
print(d) #It is the duplicate one
print(c) # it is the original list

# Shallow Copy: It will effect both the strings
import copy
original_list = [[1, 2], [3, 4]]
shallow_copied = copy.copy(original_list)

# Modifying a nested object affects both
shallow_copied[0][0] = 99

print(original_list)    # Output: [[99, 2], [3, 4]]
print("Shallow copy",shallow_copied)   # Output: [[99, 2], [3, 4]]

# Deep Copy: In this it will only effect the modified list
original_list = [[1, 2], [3, 4]]
deep_copied = copy.deepcopy(original_list)

# Modifying a nested object affects ONLY the deep copy
deep_copied[0][0] = 99

print(original_list)    # Output: [[1, 2], [3, 4]]
print("Deep copy",deep_copied)      # Output: [[99, 2], [3, 4]]

# len(), count()
e=["sam","siva","rao"]
print(len(e))
print(e.count("rao"))