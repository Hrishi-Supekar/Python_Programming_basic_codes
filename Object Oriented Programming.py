# Object-oriented programming:
# class employee:
#     name = ""  # attribute or state or class variable
#     age = 0
#     sal = 0

#     def get_info(self):  # Behavior or method or instance member func
#         self.deptno = 10  # Instance member variable
#         self.dname = "Sales"
#         print(f"{self.deptno}\t{self.dname}")
#         # return (self.deptno,self.dname)
#
#
# obj = employee()  # Object creation
# obj1 = employee()
# obj2 = employee()
#
# obj.name = "Hrishi"
# obj.age = 27
# obj.sal = 88000
#
# print(f"{obj.name}\t{obj.age}\t{obj.sal}")

# obj.get_info()  # func calling via caller object(obj)
# obj1.get_info()
# obj2.get_info()

# print(obj.get_info()) # o/p in tuple form
# ==============================================================================================================================================
# class Student():
#     institute_name = "ITP"
#
#     def get_info(self, name, id, p1, p2, p3):
#         self.sname = name
#         self.sid = id
#         self.m1 = p1
#         self.m2 = p2
#         self.m3 = p3
#
#     def show_info(self):
#         print(f"{self.sid}\t{self.sname}\t{self.m1}\t{self.m2}\t{self.m3}\t{self.total}\t{self.per}")
#
#     def cal_result(self):
#         self.total = self.m1 + self.m2 + self.m3
#         self.per = self.total / 3
#
#
# s1 = Student()
# s1.get_info("Hrishi", 1, 77, 87, 76)
# s1.cal_result()
# s1.show_info()
# ==============================================================================================================================================
# class Student():
#     institute_name = "ITP"
#
#     def get_info(self):
#         self.sname = input("Enter the name of student:")
#         self.sid = int(input("Enter the student id:"))
#         self.m1 = int(input("Enter the student marks for subject1:"))
#         self.m2 = int(input("Enter the student marks for subject1:"))
#         self.m3 = int(input("Enter the student marks for subject1:"))
#
#     def show_info(self):
#         print(f"{self.sid}\t{self.sname}\t{self.m1}\t{self.m2}\t{self.m3}\t{self.total}\t{self.per}")
#
#     def cal_result(self):
#         self.total = self.m1 + self.m2 + self.m3
#         self.per = self.total / 3


# s1 = Student()
# s1.get_info()
# s1.cal_result()
#
# s2 = Student()
# s2.get_info()
# s2.cal_result()
#
# s3 = Student()
# s3.get_info()
# s3.cal_result()
#
# s1.show_info()
# s2.show_info()
# s3.show_info()

# ==============================================================================================================================================
# Constructor:
# User can change the state of object(instance variable) using constructor
# Only one type of constructor is allowed in the class of an object.(ie-either default or parameterized)
# 1)Default Constructor:
# class Student:
#     def __init__(self):  # default constructor
#         print("Constructor invoked")
#
#     def show(self):
#         print("This is show fun")
#
#
# obj = Student()  # when we create an object of class the __init__ method is called by default by compiler/interpreter
# obj1 = Student()
# obj2 = Student()
# obj.show()
# obj1.show()
# obj2.show()
# ==============================================================================================================================================
# 2)Parameterized Constructor: Initially state to own value state we create parameterized constructor
# class student:
#     def __init__(self, m, n):  # Parameterized Constructor
#         self.a = m
#         self.b = n
#
#     def show(self):
#         print(f"{self.a}\t{self.b}")
#
#
# obj = student(2, 3)  # parameterized method with actual argument
# obj1 = student(10, 12)
# obj2 = student(20, 30)
# obj.show()
# obj1.show()
# obj2.show()
# ==============================================================================================================================================
# Python Object Oriented Programming -
#
# Python is a versatile programming language that supports various programming styles, including object-oriented programming (OOP)
# through the use of objects and classes.
#
# An object is any entity that has attributes and behaviors. For example, a parrot is an object. It has
#
# attributes - name, age, color, etc.
# behavior - dancing, singing, etc.
#
# Similarly, a class is a blueprint for that object.
#
# ___________________________________________________________________________
#
# Python Objects and Classes -
#
# An object is simply a collection of data (variables) and methods (functions). Similarly, a class is a blueprint for that object.
#
# _________________________________________________________________________
#
# Python Classes -
#
# A class is considered as a blueprint of objects. We can think of the class as a sketch (prototype) of a house.
# It contains all the details about the floors, doors, windows, etc. Based on these descriptions we build the house. House is the object.
#
# Since many houses can be made from the same description, we can create many objects from a class.
#
#
# Define Python Class-
#
# We use the class keyword to create a class in Python. For example,
#
#
# class ClassName:
#     # class definition
#
# Note: The variables inside a class are called attributes.
#
# __________________________________________________________
#
#
# Python Objects -
#
# An object is called an instance of a class. For example, suppose Bike is a class then we can create objects like bike1, bike2,
# etc from the class.
#
# # create class
# class Bike:
#     name = ""
#     gear = 0
#
# # create objects of class
# bike1 = Bike()
#
# ________________________________________________________
#
# Access Class Attributes Using Objects
# We use the . notation to access the attributes of a class. For example,
#
# # modify the name attribute
# bike1.name = "Mountain Bike"
#
# # access the gear attribute
# bike1.gear
# ______________________________________________________
#
# Example- Python Class and Objects
# # define a class
# class Bike:
#     name = ""
#     gear = 0
#
# # create object of class
# bike1 = Bike()
#
# # access attributes and assign new values
# bike1.gear = 11
# bike1.name = "Mountain Bike"
#
# print(f"Name: {bike1.name}, Gears: {bike1.gear} ")
#
# _________________________________________________________
#
# # define a class
# class Employee:
#     # define an attribute
#     employee_id = 0
#
# # create two objects of the Employee class
# employee1 = Employee()
# employee2 = Employee()
#
# # access attributes using employee1
# employee1.employeeID = 1001
# print(f"Employee ID: {employee1.employeeID}")
#
# # access attributes using employee2
# employee2.employeeID = 1002
# print(f"Employee ID: {employee2.employeeID}")
#
# _________________________________________________________________________
# Constructor -
#
# Constructor is a special method used to create and initialize an object of a class. On the other hand, a destructor
# is used to destroy the object.
#
# 1.The constructor is executed automatically at the time of object creation.
#
# 2. The primary use of a constructor is to declare and initialize data member/ instance variables of a class.
#
# Syntax of a constructor -
#
# def init(self):
#     # body of the constructor
#
# Important Points -
#
# 1. def: The keyword is used to define function.
#
# 2. init() Method: It is a reserved method. This method gets called as soon as an object of a class is instantiated.
#
# 3. self: The first argument self refers to the current object. I
#
#
# Note:
#
# For every object, the constructor will be executed only once. For example, if we create four objects, the constructor is called four times.
#
# In Python, every class has a constructor, but it’s not required to define it explicitly. Defining constructors in class is optional.
#
# Python will provide a default constructor if no constructor is defined.
#
# _________________________________________________________________________
# Types of Constructors -
#
# In Python, we have the following three types of constructors.
#
# Default Constructor
# Non-parametrized constructor
# Parameterized constructor
#
# Default Constructor -
#
# Python will provide a default constructor if no constructor is defined. Python adds a default constructor when we do not
# include the constructor in the class or forget to declare it. It does not perform any task but initializes the objects.
# It is an empty constructor without a body.
#
# Non-Parametrized Constructor -
#
# A constructor without any arguments is called a non-parameterized constructor.
# This type of constructor is used to initialize each object with default values.
#
# Parameterized Constructor -
#
# A constructor with defined parameters or arguments is called a parameterized constructor.
# We can pass different values to each object at the time of creation using a parameterized constructor.
