l = [int(x) for x in input("Enter the nos:").split()]
n = int(input("Enter the location to insert the element:"))
n1 = int(input(f"Enter the element at {n} index:"))
l.insert(n, n1)
print(l)
