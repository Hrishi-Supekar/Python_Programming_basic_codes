# add user defined names in list and print names on output screen which has len greater than 4
l = [x for x in input("Enter the names:").split()]
for i in l:
    if len(i) > 4:
        print(i, end=" ")
