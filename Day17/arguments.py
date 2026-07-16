# Keyword and positional arguments
def details(id,name, mail):
    id=5
    name="Samba"
    mail="Samba@gmail.com"
    print(id, name, mail)
details(id="id", name="name", mail="mail")

def info(id , name, mail):
    print(id, name, mail)

# Keyword arguments: In this the keys are important rather than position order 
'''
id="id" ==> in this " id "is consider as keys,the id inside double qoute is know as value.
'''
info(id="id", name="name",mail="mail")
info(id=20, name="sambasivarao",mail="sambamail@gmail.com")
info(id=30, name="Siva", mail="siva@gmail.com")
# Positional argument: In this the postion order is important, because in the function we only provide the values not with keywords so 
# order is most important
info(30, "Siva","siva@gmail.com")
info("Siva",50,"siva@gmail.com")
'''
as we see above the values only mentioned and without keywords so the computer consider it as the value
info("Siva",50,"siva@gmail.com")==> In this the " siva " is assigned to id, and "50" is assigned to name because
the values are not in positional order.

'''    

# Default arguments: It will be the common value if the user donot give the values then the default value will used.
'''
syntax:
A default argument is like a backup choice you give to the computer.
def functionname(arguments, default=value):
    Block of code
'''

def grocery(item, price):
    print("item is %s" %item)
    print("item is %.2f" %price)
grocery("rice",1600)

def go1(item="Onion", price=130):
    print(f"item is {item}, price is {price}")
go1()

def go2(item,price="200"):
    print(f"item is {item} avaiable")
    print(f"price is {price}/- Ruppess only")
go2("ghee")
 
'''
def go2(item="Potato",price):
    print(f"item is {item} avaiable")
    print(f"price is {price}/- Ruppess only")
go2(500)
parameter without a default follows parameter with a default
==> In this condition error will be raised. because the non default value should not followed by default value 
It means the default should be always placed at last aguments 
 
'''

# * argument==> it used to unpack all the elements .
'''
def functionname(*args):
    Block of code
'''

b=[10,20,30,40,50,60]
print(b)
print(*b)

c=(10,20,30,40,50,60)
print(c)
print(*c)

d="Sambasivarao"
print(d)
print(*d)

names={"name":"samba", "age":20,"number":123456789}
print(names)
print(*names)

e,*f,g=1,2,3,4,5,6,7,8,9,10
print(e)
print(*f )# => this will be unpacked 
print(f) # => This will be print as list
print(g)

fi,*mi,last="Sambasivarao"
print(fi)
print(*mi)
print(mi)
print(last)
