# # valid = "no"
# # while valid == "no":
# #     userin = input("Enter a number above 10")
# #     if userin.isnumeric():
# #         valueCheck = int(userin)
# #         if valueCheck < 10:
# #             print("That number was less than 10")
# #             valid = "no"
# #         else:
# #             print("Thank you")
# #             valid = "yes"
# #     else:
# #         print("Not a number")
# #         valid = "no"
# #
# #
# # mylist = ["Dave", "dave", "frank"]
# #
# # if "andy" in mylist:
# #     print("Andy is there")
# # else:
# #     print("There was no andy")
# #
# # uppers = 0
# # lowers = 0
# # nums = 0
# #
# # pw = "LetmeIn"
# #
# # for chars in pw:
# #     if chars.isupper():
# #         uppers += 1
# #     elif chars.islower():
# #         lowers += 1
# #     elif chars.isnumeric():
# #         nums += 1
# #     elif chars in sym:
# #         syms += 1
# #     else:
# #         print(f"{chars} is not a valid character")
#
# # if uppers < 1:
# #     print("You have not included Caps")
# #
# #
# #
# #
# # word = "walrus"
# #
# # if "W" not in word:
# #     print("no capital W")
# #
#
# complete = "no"
# while complete == "no":
#     pw = input("enter Password")
#     if len(pw) < 8:
#         print("Password must be between 8 and 20 characters")
#         complete = "no"
#     else:
#         for chars in pw:
#             if chars.isupper():
#                 uppers += 1
#             elif chars.islower():
#                 lowers += 1
#             elif chars.isnumeric():
#                 nums += 1
#             elif chars in sym:
#                 syms += 1
#             else:
#                 print(f"{chars} is not a valid character")
#                 invalid += 1
#                 invalidChars.append(chars)
#         complete = "yes"
#
# if uppers < 1:
#     print("You have not included Caps")
#
#
#
# print(" A While Loop")
# loops = 0
# while loops < 5:
#     print("This is loop", loops)
#     loops += 1

#unconditional
# print(" A For Loop")
#
# for i in range(1, 11):
#     print(f"This is loop {i}")

# mylist = [7,"Andy",43,54,75,46,37]
#
# # for i in range(len(mylist)):
# #     print(mylist[i])
#
# # for i in mylist:
# #     if i.isalpha():
# #         print(i)
#
# for i in range(120):
#     if not i % 2 == 0:
#         print(f"{i} squared is {i*i}")

while True:
    input("Press Enter to continue")