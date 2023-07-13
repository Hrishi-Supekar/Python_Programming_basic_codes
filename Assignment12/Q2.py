# 2)write a function that takes a list and returns a new list with distinct elements from the first list.

list1 = [1, 2, 3, 4, 5, 1, 2, 3, 6, 7, 8, 3, 4, 5, 10, 11]


def list_with_distinct_element(list2):
    my_dict = {}
    copy_list = []
    for i in list2:
        my_dict.update({i: i})
    for j in my_dict.values():
        copy_list.append(j)
    print(list2)
    print(copy_list)


list_with_distinct_element(list1)
