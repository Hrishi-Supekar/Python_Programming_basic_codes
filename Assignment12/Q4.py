# 4) Write a Function to create a list where the values are the squares of numbers between 1 and 30(both included)
n = int(input("Enter the number:"))


def sq_list(n1):
    l = []
    for i in range(1, n1 + 1):
        l.append(i ** 2)
    print(l)


sq_list(n)
