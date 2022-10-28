class Person:
    uniqueID = 0
    def __init__(self, name):
        self._name = name
        Person.uniqueID += 1

    def __str__(self):
        return f"{self._name} ID: {self.uniqueID}"

class Employee(Person):
    empID = 0
    def __init__(self, name, dep):
        super().__init__(name)
        self._dep = dep
        Employee.empID += 1

    def __str__(self):
        return f"{self._name} ID: {self.empID} Dep: {self._dep}"


class InsufficientFundError(Exception):
    pass

class Cust(Person):
    def __init__(self, name, initial):
        super().__init__(name)
        self._balance = initial

    def getbalance(self):
        return f"Your balance is: £{self._balance}"

    def deposit(self, amt):
        self._balance += amt
        return f"You added £{amt}. Your new Balance £{self._balance:5.2f}"

    def withdraw(self, amt):
        try:
            new = self._balance - amt < 0
            if new:
                raise InsufficientFundError("You Do not have enough Money")
        except InsufficientFundError as err:
            print("Oooops", err)
        else:
            self._balance -= amt

        return f"Balance: £{self._balance}"

jill = Cust("Jill", 6700)

print(jill.getbalance())
print(jill.withdraw(8000))
print(jill.withdraw(800))
