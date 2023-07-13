# 9: Check Palindrome Number
n = int(input("Enter the number to check:"))


def check_palindrome(n1):
    n1 = str(n1)
    if n1 == n1[::-1]:
        print("Yes the given number is palindrome!!!")
    else:
        print("No the given number is not palindrome!!!")


check_palindrome(n)
