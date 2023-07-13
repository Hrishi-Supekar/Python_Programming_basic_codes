# 6: Display numbers divisible by 5 from a list
l = [int(x) for x in input("Enter the number:").split()]


def check_number_div_by_5(l1):
    for i in l1:
        if i % 5 == 0:
            print(i)


check_number_div_by_5(l)
