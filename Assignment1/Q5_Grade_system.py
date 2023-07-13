# WAP to accept student name,rollno,3 subject marks,and print total and percentage
# and print grade as per below cond -- per >=70 - distinction
# per - 60-70 - first class
# per - 50-60 - second class
# per - 40 - 50 - pass class
# otherwise fail

name = input("Enter the name of student:")
rollno = int(input("Enter the roll no:"))
# s1 = int(input("Enter the subject 1 marks:"))
# s2 = int(input("Enter the subject 2 marks:"))
# s3 = int(input("Enter the subject 3 marks:"))
s1, s2, s3 = [int(x) for x in input("Enter the subject marks").split()]
total = s1 + s2 + s3
per = total / 300 * 100

print(f"The total marks is:{total}")
print(f"The Percentage is:{per}")

if per >= 70:
    print(f"Student {name} with rollno-{rollno} received Distinction!!")
elif per >= 60:
    print(f"Student {name} with rollno-{rollno} received First class!!")
elif per >= 50:
    print(f"Student {name} with rollno-{rollno} received Second class!!")
elif per >= 40:
    print(f"Student {name} with rollno-{rollno} received pass class!!")
else:
    print(f"Student {name} with rollno-{rollno} Failed!!")
