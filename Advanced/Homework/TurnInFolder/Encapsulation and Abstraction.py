from abc import ABC, abstractmethod
'''
Making a class called BankAccount with the attributes:account_number and balance
methods:get_balance, set_balance, and withdraw.
'''
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self._balance = balance
    def get_balance(self):
        print(self._balance)
    def set_balance(self,tBalance):
        self._balance = tBalance
    def withdraw(self,tWithdraw):
        if tWithdraw <= self._balance:
            self._balance -= tWithdraw
        else:
            print("Your balance cannot go below zero.")
bankaccount = BankAccount("51902384065",10000)
'''
Making an abstract class "Vehicle" with the methods: start_engine, stop_engine,
and drive.
'''
class Vehicle:
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    def drive(self):
        pass

class Car(Vehicle):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def start_engine(self):
        print("Starting the engine of the car.")
    def stop_engine(self):
        print("Stopping the engine of the car.")
    def drive(self):
        print("Driving the car.")
car = Car("Tesla","Model Y")

car.start_engine()
car.drive()
car.stop_engine()


'''
Encapsulation:To prevent people from modifying your bike.

Abstraction:To use a blueprint to make different kinds of bikes, but you could
modify it.
'''
class Bike:
    @abstractmethod
    def build(self):
        pass
    def modify(self):
        pass

class Colored_Bike(Bike):
    def __init__(self,color):
        self._color = color
    def build(self):
        print("Building the bike.")
    def modify(self,tColor):
        print(f"Bike was {self._color}.")
        self._color = tColor
        print(f"Now {self._color}.")
colored_bike = Colored_Bike("Blue")

colored_bike.build()

colored_bike.modify("Red")




















