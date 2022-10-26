#conditional While

# loops = 0
# while loops < 1000:
#     print("This is a loop")
#     loops += 1
#
# print("End of loop")
#
#
# lives = 3
# while lives > 0:
#     play()
#     if collision:
#         lives -=1
# print("game over")
# import random
# score = 0
# lives = 3
# while lives > 0:
#     print(f"you have {lives} lives")
#     num1 = random.randint(0, 20)
#     num2 = random.randint(0, 20)
#     num3 = num1 + num2
#     print("What is", num1, "+", num2)
#     userans = int(input())
#     if userans == num3:
#         print("correct")
#         score += 1
#     else:
#         print("Incorrect")
#         lives -= 1
# print(f"you scored {score} points ")


valid = "no"
while valid == "no":
    userin = input("Enter a number")
    if userin.isnumeric():
        print("Thank you for a number")
        valid = "yes"
    else:
        print("That was not a number")
        valid = "no"

intconv = int(userin)
userchoice = intconv * 2
print("Your number doubled = ", userchoice)

print("Carry on ")


# loops = 1
# num = int(input("Enter a number"))
# while loops <= 12:
#     print(f"{num} * {loops} is {num*loops}")
#     loops += 1
#












#uncondtional For