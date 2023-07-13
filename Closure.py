# Closure: One function return the another function.
# def outer_fun(msg):
#     print("I am in outer fun block")
#
#     def inner_fun():
#         print(f"I am in inner fun block {msg}")  # we can pass formal parameter of outer fun to inner func
#
#     return inner_fun

# =============================================================================================
# var = outer_fun("Hi student")  # actual argument passed to outer func
# var()

# def outer_fun(b):
#     print("I am in outer fun")
#
#     def inner_fun(a):
#         print("value of a:", a)
#         print("value of b:", b)
#
#     return inner_fun
#
#
# result = outer_fun(10)
# result(20)
# =============================================================================================
# def to_power(x):
#     def calc_power(n):
#         return n ** x
#
#     return calc_power
#
#
# cube = to_power(3)
# print(cube(2))
# =============================================================================================
