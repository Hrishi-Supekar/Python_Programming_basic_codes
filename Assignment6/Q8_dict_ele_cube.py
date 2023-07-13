# Print cube of values dict from list element
mylist = [3, 4, 5, 6, 7, 8, 9]
cubedict = {}
for i in mylist:
    cubedict.update({i: (i ** 3)})
print(cubedict)
