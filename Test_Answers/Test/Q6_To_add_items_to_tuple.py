# 6.Write a Python program to add an item to a tuple.
t = (23, 43, 6, 76, 78, 98, 25, 74, 58)
print(f"Old Tuple:{t}")
l = list(t)
l.append(55)
t = tuple(l)
print(f"New Tuple:{t}")
