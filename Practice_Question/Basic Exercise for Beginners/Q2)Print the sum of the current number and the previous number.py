# 2: Print the sum of the current number and the previous number
# x=0
# print(f"Current Number {x} Previous Number {x} Sum: {x}")
# for i in range(1,10):
#     print(f"Current Number {i} Previous Number {i-1} Sum: {i+(i-1)}")
# ========================OR==========================
x = 0
for i in range(10):
    print(f"Current Number {i} Previous Number {x} Sum: {i + x}")
    x = i
