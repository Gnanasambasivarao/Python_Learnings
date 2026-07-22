print( dir() )
print( __builtins__ )

# .fromkeys()
name1=['john', 'smith', 'eval','spiderman']
e=dict.fromkeys(name1)
print(e)
g=dict.fromkeys(name1,'pass')
print(g)
g['smith']='Excellent'
print(g)

# eval()
a=eval(input("Enter a value"))
b=eval(input("Enter b value"))
print(a+b)

# zip()
names=['thota','gnana','samba','siva','rao']
index=[1,2,3,4,5]
print(zip(index,names)) # <zip object at 0x00000242E2C6FDC0>
# it will return a object memory number rather than dat so donot forget to use datatype before zip so it pair the data according 
print(list(zip(index,names)))
print(tuple(zip(index,names)))
print(set(zip(index,names)))
print(dict(zip(index,names)))

# Enumurate(): it will give count for the values 
name=['thota','gnana','samba','siva','rao']
for i in range(len(name)):
    print(i, name[i])
    
b=dict(enumerate(name))
print(b)
print(b[1])
c=list(enumerate(name))
print(c)
d=set(enumerate(name))
print(d)

# ASSCII code
print(chr(65)) # In this we haves to use numbers.
print(ord('a')) # In this we have to use characterlike 'a', 'b', 'c', 'd'

# MAX, min , sum
first=list(map(eval, input().split()))
print(min(first))
print(max(first))
print(sum(first))