# 3: Print characters from a string that are present at an even index number
# msg = "This is hrishikesh supekar"
msg='pynative'
for i in range(len(msg)):
    if i%2==0:
        print(msg[i], end=" ")

