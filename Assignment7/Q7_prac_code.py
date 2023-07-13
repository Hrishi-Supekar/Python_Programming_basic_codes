# Q1.Enter the string from user for Ex=fiofadf314$%%RCNI8849#9928sgono
# and print count digits,uppercase,lower case and sp.symbol.
# msg = input("Enter the string with sp.char and numbers:")
# lcnt = 0
# ucnt = 0
# ncnt = 0
# ccnt = 0
# for i in msg:
#     if ord(i) >= 97 and ord(i) <= 122:
#         lcnt += 1
#     elif ord(i) >= 65 and ord(i) <= 90:
#         ucnt += 1
#     elif ord(i) >= 48 and ord(i) <= 57:
#         ncnt += 1
#     else:
#         ccnt += 1
# print(f"lowercase letter count is {lcnt}")
# print(f"Uppercase letter count is {ucnt}")
# print(f"Numbers count is {ncnt}")
# print(f"Special character letter count is {ccnt}")

# ---------------------------------------------------------------------------------------
# Q2.Enter any number from user and print number in word like 101== one zero one.
# n = input("Enter the number:")
# for i in n:
#     if i == "1":
#         print("one", end=" ")
#     elif i == '2':
#         print("Two", end=" ")
#     elif i == '3':
#         print("Three", end=" ")
#     elif i == '4':
#         print("Four", end=" ")
#     elif i == '5':
#         print("Five", end=" ")
#     elif i == '6':
#         print("Six", end=" ")
#     elif i == '7':
#         print("Seven", end=" ")
#     elif i == '8':
#         print("Eight", end=" ")
#     elif i == '9':
#         print("Nine", end=" ")
#     elif i == '0':
#         print("Zero", end=" ")

# ---------------------------------------------------------------------------------------
# Q3.Enter the string from user for ex. Str= oiafd3424(*&&()$)slkdng and remove special char and numbers form str.
# str = input("Enter the string:")
# mylist = []
# for i in str:
#     if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z' or i == " ":
#         # if ord(i) >= 97 and ord(i) <= 122 or ord(i) >= 65 and ord(i) <= 90:
#         mylist.append(i)
# str1 = "".join(mylist)
# print(str1)

# ---------------------------------------------------------------------------------------
# Q4.Create cube dict from existing list.
# l = [int(x) for x in input("Enter the number to add in list:").split()]
# # [print(x,end=" ") for x in l]
# mydict = {}
# for i in l:
#     mydict.update({i: i ** 3})
# print(mydict)
# ---------------------------------------------------------------------------------------
# Q5.Print the length of number without len() function.
n = input("Enter the number:")
cnt = 0
for i in n:
    cnt += 1
print(f"The length of number is {cnt}")
