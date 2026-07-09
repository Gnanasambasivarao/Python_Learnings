# WAP to print Voting Eligibility

age=int(input("Enter your age: "))
if age>0:
    if age>=18:
        print("Eligible for voting.")
    else:
        print("Not eligible.")
else:
    print("Check the Enter age and retry.")
    
# WAP to check even or odd:
num= int(input("Enter a number:"))
if num%2==0:
    print("Even")
else:
    print("ODD")
    
# WAP to print leap year:
year=int(input("Year: "))
if year%4==0:
    print("Leap year")
else:
    print("Not a leap year")