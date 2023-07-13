# Add new key-value pair in the employee dict
employee = {"eid": 101, "ename": "Hrishi", "sal": 80000, "deptno": 10, "job": "Python developer"}
key = input("Enter the key:")
val = input("Enter the value:")
employee.update({key: val})
# print(employee)
for i, j in employee.items():
    print(f"{i}:{j}")
