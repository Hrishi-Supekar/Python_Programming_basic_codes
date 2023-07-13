# 4. If the three sides of a triangle are entered through the keyboard,
# write a program to check whether thr triangle is valid or not.
# The triangle is valid if the sum of two sides is greater than the largest of the three sides.
# ______________________________________________________________________________
# s1 = int(input("Enter the first side of triangle:"))
# s2 = int(input("Enter the second side of triangle:"))
# s3 = int(input("Enter the third side of triangle:"))
s1, s2, s3 = [int(x) for x in input("Enter the 3 sides:").split()]
if s1 > s2 and s1 > s3 and (s2 + s3) > s1:
    print("The triangle is a valid triangle!!!")
elif s2 > s1 and s2 > s3 and (s1 + s3) > s2:
    print("The triangle is a valid triangle!!!")
elif s3 > s2 and s3 > s1 and (s2 + s1) > s3:
    print("The triangle is a valid triangle!!!")
else:
    print("The triangle is not a valid triangle!!!")
