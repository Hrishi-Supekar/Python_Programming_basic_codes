# WAP to print area of trianlge,rectangle,circle,square

s = int(input("Enter the side of square:"))
l, w = [int(x) for x in input("Enter the length and width of rect:").split()]
r = float(input("Enter the radius of circle:"))
b, h = [int(x) for x in input("Enter the base and height of triangle:").split()]
pi = 3.14
triarea = 0.5 * b * h
rectarea = l * w
circlearea = pi * r ** 2
squarearea = s * s
print()
print(f"Area of Traingle is {triarea}")
print(f"Area of Rectangle is {rectarea}")
print(f"Area of Square is {squarearea}")
print(f"Area of Circle is {circlearea}")
