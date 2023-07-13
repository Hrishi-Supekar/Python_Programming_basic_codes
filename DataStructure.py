# There are four collection data types in the python programming lang:
# 1.List--is a collection which is ordered and changeable(MUTABLE).Allows duplicate members.
# 2.Tuple--is a collection which is ordered and unchangeable(IMMUTABLE).Allows duplicate members.
# 3.Set--is a collection which is ordered and unindexed.No duplicate members allowed.
# 4.Dictionary--is a collection which is unordered and changeable(MUTABLE),indexed.
# No duplicate members(key) but values can be duplicate.It is key:value pair structure
# -----------------------------------------------------------------------------------------------------------------
# 1.List:
# fruits = ["Apple", "Banana", "Cherry", "Mango"]
# print(fruits[2])
# print(fruits[1])
# print(fruits[-1])
# fruits[3] = "Kiwi" # will change the value at 3rd index and will replace the element with old element
# print(fruits)
# print(fruits[::-1])  # reverse the list
# print(fruits[-1])
# print(fruits[0:2])  # slicing of list

# mixed_list = [1, 20, 30.4, True, "Welcome", 't']  # Mixed type list
# print(mixed_list[4])
# print(mixed_list[2:])  # start from 2 and till end index
# print(mixed_list[:5])  # start from 0th index and till 4th index(end not considered)


# fruits = ["Apple", "Banana", "Cherry", "Mango"]
# fruits.append("Orange") #appends the element at end of the list
# print(fruits)
# fruits.insert(2,"Kiwi") #insert the element at mentioned index and moves the later elements further.
# print(fruits)
# fruits.remove("Banana") #removes the mentioned element.
# print(fruits)
# fruits.pop(2) #removes the element mentioned at particular index
# print(fruits)
# del fruits[0] #removes the element mentioned at particular index
# print(fruits)
# del fruits #removes all elements from the list
# print(fruits) # gives the error if we print the list
# list1 = []
# list1 = fruits.copy()  # copies all content from fruits to list1.
# print(fruits)
# print(list1)
# list2 = ['A', 'B', 'C']
# list3 = list2 + fruits  # Joins two list elements the second list elements will be appended to the first list
# print(list3)

# in keyword in list--
# if 'Kiwi' in fruits:  # tells us if the element is present in the list or not
#     print("Present")
# else:
#     print("Not Present!!")

# Loop through list:
# for x in fruits:
#     print(x)    # to print element in the new line

# for x in fruits:
#     print(x, end=" ")  # use end=" " to loop the list and print list elements in single line

# for x in range(0, len(fruits)):  # by using range function but it req len() to mention end index
#     print(fruits[x])

# Addition of all list elements:
# l = [10, 24, 34, 46, 86, 43, 56, 89, 15, 69]
# sum = 0
# for x in l:
#     sum = sum + x
# print(sum)

# Addition of all even elements and odd elements:
# l = [10, 24, 34, 46, 86, 43, 56, 89, 15, 69]
# esum = 0
# osum = 0
# for x in l:
#     if x % 2 == 0:
#         esum += x
#     else:
#         osum += x
# print("Even number addition:", esum)
# print("Odd number addition:", osum)


# Addition of user defined range nos-
# n1,n2=[int(x) for x in input("Input start,end range:").split()]
# for x in range(n1,n2+1):
#     print(x,end=" ")

# Addition of user defined range nos but user defined n1 larger than n2-
# n1,n2=[int(x) for x in input("Input start,end range:").split()]
# if n1<n2:
#     for x in range(n1,n2+1):
#         print(x,end=" ")
# else:
#     for x in range(n2,n1+1):
#         print(x,end=" ")


# To print factorial of given number:
# n = int(input("Enter the number to check factorial:"))
# fact = 1
# for x in range(n, 0, -1):
#     fact = x * fact
# print("Factorial of given number is:", fact)

