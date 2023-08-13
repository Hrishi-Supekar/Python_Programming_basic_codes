# # To remove all extra duplicate element form original list and create new list of that  duplicate element:
# l = [1, 2, 3, 4, 5, 6, 6, 2, 3, 8, 9, 5, 5, 2, 2, 1, 2, 3,1,1,1,1,2,3]
# copy = l
# l1 = []
# for i in copy:
#     if copy.count(i) > 1:
#         # print(copy.count(i),end=" ")
#         for x in range(copy.count(i)-1):
#             l.remove(i)
#             l1.append(i)
# print(l)
# print(l1)
# ======================================================================================================
# class VendingMachine:
#     def __init__(self):
#         self.items = {
#             "Coke": 1.50,
#             "Chips": 1.25,
#             "Candy": 0.75,
#             "Water": 1.00,
#         }
#         self.balance = 0.0
#
#     def display_items(self):
#         print("Available Items:")
#         for item, price in self.items.items():
#             print(f"{item} - ${price:.2f}")
#
#     def insert_coin(self, amount):
#         self.balance += amount
#
#     def purchase_item(self, item_name):
#         if item_name in self.items:
#             price = self.items[item_name]
#             if self.balance >= price:
#                 self.balance -= price
#                 print(f"Dispensing {item_name}. Enjoy!")
#             else:
#                 print("Insufficient balance. Please insert more coins.")
#         else:
#             print(f"Item '{item_name}' not available in the vending machine.")
#
#     def get_balance(self):
#         return self.balance
#
#
# def main():
#     vending_machine = VendingMachine()
#
#     while True:
#         print("\nWelcome to the Vending Machine!")
#         vending_machine.display_items()
#
#         try:
#             choice = int(input("\nInsert coins (1) or purchase item (2) or exit (3): "))
#         except ValueError:
#             print("Invalid choice. Please try again.")
#             continue
#
#         if choice == 1:
#             try:
#                 coins = float(input("Insert coins (e.g., 0.25, 0.5, 1, 2): "))
#                 if coins > 0:
#                     vending_machine.insert_coin(coins)
#                 else:
#                     print("Invalid coin amount. Please insert valid coins.")
#             except ValueError:
#                 print("Invalid coin amount. Please insert valid coins.")
#
#         elif choice == 2:
#             item = input("Enter the name of the item you want to purchase: ")
#             vending_machine.purchase_item(item)
#
#         elif choice == 3:
#             print("Thank you for using the Vending Machine. Have a great day!")
#             break
#
#         else:
#             print("Invalid choice. Please try again.")
#
#
# if __name__ == "__main__":
#     main()

# ====================
# product_stock = [{'Product_id': 1, 'Product_name': 'Coke ', 'Price': 40},
#                      {'Product_id': 2, 'Product_name': 'Pepsi', 'Price': 35},
#                      {'Product_id': 3, 'Product_name': '7Up  ', 'Price': 36},
#                      {'Product_id': 4, 'Product_name': 'Maaza', 'Price': 30},
#                      {'Product_id': 5, 'Product_name': 'Coffee', 'Price': 25},
#                      {'Product_id': 6, 'Product_name': 'Milk', 'Price': 20}]
# for i in product_stock:
#     print(i['Product_id'])

# ====================
# Number = 204
#
#
# def AddNumber():
#     global Number
#     Number = Number + 200
#
#
# print("The number is:", Number)
# AddNumber()
# print("The number is:", Number)

# ===============================
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# # Calling the decorated function
# say_hello()

# ============================
# def func1(msg):  # here, we are creating a function and passing the parameter
#     print(msg)
#
#
# func1("Hii, welcome to function ")  # Here, we are printing the data of function 1
# func2 = func1  # Here, we are copying the function 1 data to function 2
# func2("hello ")  # Here, we are printing the data of function 2
# ========================================
# def outer_div(func):  # here, we are creating a function and passing the parameter
#     def inner(x, y):  # here, we are creating a function and passing the parameter
#         if x < y:
#             x, y = y, x
#             return func(x, y)  # here, we are returning the function with the parameters
#
#     return inner
#
#
# # Here, the below is the syntax of generator
# @outer_div
# def divide(x, y):  # here, we are creating a function and passing the parameter
#     print(x / y)
#
#
# divide(2, 4)
# ===================================================
# # Import module to keep track of time
# import time
#
#
# # defining function to execute for loop
# def for_loop(num):
#     l = []
#     for i in range(num):
#         l.append(i + 10)
#     return l
#
#
# # defining function to execute list comprehension
# def list_comprehension(num):
#     return [i + 10 for i in range(num)]
#
#
# # Giving values to the functions
#
# # Calculating time taken by for loop
# start = time.time()
# for_loop(10000000)
# end = time.time()
#
# print('Time taken by for loop:', (end - start))
#
# # Calculating time taken by list comprehension
# start = time.time()
# list_comprehension(10000000)
# end = time.time()
#
# print('Time taken by list comprehension:', (end - start))
# ===============================================================
# def Sum(n):
#     dsum = 0
#     for ele in str(n):
#         dsum += int(ele)
#     return dsum
#
#
# List = [47, 69, 73, 97, 105, 845, 307]
# newList = [Sum(i) for i in List ]
# print(newList)
# ===================================================================
# user_dict5 = dict()
# for numm in range(3, 20):
#     user_dict5 [numm] = numm*numm
# print("user_dict5: ", user_dict5)
# =========================================
# import pickle
#
# # Input Data
# my_data = {'BMW', 'Audi', 'Toyota', 'Benz'}
#
# # Pickle the input
# with open("demo.pickle", "wb") as file_handle:
#     pickle.dump(my_data, file_handle, pickle.HIGHEST_PROTOCOL)
#
# # Unpickle the above pickled file
# with open("demo.pickle", "rb") as file_handle:
#     res = pickle.load(file_handle)
#     print(res)  # display the output
# =======================================================
# class Student:
#     # Constructor - non parameterized
#     def __init__(self):
#         print("This is non parametrized constructor")
#
#     def show(self, name):
#         print("Hello", name)
#
#
# student = Student()
# student.show("John")
# ===========================
# def myfunc():
#   x = 300
#   print(x)
#
# myfunc()
# print(x)
# ================================
# # Python program to create a class having a method called distance
#
# class Distance(object):
#   def __init__(self, x=0, y=0):
#     self.x = x
#     self.y = y
#
#   def distance(self):
#     """Finding the distance of point_ from the origin"""
#     return (self.x ** 2 + self.y ** 2) ** 0.5
# =================================
# str = "Rohan"
# str2 = "ab"
# # Calling function
# str2 = str.join(str2)
# # Displaying result
# print(str2)
# ===========================
# for k in range(1):
#     for i in range(1):
#         for j in range(1,10):
#             print("inside loop")
#             break
#             print('after llop')
#         print("sec loop")
#     print("main loop")
# print("oustide loop")
# =================================================
# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#
#
# gen = my_generator()
# for value in gen:
#     print(value)
# =================================================
# list1 = [10, 11, 22, 121, 123, 154, 515]
# dict1 = {}
# for i in list1:
#     if str(i) == str(i[::-1]):
#         dict1.update({i:"palindrome"})
#     else:
#         dict1.update({i:'not-palindrome'})
# ===================================================
# para = """hi my name is Hrishikesh my mother's name is Kirti"""
# mydict={}
# ws = para.split()
# for i in ws:
#     mydict.update({i:ws.count(i)})
# print(mydict)
# ==================================================
# para = """hi my name is Hrishikesh my mother's name is Kirti"""
# ws = para.split()
# list1=[]
# # print(ws)
# for i in ws:
#     list1.append(i.upper())
# jlist=" ".join(list1)
# ==================================================
para = """hi my name is Hrishikesh my mother's name is Kirti"""
ws = para.split()
list1=[]
# print(ws)
for i in ws:
    list1.append(i.lower())
jlist=" ".join(list1)
# =======================================================
# para="""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
# when an unknown printer took a galley of type and scrambled it to make a type specimen book.
# It has survived not only five centuries, but also the leap into electronic typesetting,
# remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like
# Aldus PageMaker including versions of Lorem Ipsum."""
# cnt=0
# for i in para:
#     if i == "\n":
#         cnt+=1
# print(cnt+1)
# ==========================================
# para = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
# when an unknown printer took a galley of type and scrambled it to make a type specimen book.
# It has survived not only five centuries, but also the leap into electronic typesetting,
# remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like
# Aldus PageMaker including versions of Lorem Ipsum."""
# ws = para.split()
# print(ws)
# # fl = input("Enter the character:")
# for i in ws:
#     if i[0] == 'L':
#         print(i)

# ==========================================
# para = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
# when an unknown printer took a galley of type and scrambled it to make a type specimen book.
# It has survived not only five centuries, but also the leap into electronic typesetting,
# remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like
# Aldus PageMaker including versions of Lorem Ipsum."""
# ws=para.split()
# mylist=[]
# for i in ws:
#     if i[-1]=='m':
#         mylist.append(i)
# print(mylist)
# ==========================================
# para = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
# when an unknown printer took a galley of type and scrambled it to make a type specimen book.
# It has survived not only five centuries, but also the leap into electronic typesetting,
# remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like
# Aldus PageMaker including versions of Lorem Ipsum."""
# ws = para.split()
# mylist = []
# for i in ws:
#     if 'a' in i or 'A' in i or 'e' in i or 'E' in i or 'i' in i or 'I' in i or 'o' in i or 'O' in i or 'u' in i or 'U' in i:
#         mylist.append(i)
# print(mylist)
# ==========================================
# para = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
# when an unknown printer took a galley of type and scrambled it to make a type specimen book.
# It has survived not only five centuries, but also the leap into electronic typesetting,
# remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like
# Aldus PageMaker including versions of Lorem Ipsum."""
# ws = para.split()
# mylist = []
# for i in ws:
#     if 'a' not in i and 'A' not in i and 'e' not in i and 'E' not in i and 'i' not in i and 'I' not in i and 'o' not in i and 'O' not in i and 'u' not in i and 'U' not in i:
#         mylist.append(i)
# print(mylist)
# ================================
# para = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
# when an unknown printer took a galley of type and scrambled it to make a type specimen book.
# It has survived not only five centuries, but also the leap into electronic typesetting,
# remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like
# Aldus PageMaker including versions of Lorem Ipsum."""
# mylist = []
# mylist2 = []
# for i in para:
#     mylist.append(i)
# # print(mylist)/
# for i in mylist:
#     if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z' or i == " ":
#         mylist2.append(i)
# str1 = "".join(mylist2)
# print(str1)
