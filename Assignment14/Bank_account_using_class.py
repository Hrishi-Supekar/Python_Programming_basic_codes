# class Bank:
#     def __init__(self, id, name, type, amt):
#         self.acc_id = id
#         self.acc_name = name
#         self.acc_type = type
#         self.acc_bal = amt
#
#     def withdraw_amt(self):
#         self.wamt = int(input("Enter the amount to withdraw:"))
#         self.acc_bal = self.acc_bal - self.wamt
#
#     def deposit_amt(self):
#         self.damt = int(input("Enter the amount to deposit:"))
#         self.acc_bal = self.acc_bal + self.damt
#
#     def display_statement(self):
#         print(f"{self.acc_id}\t{self.acc_name}\t{self.acc_type}\t{self.acc_bal}")
#
#
# obj1 = Bank(101, "Hrishi", "saving", 67000)
# obj2 = Bank(102, "Omkar", "current", 55000)
# obj3 = Bank(103, "Alisha", "Reccurring", 88000)
# obj1.deposit_amt()
# obj1.withdraw_amt()
# obj1.display_statement()

# ====================================================================
class student:
    def __init__(self, name, rno):
        self.name = name
        self.rno = rno


n = int(input("Enter the number of student to add:"))
student_list = [student(input("Enter the name:"), int(input("Enter the rno"))) for x in range(n)]

# Adding instance to list

# student_list.append(student("hrishi", 10))
# student_list.append(student("omkar", 11))
# student_list.append(student("alisha", 12))
# student_list.append(student("kirti", 13))
# student_list.append(student("vijay", 14))

# Accessing all instance from list
for obj in student_list:
    print(obj.name, obj.rno)

for i in range(len(student_list)):
    print(student_list[i].name)


# print(student_list[0].name)
# print(student_list[1].name)
# print(student_list[2].name)
# print(student_list[3].name)
# print(student_list[4].name)


