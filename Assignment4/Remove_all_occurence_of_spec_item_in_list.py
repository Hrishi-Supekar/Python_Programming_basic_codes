# Remove all the occurrences of specific items in the list
# list1 = [23, 43, 45, 56, 67, 87, 32, 23, 23, 23, 45, 65, 56, 43]
# print(list1)
# n = int(input("Enter the element to remove:"))
# for x in list1:
#     if x == n:
#         list1.remove(x)
# print(list1)
# ==while loop==
# list1 = [23, 43, 45, 56, 67, 87, 32, 23, 23, 23, 45, 65, 56, 43]
# print(list1)
# i = 0
# n = int(input("Enter the element to remove:"))
# while i < len(list1):
#     if list1[i] == n:
#         list1.remove(list1[i])
#     i = i + 1
# print(list1)
# # ==UDF==
list1 = [23, 43, 45, 56, 67, 87, 32, 23, 23, 23, 45, 65, 56, 43]
list2 = []
cnt = 0
n = int(input("Enter the element to remove:"))
print(list1)
for x in list1:  # for length of list
    cnt += 1
# print(cnt)
for x in range(0, cnt):  # for removing element from list
    if list1[x] == n:
        continue
    else:
        list2 = list2 + [list1[x]]
print(list2)
