# Nested list -- list within list is known as nested list
# L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
#                        0     1
#             0    1        2
#   0   1            2                3   4
# print(L[0]) #a
# print(L[2])#['cc','dd',['eee','fff']]
# print(L[2][1])#dd
# print(L[2][2])#['eee','fff']
# print(L[2][2][1])#fff
# print(L[-3])#['cc','dd',['eee','fff']]

# NestedList operation:
# L[2].append('xx')  # The append operation adds item at end of list and not in middle so if there is nested list
# # it will be added at last in nested list

# L[2][2].append('yy')

# L[2].insert(1,'tt') # will insert at the specified index in list

# L[2].extend(['Hrishi', 'Omkar'])  # to add a new list in the existing list
# L.extend(['hello','Python','Programs'])
# L[2][2].extend(['Go','No'])

# x=L[2].pop(1)
# print(x)

# print(len(L))
# print(L)

# l = [[1, 2, 3], [4, 5, 6, [7, 8, 9]],[10,11]]
# print(l[0])
# for i in l:
#     print(i)

# for i in l[1]:
#     print(i)

# for i in l[1][3]:
#     print(i)

# for i in l:
#     for j in i:
#         print(j)

# Addition of list:
# l=[[1,2,3],[6,4,5],[9,7,8]]
# sum=0
# for i in l:
#     sum = 0
#     for j in i:
#         sum+=j
#     print(f"The sum of list {i}={sum}")

