# A
# AB
# ABC
# ABCD
# ABCDE

# n=int(input("Enter the number:"))
# for i in range(n):
#     x=65
#     for j in range(i+1):
#         print(chr(x),end=" ")
#         x += 1
#     print()
# ===================================================
# ABCD
# ABC
# AB
# A

# n = int(input("Enter the number:"))
# for i in range(n):
#     x = 65
#     for j in range(n, i, -1):
#         print(chr(x), end=" ")
#         x += 1
#     print()

# ===========================HW=====================================
# 1
# 23
# 456
# 78910

# n = int(input("Enter the number:"))
# x = 1
# for i in range(n):
#     for j in range(i + 1):
#         print(x, end=" ")
#         x += 1
#     print()
# =========================================
#     1
#    121
#   12321
#  1234321
# 123454321

# n = int(input("Enter the number:"))
# for i in range(1, n + 1):
#     for x in range(n - i):
#         print(" ", end=" ")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#         if i == j:
#             for k in range(j - 1, 0, -1):
#                 print(k, end=" ")
#     print()
# ==========================================
# A
# BB
# CCC
# DDDD
# EEEEE

# n=int(input("Enter the number:"))
# x=65
# for i in range(n):
#     for j in range(i+1):
#         print(chr(x),end=" ")
#     x+=1
#     print()
# ============================================
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# n = int(input("Enter the number:"))
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1, 0, -1):
#         if k % 2 == 0:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()
# =======Online=======
# n=int(input("Enter the number:"))
# for i in range(n):
#     for j in range((n-i)-1):
#         print(end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# =====================
#        1
#       1 2
#      1 2 3
#     1 2 3 4
#    1 2 3 4 5
#   1 2 3 4 5 6
#  1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# n = int(input("Enter the number:"))
# for i in range(1, n + 1):
#     for k in range(n, i, -1):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# =======================
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    for j in range(i + 1):
        print(" ", end="")
    for k in range(1, (n + 2) - i):
        print(k, end=" ")
    print()
# ====ma'am=====
# n=int(input("Enter the number:"))
# for i in range(n,0,-1):
#     for j in range(i,n+1):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(j,end=" ")
#     print()
