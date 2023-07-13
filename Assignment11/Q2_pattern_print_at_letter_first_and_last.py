# 2.Add % in front and end of every single word in a given string for ex.
# "Harry is good boy" == "%Harry% %is% %good% %boy%" like this in LC(List comprehension)

msg="Hello this is hrishikesh supekar"
l=[f"%{x}%" for x in msg.split()]
x=" ".join(l)
print(x)
