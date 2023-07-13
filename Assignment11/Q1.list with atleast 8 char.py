# 1.Write a list comprehension that builds a list containing only the names with at least 8 char.
l = ["hrishikesh", "supekar", "hello", "worldwideweb", "alisha"]
print(l)
char_list = [x for x in l if len(x) >= 8]
print(char_list)

