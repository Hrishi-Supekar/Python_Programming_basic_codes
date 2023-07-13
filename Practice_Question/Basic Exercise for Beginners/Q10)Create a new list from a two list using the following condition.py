# 10: Create a new list from a two list using the following condition
l1 = [int(x) for x in input("Enter the list elements:").split()]
l2 = [int(x) for x in input("Enter the list elements:").split()]
result_list = []


def list_even_odd(l1, l2, result_list):
    for i in l1:
        if i % 2 != 0:
            result_list.append(i)
    for j in l2:
        if j % 2 == 0:
            result_list.append(j)
    print(result_list)


list_even_odd(l1, l2, result_list)
