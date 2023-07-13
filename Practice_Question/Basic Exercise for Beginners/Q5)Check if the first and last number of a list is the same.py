# 5: Check if the first and last number of a list is the same
l1 = [int(x) for x in input("Enter the number:").split()]


def check_first_and_last(list1):
    if l1[0] == l1[-1]:
        print("True")
    else:
        print("False")


check_first_and_last(l1)
