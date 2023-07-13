# Nested Dictionary:
# d = {'emp1': {'name': 'Bob', 'job': 'Mgr', 'sal': 88000},
#      'emp2': {'name': 'Kim', 'job': 'Dev', 'sal': 68000},
#      'emp3': {'name': 'Sam', 'job': 'Admin', 'sal': 58000},
#      'emp4': {'name': 'Ram', 'job': 'Admin', 'sal': 54000},
#      'emp5': {'name': 'Rahul', 'job': 'Data Engg', 'sal': 78000},
#      'emp6': {'name': 'Sunil', 'job': 'Sql dev', 'sal': 68000}}
# print(d['emp1'])
# print(d['emp2'])
# print(d['emp3'])
# print(d['emp3']['job'])
# print(d['emp2']['name'])
# print(d['emp1']['sal'])

# for x,y in d.items():
#      print(f"{x}:")
#      for j,i in y.items():
#           print(f"{j}:{i}")
#      print()

# D1 = {'emp1': {'Name': 'Bob', 'job': 'Mgr'},
#       'emp2': {'Name': 'Kim', 'job': 'Dev'}}
#
# D2 = {'emp2': {'Name': 'Sam', 'job': 'Dev'},
#       'emp3': {'Name': 'Max', 'job': 'Janitor'}}
#
# D1.update(D2)
# print(D1)


d = {'emp1': {'name': 'Bob', 'job': 'Mgr', 'sal': 88000},
     'emp2': {'name': 'Kim', 'job': 'Dev', 'sal': 68000},
     'emp3': {'name': 'Sam', 'job': 'Admin', 'sal': 58000},
     'emp4': {'name': 'Ram', 'job': 'Admin', 'sal': 94000},
     'emp5': {'name': 'Rahul', 'job': 'Data Engg', 'sal': 78000},
     'emp6': {'name': 'Sunil', 'job': 'Sql dev', 'sal': 68000}}

# print emp with job = admin:
# for i, j in d.items():
#     for k, v in j.items():
#         if k == 'job' and v == 'Admin':
#             print(f"{i}:{j}")

# Highest salary employee:
# max = d['emp1']['sal']
# for i, j in d.items():
#     for k, v in j.items():
#         if k == 'sal' and v > max:
#             max = v
# for key,val in d.items():
#     for x,y in val.items():
#         if max == y:
#             print(f"{key}:{val}")

# Add new key-value pair:
# k = input("Enter the key:")
# v = {}
# n = int(input("Enter the number of dict element:"))
# for x in range(n):
#     x = input("Enter the key for dict:")
#     y = input("Enter the value for dict:")
#     v.update({x: y})
# d.update({k: v})
# # print(d)
# for x, v in d.items():
#     print(f"{x}:{v}")


# Delete user defined key -value pair from dict:
# key = input("enter the key which ")
# mydict = d.copy()
# for x, y in mydict.items():
#     for i, j in y.items():
#         if j == 'Admin':
#             d.pop(x)
# for x, v in d.items():
#     print(f"{x}:{v}")


