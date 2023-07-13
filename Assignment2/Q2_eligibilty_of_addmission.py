# 2.Write a Python program to find the eligibility of admission for a professional course
# based on the following criteria:
# Marks in Maths >=65
# Marks in Phy >=55
# Marks in Chem>=50
# Total in all three subject >=180
# ______________________________________________________________________________

# Maths = int(input("Enter the marks of Maths:"))
# Phy = int(input("Enter the marks of Physics:"))
# chem = int(input("Enter the marks of Chemistry:"))
Maths, Phy, chem = [int(x) for x in input("Enter the marks of 3 subject:").split()]
total = Maths + Phy + chem
if Maths >= 65 and Phy >= 55 and chem >= 50 and total >= 180:
    print("The Student is eligible for admission!!")
else:
    print("The Student is not eligible for admission!!")
