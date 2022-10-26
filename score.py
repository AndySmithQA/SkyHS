score = int(input("Enter your score: "))
if score > 100 or score < 0:
    print("That was invalid")
else:
    if score > 90:
        print("You got an A*")
    elif score > 80:
        print("You got an A")
    elif score > 70:
        print("You got a B")
    elif score > 60:
        print("You got a C")
    elif score > 50:
        print("You got a D")
    elif score > 40:
        print("You got a E")
    else:
        print("You Failed")

