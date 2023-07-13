# 3.To print greatest of 3 nos = a=30,b=40,c=50
# ______________________________________________________________________________
# n1 = int(input("Enter the first number:"))
# n2 = int(input("Enter the second number:"))
# n3 = int(input("Enter the third number:"))
n1, n2, n3 = [int(x) for x in input("Enter the 3 numbers:").split()]
if n1 > n2 and n1 > n3:
    print(f"The number {n1} is greater than {n2} & {n3}")
elif n2 > n1 and n2 > n3:
    print(f"The number {n2} is greater than {n1} & {n3}")
elif n3 > n2 and n3 > n1:
    print(f"The number {n3} is greater than {n1} & {n3}")
else:
    print("All the number are same!!")
