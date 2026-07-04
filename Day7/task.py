# Write a program to convert the given list of elements to uppercase.

# Option 1:
# a=["codegnana","python","course"]
# a[0]=a[0].upper()
# a[1]=a[1].upper()
# a[2]=a[2].upper()
# print(a)
a = ["codegnana", "python", "course"]
a = " ".join(a).upper().split()
print(a)