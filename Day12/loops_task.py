# WAP to convert the values in list to upper case 
fruits=["Apple","Banana","Manogo"]
result=[]
for i in fruits:
    result.append(i.upper())
print(result)
# Option-2:
fruit=["Apple","Banana","Manogo"]
a=str(fruit)
print(a.upper())

# WAP to print the last element to required output
b=[10,20,30,40,50,"Samba"]
res=[]
for i in b:
    res.append(i)
    if type(i)==str:
        c=i
        for j in c:
            res.append(j)
print(res)
# [10, 20, 30, 40, 50, 'Samba', 'S', 'a', 'm', 'b', 'a']

# Option 2:
b.extend(["c","o","d","e"])
print(b)

lis=[2,3,5,6,7]
lis.insert(2,4) #insert(position, value).
print(lis)

lis1=[5,6,7,8,9,10]
print(tuple(lis1[:5]))
print(tuple(lis1[:-1]))

lis2=[7,9,2,0,1,4,9,3,20]
print(sorted(lis2))
print(lis2)
lis2.sort()
print(lis2)