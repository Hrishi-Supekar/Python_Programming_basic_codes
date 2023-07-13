# Break-Breaks the current loop
# continue-skips the current iteration in loop
# pass - ignores the block of statement

# print the 1 to 10 on console except 5
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i, end=" ")

# *args,**kwargs,*args with normal parameter,Default parameter
# *args = argument (When calling function that time pass some arguments as a form of *args)

# def fun(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#
#
# fun(1, 2, 3, 4, 5)

# *args with normal parameters:
# def fun(n1, n2, *args):  # the first 2 element will go in normal variables n1,n2 and remaining will go in *args
#     print(n1, n2, end=" ")
#     for i in args:
#         print(i, end=" ")
#
#
# fun(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# l = [1, 2, 3, 4]
# l1 = [5, 6, 7, 8]
#
#
# def fun(*args):
#     # print(args)  # will print in the form of tuple
#     for i in args:
#         print(i, end=" ")
#
#
# fun(l)  # will pass list as single element
# fun(*l)  # to unpack the list and pass the list elements as single elements of list.
# fun(l, l1)
# fun(*l, *l1)

# **kwargs - keyword arguments like dictionary. When calling function that time pass keyword argument as a form of **kwargs.
# def fun(**kwargs):
#     # print(kwargs)
#     # print(type(kwargs))
#     for key, val in kwargs.items():
#         print(f"{key}:{val}")
#
#
# fun(name="Hrishi", age=27, marks=88)

# d = {'name': 'Hrishi', 'age': 27, 'marks': 88}
#
#
# def fun(**kwargs):
#     # print(kwargs)
#     for i, j in d.items():
#         print(f"{i}:{j}")
#
#
# fun(**d)  # to unpack dictionary

# d = {'name': 'Hrishi', 'age': 27, 'marks': 88}
#
#
# def fun(d): # normal way of passing arguments
#     for i, j in d.items():
#         print(f"{i}:{j}")
#
#
# fun(d)  # to unpack dictionary


# default argument:
# def fun(a, b, c=100):  # will consider c=100 if c is not given in actual parameters.
#     print(a + b + c)
#
#
# fun(2, 4, 6)


# NADK-- normal parameter,args,default parameter, kwargs

# def fun(a, b, *args, d=56, **kwargs):
#     print(a, b)
#     print(args)
#     print(d)
#     print(kwargs)
#
#
# fun(23, 45, "abc", "xyz", "pqr", x=43, y=67)
