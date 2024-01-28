from abc import ABC, abstractmethod
#Problem1
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance #Encapsulated

        def get_balance(self):
            return self._balance
        def set_balance(self, new_balance):
                self._balance = new_balance
        def withdraw(self, balance):
            if new_balance > 0:
                self._balance = new_balance
Bank = BankAccount("333333", 333,333)

Bank.withdraw()

#Problem2
class Vehicle(ABC):
    @abstractmethod
    def Car(self):
        pass

class start_engine(Vehicle)
    def __init__(self, activator):
        self._activator = activator

        def Car(self):
            return print("The Car is Activated")

class stop_engine(Vehicle):
    def __init__(self, deactivator):
        self._deactivator = deactivator

        def Car(self):
            return print("The Car is Deactivated")
class drive(Vehicle):
    def __init__(self, operate):
        self._operate = operate

        def Car(self):
            return print("The Car is Operating")
#Problem3
class Restraunt:
    def __init__(self, order, price):
        self.order = order
        self._price = price #Encapsulated

        def get_price(self):
            return self._price
        def set_price(self, new_price):
            if new_balance > 0:
                self._price = new_price
        
Sum = Restraunt("pasta", 11)

Sum.withdraw()
