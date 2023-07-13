sum = 0
l = [int(x) for x in input("Enter nos:").split()]
for i in l:
    if i % 3 == 0 and i % 5 == 0:
        sum += i
print(sum)
