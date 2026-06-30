# String Methods: These are the methods that helps to do operation on string

# Length: Used to find the number of characters in a string 
print(len("Python")) # O/p: 6
print(len("Python Course")) # O/p: 13
print(len("")) # O/p: Zero
print(len(" ")) #O/p: 1 because in python spaces ae consider as charaters so 1 space= 1 character

# Count() : used to find how many repeated elements are there in a string or list or tuple or any other datatype
# In this we cannot directly use this function , we have to use this method by object type
a="sambasivarao sambathota"
print(a.count("samba"))

# Find a string: USed to provide the index value of this  given data
# For this also the same method acces as count by object 
b="thota Gnana Sambasivarao"
print(b.find("s"))

# Escape Sequences: \n, \t,\, etc.. 
c="United kingdom"
print("",b,"\n",c)

print(" Name:Thota Gnana Sambasivarao \n Contact: +9190xxxxxxxx \n Age: 23 \t Gender: Male")

# Replace(): It used to replace the old value with new value
d="Work smart with nohard"
d=d.replace("no","")
print(d)

# Upper(): Change to upper
ed="samba"
ed=ed.upper()
print(ed)
# Lower(): Used to change from any word to lower
ed=ed.lower()                     
print(ed)
# Capitalize: Change first letter of wor to capital 
ed= ed.capitalize()
print(ed)
# Title(): used to chage first letter of every world to capital
ec="thota samba"
ec=ec.title()
print(ec)

ea="Samba"
print(ea.isupper())
print(ea.islower())
print(ea.isalpha())

eq="123"
print(eq.isdigit())

# ISalnum
ew="Samba23"
print(ew.isalnum())

# Satrtswith
name="Thota"
print("\n",name.startswith('T'))
print(name.endswith('T'))

# Strip: lstrip, rstrip: USed to remove the space 
full_name=" Thota Gnana sambasivarao "
print(full_name.strip())
fName="                samba"
print(fName.lstrip())
Lname="samba             "
print(Lname.rstrip())

# Split(): Used to divide the strings into list 
first_name="Thota Gnana Samba siva rao"
print(first_name.split())

# Join(): It used to merge the splited words 
name_="samba","siva","rao"
print("".join(name_))
print(" ".join(name_))
print("@".join(name_))

