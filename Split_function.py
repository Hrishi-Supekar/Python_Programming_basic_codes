# How to take more than one value using single input using split function

# a,b,c=input("Enter the values:").split() #Used to split the input and assign it in variable(The delimiter is space).
# print(a,b,c)
#
# h,i,j=int(input("Enter the values:").split(",")) #Used to split the input and assign it
# in variable(The delimiter is comma).
# print(h,i,j)


a, b, c = [int(x) for x in input("Enter the values").split()]
print(a, b, c)
print(a + b + c)
