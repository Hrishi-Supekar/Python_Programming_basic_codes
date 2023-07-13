# 10.print dictionary using user defined values.
d = {}
n = int(input("Enter the number of items in dict:"))
for i in range(n):
    k = input("Enter the key:")
    v = input("Enter the values:")
    d.update({k: v})
print(d)
