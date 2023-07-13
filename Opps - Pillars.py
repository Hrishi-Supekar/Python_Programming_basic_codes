# Opps pillars:
# 1)Encapsulation - Bundling the data and methods within a single unit. Ex- when creating a class, you are implementing encapsulation.
# means binding all the data members(instance variable ) and methods into single unit OR medicine Capsule.
# We can hide data in encapsulation
# Access modifier: limit access to the variable and methods of a class.
#     1)Public Member:Accessible anywhere from outside of class.(no _(underscore))
#     2)Protected Member: Accessible within the class and its subclass.(_(single underscore))
#     3)Private Member: Accessible with the class.(__(double underscore))
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Ex=
# class Employee:
#     def __init__(self, eid, name, salary):
#         self.e_name = name
#         self._e_id = eid
#         self.__e_salary = salary
#
#     def show_sal(self):
#         print(f"Emp_sal = {self.__e_salary}")
#

# E1 = Employee(101, 'Hrishi', 88000)
# print(f"Name = {E1.e_name}")
# print(f"Emp_Id = {E1._e_id}")
# E1.show_sal()
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Accessing private variable using name mangling:
# print(f"Emp_sal = {E1._Employee__e_salary}")#Name Mangaling
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Getter & Setter:
# Setter are used to set values to the variable
# Getter are used to get/return values of the variable set by setter.
# class Employee:
#     def set_name(self, name):  # Setter
#         self.e_name = name
#
#     def set_id(self, eid):
#         self.e_id = eid
#
#     def set_sal(self, sal):
#         self.e_sal = sal
#
#     def get_name(self):  # Getter
#         return self.e_name
#
#     def get_id(self):
#         return self.e_id
#
#     def get_sal(self):
#         return self.e_sal
#
#
# E1 = Employee()
# E1.set_name("Hrishi")
# E1.set_id(101)
# E1.set_sal(88000)
#
# # Print all info:
# print(E1.get_name())
# print(E1.get_id())
# print(E1.get_sal())

# ===============================================================================================================================================
# 2)Inheritance-
# Inheritance allows us to inherit attribute and methods from the base/parent class.
# This is used as we can create subclass and get functionality from the parent class
# creating new class from existing class is called inheritance.
# The new class is known as a derived class or child class & the one whose properties are acquired is
# known as base or parent class or super class.
# It provides re-usability of the code.
# Types of inheritance:
# 1)Single Inheritance --> Single derived class & Single Base class
# 2)Multilevel Inheritance --> Single derived class & with base class with level of base class
# 3)Hierarchical Inheritance --> single base class & multiple derived class
# 4)Multiple Inheritance --> single derived class & multiple base class
# 5)Hybrid Inheritance --> combination of all above inheritance
# -----------------------------------------------------------------------------------------------------------------------------------------------
# 1)Single Inheritance:
# class bank:

# def __init__(self,name, accno, bal, acctype): parameterized constructor
#     self.c_name = name;
#     self.c_accno = accno
#     self.c_bal = bal
#     self.c_acc = acctype

# def cust_info(self, name, accno, bal, acctype):
#     self.c_name = name;
#     self.c_accno = accno
#     self.c_bal = bal
#     self.c_acc = acctype


# class customer(bank):
#     cust_add = "Pune"

# def Show_info(self):
#     print(f"{self.c_name}\t{customer.cust_add}\t{self.c_accno}\t{self.c_acc}\t{self.c_bal}")


# c = customer()
# c = customer("Hrishi", 111, 880000, "saving") parameterized constructor
# c.cust_info("Hrishi", 111, 880000, "saving")
# c.Show_info()
# -----------------------------------------------------------------------------------------------------------------------------------------------
# 2)Multilevel Inheritance:
# from class A -> class B -> class C

# class A:
#
#     def get_a(self, a):
#         self.a = a
#         return self.a
#
#
# class B(A):
#
#     def get_b(self, b):
#         self.b = b
#
#
# class C(B):
#     c = 3
#
#     def mul(self):
#         self.result = self.get_a(2) * self.b * C.c
#         return self.result
#
#
# obj = C()
# obj.get_b(4)
# print(obj.mul())
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Default constructor calling using super():
# class A:
#     def __init__(self):
#         print("A Default Constructor called!!!")
#
#
# class B(A):
#     def __init__(self):
#         # super().__init__()  # If super is not present in child class then it will not call the parent constructors default constructor.
#         print("B Default Constructor called!!!")
#
#
# class C(B):
#     def __init__(self):
#         super().__init__()  # If super is present in child class then it will call the parent constructors default constructor.
#         print("C Default Constructor called!!!")
#
#
# obj = C()
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Using Parameterized constructor:
# class A:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         print(f"class_A={a}, class_A={b}")
#
#
# class B(A):
#     def __init__(self, a, b):
#         # super().__init__(a,b) # if super is not present in child class then parameterized constructor will not be called of parent class.
#         self.a = a
#         self.b = b
#         print(f"class_B={a}, class_B={b}")
#
#
# class C(B):
#     def __init__(self, a, b):
#         super().__init__(a, b)  # if super is present in child class then parameterized constructor will be called of parent class.
#         self.a = a
#         self.b = b
#         print(f"class_C={a}, class_C={b}")
#
#
# obj = C(10, 20)
# -----------------------------------------------------------------------------------------------------------------------------------------------
# 3)Multiple Inheritance:
# class subject_marks:  # m1,m2,m3,m4
#     def get_marks(self, m1, m2, m3, m4):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#         self.m4 = m4
#
#
# class other_activity:  # sport,music,yoga
#     def get_other_act(self, sport, music, yoga):
#         self.sport = sport
#         self.music = music
#         self.yoga = yoga
#
#
# class student(subject_marks, other_activity):
#     def show_res(self):
#         self.result = self.m1 + self.m2 + self.m3 + self.m4 + self.sport + self.music + self.yoga
#         self.per = self.result / 7
#         print(f"Total of all marks={self.result} & Percentage ={self.per}")
#
#
# obj = student()
# obj.get_marks(10, 20, 30, 40)
# obj.get_other_act(50, 60, 70)
# obj.show_res()
# -----------------------------------------------------------------------------------------------------------------------------------------------
# 4)Hierarchical Inheritance
# band class

# -----------------------------------------------------------------------------------------------------------------------------------------------
# 5)Hybrid Inheritance


# ===============================================================================================================================================
# 3)Abstraction
# It is used to hide internal functionality from user & user only interact with basic implementation of the function.


# ===============================================================================================================================================
# 4)Polymorphism
# poly=many & morphs=form,shape
# one task can be performed in different ways.
# it is the ability of an object to perform same action in different way.

# ===============================================================================================================================================
# class Animal:
#     pet_name = ""
#
#     def speak(self):
#         print("Animal Class")
#
#     def bread(self):
#         print("Animal bread")
#
# class Dog(Animal):
#
#     def speak(self):
#         super().speak()
#         super().bread()
#         Dog.pet_name = "Dog"
#         print("Bark")
#         print(Dog.pet_name)
#
#
# class Goat(Animal):
#
#     def speak(self):
#         Goat.pet_name = "Goat"
#         print("aaa")
#         print(Goat.pet_name)
#
#
# class Cat(Animal):
#
#     def speak(self):
#         Cat.pet_name = "Cat"
#         print("Meow")
#         print(Cat.pet_name)
#
#
# Dog_obj = Dog()
# Cat_obj = Cat()
# Goat_obj = Goat()
# Dog_obj.speak()
# Cat_obj.speak()
# Goat_obj.speak()
