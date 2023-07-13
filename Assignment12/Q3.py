# 3)write a function that takes a number as a parameter and checks whether the number is prime or not
n = int(input("Enter the number to check:"))


def prime_no_fun(n1):
    cnt = 0
    for i in range(2, n1):
        if n1 % i == 0:
            cnt = 1
    if cnt == 0:
        print("The number is prime!")
    else:
        print("The number is not prime!!")


prime_no_fun(n)
