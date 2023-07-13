# 2.Write a Python script to check whether a given key already exists in a dictionary.
d = {"n1": 1, "n2": 2, "n3": 3, "n4": 4}
k = input("Enter the key to check:")
if k in d.keys():
    print("The key is already present!")
else:
    print("The key is not present!")
# =======================OR========================
# flag = 0
# for i in d.keys():
#     if i == k:
#         flag = 1
#         break
# if flag == 0:
#     print("The key is not present!")
# else:
#     print("The key is already present!")
