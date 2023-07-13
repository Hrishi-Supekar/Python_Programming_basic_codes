from functools import reduce

l1 = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, l1))
