# 13: Print multiplication table form 1 to 10
n = int(input("Enter the number:"))
for i in range(1,n+1):
    # print(i)
    for j in range(1,11):
        print(j*i,end=" ")
    print()
