# students = {"Name": "Hrishi", "Rollno": 101, "Age": 27, "Course": "Python"}
# print(students)

# students.clear()  # Clears all element from the dict
# print(students)  # prints an empty dict

# newstudent = students.copy() #Copies all elements from old dict to new dict
# print(newstudent)


# x = ("Name1", "Name2", "Name3")
# y = "Hrishi"
# thisdict = dict.fromkeys(x, y)  # Returns a dict with the specified keys and values
# print(thisdict)

# students = {"Name": "Hrishi", "Rollno": 101, "Age": 27, "Course": "Python", "Age": 58, "city": "pune"}
# print(students.get("Age"))  # to get the specific value from the dict
# print(students["Age"])
#
# x = students.keys()  # will get all keys from the dict
# print(x)
#
# y = students.items()  # will give you all key and value from the dict
# print(y)
#
# z = students.values()  # will return all the values from the dict
# print(z)
#
# students.pop("Age")  # will delete the specified key's key-value pair from dict
# print(students)
#
# students.popitem()  # will delete the last added key-value pair from dict
# print(students)
#
# students.update({"Marks": 95})
# # will update the dict with the specified key-value pair or will basically add it at last
# print(students)
#
# for i, j in students.items():
#     print(f"{i}={j}")

# students = {"Name": "Hrishi", "Rollno": 101, "Age": 27, "Course": "Python", "m1": 65, "m2": 85, "m3": 75}
# sum = 0
# for k, v in students.items():  # will iterate the loop with key-value pair
#     if k == 'm1' or k == 'm2' or k == 'm3':
#         sum += students[k]  # will provide us value of the particular key  in the iteration.
#         # sum = sum+students[k]  # will provide us value of the particular key  in the iteration.
# students.update({"total": sum})
# print(students)

# ==========================================02/06/23===============================================


