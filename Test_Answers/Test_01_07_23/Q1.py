# 1. Find all the words in a string that are less than 4 letters using List comprehension.
# sample list -

str = "My name is hrishikesh supekar i am studying python"
mylist = [x for x in list(str.split()) if len(x) > 4]
print(mylist)
