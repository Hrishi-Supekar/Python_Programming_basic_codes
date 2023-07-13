# Print the value of key entered by user & if key not present provided msg
employee = {"eid": 101, "ename": "Hrishi", "sal": 80000, "deptno": 10, "job": "Python developer"}
key = input("Enter the key to print the value:")
if key in employee.keys():
    print(employee[key])
else:
    print("Key not present!")
