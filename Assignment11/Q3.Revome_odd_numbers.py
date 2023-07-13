# 3.Remove all odd numbers from the list using list comprehension.
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e_list = [x for x in l if x % 2 == 0]
print(e_list)
