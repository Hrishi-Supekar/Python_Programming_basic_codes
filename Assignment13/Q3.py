# Calculate the average of all list elements
from functools import reduce

l = [1, 2, 3, 4, 5]


def red(f, s):
    return f + s


print((reduce(red, l))//len(l))

