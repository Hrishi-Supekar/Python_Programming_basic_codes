# print employees dict keys only in UD form
employee = {"eid": 101, "ename": "Hrishi", "sal": 80000, "deptno": 10, "job": "Python developer"}
# print(employee.keys())
for i in employee.keys():
    print(i, end=" ")
