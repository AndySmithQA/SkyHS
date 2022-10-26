# euro = "\u20aa"
# fourbyte = "\N{euro sign}"
# print(euro)
# print(fourbyte)

# chars_as_bytes = b"stores as bytes"
# print(chars_as_bytes)

# print("Hello", end="\t")
# print("World")

# mylist = [2,3,5,6,7]
# # for i in mylist:
# #     print(i, sep=": ")
#
# print(f"{mylist}, And this, and some more")

# print( '\r\n \1 \t\2\3 \45 ')
# print( r'\r\n \1\2\3')
#
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j)
#     print("\n")

# mystr = ("this will print 'single quotes'")
#
# mystr = mystr.replace("this", "That")
#
# print(mystr)
#
# # strip takes "\n"
#
# loc = mystr.find("pri")
# print(loc)
#
# print("repeat     " * 4)

# output = "Hi {0}, you are {1} years old".format("Andy", 41)
# print(output)

# planets = {
#     'Mercury': 57.91,
#     'Venus': 108.2,
#     'Earth': 149.597870,
#     'Mars': 227.94,
# }
# #
# for i, key in enumerate(planets.keys(), 1):
#     print("{:2d} {:<10s} {:06.2f} GM".format(i, key, planets[key]))
#


#print(planets['Venus'])


#
# text = 'hello'
#
# print(text.capitalize())
# print(text.upper())
# print('<'+text.center(12)+'>')
# print('<'+text.ljust(12)+'>')
# print('<'+text.rjust(12)+'>')
# print('<'+text.zfill(12)+'>')


# print(f"Planets contains {len(planets)} Planets")



# names = ["Tom", "Harry", "Jane", "Mary"]
# suffix = ["st", "nd", "rd", "th"]
#
# n = 2
#
# s = f"{str(n+1) + suffix[n]} of {len(names)} is {names[n]}"
# print(s)

# text = "The quick brown fox jumps blah"
# print(text[12:15])
# print(text[-7:-1])
#
# print(text[-7:])

# line = 'root::0:0:superuser:/root:/bin/sh'
# print(line)
# elems = line.split(':')
#
# elems[0] ='avatar'
# elems[4] = 'The Super-user'
#
# line = ':'.join(elems)
#
# print(line)
# print(type(line))
Belgium = 'Belgium,10445852,Brussels,737966,Eurpope,1830,Euro,Catholicism,Dutch,French,German'
print(Belgium)
print(f"{'-' * len(Belgium)}")
items = Belgium.split(',')
print(items)
print(':'.join(items))
print(int(items[1]) + int(items[3]))
