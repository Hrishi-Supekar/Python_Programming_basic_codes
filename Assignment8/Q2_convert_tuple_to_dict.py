t = (23, 35, 65, 86, 98, 54, 84, 13)
mydict = {}
for i in range(0, len(t)):
    mydict.update({i: t[i]})
print(mydict)
