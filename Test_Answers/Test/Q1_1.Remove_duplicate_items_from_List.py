# 1.Remove duplicate items from List.
l = [23, 43, 45, 65, 88, 98, 90, 87, 23, 43, 65, 90]
l2 = []
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)
