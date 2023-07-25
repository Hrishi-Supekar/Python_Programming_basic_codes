# # Print second-highest number without using built-in function
# l = [10, 23, 35, 76, 2, 75, 78, 54, 24, 45, 785, 325]
# for x in range(0, len(l)):
#     for y in range(x + 1, len(l)):
#         if l[x] < l[y]:
#             temp = l[x]
#             l[x] = l[y]
#             l[y] = temp
#
# print(f"The second-highest number in list: {l[1]}")
#
# =======================================================================
# Occurrence of every character in string
# para = '''Python is a high-level, general-purpose programming language.
#         Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule.
#         Python is dynamically typed and garbage-collected.
#         It supports multiple programming paradigms, including structured (particularly procedural),
#         object-oriented and functional programming. It is often described as a "batteries included"
#         language due to its comprehensive standard library'''
# mydict = {}
# for i in para:
#     cnt = para.count(i)
#     mydict.update({i: cnt})
# print(mydict)

# OR
str="Hello this is hrishikesh"
mySet = set(str)
# print(mySet)
mydict = {}
for x in mySet:
    cnt = 0
    for i in str :
        if i == x:
            cnt += 1
    mydict[x] = cnt
print("Count of characters is:\n", mydict)
