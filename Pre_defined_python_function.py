# Lamda function -- It is the simplest way to write the function.

# normal function--
# def add(a,b):
#     print(a+b)
# add(2,3)

# lambda function--
# result = lambda a, b: a + b
# print(result(2, 3))

# even number fun:
# def iseven(a):
#     return a % 2 == 0
#
#
# print(iseven(5))

# even number fun using lambda:
# result = lambda a: a % 2 == 0
# print(result(5))

# get last char:
# last_char = lambda a:a[-1]
# print(last_char("Martin"))


# If - else in lambda function:
# func = lambda s: True if len(s) > 5 else False
# print(func("Hello"))


# func = lambda n: "prime" for i in range(n) if n%2==0


# Zip function -- Combine two list and return zip object as a form of tuple
# A = ["C", "Java", "Python", "PHP", "Web"]
# B = ["1 month", "3 month", "3 month", "2 month", "3 month"]
# t = zip(A, B)
# print(t)  # will provide address of the variable
# print(tuple(t))  # will provide tuple(1 ele from list1 and 1 ele from list2) within tuple
# print(list(t))  # will provide tuple with list
# print(dict(t))  # will provide dictionary with key as 1 ele of list1 and value as 1 ele of list2
# print(tuple(t))  # If list1 contain more element than list2 than only matching element will be printed and the extra element will be skipped.

# Enumerate function()-- Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.
# for index, val in enumerate((zip(A, B)), start=1):  # Basically used for giving index to the value
#     print(f"{index}:{val}")


# l1 = [12, 324, 35, 64, 67]
# l2 = [34, 54, 65, 32, 53]
# nl = []
# for pair in zip(l1, l2):
#     nl.append(max(pair))
# print(nl)
# user_id = ['user1', 'user2', 'user3']
# first_name = ['Hrishi', 'rahul', 'Alisha']
# last_name = ['Supekar', 'mani', 'raundale']
# print(dict(zip(user_id, (zip(first_name, last_name)))))
# result = tuple(zip(first_name,last_name))
# print(result)

# What are iterator and iterable:
# list,tuple,dict -- Iterable objects
# map,filter,reduce -- Iterators


"""Iterable -- Iterable is an object, that one can iterate over.
It generates an Iterator when passed to iter() method.
An iterator is an object, which is used to iterate over an iterable object using the __next__() method.
Iterators have the __next__() method, which returns the next item of the object."""
# Types -
# 1.List
# 2.Tuple
# 3.Dictionary
"""Iterator--An iterator is an object, which is used to iterate over an iterable object using the __next__() method.
Iterators have the __next__() method, which returns the next item of the object.
"""

# Types --
# 1.Map
# 2.Filter
# 3.Reduce

# ===========================================================
# 1.Map function: it returns object(hashcode) it is req to convert map o/p into iterable object.
# syntax-> list/tuple/dict(map(function,iterable))

# l = [1, 2, 3, 4, 5]
# sq_list = []
#
#
# def sq(l):
#     for i in l:
#         sq_list.append(i * i)
#     return sq_list
#
#
# ans = sq(l)
# print(ans)


# l = [1, 2, 3, 4, 5]
#
#
# def sq(a):
#     return a * a
#
#
# print(list(map(sq, l)))

# reverse of list element using lambda fun and map fun:
# l = ["abc", "cde", "xyz"]
# print(list(map(lambda a: a[::-1], l)))
#
# def rev(s):
#     return s[::-1]
# print(list(map(rev,l)))


# above 50 marks in another list
# marks = [56, 67, 89, 90, 23, 45, 50, 66]
# new_list = []
#
#
# def above50(marks):
#     return marks >= 50
#
#
# print(list(map(above50, marks)))  # map will not work we have to use filter function
# print(list(filter(above50, marks)))  # map will not work we have to use filter function

# 2.Filter function:


# print(list(map(filter(lambda a:len(a),names))))
#
# def fun(n):
#     vowel = 0
#     const = 0
#     l = []
#     for ch in n:
#
#         if ch == 'a' or ch == 'A' or ch == 'e' or ch == 'E' or ch == 'i' or ch == 'I' or ch == 'o' or ch == 'O' or ch == 'u' or ch == 'U':
#             vowel += 1
#         else:
#             const += 1
#     l.append(vowel)
#     l.append(const)
#     return (l)
#
#
# names = ["Anmol", "Hrishi", "Amit", "Raj", "Sham", "Abhishek"]
#
# print(list(map(fun, names)))


# 3.Reduce function: does cumulative/sequentially operation on iterable
# we have to import reduce from functools

# num = [3, 4, 5, 6, 7, 8]
#
#
# def cust_sum(fir, sec):
#     return fir + sec
#
#
# from functools import reduce
#
# result = reduce(cust_sum, num)
# print(result)


