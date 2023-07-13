n = input("enter the number:")
esum = 0
osum = 0
for i in n:
    if int(i) % 2 == 0:
        esum += int(i)
    else:
        osum += int(i)
print(f"Even digit addition={esum} & odd digit addition={osum}")
