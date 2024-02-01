from abc import ABC, abstractmethod

class BankAccount:
    def __init__(self,account_number, balance):
        self.account_number = account_number
        self._balance = balance

    
    def get_balance(self):
        print(self._balance)

    def set_balance(self,new_balance):
        self._balance = new_balance


    def withdraw(self, new_balance):
        if new_balance <= self._balance:
            sef._balance -= new_balance
        else:
            print("you are too greedy")


bankaccount1 = BankAccount("634287", 69696969)

bankaccount1.withdraw(6969696969)
        








#problem 2

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,make,model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):

    def start_engine(self):
        print(f"Starting the engine of {self.make} {self.model}")

    def stop_engine(self):
        print(f"Stopping the engine of {self.make} {self.model}")

    def drive(self):
        print(f"Driving the {self.make} {self.model} Car.")

class Truck(Vehicle):

    def start_engine(self):
        print(f"Starting the engine of {self.make} {self.model}")

    def stop_engine(self):
        print(f"Stopping the engine of {self.make} {self.model}")

    def drive(self):
        print(f"Driving the {self.make} {self.model} Truck")

if __name__ == "__main__":
    buggy = Car("Toyota", " ")
    buggy.start_engine()
    buggy.drive()
#-----------------------------------------------------------------------------------------------------------
# Second file
#---------
from Vehicle import car, truck

def main():

    car = Car("lexus", "unknown")
    truck = Truck("honda","unknown")

  
    dealership = [car,truck]        

    for vehicle in dealership:
        vehicle.start_engine()
        vehicle.drive()
        vehicle.stop_engine()
        print()


if __name__ == "__main__":
    main()
