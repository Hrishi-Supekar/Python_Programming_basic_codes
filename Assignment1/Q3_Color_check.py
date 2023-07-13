# WAP to enter any char from user and print corresponding color names
name = input("Enter the character:")
if name == 'y' or name == 'Y':
    print("The color is yellow!!")
elif name == 'b' or name == 'B':
    print("The color is Blue or Black!!")
elif name == 'r' or name == 'R':
    print("The color is Red!!")
elif name == 'p' or name == 'P':
    print("The color is Pink!!")
else:
    print("Enter the correct char")
