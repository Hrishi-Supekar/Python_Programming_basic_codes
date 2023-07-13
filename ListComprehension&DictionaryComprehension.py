# List Comprehension:To create a list in one line code.
# listname = [expression loop]
#
# l = [int(x) for x in range(1, 11)]
# print(l)
#
# sq_list = [int(x*x) for x in range(2,11)]
# print(sq_list)
#
# cube_list = [int(x**3) for x in range(2,11)]
# print(cube_list)
#
# n=int(input("Enter the total list element:"))
# l=[int(x) for x in range(n)]
# print(l)
#
# l = ["john", "martin", "xcaliber", "smith"]
# l1 = [x[0] for x in l]  # To get initial letter of alphabet
# print(l1)
#
# num = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# e_list = []
# o_list = []
# [e_list.append(x) if x % 2 == 0 else o_list.append(x) for x in num]
# # o_list = [x for x in num if x % 2 != 0]
# print(e_list)
# print(o_list)
#
num = [2, 3, 4, 5, 6, 7, 8, 9, 10]
sq_list = []
cube_list = []
[sq_list.append(x ** 2) if x % 2 == 0 else cube_list.append(x ** 3) for x in num]  # using if-else
print(sq_list)
print(cube_list)
#
#
# names = ["john", "martin", "xcaliber", "smith"]
# rev_list=[x[::-1] for x in names]
# print(f"OG list- {names}")
# print(f"Rev list - {rev_list}")
#
#
# names = ["john", "martin", "xcaliber", "smith", "ava", "mom", "otto"]
# rev_list = []
# palindrome_list = []
# [palindrome_list.append(x) if x == x[::-1] else rev_list.append(x[::-1]) for x in names]
# print(f"Palindrome list == {palindrome_list}")
# print(f"reverse list == {rev_list}")
#
# Dictionary Comprehension:It is the short way to create dictionary
# d={x:x**2 for x in range(5)}
# print(d)

# msg = "Hello this is hrishikesh supekar from pune i am studying python programming"
# my_dict = {x: msg.count(x) for x in msg}
# print(my_dict)

# num = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_odd_dict = {x: "even" if x % 2 == 0 else "odd" for x in num}
# print(even_odd_dict)

# Nested list:
# nested_list = [[i for i in range(11)] for j in range(4)]  # to print value of i times j
# print(nested_list)
