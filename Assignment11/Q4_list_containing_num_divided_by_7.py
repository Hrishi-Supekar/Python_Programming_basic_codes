# 4.Find all the numbers from 1-100 that are divided by 7 using LC.
l = [x for x in range(1, 101)]
# print(l)
list_div_7 = [x for x in l if x % 7 == 0]
print(list_div_7)
