Account_Balance=20000
card_Type="c"
password="1234"

print("Insert Card: ")
user_card_Input=input("Enter card_type: ")
if user_card_Input == card_Type:
    print("Welcome Samba")
    Password=input("Enter Password: ")
    if password == Password:
        print("Options: \n 1. Balance Enquiry \n 2. Withdraw")
        option=int(input("Enter option number: "))
        if option == 1:
            print(f"Your Balance in account is {Account_Balance}")
        elif option == 2:
            Amount_wtd=int(input("Enter amount to be withdraw: "))
            Account_Balance -= Amount_wtd
            print(f"Remaining Balance left in account is {Account_Balance}")
        else:
            print("Choose The valid number")
    else:
        print("invalid Password! Try again")
else:
    print("Invalid Card Type! Try again")   

# while True:
#     print("Insert Card: ")
#     user_card_Input=input("Enter card_type: ")
#     if user_card_Input == card_Type:
#         print("Welcome Samba")
#         Password=input("Enter Password: ")
#         if password == Password:
#             print("Options: \n 1. Balance Enquiry \n 2. Withdraw")
#             option=int(input("Enter option number: "))
#             if option == 1:
#                 print(f"Your Balance in account is {Account_Balance}")
#             elif option == 2:
#                 Amount_wtd=int(input("Enter amount to be withdraw: "))
#                 Account_Balance -= Amount_wtd
#                 print(f"Remaining Balance left in account is {Account_Balance}")
#             else:
#                 print("Choose The valid number")
#         else:
#             print("invalid Password! Try again")
#     else:
#         print("Invalid Card Type! Try again")   