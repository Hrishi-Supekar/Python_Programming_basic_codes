# WAP accept BasicSalary from user,
# if BS>=10000 then HRA - 10% of BS & TA - 5% of BS & Bonus-15000
# otherwise HRA - 1500 & TA - 2000 & bonus-1000
# find out net salary - BS+HRA+TA+bonus

BS = int(input("Enter the basic salary of employee:"))
if BS >= 10000:
    HRA = 0.1 * BS
    TA = 0.05 * BS
    bonus = 15000
    NS = BS + HRA + TA + bonus
else:
    HRA = 1500
    TA = 2000
    bonus = 1000
    NS = BS + HRA + TA + bonus
print(f"The net salary of employee is {NS}")
