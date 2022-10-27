import random
lotto = set()

while len(lotto) < 6:
    num = random.randint(1, 51)
    lotto.add(num)

print("Lotto Numbers =",lotto)