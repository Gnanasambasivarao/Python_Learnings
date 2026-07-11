# Break: It is used to terminate the entire loop
# Continue: It just skip the current iterration and the rest of the code will continue.
# Pass: It is also known as null statement , it does nothing but syntatically we need

# Break:
a=20
while a>7:
    print(a, end=" ")
    a=a-1
    if a==12:
        break
    
for i in range(40,80):
    print(i,end=" ")
    if i==62:
        break
    
b="PYthon"
for i in b:
    if i =='h':
        break
    print(i, end=" ")
    
# Continue:
for i in range(45): 
    if i == 20: 
        continue 
    print(i)
    
n=10
while n>0:
    n=n-1
    if n==3:
        continue
    print(n)

a="SamAba"    
for i in a:
    if a=="A":
        continue
    print(i)
    

# Pass:
c=114
while c>100:
    print(c)
    c-=1
    if c>105:
        pass
    

for i in range(10,100):
    print(i)
    if i == 75:
        pass

# Error occurs if no operation is done in if statement 
# for i in range(10,100):
#     print(i)
#     if i == 75:
#         (Empty)  Error raise: IndentationError: expected an indented block after 'if' statement on line 61
# So we use PAss in place of empty to avoid errors.