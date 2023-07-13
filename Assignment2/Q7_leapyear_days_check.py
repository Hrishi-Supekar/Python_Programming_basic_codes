# To ask user that how many days in a leap year.
# a. if user will get correct ans -
# then print "You have cleared the first level" and ask again another que
# "What month has an extra day in leap year?" if user will get correct answer
# then display message "Congratulations !!You have cleared the test" otherwise "You have failed the test".
# b.otherwise print following msg-
# "Your input is wrong, please try again."
# ---------------------------------------------------------------------------------------------------------------

ans = int(input("How many days are there in a leap year:"))
if ans == 366:
    print("You have cleared the first level!!!")
    day = int(input("Which month has an extra day in leap year\n"
                    "1.Jan\n2.Feb\n3.Mar\n4.Apr\n5.May\n6.Jun\n7.Jul\n8.Aug\n9.Sep\n10.Oct\n11.Nov\n12.Dec\n"))
    if day == 2:
        print("Congratulations !!You have cleared the test!!!")
    else:
        print("You have failed the test!!!")
else:
    print("Your input is wrong, please try again.")
