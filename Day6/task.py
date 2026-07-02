a=[9,1,5,2,8,4,6,3,7,0]
#[7,6,4,3,0,9,8,5,2,1]

b=a[:5]
print(b)
c=a[5:]
print(c)
b.sort()
b.reverse()
c.sort()
c.reverse()
print(c+b)