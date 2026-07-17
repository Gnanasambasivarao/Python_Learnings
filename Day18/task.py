# Railway ticket by using def function
def discount(percentage,ticket_price):
    dis =ticket_price*(percentage/100)
    final_price= ticket_price-dis
    print(f"your ticket fare is {final_price:.2f}")
    
def male(ticket_price,age):
    if age>=60:
        discount(30, ticket_price)
    else:
        print(ticket_price)

def female(ticket_price, age):
    if age>=60:
        discount(50,ticket_price)
    else:
        discount(30,ticket_price)

ticketamount=1000
age=int(input("Enter your age"))
gender=input("Enter your genter(male or female): ")
if gender.lower() == "male":
    male(ticketamount,age)
elif gender.lower() == "female":
    female(ticketamount,age)
else:
    print("Enter gender in between male or female only.")