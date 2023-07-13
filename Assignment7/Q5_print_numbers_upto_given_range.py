# If the number is divisible by 3 == Fizz
# & number divisible 5 == Buzz and num divisible by both then print FizzBuzz
n = int(input("Enter the number :"))
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}==FizzBuzz")
    elif i % 3 == 0:
        print(f"{i}==Fizz")
    elif i % 5 == 0:
        print(f"{i}==Buzz")
    else:
        print(i)
