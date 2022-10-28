##oop is aboput creating and managing data
## create objects - collections on data we can to things to

class Person:

    uniqueID = 0

    def __init__(self, name, age):
        self._name = name
        self._age = age
        Person.uniqueID += 1

    def __str__(self):
        return f"{self._name} Age: {self._age} years old" \
               f" ID: {self.uniqueID}"

per1 = Person("Andy",41)
print(per1)


class Account:
    accountID = 0
    def __init__(self, initial):
        self._balance = initial
        Account.accountID += 1

    def getbalance(self):
        return f" Your balance is: £{self._balance}"

    def deposit(self, amt):
        self._balance += amt
        return f"You added £{amt}. Your new Balance £{self._balance:5.2f}"

    def withdraw(self, amt):
        self._balance -= amt
        return f"You Withdrew £{amt}. Your new Balance £{self._balance}"

jill = Account(4690)

print(jill.deposit(6534))
print(jill.withdraw(45654560))

dave = Account(100)
print(dave.accountID)

#
# class Vehicle:
#     def __init__(self,wheels,make):
#         self._wheels = wheels
#         self._make = make
#
#     def __str__(self):
#         return f"{self._make} has: {self._wheels} wheels"
#
