# WAP to split bill among N number of individuals, so display how much amount each individual will pay 
def bill_split(n, amount):
    split=amount/n
    return round(split)

n=int(input("Enter number of persons"))
amount=float(input("Enter amount"))
print(f"Each person will pay {bill_split(n, amount)}")

#Task 2: Simple list operation. 
'''
Inn this code the += operation considered as list.extend() so it will add the value to list
as we know list is mutable
o/p: [1,2,3,4,5]
'''
number=[1,2,3,4]
def update(num):
    num += [5]

update(number)
print(number)

