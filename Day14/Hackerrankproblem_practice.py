# Printing the list of integers in string format in printing function
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")
        
    
# Triangle Quest without using string methods
for i in range(1,int(input())):
    print(((10**i)//9 )*i)

# Option 2
# for i in range(1,int(input())):
#     print(str(i)*i)

#Integers Come In All Sizes
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print((a**b)+(c**d))
# print(pow(a,b)+pow(c,d))

# Using powermod function
e=int(input())
f=int(input())
m=int(input())
print(pow(e,f))
print(pow(e,f,m))

# Using divmod function
g=int(input())
h=int(input())
print(g//h) # print the round value like res is 11.45637923 so it will return as 11
print(g%h)
print(divmod(g,h))

# Finding Leap year or not a leap year by using functions
def is_leap(year):
    leap = False
    if (year%4==0 and year%100 != 0)or year %400==0:
        leap=True
    return leap
year = int(input())
print(is_leap(year))

# WAP to print squares of a number using loop.
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)
        
# WAP to print linear algebric operation
if __name__ == '__main__':
    first = int(input())
    second = int(input())
    print(first//second)
    print(first/second)
    