# Attendance tracking analysis:
n=int(input("Enter n number of students"))
a=[]
for i in range(1,n+1):
    attendance=input(f" Student {i} Presenr(p) or Absent(ab): ")
    a.append(attendance)
def analysis(n, a):
    P_count=0
    a_count=0
    print(f"Total students are {n}")
    for i in a:
        if i == 'p':
            P_count=P_count+1
        elif i=='ab':
            a_count+=1
    print(f"Total presents are {P_count}")    
    print(f"Total absents are {a_count}")    

analysis(n,a)

# WAP to print Square pattern 
def square_p():
    n=int(input("Row"))
    m=int(input("column"))
    for _ in range(n):
        for _ in range(m):
            print("*", end="")
        print()
square_p()
         
# WAP to print right angle triangle 
a= int(input("Enter a number "))
for i in range(1,a+1):
    print("*"*i)

for i in range(1,a+1):
    print((pow(10,i)//9)*i)
    
# WAP to print Right angle triangle using 2 for loops. OUTline
a= int(input("rows: ")) 
b= int(input("cols: "))
for i in range(a):
    for j in range(b):
        if i==j or i==b-1 or j==0:
            print("*", end="")
        else:
            print(" ",end="")
    print()


# WAP to print Right angle triangle using 2 for loops.
a= int(input("rows: ")) 
b= int(input("cols: "))
for i in range(a):
    for j in range(b):
        if j<=i:
            print("*", end="")
        else:
            print("",end="")
    print()

# WAP to print inverted right angle triangle:
a= int(input("rows: ")) 
b= int(input("cols: "))
for i in range(a):
    for j in range(b):
        if j>=i:
            print("*", end="")
        else:
            print("",end="")
    print()
