# Number Guessing Game:
# Guessing chances = 5
# chance number while giving ans
import random
#

# r_n = 43
# print(r_n)
#
# for i in range(1, 6):
#     n = int(input("Enter the number between 1 -50 to check:"))
#     if n == r_n:
#         print(f"Congratulation you have guessed the number correct in {i} chances!!!!")
#         break
#     elif n in range(1, 11):
#         print("The number is far away!!")
#     elif n in range(11, 21):
#         print("The number is far away!!")
#     elif n in range(21, 31):
#         print("You are little closer to number !!")
#     elif n in range(31, 41):
#         print("Your number is closer to number!!")
#     elif n in range(41, 51):
#         print("Your number very close to number!!!")
# else:
#     print("Sorry you have Lost the Game!!!")
# ============================================With Random_gen============================================================================
r_n = random.randrange(1, 50)
print(r_n)

for i in range(1, 6):
    n = int(input("Enter the number between 1 -50 to check:"))
    if n == r_n:
        print(f"Congratulation you have guessed the number correct in {i} chances!!!!")
        break
    elif r_n in range(1, 10) and n in range(1, 10):
        if r_n in range(1, 3) and n in range(1, 3):
            print("The number is very close to number!!!")

        print("The number is far away!!")
    elif r_n in range(11, 20) and n in range(11, 20):
        print("The number is far away!!")
    elif r_n in range(21, 30) and n in range(21, 30):
        print("You are little closer to number !!")
    elif r_n in range(31, 40) and n in range(31, 40):
        print("Your number is closer to number!!")
    elif r_n in range(41, 50) and n in range(41, 50):
        print("Your number very close to number!!!")
else:
    print("Sorry you have Lost the Game!!!")
