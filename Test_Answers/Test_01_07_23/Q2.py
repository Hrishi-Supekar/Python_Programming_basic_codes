# 2.Count the number of spaces in a string using list comprehension.
# str="Python is high level programming language"

str = "Hello this is hrishikesh supekar and i am learning python language."
list1 = [x for x in list(str) if x == " "]
print(list1.count(" "))
