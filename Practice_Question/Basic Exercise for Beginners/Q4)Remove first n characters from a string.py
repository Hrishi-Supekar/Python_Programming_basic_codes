# 4: Remove first n characters from a string
n = int(input("Enter the number of char to be removed from string:"))
msg = input("Enter the string:")


# def remove_char(msg1, n1):
#     l = list(msg1)
#     for i in range(n1):
#         i = 0
#         l.pop(i)
#     print("".join(l))
# =================OR==================
def remove_char(msg1, n):
    print(msg1[n:])


remove_char(msg, n)
