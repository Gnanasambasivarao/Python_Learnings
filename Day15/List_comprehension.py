# List comprehension:
'''
Syntax: 

variable name=[expresion for var_name in collection/range]==> For loop

variable_name=[True_value for var_name in collection/range if Condition] ==> used for IF statement in list comrehension.

variable_name=[true_value if condition else default for var_name in collection/range] ==> use this when we have to use else in list comprehension also 

variable_name=[True_value for var_name in collection/range for var_name2 in collection/range if Condition] ==> used for MULTIPLE FOR LOOPS WITH IF statement in list comrehension.

'''

a=["samba","siva","rao"]
output=[i.upper() for i in a]
print(output)

b=[1,2,3,4,5,6,7,8,9]
res=[i*i for i in b]
res1=[i**2 for i in b]
res2=[pow(i,2) for i in b]
print(res)

# If usage in list comprehension
# WAP to print even and odd numbers in a range(16) using list comprehension using if statement
c=[i for i in range(16) if i%2==0]
print(c)
d=[i for i in range(16) if i%2!=0]
print(d)
# WAP to print a range of number using list comprehension 
e=[i for i in range(21)]
print(e)

# WAP to print the words from the list if the word contain letter "a" in it-+
fruits=['apple','banana','grapes', 'kiwi','mango',"dragon","Berry"]
print([i for i in fruits if 'a' in i])
# Printing a word with out alphabet "a"
print([i for i in fruits if 'a' not in i])

# If else usage in list comprehension.
# WAP to print asquare of a number if it even , if it is odd it should multiply by 5 by using list comprehension.
print([i**2 if i%2==0 else i*5 for i in range(21)])

# WAP to print
G=[1,2,3,4,5]
h=[5,4,3,2,1]
# By using two for loops with if statement.
print([i+j for i in G for j in h if i+j==6])
# By using single for loop with index valuesusing list_variable name.
print([G[i]+h[i] for i in range(len(G))])

