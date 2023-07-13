#WAP to print the marksheet of student -- name,3 subject mks,total,percentage.

name=input("Enter the name of student:")
mks1=int(input("Enter the 1st subject marks:"))
mks2=int(input("Enter the 2nd subject marks:"))
mks3=int(input("Enter the 3rd subject marks:"))
total=mks1+mks2+mks3
percentage=total/3
print(f"Name\t M1\t M2\t M3\t Total\t Percentage")
print(f"{name}\t {mks1}\t {mks2}\t {mks3}\t {total}\t {percentage:0.2f}")
