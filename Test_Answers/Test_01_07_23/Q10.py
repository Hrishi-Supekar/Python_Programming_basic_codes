# 10.Remove Negative Elements in List.
mylist=[int(x) for x in input("Enter the number:").split()]
copy_list=mylist
for i in copy_list:
    if i < 0:
        mylist.remove(i)
print(mylist)
