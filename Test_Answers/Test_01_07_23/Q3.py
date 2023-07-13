# 3.Find all the numbers from 1-1000 that have a 3 in them using list comprehension.
n = int(input("Enter the number:"))
list1 = []
for i in range(1, n + 1):
    list1.append(str(i))
mylist = [int(x) for x in list1 if '3' in x]
print(mylist)
