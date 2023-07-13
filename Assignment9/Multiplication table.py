# Print multiplication table from 1 to 10
n = int(input("Enter the number:"))
for i in range(1, n + 1):
    for j in range(1, 11):
        print(f"{i}X{j}={i * j}", end="\n")
    print()
