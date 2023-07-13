# print("Welcome to my exception program!!!")
# n1 = 23
# n2 = 34
# s = n1 + n2
# print("Sum:-", s)
# try:  # try block is used where we write all the block of code where error may occur
#     a = int(input("Enter the value of a:"))
#     b = int(input("Enter the value of b:"))
#     print(a / b)
# except:  # Except block is used where we catch the error and handle the error.
#     print("Some error occurred.")
#
# finally:
#     print("Finally")  # Will execute always
# print("Out of try except blocks")

# ===============================================================================================================================================
# print("Out of try block")
# try:
#     a=4
#     b='a'
#     print(int(b))
#     # print(name)
#
# except TypeError:
#     print("unsupported operation")
# except ValueError:
#     print("Value error")
# except ZeroDivisionError:
#     print("Division by zero not allowed")
# except:
#     print("Other exception")
# finally:
#     print("Finally")

# ===============================================================================================================================================
# try:
#     x=int(input("Enter the number upto 100:"))
#     if x > 100:
#         raise ValueError(x)
# except ValueError:
#     print(x,"is out of allowed range")
# else:
#     p=89
#     sum=p+x
#     print(sum)
# print("x")

x=int(input("enter:"))
if x > 100:
    print("hello")
else:
    p=89
    sum=p+x
    print(sum)
    print('hi')