# 1. - Design Half Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4  ex  - 56/6
# Your program should take operator  and the two numbers as input from the user and then return the result
# ______________________________________________________________________________

# n1 = int(input("Enter the first operand:"))
# n2 = int(input("Enter the second operand:"))
n1,n2 = [int(x) for x in input("Enter the value of operand:").split()]
op = input("Enter the operator:")

if op == '+':
    if n1 == 56 and n2 == 9:
        print(f"The addition of {n1} and {n2} is 77")
    else:
        print(f"The addition of {n1} and {n2} is", n1 + n2)
elif op == '*':
    if n1 == 45 and n2 == 3:
        print(f"The multiplication of {n1} and {n2} is 555")
    else:
        print(f"The multiplication of {n1} and {n2} is", n1 * n2)
elif op == '/':
    if n1 == 56 and n2 == 6:
        print(f"The multiplication of {n1} and {n2} is 4")
    else:
        print(f"The multiplication of {n1} and {n2} is", n1 / n2)
elif op == '-':
    print(f"The Subtraction of {n1} and {n2} is ", n1 - n2)
else:
    print("Invalid operator!!!")