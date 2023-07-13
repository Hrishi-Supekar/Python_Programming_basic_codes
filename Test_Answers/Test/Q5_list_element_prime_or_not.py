# 5.Write a Python program to check if each number is prime in a
# given list of numbers then create prime number dictionary.

l = [42, 54, 65, 13, 23, 17, 34, 45, 76, 11, 67]
d = {}
for i in l:
    cnt = 0
    for x in range(2, i // 2):
        if i % x == 0:
            cnt = 1
    if cnt == 0:
        d.update({i: "isPrime"})
    else:
        d.update({i: "isNotPrime"})
print(d)
