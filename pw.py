valid = 'no'
while valid == 'no':
    u = 0
    l = 0
    s = 0
    n = 0
    password = input("Please enter a password: ")
    specials = "'[@_!#$%^&*()<>?/\|}{~:]"
    if len(password) >= 8:
        for char in password:
        # count each
            if char.islower():
                l += 1
            if char.isupper():
                u += 1
            if char in specials:
                s += 1
            if char.isnumeric():
                n += 1

        if l == 0:
            print("please include a lower case character")

        if u == 0:
            print("please include an upper case character")

        if s == 0:
            print("please include a special character")

        if n == 0:
            print("please include a number")

        if l > 0 and u > 0 and s > 0 and n > 0:
            print("Valid Password")

        again = input("Try another?")
        if again not in ("N", "n"):
            valid = "no"
        else:
            valid = "yes"

    else:
        print("Password not long enough")




print("Thank you - goodbye")