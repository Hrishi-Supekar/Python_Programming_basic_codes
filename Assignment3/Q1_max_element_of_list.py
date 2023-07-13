# Max of elements in list:

l = [12, 43, 76, 44, 86, 42, 37, 14, 3, 75, 1, 600]

max = l[0]

for x in range(1, len(l)):
    if max < l[x]:
        max = l[x]
print(f"The Max element of list is {max}")
