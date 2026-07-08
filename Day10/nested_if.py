# Nested If else: In this statement we use two if statements one is inner If and Second one is Outer If

score_gained=80
required_score=45
if score_gained>0:
    print("Gained score is positive")
    if score_gained>required_score:
        print("Pass")
    else:
        print("Try in another attempt")
else:
    print("Check your score once again")
    
age=int(input("Enter age: "))
if age>0:
    if age>18:
        print("Eligible to vote")
    else:
        print(f"Minor try after {18-age} years")
else:
    print("Check your entered age")
    
a=int(input("First value"))
b=int(input("second value"))

if a>b:
    print("greater")
    if a==b:
        print("Both are equal")
    else:
        print("Different")
else:
    print(f"{b} is greatest")