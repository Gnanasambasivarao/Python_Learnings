# for loop: it used to iterate the a block of code upto n times given by user.
# In for loop the iteration is mentioned before entring to the loop
'''
Syntax:

for any_variable(name) in range(start,end):
    Block of code
    
'''
for i in range(5):
    print("Hello samba",i)
    
a=[10,20,30,40,50,60,70]
for i in a:
    print(i)
    
b="sambasivarao"
for i in b:
    print(i)
    
for i in a:
    print(i,end=",")
    
for i in a:
    print(i)
    print(type(i))
    print(type(a))
    
c=(10,20,30,40,50,60,70,80,90,100)
for i in c:
    print(i)
    print(type(c))
    print(type(i))
    

d={'year':2004,"age":20,'name':'Samba'}
for i in d:
    print(i)
    print(d[i])

for i in d.keys():
    print(i)
    print(type(i))
    
for i in d.values():
    print(i)
    print(type(i))
    
for i in d.items():
    print(i)

a=[True, False]
for i in a:
    print(a)