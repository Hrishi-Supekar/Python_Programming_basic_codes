# Delete key-value pair from employee dict
employee = {"eid": 101, "ename": "Hrishi", "sal": 80000, "deptno": 10, "job": "Python developer"}
print(employee)
key = input("Enter the key for which you want to delete key-val pair:")
employee.pop(key)
print(employee)
