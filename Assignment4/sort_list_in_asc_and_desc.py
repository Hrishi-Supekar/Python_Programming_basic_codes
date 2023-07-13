# l = [32, 43, 46, 76, 78, 8, 54, 32, 12, 62, 48, 69]
# l.sort()
# print("List in Asc order:", l)
# l.sort(reverse=True)
# print("List in Asc order:", l)

# ==UDF==
# Asc order:
l = [32, 43, 46, 76, 78, 8, 54, 3, 12, 62, 48, 69,6]
print(f"The list in Original order: {l}")
for x in range(0, len(l)):
    for y in range(x+1, len(l)):
        if l[x] > l[y]:
            temp = l[x]
            l[x] = l[y]
            l[y] = temp
print(f"The list in Ascending order: {l}")

#Desc Order:
l = [32, 43, 46, 76, 78, 8, 54, 3, 12, 62, 48, 69,6]
for x in range(0, len(l)):
    for y in range(x+1, len(l)):
        if l[x] < l[y]:
            temp = l[x]
            l[x] = l[y]
            l[y] = temp

print(f"The list in Descending order: {l}")
