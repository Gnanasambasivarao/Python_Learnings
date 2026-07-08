# Multiple If statement: In this statements it donot check in chain manner, it will execute all the block of code 
# It might be one or 2 or more answers
# As we see IF ELIF ELSE are a chain of execution , executes only one block of code if it is true so in this if it will execute all the If statments.

Marks=91
if Marks>90:
    print("Grade A")
if Marks>80:
    print("Grade B")
if Marks>70:
    print("Grade C")

'''
o/p: 
    Grade A
    Grade B
    Grade C
Note:
In this code it will execute all the if statements , thinking like one if statement as one independent

'''
# Multiple if using logical operator
samba_marks=95
siva_marks=90
if samba_marks>90 and siva_marks>90:
    print("ALL students are in Grade A")
    
if samba_marks>80 and siva_marks>80:
    print("All Students are in Grade B")
    
if samba_marks>50 or samba_marks<60:
    print("Student to be improved")