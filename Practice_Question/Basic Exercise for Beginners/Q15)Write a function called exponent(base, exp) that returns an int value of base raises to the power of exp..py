# 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
base = int(input("Enter the base number:"))
exp = int(input("Enter the exponent:"))


def exponent(base, exp):
    p = 1
    if exp > 0:
        for i in range(exp):
            p = p * base
    else:
        return "The value of exponent is -ve\nPlease enter +ve value"
    return p


print(exponent(base, exp))
