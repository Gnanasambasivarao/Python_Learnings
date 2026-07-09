# WAP to guest code :
name=input("Entername :").lower()
if name=="samba":
    print(f"Welcome {name}")
else:
    print(f"Welcome Guest {name}")
    
    
# WAP for guest code for 5 users:
list1=["samba", "siva","rao", "thota", "gnana"]
name=input().lower()
if name in list1:
    print(f"Welcome {name}")
else:
    print("Welcome guest")
    
# WAP to print vowels
character=input("Enter ")
if character in "AEIOUSaeious":
    print("It is vowel")
else:
    print("Consonent")
    
# WAP to print social media login by using nested if:
username=input("Enter username: ")
password=input("Enter your password: ")
if len(username)!=0 or len(password)!=0:
    if username=="Samba":
        if password=="Samba@123":
            print("Login sucessfull")
        else:
            print("Password is wrong")
    else:
        print("USername not found")
else:
    print("Enter any value.")
    
# WAP to print eligible criteria for student by using multiple If 
student={"age": 22,"marks":85,"Attendence":82}
if student["age"]>=18:
    print("Eligible to vote")
if student["marks"]>=60:
    print("Eligible for scholarship")
if student["Attendence"]>=75:
    print("Eligible for writing exam")
    
age=int(input())
marks=int(input())
attendance=int(input())
if age>=18:
    print("Eligible to vote")
if marks>=70:
    print("Eligible for scholarship")
if attendance>75:
    print("Eligible to write exam.")
    
# WAP IF_elif_else Cake price based caked name
amount=int(input("Enter amount")) 
if amount==1200:
    print("Redvelvet Cake is available")
elif amount==1000:
    print("Almond cake is available")
elif amount==800:
    print("Chocolate cake")
elif amount==600:
    print("Butterscoth cake")
else:
    print("Cake Not available") 

# WAP to print the name of the pizza based on price given by the user
price=int(input("Enter amount")) 
if price==1000:
    print("BBQ pizza is available")
elif amount==800:
    print("Crispy chicken pizza is available")
elif amount==600:
    print("Panner pizza")
elif amount==400:
    print("Corn pizza")
elif amount==200:
    print("French fries and coke")
else:
    print("pizza Not available") 