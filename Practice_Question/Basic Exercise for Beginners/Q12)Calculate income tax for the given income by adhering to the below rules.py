# 12: Calculate income tax for the given income by adhering to the below rules
# Taxable Income    Rate (in %)
# First $10,000     0
# Next $10,000      10
# The remaining	    20

# Expected Output:
# # For example, suppose the taxable income is 45000 the income tax payable is
# # 10000*0% + 10000*10%  + 25000*20% = $6000.

n = int(input("Enter the income of employee:"))


def tax_calc(n1):
    tax = 0
    if n1 <= 10000:
        tax = 0
    elif n1 <= 20000:
        x = n1 - 10000
        tax = x * 0.1
    else:
        tax = 10000 * 0.1
        tax = tax + (n1 - 20000) * 0.2
    return tax


print(tax_calc(n))
