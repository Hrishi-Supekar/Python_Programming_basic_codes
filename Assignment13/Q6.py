# Return a list with elements which are only divisible by 3 & 5 both
l = [4, 5, 6, 7, 8, 32, 12, 15, 20, 23, 30, 45]

# def div_3_or_5(x):
#     return x % 3 == 0 and x % 5 == 0
# print(list(filter(div_3_or_5, l)))

print(list(filter(lambda x: x % 3 == 0 and x % 5 == 0, l)))
