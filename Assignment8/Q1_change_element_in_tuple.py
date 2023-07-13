# Change the specific element in given tuple
# user specify index & user specific value

t=(23,35,65,86,98,54,84,13)
# mylist=list(t)
# n=int(input("Enter the index:"))
# n1=int(input("Enter the value:"))
# print(mylist)
# for i in range(len(t)):
#     if i == n:
#         mylist.pop(i)
#         mylist.insert(i,n1)
# print(mylist)
# t=tuple(mylist)
# print(t)

mylist=list(t)
n=int(input("Enter the index:"))
n1=int(input("Enter the value:"))
mylist[n]=n1
t=tuple(mylist)
print(t)