# Set - is a collection data type which is unordered and unindexed.No Duplicate members allowed in set.
# Set function:
# 1)Add element-
#     add() - Adds an elements to set.
# fruits = {'Apple', 'Banana', 'Cherry'}
# fruits.add('Kiwi')  # There is no order has it will be added every time ata random index.
# print(fruits)

# 2)Clear-Remove all elements from set.
# fruits.clear()

# 3) Copy - makes a copy of OG set
# x = fruits.copy()
# print(x)

# 4)Difference()- Returns a set containing the difference betw two or more sets
# x={"apple","banana","Cherry"}
# z= fruits.difference(x) # print different value from fruits
# print(z)

# 5) Union - Returns a set containing the union of set
# x = {'Apple', 'Banana', 'cherry'}
# y = {'Apple', 'Banana', 'Cherry'}
# z = x.union(y)  # contain union(same) element from both the set and print them once
# print(z)

# 6) Update- uapdate the set with union of this set an others.
# x = {'Apple', 'Banana', 'cherry'}
# y = {'Apple', 'Banana', 'Cherry'}
# x.update(y)
# print(x)

# 7) Remove - removes a specified element
# x = {'Apple', 'Banana', 'cherry'}
# x.remove('Banana')
# print(x)

# 8) Intersect -
x = {'Apple', 'Banana', 'cherry'}
# y = {'Apple', 'Banana', 'Cherry'}
# z= x.intersection(y) #prints common elements from both sets
# print(z)

# for i in x:
#     print(i)

# a, b, c = 32, 43, 65
# print(a,b,c)
t = (1, 2, 3, 4)
n1, n2, n3, n4 = t  # Unpacking the tuple
print(n1, n2, n3, n4)
