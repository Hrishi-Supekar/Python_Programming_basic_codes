# 1.Append new string in the middle of a given string
# for Ex. s1 = "Ault"
#         s2 = "Kelly"
# Req.output - AuKellylt

# s1 = "Ault"
# s2 = "Kelly"
# mylist = list(s1)
# mylist.insert(len(mylist)//2,s2)
# s3 = "".join(mylist)
# print(s3)

# =============================================================================================================================
# 2.Arrange string characters such that lowercase letters should come first.
# Given:
# str1 = PyNaTive
# Expected Output:
# yaivePNT

# str1 = "PyNaTive"
# mylist1 = []
# mylist = list(str1)
# for i in mylist:
#     if i.islower():
#         mylist1.append(i)
# for i in mylist:
#     if i.isupper():
#         mylist1.append(i)
# str2 = "".join(mylist1)
# print(str2)

# =============================================================================================================================
# 3.Convert two lists into a dictionary.
# Ex. keys = ['Ten', 'Twenty', 'Thirty']
#     values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# my_dict = {}
# for i in range(3):
#     my_dict.update({keys[i]: values[i]})
# print(my_dict)

# =============================================================================================================================
# 4.Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# Expected output:
# 80

# sampleDict = {"class": {"student": {"name": "Mike", "marks": {"Physics": 70, "history": 80}}}}
# print(sampleDict["class"]["student"]["marks"]["history"])

# =============================================================================================================================
# 5.Remove items from the set at once
# Remove items - 10,20,30
# Given:
# set1 = {10, 20, 30, 40, 50}
# Expected output:
# {40, 50}

# set1 = {10, 20, 30, 40, 50}
# my_list = list(set1)
# n = [10, 20, 30]
# for i in n:
#     for j in my_list:
#         if i == j:
#             my_list.remove(i)
# print(set(my_list))

# =============================================================================================================================
# 6.Update set1 by adding items from set2, except common items
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
# {70, 10, 20, 60}

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# mylist = []
# for i in set1:
#     if i in set2:
#         continue
#     else:
#         mylist.append(i)
# for i in set2:
#     if i in set1:
#         continue
#     else:
#         mylist.append(i)
# print(set(mylist))

# =============================================================================================================================
# 7.Swap two tuples in Python
# Given:
# tuple1 = (11, 22)
# tuple2 = (99, 88)
# Expected output:
# tuple1: (99, 88)
# tuple2: (11, 22)

# tuple1 = (11, 22)
# tuple2 = (99, 88)
#
# tuple1,tuple2=tuple2,tuple1
# print(tuple1)
# print(tuple2)
# =============================================================================================================================
# 8.Remove special symbols / punctuation from a string
# Given:str1 = "/*Jon is @developer & musician"
# Expected Output:
# "Jon is developer musician"

# str1 = "Jon is developer musician"
# mylist = []
# for i in str1:
#     if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z' or i == " ":
#         mylist.append(i)
# str1 = "".join(mylist)
# print(str1)

# =============================================================================================================================
# 9.Removal all characters from a string except integers
# Given:
# str1 = 'I am 25 years and 10 months old'
# Expected Output:
# 2510

# str1 = 'I am 25 years and 10 months old'
# mylist = []
# for i in str1:
#     if i >= '0' and i <= '9':
#         mylist.append(i)
# str1 = "".join(mylist)
# print(str1)
