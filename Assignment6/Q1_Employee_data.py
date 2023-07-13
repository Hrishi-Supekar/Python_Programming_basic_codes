# Print employee data using for loop in UD form
employee = {"eid": 101, "ename": "Hrishi", "sal": 80000, "deptno": 10, "job": "Python developer"}
for key, val in employee.items():
    print(f"{key}:{val}")
