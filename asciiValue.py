# ASCII value - A-Z == 65-90
#               a-z == 97-122
#               0-9 == 48-57


print(ord("a"))  # convert char to ascii value
print(chr(97))  # convert ascii value to char

for i in range(65, 91):
    print(chr(i), end=" ")
print()
for i in range(97, 123):
    print(chr(i), end=" ")
print()
for i in range(48, 58):
    print(chr(i), end=" ")


