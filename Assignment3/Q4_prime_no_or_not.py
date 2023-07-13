n = int(input("Enter the number:"))
cnt = 0
for x in range(2, n):  # use half of num to run the loop as we will get the factors till half.
    if n % x == 0:
        cnt = 1
if cnt == 0:
    print("The number is prime number!!")
else:
    print("The number is not prime number!!!")
