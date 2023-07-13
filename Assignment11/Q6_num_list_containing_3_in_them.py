# 6.Find all the numbers from 1 to 100 that have 3 in them.
# l = [x for x in range(1, 101)]
# y = [x for x in l if x % 10 == 3 or int(x / 10) == 3]
y = [i for i in [x for x in range(1, 101)] if i % 10 == 3 or (i // 10) == 3]
print(f"The  list containing numbers that have 3 in them : {y}")
