# 6.Write a java program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer.
# Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F
# -----------------------------------------------------------------------------4
Physics, Chemistry, Biology, Mathematics, Computer = [int(x) for x in input("Enter the 5 subject marks:").split()]
total = Physics + Chemistry + Biology + Mathematics + Computer
per = total / 500 * 100
print("The percentage is",per)
if per >= 90:
    print("The student received grade A")
elif per >= 80:
    print("The student received grade B")
elif per >= 70:
    print("The student received grade C")
elif per >= 60:
    print("The student received grade D")
elif per >= 40:
    print("The student received grade E")
elif per < 40:
    print("The student received grade F")
else:
    print("Invalid input!!")




