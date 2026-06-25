# Type conversion: It means converting from one data type to another date type
# In Python default input comes under string datatype

# Converting to Integer from remaining types
print(int(1.0))
# print(int("Samba")) ValueError: invalid literal for int() with base 10: 'Samba'
# print(int(7+6j)) ValueError: invalid literal for int() with base 10: '7+6j'
print(int(True))
print(int(False))

# Converting to float from different data type
print(float(1.0))
# print(float("Samba")) ValueError: invalid literal for float() with base 10: 'Samba'
# print(float(7+6j)) ValueError: invalid literal for int() with base 10: '7+6J'
print(float(True))
print(float(False))

# string
print(str(1.0))
print(str("Samba"))
print(str(7+6j))
print(str(True))
print(str(False))

# boolean
print(bool(5))
print(bool(5.1))
print(bool("samba"))
print(bool(5+7j))
print(bool(True))
print(bool(False))