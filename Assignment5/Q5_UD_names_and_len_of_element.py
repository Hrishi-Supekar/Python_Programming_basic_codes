# Add UD names in list and whose len >= 4 add this element in A-list and remaining name in B-list
l = [x for x in input("Enter the names:").split()]
Alsit = []
Blist = []
for i in l:
    if len(i) >= 4:
        Alsit.append(i)
    else:
        Blist.append(i)
print(Alsit)
print(Blist)
