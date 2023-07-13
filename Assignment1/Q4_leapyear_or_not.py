# WAP to check given year is leap year or not
year = int(input("Enter the year to check:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"The year {year} is leap year!!!")
else:
    print(f"The year {year} is not leap year!!!")
