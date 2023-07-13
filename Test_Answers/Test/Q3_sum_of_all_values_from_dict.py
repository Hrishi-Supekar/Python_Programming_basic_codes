# 3.Write a Python program to sum all the values in a dictionary.
d = {"n1": 1, "n2": 2, "n3": 3, "n4": 4}
sum = 0
for i in d.values():
    sum += i
print(f"The addition of dictionary values is:{sum}")
