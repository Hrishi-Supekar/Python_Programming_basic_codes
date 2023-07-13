# 7. Write a Python program to remove an item from a tuple.
t = (23, 43, 6, 76, 78, 98, 25, 74, 58)
print(f"Old Tuple:{t}")
l = list(t)
l.pop(3)
t = tuple(l)
print(f"New Tuple:{t}")
