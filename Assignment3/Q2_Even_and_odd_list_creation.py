l = [12, 43, 54, 57, 321, 65, 86, 42, 87, 45, 48, 14, 47, 85]
elist = []
olist = []

for x in l:
    if x % 2 == 0:
        elist.append(x)
    else:
        olist.append(x)

print(f"The original list is:", l)
print(f"The even list is:", elist)
print(f"The odd list is:", olist)
