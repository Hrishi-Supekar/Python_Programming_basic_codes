# Nested Loop
# patter print half pyramid
# *
# **
# ***
# ****
# *****

# n=int(input("Enter the number:"))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# -------------------------------------------------------------------------
# patter print reverse half pyramid
# *****
# ****
# ***
# **
# *

# n = int(input("Enter the number:"))
# for i in range(n):
#     for j in range(n, i, -1):  # we can use -1 for negative stepping
#         print("*", end=" ")
#     print()
# -------------------------------------------------------------------------
# Pattern print 1010 pyramid

# n=int(input("Enter the number:"))
# for i in range(n):
#     for j in range(i+1):
#         pass

# -------------------------------------------------------------------------
# pattern print of numbers
1
12
123
1234
12345

# n = int(input("Enter the number:"))
# for i in range(n):
#     for j in range(i + 1):
#         print(j + 1, end=" ")
#     print()

# -------------------------------------------------------------------------
# print pattern numbers
# 12345
# 1234
# 123
# 12
# 1

# n = int(input("Enter the number:"))
# for i in range(n,0,-1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()
# #-----------------------------------------------------------
# 54321   55555   11111
# 5432    4444    2222
# 543     333     333
# 54      22      44
# 5       1       5

# n = int(input("Enter the number:"))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()
# ===OR===
# n = int(input("Enter the number:"))
# for i in range(0,n):
#     for j in range(n,i,-1):
#         print(j, end=" ")
#     print()

# ==============================================
# n = int(input("Enter the number:"))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(i, end=" ")
#     print()
# ===OR===
# n = int(input("Enter the number:"))
# for i in range(n,0,-1):
#     for j in range(0,i):
#         print(i, end=" ")
#     print()
# ================================
# n = int(input("Enter the number:"))
# x = 1
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(x, end=" ")
#     x += 1
#     print()
# ==OR==
# n = int(input("Enter the number:"))
# for i in range(1, n + 1):
#     for j in range(n + 1, i, -1):
#         print(i, end=" ")
#     print()
