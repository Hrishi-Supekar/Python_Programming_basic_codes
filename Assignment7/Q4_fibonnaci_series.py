# Print fibonacci series up to given range
n = int(input("enter the number:"))
a, b = 0, 1
print(a, b, end=" ")
for i in range(n):
    temp = a + b
    a = b
    b = temp
    print(temp, end=" ")
