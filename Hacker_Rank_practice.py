# list1=[]
# n=int(input("range"))
# for j in range(n):
#         x=int(input("Enter choice"))
#         if x == 1:
#             i=int(input("index"))
#             e=int(input("element"))
#             list1.insert(i,e)
#         elif x == 2:
#             print(list1)
#         elif x == 3:
#             e=int(input("element"))
#             list1.remove(e)
#         elif x == 4:
#             e=int(input("element"))
#             list1.append(e)
#         elif x == 5:
#             list1.sort()
#         elif x == 6:
#             list1.pop()
#         elif x == 7:
#             list1.reverse()

#
# list1 = []
# N = int(input("x"))
# for j in range(N):
#     x, i, e = [a for a in input("y").split()]
#     if x == 'insert':
#         list1.insert(int(i), int(e))
#     elif x == 'print':
#         print(list1)
#     elif x == 'remove':
#         list1.remove(int(e))
#     elif x == 'append':
#         list1.append(int(e))
#     elif x == 'sort':
#         list1.sort()
#     elif x == 'pop':
#         list1.pop()
#     elif x == 'reverse':
#         list1.reverse()
b=[a for a in input("y").split()]
print(b)
print(len(b))