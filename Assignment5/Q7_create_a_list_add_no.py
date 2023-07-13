# create a list and add numbers in list. then create 2 different list that is square
# and cube list if number is even then add in square list and number is odd then add in cube list and
# perform square of even no and cube of odd number\

l = [int(x) for x in input("Enter the numbers:").split()]
sqlist = []
cubelist = []
for i in l:
    if i % 2 == 0:
        sqlist.append(i * i)
    else:
        cubelist.append(i * i * i)
print(sqlist)
print(cubelist)
