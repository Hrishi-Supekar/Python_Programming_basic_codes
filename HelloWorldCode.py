# print("Welcome to my first program")
# print("Hello World!!!")

# Variable - It is the memory location name where the value is stored.
# DataType - To identify the data which is stored in the memory location.
# Types of datatype-
# 1.Primitive datatype -- int,float,char,double,string,boolean.
# 2.Non-Primitive datatype -- Array,object,structure,reference variable.

# python is dyanamic way programming language.

# num = 34  #integer type variable.
# num1 = 45.67 #float type variable.
# msg = "Welcome" #String type variable.
# ch = 'W' #character type variable.
# bool = True #boolen type variable.


"""num = 34
num1 = 67
name = "Hrishikesh"
name1 = "Supekar"

print(type(num))  # to check the type of variable.
print(type(name))  # to check the type of variable.

print("Value of num =", num)
print("Value of num1 =", num1)
print("My name is =", name)
print("My name is =", name + " " + name1)
print("The addition of numbers is =", num + num1)"""

# Typecasting - Changing one datatype to another datatype.
# 1. str() - It is a predefined function, to convert the value into string datatype.
# 2. int() - It is a predefined function, to convert the value into integer datatype.
# 3. float() - It is a predefined function, to convert the value into float datatype.

"""num = "45"
num1 = 44
num2 = 45.35
print(int(num) + num1)
print(num1 + num2)
print(int(num2))
print(float(num1))"""

"""name="Hrishi"
age=27
city="Pune"

print(name)
print(age)
print(city)

print(name+"\t"+str(age)+"\t"+city)
print(f"My name is {name} and my age is {age} and I am from {city}")"""

# Addition,mul,div,sub of 2 nos
num1 = 45
num2 = 5

print(num1 + num2)
print(num1 * num2)
print(f"{num1 / num2:.3f}")  # & to print in req decimal use format specifier with .2f
print(10 // 3)  # return value in float if you require int use floor(//).
print(num1 - num2)
print(2 ** 3)  # To print power use **.
