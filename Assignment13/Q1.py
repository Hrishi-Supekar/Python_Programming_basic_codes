# Convert uppercase to lowercase and vice versa using map function
names = ['john', 'BLAKE', 'SCOTT', 'joe', 'peter', 'TONY']


def fun(n):
    if n.isupper():
        return n.lower()
    else:
        return n.upper()


print(list(map(fun, names)))
