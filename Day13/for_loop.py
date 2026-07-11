# Range: The range function return a sequence of numbers, starts from zero by default and increments by 1 by default and stops at a specified end number

'''
Syntax:
for i in range(start, end, step):
    Block of code 
    
end= end+1
like if user enter 50 then it prints upto 49if he want 50 in output then he has to enter end+1 value
'''
# For loop with stop value.
for i in range(10):
    print(i)

# For loop with start and stop values.
for i in range(5,50):
    print(i, end=" ")

# for loop using step in the range function
for i in range(2,20,2):
    print(i,end=" ")

for i in range(5,50,5):
    print(i,end=" ")

for i in range(0,31,3):
    print(i,end=" ")
    
# Task using if statement with range function: Grade system.
marks=int(input("Enter marks"))
if marks in range(91,101):
    print("Grade A")
elif marks in range(81,91):
    print("GRade B")
elif marks in range(71,81):
    print("Grade C")
elif marks in range(50,71):
    print("Grade D")
else:
    print("Try again")