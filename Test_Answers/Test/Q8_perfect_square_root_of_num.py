# 9.Write a Python program to find out perfect square root of given number without inbuilt function
n = int(input("Enter the number:"))
flag = 0
for i in range(1, n):
    if i * i == n:
        flag = 1
        break
if flag == 1:
    print(f"The perfect square root of {n} is {i}")
else:
    print(f"There is no perfect square root of {n}")
