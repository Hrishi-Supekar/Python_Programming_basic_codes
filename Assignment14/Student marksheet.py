# create 5 student marksheet
class student:
    def __init__(self, name, rno, m1, m2, m3):
        self.grade = None
        self.per = 0
        self.total = 0
        self.s_name = name
        self.s_rno = rno
        self.s_m1 = m1
        self.s_m2 = m2
        self.s_m3 = m3

    def cal_res(self):
        self.total = self.s_m1 + self.s_m2 + self.s_m3
        self.per = self.total / 3
        if self.per > 75:
            self.grade = "Grade-A"
        elif self.per > 60:
            self.grade = "Grade-B"
        elif self.per > 50:
            self.grade = "Grade-C"
        elif self.per > 40:
            self.grade = "Grade-D"
        elif self.per < 35:
            self.grade = "Failed!!"

    def display_res(self):
        print(
            f"{self.s_name}\t{self.s_rno}\t{self.s_m1}\t{self.s_m2}\t{self.s_m3}\t"
            f"{self.total}\t{round(self.per,2)}\t{self.grade}")


# Adding instance to list
n = int(input("Enter the number of student to add:"))
student_list = [student(input("Enter the name:"), int(input("Enter the rno:")), int(input("Enter the subject1 marks:")),
                        int(input("Enter the subject2 marks:")), int(input("Enter the subject3 marks:"))) for x in range(n)]

for obj in student_list:
    obj.cal_res()
    obj.display_res()

# Accessing all instance from list
# for i in range(len(student_list)):
#     print(f"{student_list[i].s_name}\t{student_list[i].s_rno}\t{student_list[i].s_m1}\t{student_list[i].s_m2}\t{student_list[i].s_m3}\t")
