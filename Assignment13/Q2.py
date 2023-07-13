# Return a list with element which are palindrome
names = ['john', 'otto', 'SCOTT', 'mom', 'peter', 'TONY','ava']


def palindrome(n):
    if n == n[::-1]:
        return n


print(list(filter(palindrome, names)))
