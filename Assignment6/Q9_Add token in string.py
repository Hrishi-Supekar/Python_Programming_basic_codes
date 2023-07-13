# msg = "asfgwwf234#4%^$sdfpj^%RFG" #use ord() and chr() for ascii
# add token in the string where number and special symbol are there
a = "Hell1o, W2or4ld!"
token = "KI$%^"
mylist1 = []
str1 = ""
mylist = list(a)
print(mylist)
for i in mylist:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        # if ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122:
        mylist1.append(i)
    if i >= '0' and i <= '9':
        # if ord(i) >= 48 and ord(i) <= 57:
        mylist1.append(token)
    # else:
    #     mylist1.append(token)
print(mylist1)
str1 = "".join(mylist1)
print(str1)
