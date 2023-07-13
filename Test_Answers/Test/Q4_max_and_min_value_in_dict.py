# 4. Write a Python program to get the maximum and minimum values of a dictionary.
mydict = {"n1": 23, "n2": 44, "n3": 52, "n4": 1, "n5": 49, "n6": 2, "n7": 42}
max = mydict['n1']
min = mydict['n1']
for i in mydict.values():
    if max < i:
        max = i
    if min > i:
        min = i
print(f"Max={max},Min={min}")
