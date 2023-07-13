# Create a list within list of sq & cube of element from list
num = [2, 3, 4, 5, 7, 8, 23, 45, 76]


def cube_sq(n):
    l = [n ** 2, n ** 3]
    return l


print(list(map(cube_sq, num)))
