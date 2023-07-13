# 11: Write a Program to extract each digit from an integer in the reverse order.
n = int(input("Enter the number:"))


def reverse_print(n1):
    str1 = str(n1)
    cnt = 0
    for i in str1:
        cnt += 1
    for j in range(1, cnt + 1):
        print(str1[-j], end=" ")


reverse_print(n)
