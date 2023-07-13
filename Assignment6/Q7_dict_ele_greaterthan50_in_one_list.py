# Separate value from dict which have value greater than 50 & less than 50
marks = {"a": 56, "b": 78, "c": 90, "d": 23, "e": 45, "f": 100, "g": 67}
mylist = []
mylist1 = []
for i in marks.values():
    if i > 50:
        mylist.append(i)
    else:
        mylist1.append(i)
print(mylist)
print(mylist1)
