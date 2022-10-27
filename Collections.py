# mynum = [45,55,34,8,3.14,5,754]
#
# print(f"min: {min(mynum)}")

# mydict = {
#     'fred': 3,
#     'jim': 8,
#     'dave': 42
# }
# # print(f"Min of myDict {max(mydict)}")
#
# a = 4
# b = 6
#
# a, b = b, a
# print(a,b)

# one, two, three = range(3)
# print(one, two, three)
#
# mytup = ('a', 'b', 'c')
#
# mylist = list(mytup)
# print(mylist)
# another = mytup * 4
# print(another)
#
# greeting = 'hello',
# print(type(greeting))
#
# string = 'The quick brown'
#
# print(string[2:4])
#
# mynum = [45, 55, 34,8,3.14,5,754]
# #
# # print(mynum[1:3])
# # print(mynum[:-2])
# # print(mynum[2:])
#
# del mynum[2:5]
# print(mynum)

# import random
# cho = random.randint(0, 7)
# print(mynum[cho])
#


#
# runners = [
#     ["Bob",45,60,72],
#     ["Jim",45,62,74]
# ]
#
# #enumList = enumerate(runners)
# for i in runners:
#     print(f"{i[0]} Lap times: {i[1:4]}")

# mytup = ('eggs', 'bacon', 'beans', 'toast','saus')
#
# x, y, *z = mytup
# print(x,y,z)
#
# t1 = ('cats', 'dogs', 'snakes', 'mice', 'camels')
# t2 = ('kelp', 'crab', 'lobster', 'fish')
#
# for a, *b, c in t1, t2:
#
#


# # myList[:0] = ["Newcastle","Palace"]
# # myList.append("Leeds")
# # myList.extend(["Everton"])
# # myList += ["Man U"]
# # mystr = "Dave"
# # mystr += " Smith"
#
# myList.insert(2,"Tottenham")
# myList[2:2] = ["Burnley", "Leicester"]
#
# myList[3] = "hdgfjhsg"
# print(myList)
# myList.pop(0)
# print(myList)
# print(myList.pop())
# print(myList)

#myList = ["Liverpool", "Man City", "Man U", "Norwich"]
# myNum = input("Enter a numebr")
#
# try:
#     float(myNum)
# except ValueError:
#     print("Not A number")

# mynum = [45, 55, 34,8,3,5,754, 55]
# print(mynum.count(55))
#
# print(mynum.index(55))
#
# mynum.reverse()
# print(mynum)
#
# mySet = {23,4,74,5,75,8,3,9}
# print(mySet)
#
# mynewset = set([2,5,7,9,10])
# print(mynewset)
#

s4 = {23, 42, 66, 123,56,66,34}
s5 = {56,27,42}
print(s4)

s4.remove(123)
s5.add(123)
print("{:02d} {:02d}".format(s4,s5))

