str1 = "Hello this is Hrishikesh Supekar"
mydict = {}
for i in str1:
    if i == " ":
        continue
    # elif i == i.upper():
    elif i.isupper():
        mydict.update({i: i})
    else:
        mydict.update({i: i.upper()})

print(mydict)
