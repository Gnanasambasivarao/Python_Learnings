# print A TO Z and a to z by using ascii code using inbuilt function like ord(), chr()

print([chr(i) for i in range(ord('A'), ord('Z')+1)])
l=[chr(i) for i in range(65,91)]
print(l)


print([chr(i) for i in range(ord('a'), ord('z')+1)])
l1=[chr(i) for i in range(97,123)]
print(l1)

# Printing the the ascii code of the name given by the user
count=0
name=input()
for i in name : #"thotagnanasambasivarao"
    print(i, "Ascii code is ", ord(i))
    count+=ord(i)
    print(count)
    