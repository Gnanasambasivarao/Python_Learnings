#Anonymous function: it is the function with namesless we 
#we define them by using lambda keyword
def cal(x):
    return 2*x+5
x=int(input("Enter a number"))
print(cal(x))

# same with lambda function
a=lambda x: 2*x+5
print(a(5))

user_in=int(input("Enter a value"))
b=lambda y: 2*y+5
print(b(user_in))
print((lambda y: 2*y+5)(user_in))

c,d=input().split()
e=lambda a,b: int(a) *int(b) 
print(e(c,d))

# WAP to print the require  letter to upper case and capitalize the letter 
first="codegnan"
second="python course"
upp=lambda a: a.upper()
low=lambda b: b.title()
print(upp(first),'\n' ,low(second))

# WAP to print first +lastname= fullname

firstname=input()
lastname=input()
print((lambda a,b: (b +" "+a).title())(firstname,lastname))

firstn,lastn=[x for x in input("Enter names").split(",")]
print((lambda a,b: (a+" " +b ).title())(firstn,lastn))

# Filters: It is used to extract the values when the condition is true , if condition false it will skip 
arr=[10,20,26,24,28,27,2,9,36,87,54,635]
print((lambda y: [y for y in arr if y%2 ==0 ])(arr))
b=list(filter(lambda y: y%2==0, arr))
c=list(filter(lambda y: y%2!=0, arr))
print(b,"\n",c)

#filter example
a=[[],{},(),set(),None,3,3.5,"Samba",4+6j,True,False]
print(a)
b=list(filter(None,a)) # --> this used to filter the list ,like remove the empty data types from the list and display the list with values
print(b)


