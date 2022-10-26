import random

delegates = [
    "1: Barry",
    "2: Chithranghan",
    "3: Corey",
    "4: Daniel",
    "5: Harshil",
    "6: James",
    "7: Jamie",
    "8: Neil",
    "9: Nicola",
    "10: Robson",
    "11: Ryan",
    "12: Rosie",
    "13: Steven A",
    "14: Steven R",
    "15: Thomas",
    "16: William",
    "17: Anthony"
]

loop = 1
while len(delegates) > 2:
    del1 = random.choice(delegates)
    delegates.remove(del1)
    del2 = random.choice(delegates)
    delegates.remove(del2)
    del3 = random.choice(delegates)
    delegates.remove(del3)
    print(f"Group {loop} is {del1} and {del2}"
          f" and {del3}")
    loop += 1
print(f"Which leaves pair 6 {delegates[0:2]}" )
