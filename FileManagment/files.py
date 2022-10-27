# f = open("new.txt", "a")
# name = input("Enter your name")
# f.write(name)
# f.write(",")
# last = input("Enter your Last name")
# f.write(last)
# f.write(",")
# age = int(input("Enter your age"))
# agestr = str(age)
# f.write(agestr + "\n")
#
# lines = ["this is one line,\n","This is another,\n"]
# f.writelines(lines)
#
# f.close()

# f = open("dvla.txt", "r")
# lines = f.readlines()
# target = input("Enter Reg").upper()
# for line in lines:
#     car = line.strip("\n")
#     car = car.split(",")
#     reg = car[0]
#     name = car[1]
#     address = car[2:5]
#     if reg == target:
#         print("File found")
#         print(f"The register owner of {reg} is"
#               f" {name}")
#         print(f"lives at {address}")
#
# f.close()

with open("dvla.txt", "r") as f:
    pass




