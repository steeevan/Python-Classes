
#question 1
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self._balance = balance

    def get_balance(self):
        print(f"account_number: {self.account_number} , balance: {self._balance}")
        
    def set_balance(self,new_balance):
        self._balance = new_balance


    def withdraw(self,minus_balance):
        if minus_balance > self._balance:
            print("ERROR YOU DO NOT HAVE ENOUGH MONEY IN YOUR BANK ACCOUNT!!!")
        else:
            self._balance -= minus_balance
        

bank_account1 = BankAccount("58299145",8471000)

bank_account1.get_balance()
bank_account1.set_balance(9167815600)
bank_account1.get_balance()
bank_account1.withdraw(91678)
bank_account1.get_balance()

#question2
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
        print(f"starting the engine of {self.make} {self.model}")

    def stop_engine(self):
        print(f"stopping the engine of {self.make} {self.model}")

    def drive(self):
        print(f"driving the {self.make} {self.model}.")

def main():
    car1 = Car("Lamborghini","Aventador")
    car1.start_engine()
    car1.stop_engine()
    car1.drive()

if __name__ == "__main__":
    main()

#question 3
from abc import ABC, abstractmethod

class Gun(ABC):
    def __init__(self,typee,model):
        self.typee = typee
        self.model = model

    @abstractmethod
    def start_firing(self):
        pass

    @abstractmethod
    def stop_firing(self):
        pass

    @abstractmethod
    def reloading(self):
        pass

class USgun(Gun):

    def start_firing(self):
        print(f"start firing the {self.typee} {self.model}")

    def stop_firing(self):
        print(f"stop firing the {self.typee} {self.model}")

    def reloading(self):
        print(f"reloading the {self.typee} {self.model}.")

def main():
    gun1 = USgun("assult rifle","M6")
    gun1.start_firing()
    gun1.stop_firing()
    gun1.reloading()

if __name__ == "__main__":
    main()
