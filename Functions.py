# msg = "my name is hrishikesh supekar"
#
# print(msg.capitalize())  # it converts string first letter into capital
# print(msg.upper())  # it converts string into upper case
# print(msg.lower())  # it converts string into lower case
# print(msg.count("h"))  # to check the occurrence of a particular char
# print(msg.find("is"))  # gives the location of first char it found in the string mentioned in the find().
# print(msg.endswith("kar"))  # checks if the string ends with the given string


# Function-Self contained block of program is called as functions
# Category of functions:
# 1.Without argument and without return type
# 2.With argument and without return type
# 3.Without argument and with return type
# 4.With argument and with return type

# Function sections:
# definition -- body of function
# calling

# Function Syntax
# def function_name():
#     block of statement....

# function_name()

# make function to add two number:
# def Add():
#     print("Addition", 1 + 2)
#
#
# def fun():
#     print("Hello World!")
#
#
# def fun2():
#     print("In fun2")
#
#
# def fun3():
#     print("In fun3")
#
#
# fun()  # function seq is depended on function calling seq
# fun2()
# fun3()
# Add()  # Function calling should be after the function definition


# to find out factorial of given number:
# Type 1: w/o return & w/o parameters
# def fact():
#     n = int(input("Enter the number:"))
#     f=1
#     for x in range(1,n+1):
#         f=f*x
#     print(f)


# Type 2:w/o return & w parameters
# n = int(input("Enter the number:"))
#
#
# def fact(n):  # Formal Parameter
#     f = 1
#     for x in range(1, n + 1):
#         f = f * x
#     print(f)
#
# Type 3:w return & w parameters
#
# n = int(input("Enter the number:"))
#
#
# def fact(n):  # Formal Parameter
#
#     f = 1
#     for x in range(1, n + 1):
#         f = f * x
#     return f  # we can return more than one value
#
#
# ans = fact(n)  # actual Parameters
# print(ans)


# Type 4:w return & w/o parameters


# def fact():  # Formal Parameter
#
#     n = int(input("Enter the number:"))
#     f = 1
#     for x in range(1, n + 1):
#         f = f * x
#     return f  # we can return more than one value
#
#
# ans = fact()  # actual Parameters
# print(ans)
# =============================================================================================
# To print reverse of each element of list and print using 4 types

# Type1: w return & w para:
# l = [23, 21, 34, 45, 76, 78, 98]
#
#
# def rev_each_elem(l):
#     l1 = []
#     for i in l:
#         l1.append(int(str(i)[::-1]))
#     return l1
#
#
# ans = rev_each_elem(l)
# print(ans)

# Type2: w/o return & w para:
# l = [23, 21, 34, 45, 76, 78, 98]
#
#
# def rev_each_elem(l):
#     l1 = []
#     for i in l:
#         l1.append(int(str(i)[::-1]))
#     print(l1)
#
#
# rev_each_elem(l)

# Type3: w return & w/o para:


# def rev_each_elem():
#     l = [23, 21, 34, 45, 76, 78, 98]
#     l1 = []
#     for i in l:
#         l1.append(int(str(i)[::-1]))
#     return l1
#
#
# ans = rev_each_elem()
# print(ans)


# Type4: w/o return & w/o para:


# def rev_each_elem():
#     l = [23, 21, 34, 45, 76, 78, 98]
#     l1 = []
#     for i in l:
#         l1.append(int(str(i)[::-1]))
#     print(l1)
#
#
# rev_each_elem()


# ===============================================================================
# To print reverse of each element of list and print the rev_dictionary using 4 types

# Type1: w return & w para:
# l = [23, 21, 34, 45, 76, 78, 98]
# def rev_each_elem(l):
#     rev_dict = {}
#     for i in l:
#         rev_dict.update({i:int(str(i)[::-1])})
#     return rev_dict
#
#
# ans = rev_each_elem(l)
# print(ans)

# Type2: w/o return & w para:
# l = [23, 21, 34, 45, 76, 78, 98]
# def rev_each_elem(l):
#     rev_dict = {}
#     for i in l:
#         rev_dict.update({i: int(str(i)[::-1])})
#     print(rev_dict)
#
#
# rev_each_elem(l)

# Type3: w return & w/o para:
# def rev_each_elem():
#     l = [23, 21, 34, 45, 76, 78, 98]
#     rev_dict = {}
#     for i in l:
#         rev_dict.update({i:int(str(i)[::-1])})
#     return rev_dict
#
#
# ans = rev_each_elem()
# print(ans)

# Type4: w/o return & w/o para:
# def rev_each_elem():
#     l = [23, 21, 34, 45, 76, 78, 98]
#     rev_dict = {}
#     for i in l:
#         rev_dict.update({i: int(str(i)[::-1])})
#     print(rev_dict)
#
#
# rev_each_elem()

